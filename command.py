import datetime
import webbrowser
import random
import tts

def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я вмію: ..."
        text += "вимовляти час ..."
        text += "розповідати анекдоти ..."
        text += "і ще кілька функцій))"
        tts.va_speak(text)

    if cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Зараз " + str(now.hour) + " : " + str(now.minute)
        tts.va_speak(text)

    if cmd == 'joke':
        jokes = ['Як сміються програмісти? ... хе-хе-хе',
                "Еск'юел запит заходить у бар, підходить до двох столів і запитує .. «можна приєднатися?»",
                'Програміст це машина для перетворення кави в код']

        tts.va_speak(random.choice(jokes))

    if cmd == 'open_browser':
        opera_path = 'C:/Users/brodi/AppData/Local/Programs/Opera GX/opera.exe'
        webbrowser.get(opera_path).open("http://python.org")
        
    if cmd == 'thanks':
        text = ['Завжди рада допомогти.',
                'Не за що дякувати мене, я просто виконую свою роботу.',
                'Завжди до ваших послуг.']
        tts.va_speak(random.choice(text))    
        
    if cmd == 'exit':
        text = "Сподіваюся, ви скоро знову запустите мене ..."
        tts.va_speak(text)
        exit(0)