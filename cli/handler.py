import json
from gptop.operator import Operator
from .utils import announce


def handle(namespace: str, prompt: str):
    """
    Asks the operator to find and execute relevant
    operations based on the provided prompt.
    - prompt: The prompt the operator should handle

    Returns: The output generated from the executed operation(s)
    """
    try:
        operator = Operator(namespace=namespace)

        print("Finding operations...")
        operations = operator.find(prompt=prompt)
        if not operations:
            print("Found no operations")
            return
        announce(f"Found {len(operations)} operations")

        print("Picking an operation...")
        operation = operator.pick(prompt=prompt, operations=operations)
        if not operation:
            announce("No operation picked")
            return
        announce(operation.name, prefix="Picked operation:\n")

        print("Preparing for execution...")
        input = operator.prepare(prompt=prompt, operation=operation)
        announce(input, prefix="Operation prepared with input:\n")

        print("Executing operation...")
        result = operator.execute(operation=operation, input=input)
        announce(result, prefix="Execution result:\n")

        print("Reacting to result...")
        reaction = operator.react(prompt=prompt, operation=operation,
                                  values=json.dumps(input), result=result)
        announce(reaction, "Reaction:\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None