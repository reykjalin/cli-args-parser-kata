import pytest

from parse import ArgumentParser


class TestParser:
    def test_parse_simple(self):
        parser = ArgumentParser([])
        assert parser.parse_simple("--foo") == {"foo": True}

    def test_parse_composite(self):
        parser = ArgumentParser([])
        assert parser.parse_composite(["--foo", "bar"]) == {"foo": "bar"}
