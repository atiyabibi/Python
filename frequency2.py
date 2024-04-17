#4th program
#To find minimum frequency
word=input()
print(word)
store=dict()
for ch in word:
    if ch not in store:
        store[ch]=1
    else:
        store[ch]=store[ch]+1
print(store)   
resultchar='#'
resfrequency=100
dickeys=store.keys()
for ele in dickeys:
    if resfrequency>store[ele]:
        resfrequency=store[ele]
        resultchar=ele
print(resultchar,resfrequency)

Output
aabcdbefccde
{'a': 2, 'b': 2, 'c': 3, 'd': 2, 'e': 2, 'f': 1}
f 1
