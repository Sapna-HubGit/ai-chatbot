import tkinter as tk
from tkinter import scrolledtext
from chatbot import ask_gpt

def get_response():
    user_msg = user_input.get()
    if user_msg.strip() == "":
        return
    chat_box.insert(tk.END, "You: " + user_msg + "\n")
    response = ask_gpt(user_msg)
    chat_box.insert(tk.END, "Bot: " + response + "\n\n")
    user_input.delete(0, tk.END)

root = tk.Tk()
root.title("Free AI ChatBot (OpenRouter)")
root.geometry("520x420")

chat_box = scrolledtext.ScrolledText(root, width=60, height=20)
chat_box.pack(pady=10)

user_input = tk.Entry(root, width=40)
user_input.pack(side=tk.LEFT, padx=(10, 5), pady=5)

send_button = tk.Button(root, text="Send", command=get_response)
send_button.pack(side=tk.LEFT)

root.mainloop()
