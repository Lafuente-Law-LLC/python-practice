import inspect

snapshots: list[dict] = []


def factorial(n: int):

    snapshot(tag=f"entry_n_{n}")

    if n <= 0:
        return 1
    else:
        return (n * factorial(n - 1))


def snapshot(tag: str | None = None) -> None:
    stack = inspect.stack()
    if len(stack) < 2:
        return

    caller_frame_info = stack[1]

    func_name = caller_frame_info.function
    frame_object = caller_frame_info.frame

    local_vars = frame_object.f_locals.copy()

    snapshots.append({'function': func_name, 'depth': len(
        stack), 'locals': local_vars, 'tag': tag})

    del frame_object
