from voice.recognizer import VoiceRecognizer
from voice.speaker import VoiceSpeaker
from features import time_date
from features.stopwatch import Stopwatch     # ✅ Stopwatch
from features.timer import Timer             # ✅ Timer
from features import apps
from features import music
from features import memory
from features import jokes


class Assistant:
    def __init__(self):
        self.recognizer = VoiceRecognizer()
        self.speaker = VoiceSpeaker()
        self.user_name = None
        self.assistant_name = "Doyal Baba"
        self.stopwatch = Stopwatch()         # ✅ Stopwatch instance
        self.timer = Timer(self.speaker)     # ✅ Timer instance

    def greet(self):
        self.speaker.speak(f"Hello! I am {self.assistant_name}. How can I help you?")

    def listen_command(self):
        try:
            command = self.recognizer.listen()
            print(f"🎧 You said: {command}")
            return command.lower()
        except Exception as e:
            self.speaker.speak("Sorry, I couldn't understand that.")
            print(f"Error: {e}")
            return ""

    def process_command(self, command):
        if "your name" in command:
            self.speaker.speak(f"My name is {self.assistant_name}.")

        elif "my name is" in command:
            self.user_name = command.split("my name is")[-1].strip().capitalize()
            memory.remember("user_name", self.user_name)
            self.speaker.speak(f"Nice to meet you, {self.user_name}.")

        elif "what's my name" in command or "what is my name" in command:
            remembered_name = memory.recall("user_name")
            if remembered_name:
                self.speaker.speak(f"Your name is {remembered_name}.")
            else:
                self.speaker.speak("I don't know your name yet.")

        elif "time" in command:
            current_time = time_date.get_time()
            self.speaker.speak(f"The current time is {current_time}.")

        elif "date" in command:
            current_date = time_date.get_date()
            self.speaker.speak(f"Today's date is {current_date}.")

        elif "start stopwatch" in command:
            self.speaker.speak("Starting stopwatch.")
            self.stopwatch.start()

        elif "stop stop watch" in command:
            elapsed = self.stopwatch.stop()
            hrs, rem = divmod(int(elapsed), 3600)
            mins, secs = divmod(rem, 60)
            self.speaker.speak(f"Stopwatch stopped. Total time was {hrs} hours {mins} minutes and {secs} seconds.")

        elif "set timer" in command:
            self.timer.start_timer(command)
        
        elif "open notepad" in command:
            self.speaker.speak("Opening Notepad.")
            apps.open_notepad()

        elif "open calculator" in command:
            self.speaker.speak("Opening Calculator.")
            apps.open_calculator()
        
        elif "play music" in command or "start music" in command:
            self.speaker.speak("Playing music.")
            music.play_music()

        elif "stop music" in command:
            self.speaker.speak("Stopping music.")
            music.stop_music()

        elif "joke" in command or "make me laugh" in command:
            joke = jokes.tell_joke()
            self.speaker.speak(joke)

        elif "exit" in command or "quit" in command or "goodbye" in command:
            self.speaker.speak("Goodbye!")
            exit()

        else:
            self.speaker.speak("Sorry, I can't do that yet.")

    def run(self):
        self.greet()
        while True:
            command = self.listen_command()
            if command:
                self.process_command(command)
