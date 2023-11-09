from paperbox.cli.ollama import run_ollama_passthrough_pipe
from paperbox.io.markdown_management import (
    get_all_markdown_file_names,
    get_all_markdown_folder_names,
    add_markdown_folder,
    delete_markdown_folder,
    add_markdown_file,
    delete_markdown_file,
    rename_markdown_folder,
    rename_markdown_file,
    move_markdown_file,
    copy_markdown_file,
)
from paperbox.llm_pipelines.document_relevance_sorter import DocumentRelevanceSorter
from paperbox.io.markdown_document_loader import MarkdownDocumentLoader
from paperbox.llm_pipelines.ollama_markdown_editor import OllamaMarkdownEditor
from langchain.schema.document import Document
from langchain.llms.ollama import Ollama
from rich.console import Console
from rich.markdown import Markdown
from textwrap import dedent
from dataclasses import dataclass
import inquirer
from typing import List
import cmd


@dataclass
class CMDState(object):
    """A class to hold the state of the CLI."""

    current_file_path: str = None
    current_ordered_loaded_documents: List[Document] = None
    llm = Ollama(model="llama2")


class Editor(cmd.Cmd):
    intro = dedent(
        """
            ____                        ____            
           / __ \____ _____  ___  _____/ __ )____  _  __
          / /_/ / __ `/ __ \/ _ \/ ___/ __  / __ \| |/_/
         / ____/ /_/ / /_/ /  __/ /  / /_/ / /_/ />  <  
        /_/    \__,_/ .___/\___/_/  /_____/\____/_/|_|  
                   /_/                                                                                
        """
    )
    prompt = "(paperbox) "
    boot_instructions = dedent(
        f"""
        \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
        #######################################################\n
        Welcome to the Paperbox Editor!\n
        Type [bold magenta]help[/] to see the list of commands.\n
        #######################################################
        """
    )

    # def onecmd(self, line: str) -> bool:
    #     """Override the onecmd method to catch exceptions."""
    #     try:
    #         return super().onecmd(line)
    #     except Exception as e:
    #         self.console.print(f"Error: {e}", style="bold red")
    #         return False  # Don't exit the CLI

    def preloop(self) -> None:
        self.console = Console()
        self.state = CMDState()
        self.console.print(self.boot_instructions, style="bold yellow")

    def do_e(self, line) -> None:
        """
        Edit a file.
        Usage: e <natural_language_query_on_loaded_file>
        """
        if None in [
            self.state.current_file_path,
            self.state.current_ordered_loaded_documents,
        ]:
            self.console.print(
                "No file loaded. Use [bold magenta]load[/] to load a file.",
                style="bold yellow",
            )
            return
        doc_rel_sorter = DocumentRelevanceSorter(
            documents=self.state.current_ordered_loaded_documents
        )
        relevant_sections = doc_rel_sorter.get_sorted_by_relevance_to_query(
            query=line, k=3, apply_long_context_reorder=False
        )
        # have user choose which section to edit
        section_choices = [
            f"{section.page_content[:50]}" for section in relevant_sections
        ]
        section_choices.append("Cancel")
        section_choice = inquirer.prompt(
            [
                inquirer.List(
                    "section",
                    message="Which section would you like to edit?",
                    choices=section_choices,
                )
            ]
        )["section"]
        if section_choice == "Cancel":
            return
        section_index = section_choices.index(section_choice)
        section_to_edit = relevant_sections[section_index]
        # Regenerate this section's markdown based on input
        md_editor = OllamaMarkdownEditor(
            loaded_ollama_llm=self.state.llm,
            section_to_rewrite=section_to_edit,
            document_context=self.state.current_ordered_loaded_documents,
        )
        # TODO: Replace print with action
        print(md_editor.rewrite_section(instructions=line))

    def do_load(self, file_path: str) -> None:
        """Load a file to edit."""
        self.console.print(f"Loading file {file_path}", style="bold blue")
        if file_path == self.state.current_file_path:
            self.console.print(f"File {file_path} already loaded", style="bold yellow")
            return
        md_doc_loader = MarkdownDocumentLoader(
            file_path=file_path
        )  # throws FileNotFoundError / ValueError
        self.state.current_file_path = file_path
        self.state.current_ordered_loaded_documents = (
            md_doc_loader.retrieve_from_disk_as_elements()
        )

    def do_ollama(self, line) -> None:
        """
        Ollama Passthrough.
        Run ollama with the given input and return the output.

        Help: ollama help
        """
        self.console.print(run_ollama_passthrough_pipe(line), style="bold blue")

    def do_list_markdown_files(self, _) -> None:
        """List all markdown files."""
        self.console.print("\n".join(get_all_markdown_file_names()), style="bold blue")

    def do_list_markdown_folders(self, _) -> None:
        """List all markdown folders."""
        self.console.print(
            "\n".join(get_all_markdown_folder_names()), style="bold blue"
        )

    def do_add_markdown_folder(self, folder_name: str) -> None:
        """Add a markdown folder."""
        add_markdown_folder(folder_name)
        self.console.print(f"Added folder {folder_name}", style="bold blue")

    def do_delete_markdown_folder(self, folder_name: str) -> None:
        """Delete a markdown folder."""
        delete_markdown_folder(folder_name)
        self.console.print(f"Deleted folder {folder_name}", style="bold blue")

    def do_add_markdown_file(self, file_name: str) -> None:
        """Add a markdown file."""
        add_markdown_file(file_name)
        self.console.print(f"Added file {file_name}", style="bold blue")

    def do_delete_markdown_file(self, file_name: str) -> None:
        """Delete a markdown file."""
        delete_markdown_file(file_name)
        self.console.print(f"Deleted file {file_name}", style="bold blue")

    def do_rename_markdown_folder(self, old_new_folder: str) -> None:
        """Rename a markdown folder."""
        rename_markdown_folder(*old_new_folder.split(" "))
        self.console.print(
            f"Renamed folder {old_new_folder.split(' ')[0]} to {old_new_folder.split(' ')[1]}",
        )

    def do_rename_markdown_file(self, old_new_file: str) -> None:
        """Rename a markdown file."""
        rename_markdown_file(*old_new_file.split(" "))
        self.console.print(
            f"Renamed file {old_new_file.split(' ')[0]} to {old_new_file.split(' ')[1]}",
        )

    def do_move_markdown_file(self, old_new_file: str) -> None:
        """Move a markdown file."""
        move_markdown_file(*old_new_file.split(" "))
        self.console.print(
            f"Moved file {old_new_file.split(' ')[0]} to {old_new_file.split(' ')[1]}",
        )

    def do_copy_markdown_file(self, old_new_file: str) -> None:
        """Copy a markdown file."""
        copy_markdown_file(*old_new_file.split(" "))
        self.console.print(
            f"Copied file {old_new_file.split(' ')[0]} to {old_new_file.split(' ')[1]}",
        )

    def do_exit(self, _) -> bool:
        """Exit the CLI."""
        self.console.print("[italic red]Exiting PaperBox...[/]", style="italic blue")
        return True  # Exits the CLI

    def default(self, line) -> None:
        self.console.print(
            f"Command [bold red]{line}[/] not recognized", style="bold yellow"
        )
