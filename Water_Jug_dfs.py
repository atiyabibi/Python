def water_jug_dfs(capacity_x,capacity_y,target):
    stack=[(0,0,[])]
    visited_states=set()
    while stack:
        x,y,path=stack.pop()
        if (x,y) in visited_states:
            continue
        visited_states.add((x,y))
        if x==target or y==target:
            return path+[(x,y)]
        operations={
            ("fill_x",capacity_x,y),
            ("fill_y",x,capacity_y),
            ("empty_x",0,y),
            ("empty_y",x,0),
            ("pour_x_to_y",max(0,x-(capacity_y-y)),min(capacity_y,y+x)),
            ("pour_y_to_x",min(capacity_x,x+y),max(0,y-(capacity_x-x)))
        }
        for operation,new_x,new_y in operations:
            if 0<=new_x<=capacity_x and 0<=new_y<=capacity_y:
                stack.append((new_x,new_y,path+[(x,y,operation)]))
    return None
capacity_x=4
capacity_y=3
target=2
solution=water_jug_dfs(capacity_x,capacity_y,target)
if solution:
     print("solution found")
     for state in solution:
         print(f'({state[0]},{state[1]})')
else:
    print("No solution")
