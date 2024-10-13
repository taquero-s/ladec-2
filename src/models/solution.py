import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Solution(ABC):
    """Abstract solution class used for extensibility to child classes
    with same methods.
    """

    path: Path | str

    @abstractmethod
    def q1(self) -> list[tuple[datetime.date, str]]:
        """Top 10 fechas donde hay más tweets. Mencionar el usuario (username)
        que más publicaciones tiene por cada uno de esos días.
        """

    @abstractmethod
    def q2(self) -> list[tuple[str, int]]:
        """Top 10 emojis más usados con su respectivo conteo."""

    @abstractmethod
    def q3(self) -> list[tuple[str, int]]:
        """Top 10 histórico de usuarios (username) más influyentes en función
        del conteo de las menciones (@) que registra cada uno de ellos.
        """
