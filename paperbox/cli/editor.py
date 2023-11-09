from paperbox.cli.ollama import run_ollama_passthrough_pipe
from paperbox.io.markdown_management import (
    get_all_markdown_file_names,
    add_markdown_folder,
    delete_markdown_folder,
    add_markdown_file,
    delete_markdown_file,
    rename_markdown_file,
    move_markdown_file,
    copy_markdown_file,
)
from rich.console import Console
from rich.markdown import Markdown
from textwrap import dedent
import cmd


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

    def onecmd(self, line: str) -> bool:
        try:
            return super().onecmd(line)
        except Exception as e:
            self.console.print(f"Error: {e}", style="bold red")
            return False  # Don't exit the CLI

    def preloop(self) -> None:
        self.console = Console()
        self.console.print(self.boot_instructions, style="bold yellow")

    def do_ollama(self, line) -> None:
        """
        Ollama Passthrough.
        Run ollama with the given input and return the output.

        Usage: ollama <input>

        Help: ollama help
        """
        self.console.print(run_ollama_passthrough_pipe(line), style="bold blue")

    def do_list_markdown_files(self, _) -> None:
        """List all markdown files."""
        self.console.print("\n".join(get_all_markdown_file_names()), style="bold blue")

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
