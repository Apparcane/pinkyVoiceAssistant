import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
import webbrowser
import random

# initialize (start bot)
print(f"{config.VA_NAME} Начала свою работу ...")
# tts.va_speak("Приветствую создатель, ожидаю команды...")

def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Либо я вас не расслышала, либо я не зню такой команды.")
        else:
            execute_cmd(cmd['cmd'])

def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd

def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc

def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "и открывать браузер"
        tts.va_speak(text)

    if cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Сейч+ас " + now.hour + " : " + now.minute
        tts.va_speak(text)
    
    if cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                 'Программист это машина для преобразования кофе в код']

        tts.va_speak(random.choice(jokes))

    if cmd == 'open_browser':
        opera_path = 'C:/Users/brodi/AppData/Local/Programs/Opera GX/opera.exe'
        webbrowser.get(opera_path).open("http://python.org")

    if cmd == 'diplom':
        pass

stt.va_listen(va_respond)   