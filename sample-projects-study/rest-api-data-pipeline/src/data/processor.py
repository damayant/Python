"""Data processing and cleaning module."""

import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Generator, List, Optional


class DataValidator:
    """Validates and cleans data according to schema."""

    def __init__(self, required_fields: Optional[List[str]] = None):
        """Initialize validator.

        Args:
            required_fields: List of required field names
        """
        self.required_fields = required_fields or []
        self.logger = logging.getLogger(self.__class__.__name__)

    def validate(self, record: Dict[str, Any]) -> bool:
        """Validate that record has all required fields.

        Args:
            record: Data record to validate

        Returns:
            True if valid, False otherwise
        """
        if not isinstance(record, dict):
            self.logger.warning(f"Record is not a dictionary: {type(record)}")
            return False

        for field in self.required_fields:
            if field not in record:
                self.logger.warning(f"Missing required field: {field}")
                return False

        return True

    def clean(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Clean record by removing null/empty values and stripping strings.

        Args:
            record: Data record to clean

        Returns:
            Cleaned record
        """
        if not isinstance(record, dict):
            return record

        cleaned = {}
        for key, value in record.items():
            if value is None:
                continue
            if isinstance(value, str):
                value = value.strip()
                if not value:
                    continue
            cleaned[key] = value

        return cleaned


class BaseDataProcessor(ABC):
    """Abstract base class for data processors."""

    def __init__(self, validator: Optional[DataValidator] = None):
        """Initialize processor.

        Args:
            validator: Data validator instance
        """
        self.validator = validator
        self.logger = logging.getLogger(self.__class__.__name__)
        self._processed_count = 0
        self._skipped_count = 0

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Process data.

        Args:
            data: Data to process

        Returns:
            Processed data
        """
        pass

    def _process_record(self, record: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Process a single record with validation and cleaning.

        Args:
            record: Data record to process

        Returns:
            Cleaned record or None if validation fails
        """
        if self.validator:
            if not self.validator.validate(record):
                self._skipped_count += 1
                return None
            record = self.validator.clean(record)

        self._processed_count += 1
        return record

    def get_stats(self) -> Dict[str, int]:
        """Get processing statistics.

        Returns:
            Dictionary with processing stats
        """
        return {
            "processed": self._processed_count,
            "skipped": self._skipped_count,
        }

    def reset_stats(self) -> None:
        """Reset processing statistics."""
        self._processed_count = 0
        self._skipped_count = 0


class DataProcessor(BaseDataProcessor):
    """Processes data in-memory (not suitable for large datasets)."""

    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process list of records.

        Args:
            data: List of data records

        Returns:
            List of processed records
        """
        if not isinstance(data, list):
            raise ValueError("Data must be a list of records")

        self.reset_stats()
        processed_data = []

        for record in data:
            processed_record = self._process_record(record)
            if processed_record is not None:
                processed_data.append(processed_record)

        self.logger.info(
            f"Processed {self._processed_count} records, "
            f"skipped {self._skipped_count}"
        )
        return processed_data


class StreamingDataProcessor(BaseDataProcessor):
    """Processes data using generators (suitable for large datasets)."""

    def __init__(
        self,
        validator: Optional[DataValidator] = None,
        batch_size: int = 100,
    ):
        """Initialize streaming processor.

        Args:
            validator: Data validator instance
            batch_size: Number of records to process before yielding
        """
        super().__init__(validator)
        self.batch_size = batch_size
        if batch_size <= 0:
            raise ValueError("batch_size must be greater than 0")

    def process(self, data: Generator) -> Generator[List[Dict[str, Any]], None, None]:
        """Process data stream in batches.

        Args:
            data: Generator or iterable of data records

        Yields:
            Batches of processed records
        """
        self.reset_stats()
        batch = []

        try:
            for record in data:
                processed_record = self._process_record(record)
                if processed_record is not None:
                    batch.append(processed_record)

                if len(batch) >= self.batch_size:
                    yield batch
                    batch = []

            # Yield remaining records
            if batch:
                yield batch

        except Exception as e:
            self.logger.error(f"Error during stream processing: {str(e)}")
            raise

        self.logger.info(
            f"Stream processing complete. "
            f"Processed: {self._processed_count}, Skipped: {self._skipped_count}"
        )

    def process_file(self, filepath: str, record_parser) -> Generator:
        """Process data from file in streaming fashion.

        Args:
            filepath: Path to data file
            record_parser: Callable to parse each line into record

        Yields:
            Batches of processed records
        """
        self.logger.info(f"Starting to process file: {filepath}")

        def record_generator():
            try:
                with open(filepath, "r") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            record = record_parser(line)
                            yield record
                        except Exception as e:
                            self.logger.warning(
                                f"Failed to parse line: {line}, Error: {str(e)}"
                            )

            except IOError as e:
                self.logger.error(f"Failed to read file {filepath}: {str(e)}")
                raise

        yield from self.process(record_generator())

