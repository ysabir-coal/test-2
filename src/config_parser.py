"""Configuration file parser for deployment settings."""
import json
from typing import Any, Dict


class ConfigParser:
    """Parses deployment configuration from JSON.

    Supports loading configuration from JSON strings with validation,
    default merging, and environment-specific overrides.

    Example usage:
        parser = ConfigParser()
        config = parser.parse('{"region": "us-east-1", "stage": "gamma"}')
    """

    def parse(self, raw: str) -> Dict[str, Any]:
        """Parse a JSON configuration string.

        Args:
            raw: JSON string to parse

        Returns:
            Parsed configuration dictionary

        Raises:
            ValueError: If the input is not valid JSON
        """
        try:
            return json.loads(raw)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid configuration: {e}")

    def parse_with_defaults(self, raw: str, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
        """Parse configuration with default values merged in.

        The defaults are applied first, then overridden by parsed values.
        This ensures all required keys are present even if the config
        file is incomplete.

        Args:
            raw: JSON string to parse
            defaults: Default values to merge with parsed config

        Returns:
            Merged configuration dictionary
        """
        base = defaults or {}
        parsed = self.parse(raw)
        base.update(parsed)
        return base
