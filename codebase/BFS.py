from map import MAP


# nrow=6
# ncol=6
# obstacles = [(2,1),(3,1),(4,1),(2,2),(2,3),(2,4),(3,4),(4,4)]
# # obstacles = [(1,2),(3,2),(4,2),(3,1),(3,4)]
# start = (5,2)
# goal  = (0,3)

# # start = (0,5)
# # goal = (3,2)



nrow=12
ncol=12
obstacles = [(2,2),(2,3),(2,4),(4,2),(4,3),(4,4),
             (5,12),(6,12),(7,12),(8,12),(9,12),
             (5,8),(6,8),(7,8),(8,8),(9,8),
             (8,4),(8,5),(8,6),(8,7),(8,8),
             (16,13),(16,13),(16,16),(16,17),(16,18),
             (3,6),(3,7),(3,8),(3,9),(3,10)];
start = (0,0)
goal = (10,6)




# action_cost = {(0,1):1,(0,-1):1,(1,0):1,(-1,0):1}
action_cost = {(0,1):1,(0,-1):1,(1,0):1,(-1,0):1,
               (1,1):1.4, (1,-1):1.4,(-1,1):1.4,(-1,-1):1.4}



maps = MAP(nrow, ncol, start, goal, obstacles)

fig = maps.plot_map()
fig.show(True)


def get_neighbour_costs(vertex):
    neighbour_costs = {}
    x = vertex[0]
    y = vertex[1]
    for action in action_cost:
        dx = action[0]
        dy = action[1]
        x_neighbour = x+dx
        y_neighbour = y+dy

        if x_neighbour in range(0,ncol):
            if y_neighbour in range(0,nrow):
                if (x_neighbour, y_neighbour) not in obstacles:
                    neighbour_costs[(x_neighbour,y_neighbour)] = cost_map[vertex] + action_cost[action]

    return neighbour_costs


### starting BFS Algorithm

cost_map  = {start:0}
parent_map= {start:None}
Q = [start]

while Q != []:
    # exploit frontier
    frontier = Q.pop(0)
    frontier_cost= cost_map[frontier]
    maps.set_node(*frontier,state='red',f=frontier_cost)

    # explore frontier
    neighbour_costs = get_neighbour_costs(frontier)

    for neighbour in neighbour_costs:
        new_cost = neighbour_costs[neighbour]
        if neighbour in cost_map:
            if cost_map[neighbour] <= new_cost:   # travelling cost
                continue
            else:
                cost_map[neighbour] = new_cost
                parent_map[neighbour]= frontier
                maps.set_node(*neighbour, state='green',f=new_cost)
                continue

        Q.append(neighbour)
        cost_map[neighbour]  =new_cost
        parent_map[neighbour]=frontier
        maps.set_node(*neighbour, state='green',f=new_cost)

        if neighbour == goal:
            break
    if neighbour == goal:
        break


# retrace path
parent = goal
while parent is not None:
    if parent==start:
        maps.set_node(*parent, state='blue', f=cost_map[parent], stop=True)
    else:
        maps.set_node(*parent, state='blue', f=cost_map[parent])

    child  = parent
    parent = parent_map[child]



print(cost_map)


