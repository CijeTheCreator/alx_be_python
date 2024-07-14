def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            return "Error: Cannot divide by zero."

        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."

