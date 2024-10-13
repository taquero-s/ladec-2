"""Baseline for development of children functions."""

import emoji
import polars as pl

from src.models.solution import Solution


class Time(Solution):
    """Solution that focuses on the optimization of execution time."""

    def _get_dataframe(self, schema: dict | None = None) -> pl.DataFrame:
        return pl.read_ndjson(self.path, schema=schema)

    def q1(self):
        pdf = self._get_dataframe(
            schema={"date": pl.String(), "user": pl.Struct({"username": pl.String()})}
        )
        response = (
            pdf.select(
                pl.col("date").str.to_datetime().dt.truncate("1d"),
                pl.col("user").struct.field("username"),
            )
            .group_by("date", "username")
            .agg(pl.len().alias("freq"))
            .with_columns(max_freq=pl.col("freq").max().over("date"))
            .group_by("date")
            .agg(
                pl.when(pl.col("freq") == pl.col("max_freq"))
                .then("username")
                .drop_nulls()
                .first(),
                pl.col("freq").sum(),
            )
            .sort("freq", descending=True)
            .select("date", "username")
            .limit(10)
        )
        return self._response_to_list(response)

    def q2(self):
        plf = self._get_dataframe(schema={"content": pl.String()})
        response = (
            plf.select("content")
            .with_columns(
                emojis=pl.col("content").map_elements(
                    lambda x: [token.chars for token in emoji.analyze(x)],
                    return_dtype=pl.List(pl.String()),
                )
            )
            .filter(pl.col("emojis").list.len() > 0)
            .select(pl.col("emojis").list.explode())
            .group_by("emojis")
            .len()
            .sort("len", descending=True)
            .limit(10)
        )
        return self._response_to_list(response)

    def q3(self):
        plf = self._get_dataframe(
            schema={"mentionedUsers": pl.Struct({"username": pl.String()})}
        )
        response = (
            plf.filter(pl.col("mentionedUsers").is_not_null())
            .select(pl.col("mentionedUsers").explode().struct.field("username"))
            .group_by("username")
            .len()
            .sort("len", descending=True)
            .limit(10)
        )
        return self._response_to_list(response)

    @staticmethod
    def _response_to_list(pdf: pl.DataFrame) -> list:
        return list(zip(*pdf.to_dict(as_series=False).values()))
