from langchain.llms import Ollama
from langchain.schema import Document, StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.prompt_template import format_document
from typing import List
from textwrap import dedent


class OllamaMarkdownEditor:
    """Defines an Ollama LangChain Markdown Editor."""

    def __init__(
        self,
        section_to_rewrite: Document,
        document_context: List[Document],
        ollama_model_name: str,
    ) -> None:
        self.section_to_rewrite = section_to_rewrite
        self.document_context = document_context
        self.ollama_model_name = ollama_model_name
        self.doc_prompt = PromptTemplate.from_template("{page_content}")
        self.loaded_ollama_llm = Ollama(model=self.ollama_model_name)

    def rewrite_section(self, instructions: str) -> str:
        """
        Rewrite Section According to Instructions.

        Params:
            instructions (str): instructions for rewriting.

        Returns:
            str: rewritten section.
        """
        content = "\n\n".join(
            format_document(doc, self.doc_prompt) for doc in self.document_context
        )

        rewrite_chain = (
            {
                "content": content,
                "instructions": instructions,
                "section_to_rewrite": self.section_to_rewrite.page_content,
            }
            | PromptTemplate.from_template(
                dedent(
                    """
                    You are a capable Markdown note taker. You are to rewrite the selected \n
                    section of the document given 1) Rewrite Instructions, 2) The Document for Context, \n
                    3) The Current Section. You must follow these rules in writing: \n
                        1) For any math, use LaTeX for Markdown. \n
                        2) Follow the style of the rest of the document. \n
                    ==== Rewrite Instructions ==== \n
                    {instructions} \n
                    ==== Document Context ==== \n
                    {content} \n
                    ==== Section to Rewrite ==== \n
                    {section_to_rewrite} \n
                    """
                )
            )
            | self.loaded_ollama_llm
            | StrOutputParser()
        )

        return rewrite_chain.invoke({"instructions": instructions})
