from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_transformers import (
    LongContextReorder,
)
from langchain.schema.document import Document
from typing import List


class DocumentRelevanceSorter(object):
    """Encapsulates the sorting of a list of Document objects by relevance."""

    def __init__(
        self,
        documents: List[Document],
    ) -> None:
        """
        Initialize the DocumentRelevanceSorter.

        Params:
            documents (List[Document]): The list of Document objects to sort.
        """
        self.documents = documents
        self.long_context_reorder = LongContextReorder()
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def get_sorted_by_relevance_to_query(
        self, query: str, k: int = None, apply_long_context_reorder: bool = False
    ) -> List[Document]:
        """
        Sort the list of Document objects by relevance to a query.

        Params:
            query (str): The query to sort by.
            k (int): The number of documents to return.
            apply_long_context_reorder (bool): Whether to apply long context reorder.

        Returns:
            List[Document]: The sorted list of Document objects.
        """
        retriever = Chroma.from_documents(
            documents=self.documents, embedding=self.embeddings
        ).as_retriever(
            search_kwargs={
                "k": len(self.documents) if k is None else k,
            }
        )
        relevant_documents = retriever.get_relevant_documents(query=query)
        if apply_long_context_reorder:
            relevant_documents = self._apply_long_context_reorder(
                documents=relevant_documents
            )
        return relevant_documents

    def _apply_long_context_reorder(self, documents: List[Document]) -> List[Document]:
        """
        Take sorted list by relevance and apply long context reorder.
        This means that most relevant documents are near beginning or end of list.

        Params:
            documents (List[Document]): The list of Document objects to sort.

        Returns:
            List[Document]: The list with long context reorder applied.
        """
        return self.long_context_reorder.transform_documents(documents=documents)
