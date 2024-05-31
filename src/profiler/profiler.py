import time


def timer(func):
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        print("Raw runtime: ", run_time)
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return result

    return wrap
