from tkinter import messagebox

from utils.app_formula import calculate_accuracy


def end_program(root, widgets, sentence, user_input, remaining_time):
    """
    Ends the typing test, calculates results, and displays them in a popup.

    Args:
        root (tk.Tk): The main Tkinter application window.
        widgets (dict): A dictionary containing the application's widgets.
        sentence (str): The target sentence for the typing test.
        user_input (str): The input typed by the user.
    """
    matched = sum(1 for i, char in enumerate(user_input) if i < len(sentence) and char == sentence[i])
    unmatched = len(user_input) - matched
    missing = len(sentence) - len(user_input)

    result_message = f"""
        
        Incorrect Characters: {unmatched}
        Missing Characters: {missing}
        Remaining Time: {remaining_time}
        
        WPM: {matched} 
        Accuracy: {calculate_accuracy(matched, unmatched, missing)}
    """

    # Stop the timer before displaying the result
    from gui.events import stop_timer
    stop_timer(root)

    messagebox.showinfo("Results", result_message)
    root.destroy()
