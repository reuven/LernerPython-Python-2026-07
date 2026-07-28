import hashlib
import random
import time

def heavy_hash(n):
    m = hashlib.sha256()  # initialize the hashing machine
    results = f'!{n}!'.encode()
    for _ in range(100_000):
        m.update(results)
    return m.hexdigest()

if __name__ == '__main__':
    random.seed(0)
    numbers = [random.randint(-10_000_000, 10_000_000)
               for i in range(1000)]

    output = []
    print('Starting')
    start_time = time.time()

    for one_number in numbers:
        output.append(heavy_hash(one_number))

    print('Ending')
    end_time = time.time()

    total_time = end_time - start_time
    print(f'{total_time=}')
