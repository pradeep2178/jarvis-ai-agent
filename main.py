import argparse

from jarvis.agent import JarvisAgent
from jarvis.ai import AIClient
from jarvis.voice import VoiceInterface


def run(use_voice: bool = False) -> None:
    voice = VoiceInterface() if use_voice else None
    agent = JarvisAgent(voice_interface=voice, ai_client=AIClient())

    print("Jarvis is online.")
    if voice is not None:
        agent.speak_reply("Jarvis is online. Awaiting your command.")

    while True:
        command = agent.listen_for_command(use_voice=use_voice)
        if not command:
            continue

        response = agent.handle_command(command)
        print(response)

        if voice is not None:
            agent.speak_reply(response)

        if response.lower().startswith("goodbye"):
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start the Jarvis-inspired AI agent.")
    parser.add_argument("--voice", action="store_true", help="Enable microphone input and speech output.")
    args = parser.parse_args()
    run(use_voice=args.voice)
