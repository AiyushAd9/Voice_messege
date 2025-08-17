import time
import threading
import sys

class Stopwatch:
    def __init__(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.thread = None

    def _display_time(self):
        while self.running:
            elapsed = time.time() - self.start_time
            mins, secs = divmod(int(elapsed), 60)
            hrs, mins = divmod(mins, 60)
            time_str = f"\r⏱️ Stopwatch Running: {hrs:02}:{mins:02}:{secs:02}"
            sys.stdout.write(time_str)
            sys.stdout.flush()
            time.sleep(1)
        print()  # Move to new line after stop

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.thread = threading.Thread(target=self._display_time)
            self.thread.start()
            print("✅ Stopwatch started.")

    def stop(self):
        if self.running:
            self.running = False
            self.thread.join()
            self.elapsed_time = time.time() - self.start_time
            mins, secs = divmod(int(self.elapsed_time), 60)
            hrs, mins = divmod(mins, 60)
            print(f"🛑 Stopwatch stopped. Total time: {hrs:02}:{mins:02}:{secs:02}")
            return self.elapsed_time
        else:
            print("⚠️ Stopwatch is not running.")
            return 0
