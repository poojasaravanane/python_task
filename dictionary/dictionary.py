##1 char of string
user_input = input("enter string: ")
char_count={}
for char in user_input:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
print("character of string is : ",char_count)        

##2 clear 
std={"name":"anu",
     "age":8,
     "sec":"a"}
std.clear()
print(std)

##3 copy
original_dict = {'a': 1, 'b': 2}
copied_dict = original_dict.copy()
print(copied_dict)

##4 fromkeys 
a = ("hi","hey","hello")
b = ("good morning")
c = dict.fromkeys(a,b)
print(c)

##5 get 
channel={
    "name": "sun tv",
    "year":2013,
    "acc":"media ant"
    }
channels = channel.get("acc")
print(channels)

##6 items 
channel={
    "name": "sun tv",
    "year":2003,
    "acc":"media ant"
    }
x = channel.items()
print(x)

##7 keys 
channel={
    "name": "sun tv",
    "year":1993,
    "acc":"media ant"
    }
v = channel.keys()
print(v)

##8 pop 
channels={
    "name": "sun tv",
    "year":1993,
    "acc":"media ant"
    }
channels.pop("acc")
print(channels)

##9 popitem 
channel2={
    "name": "sun tv",
    "year":1993,
    "acc":"media ant"
    }
channel2.popitem()
print(channel2)

##10 setdefault 
channel3={
    "name": "sun tv",
    "year":2004,
    "acc":"media ant"
    }
z = channel3.setdefault("rate","not here")
print(z)

##11 update 
channel3={
    "name": "sun tv",
    "acc":"media ant"
    }
channel3.update({"year":2004,})
print(channel3)

##12 values 
channel3={
    "name": "sun tv",
    "year":2004,
    "acc":"media ant"
    }
f = channel3.values()
print(f)
