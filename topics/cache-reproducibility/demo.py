"""Deterministic illustration using synthetic inputs only."""

import json


def count_work(requests):
    combined, transforms, audits = set(), set(), set()
    for coords, transform_version, audit_version in requests:
        transform_key = (coords, transform_version)
        audit_key = (transform_key, audit_version)
        combined.add(audit_key)
        transforms.add(transform_key)
        audits.add(audit_key)
    return {
        "combined": {"transform": len(combined), "audit": len(combined)},
        "split": {"transform": len(transforms), "audit": len(audits)},
    }


if __name__ == "__main__":
    requests = [
        ((10, 20), "tx1", "audit1"),
        ((10, 20), "tx1", "audit1"),  # Exact repeat.
        ((10, 20), "tx1", "audit2"),  # Only the audit changes.
        ((10, 20), "tx2", "audit2"),  # Both keys must invalidate.
    ]
    result = count_work(requests)
    assert result == {
        "combined": {"transform": 3, "audit": 3},
        "split": {"transform": 2, "audit": 3},
    }, result
    print(json.dumps(result, sort_keys=True))
