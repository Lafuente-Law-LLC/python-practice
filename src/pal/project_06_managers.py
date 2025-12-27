import copy
from typing import Callable, Any


class MockDB:
    def __init__(self, data: dict):
        self.data = data
        self.snapshot: dict | None = None
        self.exit_run = False

    def __enter__(self):
        self.snapshot = copy.deepcopy(self.data)
        self.exit_run = False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit_run = True

        if exc_type:
            self.data = self.snapshot
            print("Rollback performed.")

        else:
            print("Commit successfull.")
            pass


def transaction_manual(db: MockDB, fn: Callable[[MockDB], None]) -> None:
    snapshot = copy.deepcopy(db.data)

    try:
        fn(db)
        print("Commit successful.")
    except Exception:
        db.data = snapshot
        print("Rollback")
        raise
    finally:
        pass
