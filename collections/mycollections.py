#1 count
from collections import Counter
animals = ['cat', 'dog', 'rat', 'donkey', 'cat', 'donkey', 'cat']
count = Counter(animals)
print(count)

#2 namedtuple
from collections import namedtuple
details=namedtuple('details',['name','percentage','grade'])
x=details(name='pooja',percentage=89,grade='B')
print(x.name)
print(x[1])
print(x._asdict)

#3 deque
from collections import deque
dq = deque(['a', 'b', 'c'])

dq.append('d')
print("After append:", dq)
dq.appendleft('z')
print("After appendleft:", dq)
dq.pop()
print("After pop:", dq)
dq.popleft()
print("After popleft:", dq)

#4 defaultdict
from collections import defaultdict
count=defaultdict(int)
watch=['titan','fasttrack','sonata','zimson','fasttrack','sonata']
for word in watch:
    count[word] +=1
print(count)

#5 ordereddict
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

#6 chainmap
from collections import ChainMap
dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}
combined = ChainMap(dict1, dict2)
print(combined['x'])  
 






















