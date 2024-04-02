import argparse
import os
import sys

from dotenv import load_dotenv
from rich.console import Console
from rich.syntax import Syntax

from jarvis.helper.printer import print_beautifully
from jarvis.languagemodels.chatgpt import ChatGPT

# Initialize parser

# parser = argparse.ArgumentParser()
# parser.add_argument("arg1")
# args = parser.parse_args()

# Import the environment variables
load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")


# print(config)


def main():
    """Prints hello world
    Returns
    -------
    None
    """
    prompt = " ".join(sys.argv[1:])

    chat_client = ChatGPT(openai_api_key, "gpt-3.5-turbo")
    result = chat_client.get_response(prompt)

    syntax = Syntax(
        result, "python", theme="material", word_wrap=True, padding=2, code_width=200
    )
    console = Console()
    console.print(syntax)


if __name__ == "__main__":
    main()
