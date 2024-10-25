import time

fn main():
    start = time.perf_counter_ns()
    print('hello world')
    end = time.perf_counter_ns()
    
    elapsed_time = end - start
    print("start: ", start)
    print("end: ", end)
    print("elasped time: ", elapsed_time)

