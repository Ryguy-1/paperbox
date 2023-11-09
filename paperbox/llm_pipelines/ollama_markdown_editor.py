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
                You are editing a markdown document. \n
                
                ======== EXAMPLE INPUTS ========\n
                Input: #$#make it say port 4000 instead !!!! docker run -it --gpus all -p 5000:5000 paperbox:latest#$#\n
                Output: docker run -it --gpus all -p 4000:4000 paperbox:latest\n

                Input: #$#change the username from 'admin' to 'user' !!!! ssh admin@192.168.0.1#$#\n
                Output: ssh user@192.168.0.1\n

                Input: #$#add 'https://' at the beginning of example !!!! www.example.com#$#\n
                Output: https://www.example.com\n

                Input: #$#rewrite at 6 part to make it more formal !!!! Hey, wanna come to my place at 6? We're having a game night!#$#\n
                Output: You are cordially invited to an evening of games and entertainment at my residence, commencing at 6 o'clock PM.\n

                ======== YOUR INPUT ========\n
                Input: #$#{inst} !!!! {rewrite_context}#$#\n
                Output:
                """
            ),
            partial_variables={
                "rewrite_context": self.section_to_rewrite.page_content,
            },
        )
        chain = rewrite_template | self.loaded_ollama_llm | StrOutputParser()
        return chain.invoke({"inst": instructions})


# # Set up the rewrite prompt with instructions and context
