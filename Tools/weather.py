# File: Tools/weather.py

import json

class Weather:

    @staticmethod
    def get_current_weather(location, unit="fahrenheit"):
        """Get the current weather for a location."""
        weather_info = {
            "location": location,
            "temperature": "72",
            "unit": unit,
            "forecast": ["snowy", "rainy", "cloudy"]
        }
        return json.dumps(weather_info)

    function_metadata = {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
