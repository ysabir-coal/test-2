"""Tests for configuration parser module."""
import pytest
from config_parser import ConfigParser


class TestConfigParser:
    def test_load_empty_config(self):
        parser = ConfigParser()
        result = parser.parse("{}")
        assert result == {}

    def test_load_with_region(self):
        parser = ConfigParser()
        result = parser.parse('{"region": "us-east-1"}')
        assert result["region"] == "us-east-1"

    def test_invalid_json_raises(self):
        parser = ConfigParser()
        with pytest.raises(ValueError):
            parser.parse("not json{{{")

    def test_nested_config(self):
        parser = ConfigParser()
        result = parser.parse('{"deploy": {"target": "prod", "regions": ["us-east-1"]}}')
        assert result["deploy"]["target"] == "prod"
        assert "us-east-1" in result["deploy"]["regions"]
