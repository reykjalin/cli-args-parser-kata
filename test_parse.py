import pytest

from parse import ArgumentParser


class TestListParser:
    def test_parse_simple(self):
        parser = ArgumentParser([])
        assert parser.parse_simple("--foo") == {"foo": True}

    def test_parse_composite(self):
        parser = ArgumentParser([])
        assert parser.parse_composite(["--foo", "bar"]) == {"foo": "bar"}

    def test_parse_composite_int(self):
        parser = ArgumentParser([])
        assert parser.parse_composite(["--foo", "2"]) == {"foo": 2}

    def test_parse(self):
        parser = ArgumentParser(["parse", "--foo", "--bar", "baz", "--number", "1"])
        assert parser.parse() == {"foo": True, "bar": "baz", "number": 1}

        
class TestListParser:
    def test_parse_simple(self):
        parser = ArgumentParser("python --foo")
        assert parser.parse() == {"foo": True}

    def test_parse_composite(self):
        parser = ArgumentParser("python --foo bar")
        assert parser.parse() == {"foo": "bar"}

    def test_parse_composite_int(self):
        parser = ArgumentParser("python --foo 2")
        assert parser.parse() == {"foo": 2}

    def test_parse(self):
        parser = ArgumentParser("parse --foo --bar baz --number 1")
        assert parser.parse() == {"foo": True, "bar": "baz", "number": 1}
        
