import subprocess


def run_ollama_passthrough_pipe(input: str) -> str:
    """
    Run ollama with the given input and return the output.

    Params:
        input (str): The input to ollama.

    Returns:
        str: The output of ollama.
    """
    command = f"ollama {input}"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.stdout if result.returncode == 0 else result.stderr
