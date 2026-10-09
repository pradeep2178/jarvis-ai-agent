# Jarvis AI Agent

A Windows 11 desktop assistant inspired by Iron Man's Jarvis. This project gives you a Python-based AI assistant with:

- voice recognition using microphone input
- speech output using text-to-speech
- AI-powered chat via OpenAI API (when configured)
- quick system actions such as opening apps and websites
- a clean command loop for natural interaction

## Features

- "Jarvis, what time is it?"
- "Jarvis, open notepad"
- "Jarvis, search for Python automation tutorials"
- "Jarvis, who are you?"
- "Jarvis, open GitHub"

## Project Structure

- `main.py` — entry point
- `jarvis/agent.py` — command handling logic
- `jarvis/ai.py` — OpenAI integration
- `jarvis/system_tools.py` — app launching and web actions
- `jarvis/voice.py` — speech recognition and text-to-speech
- `jarvis/config.py` — environment settings

## Setup

1. Clone the repository.
2. Create a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file from `.env.example` and add your API key if you want AI responses:

   ```bash
   copy .env.example .env
   ```

5. Run the assistant:

   ```bash
   python main.py --voice
   ```

   Or run text-only mode:

   ```bash
   python main.py
   ```

## Notes

- For microphone support on Windows, you may need to install the Microsoft Visual C++ build tools or use `pip install pipwin` and install `pyaudio` through that route if the wheel fails.
- Without an `OPENAI_API_KEY`, the assistant still works in offline mode for common commands.
- The project is intentionally designed as a safe "desktop assistant" starter, with no destructive system controls enabled.

## Example Commands

- `jarvis open notepad`
- `jarvis open github`
- `jarvis search for AI news`
- `jarvis what time is it`
- `jarvis who are you`

## License

MIT
