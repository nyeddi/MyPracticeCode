def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    print names
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        print 
        print label,name, people
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]
            #print data
        #print data

if __name__ == '__main__':
    storage = {}
    init(storage)
    store(storage,'raji jddd sjfkd')
    store(storage,'raj kum red')
    print lookup(storage,'middle','kum')
