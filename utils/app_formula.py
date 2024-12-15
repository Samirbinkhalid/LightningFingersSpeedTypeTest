def calculate_accuracy(matched, unmatched, missing):
    total_characters = matched + unmatched + missing
    if total_characters == 0:
        return 0  # Avoid division by zero; handle as needed.
    accuracy = (matched / total_characters) * 100
    return round(accuracy, 2)  # Return accuracy as a percentage rounded to 2 decimal places
