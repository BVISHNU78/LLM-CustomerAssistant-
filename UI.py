import tkinter as tk
from tkinter import scrolledtext, simpledialog
import threading
import requests

API_URL = "http://localhost:8000/ask"

class SimpleChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chat with Meeting Booking")
        self.root.geometry("600x550")

        self.chat_area = scrolledtext.ScrolledText(root, state='disabled', wrap='word')
        self.chat_area.pack(padx=10, pady=10, fill='both', expand=True)

        bottom_frame = tk.Frame(root)
        bottom_frame.pack(fill="x", padx=10, pady=(0,10))

        self.entry = tk.Entry(bottom_frame, font=("Arial", 14))
        self.entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
        self.entry.bind('<Return>', self.send_message)

        self.send_btn = tk.Button(bottom_frame, text="Send", command=self.send_message)
        self.send_btn.pack(side='left', padx=(0,5))

        self.book_btn = tk.Button(bottom_frame, text="Book Meeting", command=self.book_meeting)
        self.book_btn.pack(side='left')

    def send_message(self, event=None):
        query = self.entry.get().strip()
        if not query:
            return
        self.entry.delete(0, tk.END)
        self.append_message("You", query)
        threading.Thread(target=self.get_response, args=(query,), daemon=True).start()

    def append_message(self, sender, message):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.see(tk.END)

    def get_response(self, query):
        try:
            response = requests.post(API_URL, json={"query": query})
            data = response.json()
            answer = data.get("answer", "No answer received.")
        except Exception as e:
            answer = f"Error: {e}"
        self.append_message("Assistant", answer)

    def book_meeting(self):
        date = simpledialog.askstring("Meeting Date", "Enter meeting date (YYYY-MM-DD):", parent=self.root)
        if not date:
            return
        time = simpledialog.askstring("Meeting Time", "Enter meeting time (HH:MM 24h):", parent=self.root)
        if not time:
            return
        duration = simpledialog.askstring("Duration", "Enter duration in minutes:", parent=self.root)
        if not duration:
            return

        meeting_info = f"Meeting booked on {date} at {time} for {duration} minutes."
        self.append_message("System", meeting_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleChatApp(root)
    root.mainloop()
