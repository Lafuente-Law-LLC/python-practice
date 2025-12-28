import asyncio
import threading
import time


async def worker(delay: float) -> tuple[int, float]:
    tid = threading.get_ident()
    await asyncio.sleep(delay)
    return tid, delay

async def run(delays: list[float]) -> dict:

    start_time = time.perf_counter()
    tasks = [worker(d) for d in delays]

    results = await asyncio.gather(*tasks)
    end_time = time.perf_counter()

    thread_ids = [r[0] for r in results]

    return {
        'thread_ids': thread_ids,
        'elapsed': end_time - start_time,
        'results': results
    }
