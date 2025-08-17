import os
import queue
import sounddevice as sd
import vosk
import json
import pandas as pd
from tabulate import tabulate  # pip install tabulate


class VoiceRecognizer:
    def __init__(self, model_path="vosk-model-small-en-in-0.4", sample_rate=16000):
        # Check model path
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"❌ Vosk model not found at path: {model_path}")

        self.model = vosk.Model(model_path)
        self.sample_rate = sample_rate
        self.q = queue.Queue()

        # 🎧 List audio devices
        self.list_audio_devices()

        # Choose input device
        self.device_index = int(input("\n🔧 Enter the index of your microphone device: "))

    def list_audio_devices(self):
        print("\n🎧 Available Audio Devices:\n")
        devices = sd.query_devices()
        device_list = []

        for idx, dev in enumerate(devices):
            device_info = f"{dev['name']}, {dev['hostapi']} ({dev['max_input_channels']} in, {dev['max_output_channels']} out)"
            device_list.append({"Index": idx, "Device": device_info})

        df = pd.DataFrame(device_list)
        print(tabulate(df, headers="keys", tablefmt="fancy_grid"))

    def callback(self, indata, frames, time, status):
        if status:
            print("⚠️ Stream status:", status)
        self.q.put(bytes(indata))

    def listen(self):
        with sd.RawInputStream(
            samplerate=self.sample_rate,
            blocksize=8000,
            dtype='int16',
            channels=1,
            callback=self.callback,
            device=self.device_index
        ):
            rec = vosk.KaldiRecognizer(self.model, self.sample_rate)
            print("🎙️ Speak something...")
            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    text = result.get("text", "")
                    if text:
                        return text.lower()
