import argparse
import os
import sys

from dotenv import load_dotenv
from rich.console import Console
from rich.syntax import Syntax

from jarvis.helper.printer import print_beautifully
from jarvis.languagemodels.chatgpt import ChatGPT

# Initialize parser

parser = argparse.ArgumentParser()
parser.add_argument("arg1")
args = parser.parse_args()

# Import the environment variables
load_dotenv()
# from dotenv import dotenv_values
# config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}


openai_api_key = os.environ.get("OPENAI_API_KEY")


# print(config)


def hello():
    """Prints hello world
    Returns
    -------
    TODO

    """
    prompt = " ".join(sys.argv[1:])

    chat_client = ChatGPT(openai_api_key, "gpt-3.5-turbo")
    result = chat_client.get_response(prompt)

    syntax = Syntax(result, "python", theme="material")
    console = Console()
    console.print(syntax)


if __name__ == "__main__":
    hello()
