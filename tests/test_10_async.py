import pytest
import asyncio
import time

from pal import project_10_async

def test_async_is_single_threaded():
    delays = [0.01, 0.01, 0.01]
    result = asyncio.run(project_10_async.run(delays))
    thread_ids = result['thread_ids']

    assert len(set(thread_ids)) == 1
    assert len(thread_ids) == 3

def test_concurrency_scaling():
    delays = [0.1, 0.1, 0.1]

    stats = asyncio.run(project_10_async.run(delays))
    elapsed = stats['elapsed']

    assert elapsed < sum(delays)
    assert elapsed >= max(delays)

    overhead_margin = 0.05
    assert elapsed < max(delays) + overhead_margin

