import tkinter as tk


def create_widgets(root):
    """
    Creates and configures all widgets used in the application.

    Args:
        root (tk.Tk): The main Tkinter application window.

    Returns:
        dict: A dictionary containing all the created widgets.
    """
    # Fonts and colors for styling
    font_main = ("Arial", 18)
    font_secondary = ("Arial", 16)
    text_color = "#D3D3D3"
    timer_color = "#FFAB40"
    highlight_green = "#8FFF8F"
    highlight_red = "#FF6F6F"

    # Create the sentence display widget
    sentence_label = tk.Text(
        root,
        font=font_main,
        height=2,
        wrap="word",
        state="disabled",
        bg="#2C2C2C",
        fg=text_color,
        bd=0
    )
    sentence_label.tag_configure("green", foreground=highlight_green)
    sentence_label.tag_configure("red", foreground=highlight_red)
    sentence_label.tag_configure("center", justify="center")
    sentence_label.pack(pady=40, fill="x")

    # Create the user input display widget
    input_label = tk.Label(
        root,
        text="",
        font=font_secondary,
        fg="#ADD8E6",  # Light blue text
        bg="#2C2C2C",
        wraplength=700,
        justify="center"
    )
    input_label.pack(pady=20)

    # Create the timer display widget
    timer_label = tk.Label(
        root,
        text="60",  # Initial timer value
        font=font_secondary,
        fg=timer_color,
        bg="#2C2C2C"
    )
    timer_label.place(relx=0.95, rely=0.95, anchor="se")  # Position at bottom-right

    # Return all widgets as a dictionary
    return {
        "sentence_label": sentence_label,
        "input_label": input_label,
        "timer_label": timer_label
    }
