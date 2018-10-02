import pytest

from parse import ArgumentParser


class TestParser:
    def test_parse(self):
        parser = ArgumentParser(["parse.py", "--foo"])
        assert parser.parse() == {"foo": True}
