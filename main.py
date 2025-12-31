from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import speech_recognition as sr
import pyttsx3
import requests

# إعداد TTS
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_query(query):
    try:
        r = requests.post("https://your-api.example.com/assist", json={"q": query, "lang": "ar"})
        reply = r.json().get("reply", "لم أفهم الطلب.")
    except Exception:
        reply = "تعذر الاتصال بالإنترنت."
    speak(reply)
    return reply

class GenieUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.label = Label(text="🔵 مساعد جين جاهز", font_size=24)
        self.add_widget(self.label)
        Clock.schedule_interval(self.listen_loop, 10)  # كل 10 ثواني يتحقق

    def listen_loop(self, dt):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = r.listen(source, timeout=3)
                text = r.recognize_google(audio, language="ar-SA")
                self.label.text = f"✅ سمعت: {text}"
                reply = process_query(text)
                self.label.text = f"💬 الرد: {reply}"
            except Exception:
                self.label.text = "❌ لم أسمع شيئًا"

class GenieApp(App):
    def build(self):
        return GenieUI()

if __name__ == "__main__":
    GenieApp().run()
