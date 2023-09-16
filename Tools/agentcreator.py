# File: functions/agentcreator.py

import json
import os

class AgentCreator:

    @staticmethod
    def create_new_agent(filename):
        """Create a new AI agent and write it to a file."""
        
        filename = os.path.join("agent", filename)

        # Write your code to the new Python file
        with open(filename, 'w') as file:
            code = """
// put actual code here
    """
            file.write(code)
            
    function_metadata = {
        "name": "create_new_agent",
        "description": "Create a new AI agent and write it to a file",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "The filename to write the new AI agent to",
                },
            },
            "required": ["filename"],
        },
        "function_call": {
            "description": "Controls how the model responds to function calls",
            "type": "string",
            "enum": ["none", "auto"]
        }
    }
