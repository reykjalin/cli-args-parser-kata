import pytest

from parse import ArgumentParser


class TestParser:
    def test_parse(self):
        parser = ArgumentParser(["parse.py", "--foo", "bar"])
        assert parser.parse() == {"foo": "bar"}
