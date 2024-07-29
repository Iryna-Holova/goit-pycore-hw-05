# Python Task Solutions

This repository contains solutions for various tasks implemented in Python. Each task is presented in a separate file.

Task List:

1. Caching Fibonacci
2. Generator Numbers
3. Count Logs by Level
4. Console Bot with Error Handling

## Task 1: Caching Fibonacci

[**File:** `task_1.py`](./task_1.py)

### Description:

This task implements a function to calculate Fibonacci numbers using caching to improve performance by storing previously computed values.

### Usage:

```python
from task_1 import caching_fibonacci

fib = caching_fibonacci()
print(fib(10)) # Outputs: 55
print(fib(15)) # Outputs: 610
```

## Task 2: Generator Numbers

[**File:** `task_2.py`](./task_2.py)

### Description:

This task includes a generator function that iterates over all valid numbers in a text and yields them. Additionally, a function is provided to calculate the total income from the valid numbers in the text.

### Usage:

```python
from task_2 import generator_numbers, sum_profit

example_text = (
"The total income of the employee consists of several parts: "
"1000.01 as the main income, supplemented by additional revenues "
"of 27.45 and 324.00 dollars."
)
total_income = sum_profit(example_text, generator_numbers)
print(f"Total income: {total_income}") # Outputs: Total income: 1351.46
```

## Task 3: Count Logs by Level

[**File:** `task_3.py`](./task_3.py)

### Description:

This task processes log files, parses them into structured data, and provides functionalities to count and filter logs by their levels.

### Usage:

```bash
python task_3.py <log_file> [<log_level>]
```

### Example

example.log

```log
2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
```

```bash
python task_3.py example.log error

Level     | Count
----------|--------
DEBUG     | 3
ERROR     | 2
WARNING   | 1
INFO      | 4

Filtered logs by level: ERROR
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
```

_Ensure to replace `example.log` with the actual path to your log file._

## Task 4: Console Bot with Error Handling

[**File:** `task_4.py`](./task_4.py)

### Description:

This task implements a console bot that handles various commands and processes user input. The bot is enhanced with error handling using decorators to manage user input errors gracefully.

### Usage:

1. Run the script `task_4.py`:

```bash
python task_4.py
```

2. Enter commands to interact with the phonebook.

### Commands

- `hello`: The bot will greet you and ask how it can help you.
- `add <name> <phone>`: Adds a contact with the given name and phone number. Example: `add John 123456789`.
- `change <name> <new_phone>`: Changes the phone number of the contact with the given name. Example: `change John 987654321`.
- `phone <name>`: Retrieves the phone number of the contact with the given name. Example: `phone John`.
- `all`: Lists all contacts with their phone numbers.
- `exit` or `close`: Exits the assistant bot.

### Example

```bash
Enter a command: add
Invalid input. Please provide name and phone number.
Enter a command: add Bob
Invalid input. Please provide name and phone number.
Enter a command: add Jim 0501234356
Contact added.
Enter a command: phone Jim
0501234356
Enter a command: all
Jim: 0501234356
Enter a command: exit
Good bye!
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
