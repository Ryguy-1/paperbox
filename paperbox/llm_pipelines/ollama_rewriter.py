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
            template="""You are a professional editor. 
                You are tasked with rewriting one section at a time, following the instructions given closely.
                You are given 1) the document context and 2) the instructions.
                Stick closely to the original length and meaning of the section unless instructed otherwise.
                Section to Rewrite: {section_to_rewrite}
                Instructions: {inst}
                Rewritten Section:""",
            partial_variables={
                "section_to_rewrite": self.section_to_rewrite.page_content,
            },
        )
        chain = rewrite_template | self.llm | StrOutputParser()
        output = chain.invoke({"inst": instructions})
        output = output.strip()
        return output
