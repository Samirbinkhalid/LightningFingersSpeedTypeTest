import tkinter as tk
import random
import json

"""
Handles difficulty selection and sentence retrieval logic.
"""

SENTENCES_FILE_PATH = "config/sentences.json"


def load_sentences():
    """
    Loads sentences from a JSON file.

    Returns:
        dict: A dictionary containing sentences categorized by difficulty.
    """
    try:
        with open(SENTENCES_FILE_PATH, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading sentences: {e}")
        return {
            'easy': ['The cat sat on the mat.'],
            'medium': ['The curious fox jumped over the tall fence.'],
            'hard': ['The extraordinary performance by the orchestra left the audience in awe.']
        }


sentences_dict = load_sentences()


def select_difficulty(root):
    """
    Displays a difficulty selection popup and retrieves the selected sentence.

    Args:
        root (tk.Tk): The main Tkinter application window.

    Returns:
        str: A randomly selected sentence based on the chosen difficulty level.
    """
    def set_difficulty(level):
        nonlocal selected_sentence
        selected_sentence = random.choice(sentences_dict[level])
        difficulty_window.destroy()

    selected_sentence = None
    difficulty_window = tk.Toplevel(root)
    difficulty_window.title("Select Difficulty")
    difficulty_window.geometry("300x200")
    difficulty_window.config(bg="#2C2C2C")

    tk.Label(
        difficulty_window, text="Select Difficulty Level", font=("Arial", 14), fg="#D3D3D3", bg="#2C2C2C"
    ).pack(pady=20)

    tk.Button(
        difficulty_window, text="EASY", font=("Arial", 12), fg="#ADD8E6", bg="#444444",
        command=lambda: set_difficulty('easy'), width=10, bd=0
    ).pack(pady=5)

    tk.Button(
        difficulty_window, text="MEDIUM", font=("Arial", 12), fg="#FFAB40", bg="#444444",
        command=lambda: set_difficulty('medium'), width=10, bd=0
    ).pack(pady=5)

    tk.Button(
        difficulty_window, text="HARD", font=("Arial", 12), fg="#FF6F6F", bg="#444444",
        command=lambda: set_difficulty('hard'), width=10, bd=0
    ).pack(pady=5)

    difficulty_window.transient(root)
    difficulty_window.grab_set()
    root.wait_window(difficulty_window)
    return selected_sentence
