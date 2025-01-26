from gtts import gTTS
import os
import platform
import speech_recognition as sr


# REQ: (For speaking)
# "pip install gtts"

# REQ: (For listening)
# "pip install SpeechRecognition"
# "pip install PyAudio"

class Talk:
    def __init__(self):
        self.os_name = platform.system()
        self.tts = None
        self.recognizer = None
        pass

    def speak(self, text):
        self.tts = gTTS(text=text, lang='tr')

        self.tts.save("output.mp3")

        if self.os_name == "Windows":
            os.system("start output.mp3")  # For Windows
        elif self.os_name == "Linux":
            os.system("mpg321 output.mp3")  # For Raspberry Pi
        else:
            print("OS not supported")

    def listen(self):
        self.recognizer = sr.Recognizer()

        try:
            # Mikrofonu kullan
            with sr.Microphone() as source:
                print("Konusmaya baslayabilirsiniz...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

                # Konuşmayı metne çevir
                print("Konusma algilaniyor...")
                text = self.recognizer.recognize_google(audio, language='tr-TR')
                print("Metin: ", text)

                return text

        except sr.UnknownValueError:
            print("Konusma anlasilamadi.")

            return "Konusma anlasilamadi."
        except sr.RequestError as e:
            print(f"Google API'ye baglanilamadi; Hata: {e}")

            return f"Google API'ye baglanilamadi; Hata: {e}"

    def special_speak(self, text):
        self.speak(f"Sensin {text}")
