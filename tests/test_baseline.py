import datetime
from pathlib import Path

import pytest

from src.models.baseline import Baseline


class TestBaseline:
    @pytest.fixture(scope="function")
    def baseline(self, assets: Path) -> Baseline:
        baseline = Baseline(path=assets / "tweets_sample.json")

        return baseline

    def test_baseline_q1(self, baseline: Baseline):
        response = baseline.q1()
        assert len(response) == 10

        for date, user in response:
            assert isinstance(date, datetime.date)
            assert isinstance(user, str)

    def test_baseline_q2(self, baseline: Baseline):
        response = baseline.q2()
        assert len(response) == 10

        for user, count in response:
            assert isinstance(user, str)
            assert isinstance(count, int)

    def test_baseline_q3(self, baseline: Baseline):
        response = baseline.q3()
        assert len(response) == 10

        for user, count in response:
            assert isinstance(user, str)
            assert isinstance(count, int)
