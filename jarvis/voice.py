import pyttsx3
import speech_recognition as sr


class VoiceInterface:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)

    def speak(self, text: str) -> None:
        if not text:
            return
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self) -> str:
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening for your command...")
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=5)

            try:
                return self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                print("I could not understand that command.")
                return ""
            except sr.RequestError as exc:
                print(f"Speech recognition error: {exc}")
                return ""
        except OSError as exc:
            print(f"Microphone unavailable: {exc}")
            return ""

    def listen_from_text_input(self) -> str:
        try:
            return input("Command> ").strip()
        except KeyboardInterrupt:
            return "exit"
