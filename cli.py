import warnings

warnings.filterwarnings("ignore")
from paperbox.cli.editor import Editor

if __name__ == "__main__":
    Editor().cmdloop()
