from map import MAP
from math import sqrt

nrow=20
ncol=20

obstacles = [(2,1),(3,1),(4,1),(2,2),(2,3),(2,4),(3,4),(4,4),
             (7,8), (9,12), (10,8), (9,9), (0,9), (1,9), (2,9),(3,9), (4,9), (5,9), (6,9), (7,9), (8,9),
             (10,9),(11,9), (12,9), (13,9), (14,9), (15,9), (16,9), (17,9), (18,9),
             (19,5), (18,5), (17,5), (16,5), (15,5), (14,5), (13,5), (12,5), (11,5), (10,5),
             (11,13), (12,13), (13,13), (14,13), (15,13), (16,13), (17,13), (10,13),
             (13,11), (13,12), (13,13), (13,14), (13,15), (13,16), (13,17), (13,10)]

# obstacles = [(1,2),(3,2),(4,2),(3,1),(3,4)]

start = (0,1)
goal  = (3,12)

# start = (0,5)
# goal = (3,2)



# nrow=12
# ncol=12
# obstacles = [(2,2),(2,3),(2,4),(4,2),(4,3),(4,4),
#              (5,12),(6,12),(7,12),(8,12),(9,12),
#              (5,8),(6,8),(7,8),(8,8),(9,8),
#              (8,4),(8,5),(8,6),(8,7),(8,8),
#              (16,13),(16,13),(16,16),(16,17),(16,18),
#              (3,6),(3,7),(3,8),(3,9),(3,10)];
# start = (0,0)
# goal = (10,6)

# action_cost = {(0,1):1,(0,-1):1,(1,0):1,(-1,0):1}

action_cost = {(0,1 ):1,(0,-1):1,(1,0):1,(-1,0):1,(1,1):1.4,(1,-1):1.4,(-1,1):1.4,(-1,-1):1.4}



maps = MAP(nrow, ncol, start, goal, obstacles)

fig = maps.plot_map()
fig.show(True)


# heuristics = {(i,j):(abs(goal[0]-x),abs(goal[1]-y))  for i in range(0,ncol) for j in range(0,nrow)}

def get_heuristic_cost(x,y):
    # return abs(goal[0]-x)+abs(goal[1]-y)
    return sqrt((goal[0]-x)**2+(goal[1]-y)**2)

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
                    neighbour_costs[(x_neighbour,y_neighbour)] = [cost_map[vertex][0] + action_cost[action],
                                                                  get_heuristic_cost(x_neighbour, y_neighbour)]
    # print(neighbour_costs)
    return neighbour_costs


### starting astar Algorithm

cost_map  = {start: [0, get_heuristic_cost(*start)]} # g,h
parent_map= {start:None}
Q = [start]


while Q != []:
    # exploit frontier
    frontier   = min(Q, key=lambda x: sum(cost_map[x])) #todo :: use sorting and insertion for speed up
    Q.remove(frontier)
    gcost, hcost= cost_map[frontier]
    maps.set_node(*frontier,state='red',g=gcost, h=hcost, f=gcost+hcost)

    # explore frontier
    neighbour_costs = get_neighbour_costs(frontier)
    for neighbour in neighbour_costs:
        n_gcost, n_hcost = neighbour_costs[neighbour]
        n_fcost = n_gcost + n_hcost

        if neighbour in cost_map:
            if sum(cost_map[neighbour]) <= n_fcost:   # travelling cost - todo :: use order in when f cost is same
                continue
            else:
                cost_map[neighbour]  = [n_gcost, n_hcost]
                parent_map[neighbour]= frontier
                maps.set_node(*neighbour, state='green', g=n_gcost, f=n_fcost, h=n_hcost, stop=False)
                continue

        Q.append(neighbour)
        cost_map[neighbour] = [n_gcost, n_hcost]
        parent_map[neighbour]= frontier
        maps.set_node(*neighbour, state='green', g=n_gcost, f=n_fcost, h=n_hcost, stop=False)
        if neighbour == goal:
            break
    if neighbour == goal:
        break


# retrace path
parent = goal
while parent is not None:
    if parent == start:
        maps.set_node(*parent, state='blue', g=cost_map[parent][0], h=cost_map[parent][1], f=sum(cost_map[parent]), stop=False)
    else:
        maps.set_node(*parent, state='blue', g=cost_map[parent][0], h=cost_map[parent][1], f=sum(cost_map[parent]))
    child  = parent
    parent = parent_map[child]



