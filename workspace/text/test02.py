def lookup(data, label, name):
    return data[label].get(name)

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['end'] = {}
    
stor = {}
init(stor)
#print stor
stor['first'].setdefault('xue', []).append('xue chuan cong')
#print lookup(stor, 'first', 'xue')
#print stor
def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        labels = ('first', 'middle', 'end')
        if len(names) == 2: names.insert(1, '')
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

myname = {}
init(myname)
print myname
store(myname, 'xue chuan cong', 'xi jin ping', 'deng xiao ping')
print lookup(myname, 'end', 'cong')
print lookup(myname, 'end', 'ping')







                  
    