# Initialize parser
import argparse
import os
import sys

from dotenv import load_dotenv
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from rich.console import Console
from rich.syntax import Syntax

from jarvis.helper.printer import print_beautifully
from jarvis.languagemodels.chatgpt import ChatGPT

parser = argparse.ArgumentParser()
parser.add_argument("prompt")
parser.add_argument("--rag", type=int)
parser.add_argument("--dir", type=str)
args = parser.parse_args()


# parser = argparse.ArgumentParser()
# parser.add_argument("arg1")
# args = parser.parse_args()

# Import the environment variables
load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")


# print(config)
from jarvis.helper.documentloader import TextFileLoader


def main():
    """Prints hello world
    Returns
    -------
    None
    """
    prompt = " ".join(args.prompt)

    if args.rag:
        loader = TextFileLoader(args.dir)
        documents = loader.create_documents()
        llm = ChatOpenAI()
        embeddings = OpenAIEmbeddings()
        vector = FAISS.from_documents(documents, embeddings)
        prompt = ChatPromptTemplate.from_template(
            """Answer the following question based only on the provided context:

            <context>
            {context}
            </context>

            Question: {input}"""
        )
        document_chain = create_stuff_documents_chain(llm, prompt)

        retriever = vector.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        response = retrieval_chain.invoke({"input": args.prompt})
        print(response["answer"])

        return

    chat_client = ChatGPT(openai_api_key, "gpt-3.5-turbo")
    result = chat_client.get_response(prompt)

    syntax = Syntax(
        result, "python", theme="material", word_wrap=True, padding=2, code_width=200
    )
    console = Console()
    console.print(syntax)


if __name__ == "__main__":
    main()
