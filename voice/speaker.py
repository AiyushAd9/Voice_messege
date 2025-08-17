import pyttsx3

class VoiceSpeaker:
    def __init__(self, rate=165, volume=1.0, voice_index=0):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[voice_index].id)

    def speak(self, text):
        print(f"🗣️ Assistant says: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
