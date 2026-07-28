from concurrent.futures import ThreadPoolExecutor
import time
import random

random.seed(0)

def wait_a_bit():
    time.sleep(random.randint(0, 5))
    return 'done'
    
if __name__ == '__main__':
    start_time = time.time()

    output = []
    with ThreadPoolExecutor(max_workers=1000) as e:
        for i in range(1000):
            output.append(e.submit(wait_a_bit))

    output = [one_result.result()
              for one_result in output]

    end_time = time.time()

    total_time = end_time - start_time
    print(f'{total_time=}')
