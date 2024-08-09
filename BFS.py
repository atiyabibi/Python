tree={
    1:[2,9,10],
    2:[3,4],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[8],
    8:[],
    9:[],
    10:[]
}
def bfs(tree,start):
    q=[start]
    visited=[]
    while q:
        print("Before:",q)
        node=q.pop(0)
        visited.append(node)
        for child in (tree[node]):
            if child not in q and child not in visited:
                q.append(child)
        print("After:",q)
    return visited
res=bfs(tree,1)
print(res)


