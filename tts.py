import torch
import sounddevice as sd
import time
import os

# language = 'ru'
# model_id = 'ru_v3'
sample_rate = 48000
speaker = 'baya'  # aidar baya kseniya xenia
put_accent = True
put_yo = True
device = torch.device('cpu')
text = "Привет мой господин, я слушаю и повенуюсь!"

local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/ru_v3.pt',
                                   local_file)  


model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

def va_speak(what: str):
    audio = model.apply_tts(text=what+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    #Воспроизведение
    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()