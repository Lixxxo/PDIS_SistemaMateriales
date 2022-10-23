from dataclasses import dataclass
from datetime import datetime


@dataclass
class Movement:
    """Class for keeping track of movements in the database."""
    id: int
    movement_type: str
    material_quantity: int
    material_id: int
    hour: datetime = datetime.now()


@dataclass
class Material:
    """Class for keeping track of materials in the database."""
    id: int
    name: str
    price: int
    quantity: int = 0
