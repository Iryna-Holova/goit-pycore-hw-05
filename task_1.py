"""
Task 1. Caching fibonacci
"""

from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """
    Creates and returns a function to calculate Fibonacci numbers using
    caching.

    Returns:
        Callable[[int], int]: A function that calculates the n-th Fibonacci
        number.
    """
    cache = {}

    def fibonacci(n: int) -> int:
        """
        Calculates the n-th Fibonacci number using recursion and caching.

        Args:
            n (int): The position of the Fibonacci number to calculate.

        Returns:
            int: The n-th Fibonacci number.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()

    # Example usage
    print(fib(10))  # Outputs: 55
    print(fib(15))  # Outputs: 610
