from pathlib import Path
from abc import ABCMeta, abstrctmethod

from langchain_community.document_loaders import TextLoader


class FileLoader(ABCMeta):
    """Abstract class for file loaders"""

    @abstractmethod
    def __init__(self, location):
        pass

    @abstractmethod
    def create_documents(self):
        pass


class TextFileLoader(FileLoader):
    """Docstring for TextFileLoader."""

    def __init__(self, location):
        """TODO: to be defined.

        Parameters
        ----------
        location : TODO


        """

        self._location = location

    def create_documents(self):
        """TODO: Docstring for create_documents_from_file.
        Returns
        -------
        TODO

        """
        file_path = Path(self._location)
        data_files = list(file_path.glob("**/*.txt"))
        documents = []

        for file in data_files:
            loader = TextLoader(file)
            doc = loader.load()
            documents.append(doc[0])
        return documents
