import time
import re
from threading import Thread

class Timer:
    def __init__(self, speaker):
        self.speaker = speaker

    def extract_time(self, command):
        pattern = r'(\d+)\s*(seconds?|minutes?|hours?)'
        match = re.search(pattern, command)
        if match:
            value = int(match.group(1))
            unit = match.group(2)
            return value, unit
        return None, None

    def start_timer(self, command):
        value, unit = self.extract_time(command)
        if value is None or unit is None:
            self.speaker.speak("Sorry, I couldn't understand the timer duration.")
            return

        # Convert to seconds
        seconds = value
        if "minute" in unit:
            seconds *= 60
        elif "hour" in unit:
            seconds *= 3600

        self.speaker.speak(f"Timer set for {value} {unit}.")
        Thread(target=self._countdown, args=(seconds,)).start()

    def _countdown(self, seconds):
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer_format = f"{mins:02d}:{secs:02d}"
            print(f"⏳ Timer running: {timer_format}", end="\r")
            time.sleep(1)
            seconds -= 1

        print("\n✅ Timer ended!")
        self.speaker.speak("Time's up!")
