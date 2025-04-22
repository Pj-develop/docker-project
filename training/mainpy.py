import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


def getLanguage(argument):
    switcher = {
        1: "en-IN",
        2: "hi-IN",
        3: "kn-IN",
        4: "gu-IN",
        5: "mr-IN",
        6: "te-IN",
        7: "ur-IN",
        8: "ta-IN"
    }
    return switcher.get(argument, 0)


def getSelection():
    while True:
        try:
            userInput = int(input())
            if (userInput < 1 or userInput > 8):
                print("Not a valid selection! Try again.")
                continue
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break


# Listening to the audio from the microphone and converting to text
def startConversion(lang='en-IN'):
    with sr.Microphone() as source:
        print('Listening...')
        audio_text = r.listen(source, timeout=5)  # Adjust timeout as needed

        try:
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text, language=lang)
            print(text)
        except sr.UnknownValueError:
            print('Sorry, I could not understand the audio.')
        except sr.RequestError as e:
            print(f'Sorry.. an error occurred: {e}')


if __name__ == '__main__':
    # Display language options to the user
    print('Please Select Language for Translate : ')
    print('1. English')
    print('2. Hindi')
    print('3. Kannada')
    print('4. Gujarati')
    print('5. Marathi')
    print('6. Telugu')
    print('7. Urdu')
    print('8. Tamil')

    # Get language selection from the user
    languageSelection = getLanguage(getSelection())

    # Call startConversion method to start the process
    startConversion(languageSelection)
