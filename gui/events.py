import tkinter as tk
from logic.results import end_program

"""
This module handles events, including key press handling and the timer countdown.
"""

timer_instance = None


def bind_events(root, widgets, sentence):
    """
    Binds key press events to the application and handles user input.

    Args:
        root (tk.Tk): The main Tkinter application window.
        widgets (dict): A dictionary containing the application's widgets.
        sentence (str): The target sentence for the typing test.
    """
    def on_key_press(event):
        """
        Handles user key presses, updates input and sentence display.

        Args:
            event (tk.Event): The key press event triggered by the user.
        """
        user_input = widgets['input_label'].cget("text")
        remaining_time = int(widgets['timer_label'].cget("text"))
        if event.char.isalpha() or event.char in [" ", "."]:
            user_input += event.char
            widgets['input_label'].config(text=user_input)
            update_sentence_label(widgets, sentence, user_input)
            if len(user_input) == len(sentence):  # Sentence completed
                end_program(root, widgets, sentence, user_input, remaining_time)
        elif event.keysym == "Return":  # User pressed Enter
            end_program(root, widgets, sentence, user_input, remaining_time)

    def update_sentence_label(widgets, sentence, user_input):
        """
        Updates the sentence label, highlighting matched and unmatched characters.

        Args:
            widgets (dict): A dictionary containing the application's widgets.
            sentence (str): The target sentence for the typing test.
            user_input (str): The current input typed by the user.
        """
        widgets['sentence_label'].config(state="normal")
        widgets['sentence_label'].delete("1.0", tk.END)

        for i, char in enumerate(sentence):
            if i < len(user_input):
                if user_input[i] == char:
                    widgets['sentence_label'].insert(tk.END, char, "green")
                else:
                    widgets['sentence_label'].insert(tk.END, char, "red")
            else:
                widgets['sentence_label'].insert(tk.END, char)

        widgets['sentence_label'].tag_add("center", "1.0", "end")
        widgets['sentence_label'].config(state="disabled")

    root.bind("<KeyPress>", on_key_press)


def start_timer(root, widgets, sentence):
    """
    Starts the countdown timer and ends the test when the timer reaches zero.

    Args:
        root (tk.Tk): The main Tkinter application window.
        widgets (dict): A dictionary containing the application's widgets.
        sentence (str): The target sentence for the typing test.
    """
    def countdown():
        """
        Counts down the timer and updates the timer label.
        """
        remaining_time = int(widgets['timer_label'].cget("text"))
        if remaining_time > 0:
            widgets['timer_label'].config(text=str(remaining_time - 1))
            global timer_instance
            timer_instance = root.after(1000, countdown)  # Schedule the next countdown after 1 second
        else:
            widgets['timer_label'].config(text="Time's up!")
            end_program(root, widgets, sentence, widgets['input_label'].cget("text"), remaining_time)

    countdown()


def stop_timer(root):
    """
    Stops the running timer.
    """
    global timer_instance
    if timer_instance:
        root.after_cancel(timer_instance)  # Cancel the scheduled callback
        timer_instance = None
