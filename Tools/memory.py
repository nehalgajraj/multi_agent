# File: Tools/memory.py

import json
from Memory.memory import MemoryAccess

class Memory:

    def __init__(self, collection_name):
        self.memory_access = MemoryAccess(collection_name)

    def add_to_memory(self, args):
        """Add a document to the memory."""
        document = args.get('document')
        metadata = args.get('metadata', {})
        ids = args.get('ids', [])  # Expecting 'ids' to be provided in 'args'
        self.memory_access.add([document], [metadata], [ids])
        return json.dumps({"status": "success"})

    function_metadata_add = {
        "name": "add_to_memory",
        "description": "Add a document to the memory",
        "parameters": {
            "type": "object",
            "properties": {
                "document": {"type": "string", "description": "The document to add"},
                "metadata": {"type": "object", "description": "The metadata for the document"},
                "ids": {"type": "string", "description": "The ids for the document"},
            },
            "required": ["document", "metadata", "ids"],
        },
    }

    def get_from_memory(self, args):
        """Retrieve a document from the memory."""
        query = args.get('query')
        results = self.memory_access.get(query)
        return json.dumps(results)

    function_metadata_get = {
        "name": "get_from_memory",
        "description": "Retrieve a document from the memory",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "The query to search for"},
            },
            "required": ["query"],
        },
    }
