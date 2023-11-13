# Welcome to BoxBox 📦

## PAPERBOX IS CURRENTLY IN DEVELOPMENT AND IS NOT YET READY FOR USE

## What is PaperBox?

PaperBox is a command line tool that allows you to take notes in plain English, shorthand, or whatever's quickest. It uses LLMs to translate your work to beautiful renderable scripts in real time to be viewed from a local server and saved in the format of your choice. Due to this fact, even generating math notes with tools like LaTeX can be done with relative ease. PaperBox is built on top of [Google](https://www.google.com), using custom LLMs to translate between natural language and any renderable scripting language.

PaperBox would then translate your note into a LaTeX-formatted script, making it easy to view and save in the desired format.

# How to use PaperBox

1. Install [Docker](https://docs.docker.com/engine/install/)

2. (Optional) Install [Nvidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation)

3. Get the PaperBox Docker image

   ```
   docker pull ryguy-1/paperbox:latest
   ```

4. Run the PaperBox Docker image (with interactive terminal)

   ```
   docker run -it --gpus all -p 4000:4000 paperbox:latest
   ```

5. Open a browser and navigate to [http://localhost:4000](http://localhost:4000)
