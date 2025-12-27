
class Divider:
    def __init__(self, numerator):
        self.numerator = numerator

    def divide(self, denominator):
        try:
            result = self.numerator / denominator
            return result
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        except TypeError:
            return "Error: Denominator must be a number."
        else:
            return "Error: Denominator must be a number - others."


# Example usage:
divider = Divider(10)
print(divider.divide(2))    # Output: 5.0
print(divider.divide(0))    # Output: Error: Cannot divide by zero.
print(divider.divide("a"))  # Output: Error: Denominator must be a number.
print(divider.divide("_"))
