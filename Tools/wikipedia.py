# File: Tools/wikipedia.py

import json
import wikipedia

class Wikipedia:

    @staticmethod
    def get_summary(page):
        """Get the summary of a Wikipedia page."""
        try:
            summary = wikipedia.summary(page)
        except wikipedia.PageError:
            summary = "Page not found"
        except wikipedia.DisambiguationError:
            summary = "Multiple pages match this query"
        return json.dumps({"page": page, "summary": summary})

    function_metadata = {
        "name": "get_summary",
        "description": "Get the summary of a given Wikipedia page",
        "parameters": {
            "type": "object",
            "properties": {
                "page": {
                    "type": "string",
                    "description": "The Wikipedia page",
                },
            },
            "required": ["page"],
        },
    }
