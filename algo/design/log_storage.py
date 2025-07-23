from collections import defaultdict
from typing import List

class LogSystem:
    def __init__(self):
        # Store logs in a list as (timestamp, id) tuples
        self.logs = []

        # Define time index boundaries for each granularity
        self.granularity_index = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def put(self, log_id: int, timestamp: str) -> None:
        """
        Add a log entry as (timestamp, id).
        """
        self.logs.append((timestamp, log_id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        """
        Return log ids whose timestamp falls in the [start, end] range based on the granularity.
        """
        index = self.granularity_index[granularity]
        start_prefix = start[:index]
        end_prefix = end[:index]
        result = []

        for timestamp, log_id in self.logs:
            ts_prefix = timestamp[:index]
            if start_prefix <= ts_prefix <= end_prefix:
                result.append(log_id)

        return result
