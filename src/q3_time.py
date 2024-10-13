from typing import List, Tuple

from src.solutions import Time


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    return Time(path=file_path).q3()
