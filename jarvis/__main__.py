import sys
import argparse
from jarvis.helper.printer import print_beautifully

# Initialize parser

parser = argparse.ArgumentParser()
parser.add_argument("arg1")
args = parser.parse_args()


def hello():
    """Prints hello world
    Returns
    -------
    TODO

    """
    _text = " ".join(sys.argv[1:])
    print_beautifully(_text)



if __name__ == "__main__":
    hello()
