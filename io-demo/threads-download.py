from concurrent.futures import ThreadPoolExecutor
import time

def download_file(file_id):
    print(f'Starting to download {file_id}')
    time.sleep(2)
    print(f'Done downloading {file_id}')
    return f'file_{file_id}.txt'

if __name__ == '__main__':
    start_time = time.time()

    output = []
    with ThreadPoolExecutor(max_workers=500) as e:
        for i in range(1000):
            output.append(e.submit(download_file, i))

    output = [one_result.result()
              for one_result in output]

    end_time = time.time()

    total_time = end_time - start_time
    print(f'{total_time=}')
