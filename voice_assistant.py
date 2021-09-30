import re
from speak_and_listen import speak, hear_me
    

def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            print("No me ha dicho su nombre....")
    
    return name


def main():
    
    speak("Hola, como te llamas?")

    text = hear_me()

    name = identify_name(text)
    if name:
        speak("Encantado de conocerte, {}".format(name))
    else:
        speak("Bueno pepito... no te entiendo, podés repetir?")
    

if __name__ == "__main__":
    main()