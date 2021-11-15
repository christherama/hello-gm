from dataclasses import dataclass, field
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
@dataclass
class Patient:
    __tablename__ = "patient"
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(
        init=False,
        metadata={
            "sa": Column(Integer, primary_key=True)
        }
    )
    first_name: str = field(
        init=False,
        metadata={
            "sa": Column(String(50))
        }
    )
    last_name: str = field(
        init=False,
        metadata={
            "sa": Column(String(50))
        }
    )
