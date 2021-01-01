import pytest

__all__ = ("TestCases",)


class TestCases:
    class Common:
        invalid_body_create = [
            pytest.param({}, id="empty"),
            pytest.param({"foo": "bar"}, id="invalid object")
        ]
