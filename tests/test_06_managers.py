import pytest

from pal import project_06_managers


def test_context_manager_commit():
    db = project_06_managers.MockDB({"balance": 100})
    with db:
        db.data["balance"] = 200

    assert db.data["balance"] == 200
    assert db.exit_run is True


def test_context_manager_rollback():
    db = project_06_managers.MockDB({"balance": 100})

    with pytest.raises(ValueError):
        with db:
            db.data["balance"] = 9999
            raise ValueError("Transaction failed!")

    assert db.data["balance"] == 100
    assert db.exit_run is True


def test_manual_transaction_equivalence():
    db = project_06_managers.MockDB({"balance": 100})

    def transaction_logic(database):
        database.data["balance"] = 500
        raise RuntimeError("Manual failure")

    with pytest.raises(RuntimeError):
        project_06_managers.transaction_manual(db, transaction_logic)

    assert db.data['balance'] == 100
