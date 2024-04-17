#3rd program
#To find the maximum frequency of string
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
resfrequency=0
dickeys=store.keys()
for ele in dickeys:
    if store[ele]>resfrequency:
        resfrequency=store[ele]
        resultchar=ele
print(resultchar,resfrequency)

Output
aabcdbefghccde
{'a': 2, 'b': 2, 'c': 3, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1}
c 3

