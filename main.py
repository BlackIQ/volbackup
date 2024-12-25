from datetime import datetime

from utils.docker import get_mounts
from utils.zip import zip_directory
from utils.s3 import upload_file

def main():
    current_date: str = datetime.now().strftime('%Y-%m-%d')
    current_time: str = datetime.now().strftime('%H-%M-%S')

    mounts: dict = get_mounts()
        
    for container in mounts:
        container_name = container['container']
        
        for mount in container['mounts']:
            if mount['type'] == 'bind':
                source_dir = mount['source']
                destination_dir = mount['destination']
                
                without_first: str = destination_dir[1:]
                replaced_name = without_first.replace('/', '-')
                
                dir_data_path = current_date.replace('-', '/')
                dir_path = f'{container_name}/{dir_data_path}'

                file_name = f'{container_name}-{current_date}-{current_time}---{replaced_name}.zip'
                
                zip_directory(source_dir, f'./tmp/{file_name}')

                upload_file(f'./tmp/{file_name}', f'{dir_path}/{file_name}')
        
if __name__ == '__main__':
    main()
