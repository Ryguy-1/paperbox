# from paperbox.cli.editor import Editor

# if __name__ == "__main__":
#     Editor().cmdloop()

from paperbox.io.markdown_loader import LangchainMarkdownLoader
print(LangchainMarkdownLoader("README.md").load_from_disk())