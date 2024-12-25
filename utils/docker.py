import docker

def get_mounts():
    client = docker.from_env()
    
    items = []
    
    for container in client.containers.list(all=True):
        item = {
            'container': container.name,
            'mounts': []
        }
        
        mounts = container.attrs['Mounts']
                                
        for mount in mounts:
            mount_item = {}
            
            mount_item['type'] = mount['Type']
            mount_item['source'] = mount['Source']
            mount_item['destination'] = mount['Destination']
            
            item['mounts'].append(mount_item)
            
        items.append(item)
        
    return items
