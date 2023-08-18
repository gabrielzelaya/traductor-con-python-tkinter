import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class TextTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Translator")

        self.translator = Translator()

        self.create_ui()

    def create_ui(self):
        self.input_label = tk.Label(self.root, text="Enter text:", font=("Arial", 14))
        self.input_label.pack(pady=10)

        self.input_text = tk.Text(self.root, height=5, width=40, font=("Arial", 12))
        self.input_text.pack()

        self.from_label = tk.Label(self.root, text="From language:", font=("Arial", 14))
        self.from_label.pack()

        self.from_language = ttk.Combobox(self.root, values=list(LANGUAGES.values()), font=("Arial", 12))
        self.from_language.set("en")
        self.from_language.pack()

        self.to_label = tk.Label(self.root, text="To language:", font=("Arial", 14))
        self.to_label.pack()

        self.to_language = ttk.Combobox(self.root, values=list(LANGUAGES.values()), font=("Arial", 12))
        self.to_language.set("es")
        self.to_language.pack()

        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text, font=("Arial", 14))
        self.translate_button.pack(pady=10)

        self.output_label = tk.Label(self.root, text="Translated text:", font=("Arial", 14))
        self.output_label.pack()

        self.output_text = tk.Text(self.root, height=5, width=40, font=("Arial", 12))
        self.output_text.pack()

    def translate_text(self):
        input_text = self.input_text.get("1.0", "end-1c")
        from_lang = self.from_language.get()
        to_lang = self.to_language.get()

        if input_text:
            translated = self.translator.translate(input_text, src=from_lang, dest=to_lang)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated.text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextTranslatorApp(root)
    root.mainloop()
