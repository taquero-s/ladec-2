import datetime
from typing import List, Tuple

from src.solutions import Memory


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    return Memory(path=file_path).q1()
