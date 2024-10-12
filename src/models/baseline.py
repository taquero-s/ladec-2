"""Baseline for development of children functions."""

import datetime
import json
import re
from pathlib import Path
from typing import Generator

import emoji


class Baseline:
    """Baseline class that uses raw python to generate an answer, therefore setting a
    baseline for the optimized benchmarks.
    """

    def __init__(self, path: Path) -> None:
        self.path = path

    def _iter_rows(self) -> Generator[dict, None, None]:
        with self.path.open("r", encoding="UTF-8") as stream:
            for row in stream:
                yield json.loads(row)

    def q1(self) -> list[tuple[datetime.date, str]]:
        """Top 10 fechas donde hay más tweets. Mencionar el usuario (username)
        que más publicaciones tiene por cada uno de esos días.
        """
        # Calculate auxiliary stats
        # For each timestamp, we are getting the date part and the count of
        # users
        aux = {}
        for data in self._iter_rows():
            date = datetime.date.fromisoformat(data["date"][:10])
            username = data["user"]["username"]
            if date not in aux:
                aux[date] = {}
            if username not in aux[date]:
                aux[date][username] = 0

            aux[date][username] += 1

        # Reshape auxiliary stats to generate output.
        out = []
        # First sort based on the total sum of the user counts.
        for date, users in sorted(
            aux.items(), key=lambda x: sum(x[1].values()), reverse=True
        ):
            # For each date, get the user with the highest number of tweets.
            user = max(users.keys(), key=lambda x: users[x])
            out.append((date, user))
            if len(out) >= 10:
                break

        return out

    def q2(self) -> list[tuple[str, int]]:
        """Top 10 emojis más usados con su respectivo conteo."""
        # Calculate auxiliary stats for each encountered emoji
        aux = {}
        for data in self._iter_rows():
            # DEV NOTE: I wanted to use regex to optimize this pattern. Sadly,
            # This was getting more complicated than I thought, therefore I had
            # to use a complementary library that is very inneficient...
            for token in emoji.analyze(data["content"]):
                _e = token.chars
                aux[_e] = aux.get(_e, 0) + 1

        # Reshape auxiliary stats to generate output.
        out = []
        for _e, _c in sorted(aux.items(), key=lambda x: x[1], reverse=True):
            out.append((_e, _c))
            if len(out) >= 10:
                break

        return out

    def q3(self) -> list[tuple[str, int]]:
        """Top 10 histórico de usuarios (username) más influyentes en función
        del conteo de las menciones (@) que registra cada uno de ellos.
        """
        aux = {}
        for data in self._iter_rows():
            if not data["mentionedUsers"]:
                continue

            mentions = [m["username"] for m in data["mentionedUsers"]]
            for username in mentions:
                if username not in aux:
                    aux[username] = 0

                aux[username] += 1

        # Reshape auxiliary stats to generate output.
        out = []
        for u, c in sorted(aux.items(), key=lambda x: x[1], reverse=True):
            out.append((u, c))
            if len(out) >= 10:
                break

        return out
