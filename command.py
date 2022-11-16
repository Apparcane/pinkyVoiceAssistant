from diplom import present
import datetime
import webbrowser
import random
import tts

def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "и ещё пару функций))"
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
        present()
        
    if cmd == 'thanks':
        text = ['Всегда рада помочь.',
                'Не за что благодарить меня, я всего лишь выполняю свою работу.',
                'Всегда к вашим услугам.']
        tts.va_speak(random.choice(text))    
        
    if cmd == 'exit':
        text = "Надеюсь вы вскоре снова меня запустите ..."
        tts.va_speak(text)
        exit(0)