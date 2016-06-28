def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    print names
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        if name in data[label]:
            data[label][name].append(full_name)
        else:
            data[label][name] = [full_name]
         
            
if __name__ == '__main__':
    storage = {}
    init(storage)
    store(storage,'raji jddd sjfkd')
    store(storage,'raj kum red')
    print lookup(storage,'middle','kum')
