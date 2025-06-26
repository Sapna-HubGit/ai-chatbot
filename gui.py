import customtkinter as ctk
from chatbot import ask_gpt

# Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create App
app = ctk.CTk()
app.title("🤖 Modern AI ChatBot")
app.geometry("600x500")

# Chat display
chat_display = ctk.CTkTextbox(app, width=560, height=350, font=("Arial", 13), wrap="word")
chat_display.pack(pady=15)
chat_display.insert("end", "🤖 Bot: Hello! How can I help you today?\n\n")
chat_display.configure(state="disabled")

# Message input
input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=10)

user_input = ctk.CTkEntry(input_frame, width=400, font=("Arial", 12))
user_input.pack(side="left", padx=10)

def send_message():
    message = user_input.get()
    if message.strip() == "":
        return
    chat_display.configure(state="normal")
    chat_display.insert("end", f"🧍 You: {message}\n")
    chat_display.see("end")

    response = ask_gpt(message)
    chat_display.insert("end", f"🤖 Bot: {response}\n\n")
    chat_display.configure(state="disabled")
    chat_display.see("end")

    user_input.delete(0, "end")

send_btn = ctk.CTkButton(input_frame, text="Send", command=send_message)
send_btn.pack(side="left")

app.mainloop()
