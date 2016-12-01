#print 'hello, word!'
#print 'it is my improvement'
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['end'] = {}
    return
stor = {}
init(stor)
#print stor
def lookup(data, label, name):
    return data[label].get(name)
me = 'xue chuan cong'  
stor['end'].setdefault('cong', []).append(me)    
lookup(stor, 'end', 'cong')
#print stor   
def store(data, full_name):
    names = full_name.split()
    labels = ('first', 'middle', 'end') 
    if len(names) == 2:
        names.insert(1, '')
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            data['label'].append(full_name)
        else:
            data[label][name] = [full_name]
            
myname = {}
init(myname)
store(myname, 'xue chuan cong')
lookup(myname, 'end', 'cong')   
print myname     
        
        
        
        
        
        
        
        
        
        