# from paperbox.cli.editor import Editor

# if __name__ == "__main__":
#     Editor().cmdloop()
import warnings

warnings.filterwarnings("ignore")
from paperbox.llm_pipelines.markdown_document_loader import MarkdownDocumentLoader
from paperbox.llm_pipelines.document_relevance_sorter import DocumentRelevanceSorter

loader = MarkdownDocumentLoader(file_path="README.md")
documents = loader.retrieve_from_disk_as_elements()
sorter = DocumentRelevanceSorter(documents=documents)
sorted_documents = sorter.get_sorted_by_relevance_to_query(
    query="paperbox", k=2, apply_long_context_reorder=True
)
for document in sorted_documents:
    print(document.page_content)
