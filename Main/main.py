# Import libraries
import openai
import json
from typing import List, Dict, Callable, Any
from Tools.tools import TOOLS
from Memory.memory import MemoryAccess
from Tools.memory import Memory

class generator:
    def __init__(self, TOOLS: List[Dict], memory_collection_name: str):
        # Initialize memory access
        self.memory = Memory("memory_collection_name")

        # Initialize available functions and metadata
        self.available_functions = self.map_functions(TOOLS)
        self.functions_metadata = self.extract_metadata(TOOLS)
        
    def map_functions(self, TOOLS: List[Dict]) -> Dict[str, Callable]:
        functions =  {func_map["metadata"]["name"]: func_map["function"] for func_map in TOOLS}
        functions.update({
            self.memory.function_metadata_add["name"]: self.memory.add_to_memory,
            self.memory.function_metadata_get["name"]: self.memory.get_from_memory
        })
        return functions

    def extract_metadata(self, TOOLS: List[Dict]) -> List[Dict]:
        metadata = [func_map["metadata"] for func_map in TOOLS]
        metadata.append(self.memory.function_metadata_add)
        metadata.append(self.memory.function_metadata_get)
        return metadata


    def call_function(self, function_name: str, function_args: str) -> Dict[str, Any]:
        function_to_call = self.available_functions[function_name]
        function_args = json.loads(function_args.strip())
        return function_to_call(function_args)

    def run(self, prompt: str, user: str) -> openai.api_resources.abstract.APIResource:
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user},
        ]

        function_call_count = 0
        while function_call_count < 5:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=messages,
                functions=self.functions_metadata,
                function_call="auto",
            )

            response_message = response["choices"][0]["message"]

            # If the model returned a message without a function call, break the loop
            if not response_message.get("function_call"):
                break

            # If the model wants to call a function, call it and append the results to the messages
            function_response = self.call_function(
                response_message["function_call"]["name"], 
                response_message["function_call"]["arguments"]
            )

            messages.append(response_message)
            messages.append(
                {
                    "role": "function",
                    "name": response_message["function_call"]["name"],
                    "content": json.dumps(function_response),
                }
            )

            function_call_count += 1

        return response
