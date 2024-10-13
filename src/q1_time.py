import datetime
from typing import List, Tuple

from src.solutions import Time


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    return Time(path=file_path).q1()
