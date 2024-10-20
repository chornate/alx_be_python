def safe_divide(numerator, denominator):
    try:
        # Convert the inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform the division, handling division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."
        
        return f"The result of the division is {numerator / denominator}"

    except ValueError:
        # Handles non-numeric input
        return "Error: Please enter numeric values only."
