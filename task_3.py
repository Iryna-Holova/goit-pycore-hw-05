"""
Task 3. Count logs by level
"""

import sys


def parse_log_line(line: str) -> dict:
    """
    Parses a log line into a dictionary with the following keys:
    date, time, level, message.

    Args:
        line (str): The log line to parse.

    Returns:
        dict: A dictionary containing the parsed log data.

    Raises:
        ValueError: If the log line is invalid.
    """
    try:
        date, time, level, *message = line.split()
        return {
            "date": date,
            "time": time,
            "level": level.upper(),
            "message": " ".join(message),
        }
    except ValueError:
        print(f"Invalid log line: {line}")
        return {}


def load_logs(file_path: str) -> list:
    """
    Loads log lines from a file and parses them into a list of dictionaries.

    Args:
        file_path (str): The path to the log file.

    Returns:
        list: A list of dictionaries containing the parsed log data.

    Raises:
        FileNotFoundError: If the log file cannot be found.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            logs_list = [parse_log_line(line) for line in file if line.strip()]
            return [log for log in logs_list if log]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters the list of logs by the specified level.

    Args:
        logs (list): A list of dictionaries containing log data.
        level (str): The level to filter by.

    Returns:
        list: A list of dictionaries containing only logs with the specified
        level.
    """
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list) -> dict:
    """
    Counts the number of logs by level in the list of logs.

    Args:
        logs (list): A list of dictionaries containing log data.

    Returns:
        dict: A dictionary containing the count of logs by level.
    """
    return {
        level: len([log for log in logs if log["level"] == level])
        for level in set(log["level"] for log in logs)
    }


def display_log_counts(counts: dict) -> None:
    """
    Displays the count of logs by level in the console.

    Args:
        counts (dict): A dictionary containing the count of logs by level.
    """
    print(f"\n{'Level':10}| Count")
    print(f"{'-'*10}|{'-'*8}")
    for level, count in counts.items():
        print(f"{level:10}| {count}")


def display_logs(logs: list) -> None:
    """
    Displays the list of logs in the console.

    Args:
        logs (list): A list of dictionaries containing log data.
    """
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main() -> None:
    """
    Main function that loads logs, filters by level, and displays the results.
    """
    if len(sys.argv) < 2:
        print("Usage: python task_3.py <log_file>")
        sys.exit(1)

    path = sys.argv[1]
    logs_list = load_logs(path)

    if len(logs_list) == 0:
        print("No logs found")
        sys.exit(1)

    log_counts = count_logs_by_level(logs_list)
    display_log_counts(log_counts)

    if len(sys.argv) >= 3:
        log_level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs_list, log_level)
        print(f"\nFiltered logs by level: {log_level}")
        display_logs(filtered_logs)


if __name__ == "__main__":
    main()
