"""
Pod Model Module

Defines the data models for pods and their resource requirements.
Represents workload units that can be scheduled on nodes.

Key Features:
- Pod status tracking
- Resource requirement specification
- Creation timestamps
- Node assignment tracking
"""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
import uuid
from datetime import datetime


class PodStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    FAILED = "failed"
    SUCCEEDED = "succeeded"


class PodResources(BaseModel):
    cpu_cores: int = Field(..., ge=1, description="Number of CPU cores required")
    memory_mb: int = Field(..., ge=0, description="Memory required in MB")


class Pod(BaseModel):
    """
    Represents a workload unit that can be scheduled on a node.
    
    Contains resource requirements, status information, and node assignment.
    Tracks creation time and current state.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    node_id: Optional[str] = None
    status: PodStatus = PodStatus.PENDING
    resources: PodResources
    created_at: datetime = Field(default_factory=datetime.now)


class PodCreation(BaseModel):
    name: str
    resources: PodResources
