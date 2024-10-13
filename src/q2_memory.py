from typing import List, Tuple

from src.solutions import Memory


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    return Memory(path=file_path).q2()
