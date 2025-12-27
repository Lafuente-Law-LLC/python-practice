from typing import Any


def spy_log(message: str, history: list = []) -> list:
    history.append(message)
    return history


def clean_log(message: str, history: list | None = None) -> list:
    if history is None:
        history = []
    history.append(message)
    return history


def inspect_defaults(func: Any) -> tuple | None:
    return func.__defaults__
