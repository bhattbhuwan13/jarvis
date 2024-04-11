from pathlib import Path
from abc import ABCMeta, abstrctmethod


class FileLoader(ABCMeta):
    """Abstract class for file loaders"""

    @abstractmethod
    def __init__(self, location):
        pass

    @abstractmethod
    def create_documents_from_file(self):
        pass
