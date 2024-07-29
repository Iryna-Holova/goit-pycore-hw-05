"""
Task 2. Generator numbers
"""

from typing import Generator, Callable
import re


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Generator that iterates over all the valid numbers in the text and yields
    them.

    Args:
        text (str): The text to be analyzed.

    Yields:
        float: The next valid number in the text.
    """
    pattern = r"\b\d+(?:\.\d+)?\b"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)


def sum_profit(
    text: str,
    func: Callable[[str], Generator[float, None, None]]
) -> float:
    """
    Calculates the total income from the valid numbers in the text
    using the provided function.

    Args:
        text (str): The text to be analyzed.
        func (Callable): The function that generates the valid numbers.

    Returns:
        float: The total income from valid numbers in the text.
    """
    total = 0
    for number in func(text):
        total += number
    return total


if __name__ == "__main__":
    example_text = "The total income of the employee consists of several \
        parts: 1000.01 as the main income, supplemented by additional \
        revenues of 27.45 and 324.00 dollars."
    total_income = sum_profit(example_text, generator_numbers)
    print(f"Total income: {total_income}")
