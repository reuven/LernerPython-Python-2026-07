import time

def download_file(file_id):
    print(f'Starting to download {file_id}')
    time.sleep(2)
    print(f'Done downloading {file_id}')
    return f'file_{file_id}.txt'

if __name__ == '__main__':
    start_time = time.time()

    for i in range(5):
        result = download_file(i)
        print(result)

    end_time = time.time()

    total_time = end_time - start_time
    print(f'{total_time=}')
