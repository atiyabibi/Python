global facts
global rules
rules=True
facts=[['plant','mango'],['eating','mango'],['seed','sprouts']]
def assert_fact(fact):
    global facts
    global rules
    if not fact in facts:
        facts+=[fact]
        rules=True
while rules:
    rules=False
    for a1 in facts:
        if a1[0]=='seed':
            assert_fact(['plant',a1[1]])
        if a1[0]=='plant':
            assert_fact(['fruit',a1[1]])
        if a1[0]=='plant' and ['eating',a1[1]] in facts:
            assert_fact(['human',a1[1]])
print(facts)
