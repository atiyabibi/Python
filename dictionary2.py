#2nd program
word=input()
print(word)
store=dict()

for ch in word:
    if ch not in store:
        store[ch]=1
    else:
        store[ch]=store[ch]+1
print(store)   

Output
aabcdbefghccde
{'a': 2, 'b': 2, 'c': 3, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1}


