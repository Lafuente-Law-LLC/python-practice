from __future__ import annotations


class ObjectAuditor:

    """
    Project 1 - Binding vs Equality Auditor

    Required:
    -

    """

    def audit(self, a, b) -> dict:
        out = {
            "id_a": id(a),
            "id_b": id(b),
            "type_a": type(a),
            "type_b": type(b),
            "is_alias": (a is b),
        }

        try:
            out["is_equal"] = (a == b)
        except Exception:
            out["is_equal"] = None

        return out

    def explain(self, a, b) -> str:
        r = self.audit(a, b)

        if r["is_alias"]:
            eq = r["is_equal"]
            eq_clause = ()
