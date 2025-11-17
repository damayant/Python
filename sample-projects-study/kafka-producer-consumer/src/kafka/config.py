"""Configuration module for Kafka services."""

import os
from typing import List, Optional

from pydantic import BaseModel, Field


class KafkaConfig(BaseModel):
    """Configuration for Kafka services."""

    bootstrap_servers: List[str] = Field(
        default_factory=lambda: [os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")]
    )
    topic: str = Field(default=os.getenv("KAFKA_TOPIC", "default-topic"))
    group_id: Optional[str] = Field(default=os.getenv("KAFKA_GROUP_ID"))
    client_id: str = Field(default=os.getenv("KAFKA_CLIENT_ID", "python-client"))
    auto_offset_reset: str = Field(
        default=os.getenv("KAFKA_AUTO_OFFSET_RESET", "earliest")
    )
    enable_auto_commit: bool = Field(
        default=os.getenv("KAFKA_ENABLE_AUTO_COMMIT", "false").lower() == "true"
    )
    max_poll_records: int = Field(
        default=int(os.getenv("KAFKA_MAX_POLL_RECORDS", "500"))
    )
    session_timeout_ms: int = Field(
        default=int(os.getenv("KAFKA_SESSION_TIMEOUT_MS", "30000"))
    )
    request_timeout_ms: int = Field(
        default=int(os.getenv("KAFKA_REQUEST_TIMEOUT_MS", "30000"))
    )
    retries: int = Field(default=int(os.getenv("KAFKA_RETRIES", "3")))
    retry_backoff_ms: int = Field(
        default=int(os.getenv("KAFKA_RETRY_BACKOFF_MS", "100"))
    )

    class Config:
        """Pydantic config."""

        extra = "allow"

    def to_dict(self) -> dict:
        """Convert config to dictionary for Kafka client.

        Returns:
            Dictionary of configuration
        """
        return self.model_dump()

