"""A basic calculator module.""" 
 
class Calculator: 
    """Performs arithmetic operations.""" 
    def add(self, a, b): 
        """Returns the sum of two numbers.""" 
        return a + b 
    def subtract(self, a, b): 
        """Returns the difference of two numbers.""" 
        return a - b 
    def multiply(self, a, b): 
        """Returns the product of two numbers.""" 
        return a * b 
    def divide(self, a, b): 
        """Returns the quotient of two numbers.""" 
        if b == 0: 
            raise ValueError("Cannot divide by zero") 
        return a / b 
