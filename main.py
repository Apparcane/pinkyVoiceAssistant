import config
from command import execute_cmd
import stt
import tts
from fuzzywuzzy import fuzz

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

stt.va_listen(va_respond)   