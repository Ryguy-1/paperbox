from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.schema.document import Document
from langchain.vectorstores.utils import filter_complex_metadata
from typing import List


class MarkdownDocumentLoader(object):
    """Encapsulates the loading of a markdown file into Document Objects."""

    def __init__(self, file_path: str) -> None:
        """
        Initialize the MarkdownDocumentLoader.

        Params:
            file_path (str): The path to the markdown file.
        """
        self.file_path = file_path
        self.allowed_types = (str, bool, int, float)

    def retrieve_from_disk_as_elements(self) -> List[Document]:
        """
        Load the markdown file into a Document object.

        Returns:
            List[Document]: A list of Document objects.
        """
        loader = UnstructuredMarkdownLoader(
            file_path=self.file_path, mode="elements", strategy="fast"
        )
        return filter_complex_metadata(
            loader.load(),
            allowed_types=self.allowed_types,
        )

    def retrieve_from_disk_as_single(self) -> List[Document]:
        """
        Load the markdown file into a Document object.

        Returns:
            List[Document]: A list of Document objects (single element).
        """
        loader = UnstructuredMarkdownLoader(
            file_path=self.file_path, mode="single", strategy="fast"
        )
        return filter_complex_metadata(
            [loader.load()],
            allowed_types=self.allowed_types,
        )
