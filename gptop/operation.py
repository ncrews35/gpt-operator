import json
from .utils import llm_response

__all__ = ["Operation"]


class Operation:

    def __init__(self, id: str, type: str, name: str, description: str, metadata: any, schema: any):
        """
        Holds the properties of an operation prepared for execution.
        - id: The identifier of the operation
        - type: The type of operation
        - name: The name of the operation
        - description: The description of the operation
        - metadata: Metadata defined in the manifest file
        - schema: Schema to be hydrated by the LLM
        """

        self.id = id
        self.type = type
        self.name = name
        self.description = description
        self.metadata = metadata
        self.schema = schema

    def __repr__(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def TYPE(cls):
        return "NO_OP"

    def vector_metadata(self):
        """
        Returns a dictionary containing the operation's metadata.
        """
        metadata_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "type": self.type,
            "metadata": self.metadata,
            "schema": self.schema
        }
        return {key: value for key, value in metadata_dict.items() if value is not None}

    def embedding_obj(self):
        """
        Returns a string representation of the operation's properties.
        """
        return "; ".join([
            f"Name: {self.name}",
            f"Description: {self.description}",
            f"Type: {self.type}",
            f"Metadata: {self.metadata}",
            f"Schema: {self.schema}"
        ])

    def llm_message(self):
        """
        Returns a list of dictionaries containing the LLM message.
        """
        return [
            {"role": "system", "content": """
                Given an operation with a predefined schema and a user prompt,
                provide the data needed to execute the operation based on the prompt.
                """.replace("\n", " ")},
            {"role": "user", "content": "Output the data needed and nothing more."}
        ]

    def llm_modifier(self, response):
        """
        Modifies the LLM response.

        Returns: The modified LLM response
        """
        return llm_response(response)

    def execute(self, input: any):
        """
        Executes the operation.

        Returns: The response provided by the execution API
        """

        return "No-op"