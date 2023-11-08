import cmd
from rich.console import Console
from rich.markdown import Markdown
from textwrap import dedent


class Editor(cmd.Cmd):
    intro = dedent(
        """
 ____                                 ____                     
/\  _`\                              /\  _`\                   
\ \ \L\ \ __     _____      __   _ __\ \ \L\ \    ___   __  _  
 \ \ ,__/'__`\  /\ '__`\  /'__`\/\`'__\ \  _ <'  / __`\/\ \/'\ 
  \ \ \/\ \L\.\_\ \ \L\ \/\  __/\ \ \/ \ \ \L\ \/\ \L\ \/>  </ 
   \ \_\ \__/.\_\\ \ ,__/\ \____\\ \_\  \ \____/\ \____//\_/\_\
    \/_/\/__/\/_/ \ \ \/  \/____/ \/_/   \/___/  \/___/ \//\/_/
                   \ \_\                                       
                    \/_/                                       
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

    def do_llm_list(self, _):
        """
        List all Local LLMs.

        Usage: llm_list
        """
        self.console.print(f"LLM List: {[]}", style="bold blue")

    def do_exit(self, _):
        """Exit the CLI."""
        self.console.print("[italic red]Exiting PaperBox...[/]", style="italic blue")
        return True  # Exits the CLI

    def default(self, line):
        self.console.print(
            f"Command [bold red]{line}[/] not recognized", style="bold yellow"
        )
