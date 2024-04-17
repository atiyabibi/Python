#Dictionaries 

#ist program
word=input()
print(word)
store=dict()
print(store)
store['p']=23
store['Q']=12
store['s']=15
store[26]=88
store["hi"]=55
store['a']='hello'
print(store)
allkeys=store.keys()
print(allkeys)
#for each loops
for ele in allkeys:
    print(ele)
for ch in "abcdef":
    print(ch)
for val in[12,13,14,15,16,17]:
    print(val)
for key in ['a','b,15,16,18']:
    print(key,end=" ")

Output
dictionaries
{}
{'p': 23, 'Q': 12, 's': 15, 26: 88, 'hi': 55, 'a': 'hello'}
dict_keys(['p', 'Q', 's', 26, 'hi', 'a'])
p
Q
s
26
hi
a
a
b
c
d
e
f
12
13
14
15
16
17
a b,15,16,18 



