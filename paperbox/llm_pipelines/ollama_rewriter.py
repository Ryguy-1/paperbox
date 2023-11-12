from langchain.llms.ollama import Ollama
from langchain.schema import Document, StrOutputParser
from langchain.prompts import PromptTemplate


class OllamaRewriter(object):
    """Defines an Ollama LangChain Rewriter Prompted Model."""

    def __init__(
        self,
        section_to_rewrite: Document,
        ollama_model_name: str,
    ) -> None:
        """
        Initialize the Ollama Rewriter.

        Params:
            section_to_rewrite (Document): The section to rewrite.
            ollama_model_name (str): The Ollama model name to use.
        """
        self.section_to_rewrite = section_to_rewrite
        self.ollama_model_name = ollama_model_name
        self.llm = Ollama(model=self.ollama_model_name, temperature=0.7)

    def rewrite_section(self, instructions: str) -> str:
        """
        Rewrite Section According to Instructions.

        Params:
            instructions (str): Instructions for rewriting.

        Returns:
            str: Rewritten section.
        """
        rewrite_template = PromptTemplate.from_template(
            template="""
                You are an AI assistant. Your job is to rewrite the following section of text.
                Stick as closely to the instructions as possible or I will be really sad.
                Take a deep breath and answer accurately.

                
                The section to rewrite is: {section_to_rewrite}
                The instructions are: {inst}
                The final rewrite is:""",
            partial_variables={
                "section_to_rewrite": self.section_to_rewrite.page_content,
            },
        )
        chain = rewrite_template | self.llm | StrOutputParser()
        output = chain.invoke({"inst": instructions})
        output = output.strip()
        return output
