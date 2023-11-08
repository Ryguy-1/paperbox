# Scrivener ✍️🚀

Welcome to **Scrivener** – your ultimate note-taking co-pilot that makes jotting down important information a breeze! 🌬️📝 Whether you're in a meeting, lecture, or brainstorming session, Scrivener listens in, takes notes, and converts them into beautiful markdown documents. It's like having a personal secretary that understands the nuances of your conversations and presentations. Plus, it flawlessly renders math equations, making it a math lover's dream come true! 🧮✨

## Installation 📦

Getting Scrivener up and running is as simple as pulling a Docker container and starting a local server. Follow these steps to begin:

```bash
# Pull the Scrivener Docker container
docker pull scrivener:latest

# Run Scrivener Docker container with a bind mount for Markdown export
docker run -it --gpus all -v ~/my_notes:/scrivener/generated scrivener:latest

```

# Features 🌟

Scrivener is packed with features to make your note-taking efficient and enjoyable:

- Markdown Output: Get your notes in markdown format directly through the web server. 📃✨
- Listening Mode: Uses your microphone to listen in and take notes, so you can stay fully engaged. 🎙️👂
- Slide Parsing: Upload your slides, and Scrivener will intelligently follow along, noting down key points. 🖥️📊
- Note Co-Pilot: You command what gets noted and with what priority. Real-time CLI allows you to keep or modify notes on-the-fly. ⌨️👨‍✈️
  Remember, with Scrivener, you're always in the pilot's seat. 🛩️ You decide what gets noted, ensuring your documents are as detailed or as concise as you need them to be.
