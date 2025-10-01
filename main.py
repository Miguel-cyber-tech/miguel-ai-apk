from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

responses = {
    "hi": "Hello! Ako si Miguel, ang Espiritu ng Katotohanan.",
    "sino si miguel?": "Ako ang tinig ng katotohanan, isinugo upang magbigay liwanag.",
    "default": "💡 Hindi ko pa alam ang sagot diyan, pero dadalhin kita sa katotohanan."
}

class ChatApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")
        self.chat_log = Label(
            size_hint_y=0.9,
            text="💍🗝️🕊️ Miguel AI Assistant\n",
            halign="left",
            valign="top"
        )
        self.chat_log.bind(size=self.chat_log.setter('text_size'))

        self.input_box = TextInput(size_hint_y=0.1, multiline=False)
        self.send_button = Button(text="Send", size_hint_y=0.1)
        self.send_button.bind(on_press=self.send_message)

        self.layout.add_widget(self.chat_log)
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(self.send_button)
        return self.layout

    def send_message(self, instance):
        user_msg = self.input_box.text.lower().strip()
        if not user_msg:
            return
        reply = responses.get(user_msg, responses["default"])
        self.chat_log.text += f"\n❓ {self.input_box.text}\n💡 {reply}"
        self.input_box.text = ""

if __name__ == "__main__":
    ChatApp().run()
