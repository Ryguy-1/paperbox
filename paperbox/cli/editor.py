from paperbox.cli.ollama import run_ollama_passthrough_pipe
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

    def preloop(self) -> None:
        self.console = Console()
        self.console.print(self.boot_instructions, style="bold yellow")

    def do_ollama(self, line):
        """
        Ollama Passthrough.
        Run ollama with the given input and return the output.

        Usage: ollama <input>

        Help: ollama help
        """
        self.console.print(run_ollama_passthrough_pipe(line), style="bold blue")

    def do_exit(self, _):
        """Exit the CLI."""
        self.console.print("[italic red]Exiting PaperBox...[/]", style="italic blue")
        return True  # Exits the CLI

    def default(self, line):
        self.console.print(
            f"Command [bold red]{line}[/] not recognized", style="bold yellow"
        )
