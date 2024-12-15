import tkinter as tk
from gui.widgets import create_widgets
from logic.difficulty import select_difficulty
from gui.events import bind_events, start_timer

"""
Main entry point for the Typing Test application.
"""

if __name__ == "__main__":
    # Initialize the main Tkinter application window
    root = tk.Tk()
    root.title("Lightning Fingers - Speed Type Test")
    root.geometry("800x500")
    root.config(bg="#2C2C2C")  # Set a dark theme for the application

    # Create all necessary widgets for the application
    widgets = create_widgets(root)

    # Display the difficulty selection popup and get the sentence
    sentence = select_difficulty(root)

    # Populate the initial sentence in the sentence label
    widgets['sentence_label'].config(state="normal")
    widgets['sentence_label'].delete("1.0", tk.END)
    widgets['sentence_label'].insert("1.0", sentence)
    widgets['sentence_label'].tag_add("center", "1.0", "end")
    widgets['sentence_label'].config(state="disabled")

    # Bind key press events and start the timer
    bind_events(root, widgets, sentence)
    start_timer(root, widgets, sentence)

    # Run the Tkinter main event loop
    root.mainloop()
