import openai
import json
from Tools.tools import TOOLS as FUNCTIONS
from typing import List, Dict, Callable, Any

class AI_generator:
    def __init__(self, FUNCTIONS: List[Dict]):
        self.available_functions = self.map_functions(FUNCTIONS)
        self.functions_metadata = self.extract_metadata(FUNCTIONS)

    def map_functions(self, FUNCTIONS: List[Dict]) -> Dict[str, Callable]:
        return {func_map["metadata"]["name"]: func_map["function"] for func_map in FUNCTIONS}

    def extract_metadata(self, FUNCTIONS: List[Dict]) -> List[Dict]:
        return [func_map["metadata"] for func_map in FUNCTIONS]

    def call_function(self, function_name: str, function_args: str) -> Dict[str, Any]:
        function_to_call = self.available_functions[function_name]
        function_args = json.loads(function_args.strip())
        return function_to_call(**function_args)

    def generate_response(self, prompt: str, user: str) -> openai.api_resources.abstract.APIResource:
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
