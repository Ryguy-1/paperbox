from langchain.llms.ollama import Ollama
from langchain.schema import Document, StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.prompt_template import format_document
from typing import List
from textwrap import dedent


class OllamaMarkdownEditor(object):
    """Defines an Ollama LangChain Markdown Editor."""

    def __init__(
        self,
        section_to_rewrite: Document,
        document_context: List[Document],
        loaded_ollama_llm: Ollama,
    ) -> None:
        self.section_to_rewrite = section_to_rewrite
        self.document_context = document_context
        self.loaded_ollama_llm = loaded_ollama_llm

    def rewrite_section(self, instructions: str) -> str:
        """
        Rewrite Section According to Instructions.

        Params:
            instructions (str): Instructions for rewriting.

        Returns:
            str: Rewritten section.
        """
        rewrite_template = PromptTemplate.from_template(
            template=dedent(
                """
                You are a capable Markdown note taker. You are to rewrite the selected
                section of the document given 1) Rewrite Instructions, 2) The Document for Context,
                3) The Current Section. You must follow these rules in writing:
                    1) For any math, use LaTeX for Markdown.
                    2) Follow the style of the rest of the document.
                ==== Rewrite Instructions ====
                {inst}
                ==== Document Context ====
                {document_context}
                ==== Section to Rewrite ====
                {rewrite_context}
                """
            ),
            partial_variables={
                "document_context": "\n\n".join(
                    [x.page_content for x in self.document_context]
                ),
                "rewrite_context": self.section_to_rewrite.page_content,
            },
        )


# # Set up the rewrite prompt with instructions and context
