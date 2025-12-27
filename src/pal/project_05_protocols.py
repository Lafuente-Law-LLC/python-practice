from typing import Any, Iterable


class Countdown:

    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration

        val = self.current

        self.current -= 1

        return val

    def __bool__(self):
        return bool(self.current)


def manual_for_loop(iterable: Iterable) -> list:
    results = []

    iterator = iter(iterable)

    while True:
        try:
            item = next(iterator)
            results.append(item)
        except StopIteration:
            break

    return results
