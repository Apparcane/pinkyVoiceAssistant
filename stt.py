import vosk
import sys
import sounddevice as sd
import queue
import json

model = vosk.Model("small_model_ukr")

samplerate = 16000
device = 1

q = queue.Queue()

def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                           channels=1, callback=q_callback):
        print('#' * 80)
        print('Press Ctrl+C to stop the recording')
        print('#' * 80)

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])
                # print(rec.Result())
            # else:
            #     print(rec.PartialResult)
        