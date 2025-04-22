import speech_recognition as sr
import json
from bardapi import BardCookies

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Bard API configuration (assuming you have the correct cookies and BardAPI setup)
cookie_dict = {
"_Secure-1PSID" : "ewgupzuLY9IYjl-VDq2dJIWelvKKMaBUjek54WIUdTcYNRoCALJvTOVdkm3MITdO-gyVFA",
"_Secure-1PSIDTS" : "sidts-CjEBPVxjShH1TVUFmyEZoQcidWbBskvM4nb6gJefQq5UuoCoGo-CXZ17ADatstEaqAKrEAA",
"_Secure-1PSIDCC" :  "ABTWhQGLt3s6w24xE1KIkxjtVfLQKwc1j3R6Y8JHZGLO8w0d-MQoNKQj2ogyjKTXCFlw7qXc8CQ"
}
bard = BardCookies(cookie_dict=cookie_dict)

def get_language(argument):
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
    while True:
        try:
            userInput = int(input())
            if (userInput < 1 or userInput > 9):
                print("Not an integer! Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
        else:
            return language_code

def convert_audio_to_text(path, language):
    """Converts audio to text using speech recognition."""
    with sr.AudioFile(path) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text, language=language)
            return text
        except Exception as e:
            print(f"Error during speech recognition: {e}")
            return ""

def create_json_file(data, output_path="output.json"):
    """Creates a JSON file with the given data."""
    with open(output_path, "w") as json_file:
        json.dump(data, json_file, indent=2)
    print(f"JSON file saved at: {output_path}")

def process_fir_request(text):
    """Uses Bard API to convert text to FIR format."""
    query = "Convert this text to FIR format:\n" + text
    reply = bard.get_answer(query)  # Assuming BardAPI has a get_answer method
    return reply

if __name__ == "__main__":
    language_code = get_language()
    audio_path = input("Enter the path to the audio file: ")
    text = convert_audio_to_text(audio_path, language_code)

    if text:
        fir_response = process_fir_request(text)
        # Handle the FIR response (e.g., display, save as JSON, etc.)
    else:
        print("Unable to transcribe audio.")
