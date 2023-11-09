from langchain.document_loaders import UnstructuredMarkdownLoader


class LangchainMarkdownLoader(object):
    """Encapsulates the loading of a markdown file into a Document object."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.loader = UnstructuredMarkdownLoader(
            file_path=file_path, mode="elements", strategy="fast", 
        )

    def load_from_disk(self):
        """
        Load the markdown file into a Document object.

        Returns:
            Document: A Document object.
        """
        return self.loader.load()
