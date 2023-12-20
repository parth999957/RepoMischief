from map import MAP
from math import sqrt

class Navigate(object):
    """docstring for Navigate"""
    def __init__(self, navigation_map):
        super(Navigate, self).__init__()
        self.navigation_map = navigation_map
        self.action_cost = {(0,1):1,(0,-1):1,(1,0):1,(-1,0):1}
        # self.action_cost = {(0,1):1,(0,-1):1,(1,0):1,(-1,0):1,(1,1):1.4, (1,-1):1.4,(-1,1):1.4,(-1,-1):1.4}

    def get_neighbour_costs_bfs(self, vertex):
        cost_map = self.cost_map
        action_cost = self.action_cost
        ncol = self.navigation_map.ncol
        nrow = self.navigation_map.nrow
        obstacles =self.navigation_map.obstacles

        neighbour_costs = {}
        x = vertex[0]
        y = vertex[1]
        for action in self.action_cost:
            dx = action[0]
            dy = action[1]
            x_neighbour = x+dx
            y_neighbour = y+dy

            if x_neighbour in range(0,ncol):
                if y_neighbour in range(0,nrow):
                    if (x_neighbour, y_neighbour) not in obstacles:
                        neighbour_costs[(x_neighbour,y_neighbour)] = cost_map[vertex] + action_cost[action]

        return neighbour_costs


    def search_BFS(self):
        ### starting BFS Algorithm
        maps = self.navigation_map
        start = maps.start
        goal = maps.goal
        cost_map  = {start:0}; self.cost_map = cost_map
        parent_map= {start:None}; self.parent_map = parent_map
        Q = [start]

        fig = maps.plot_map()
        fig.show(True)

        while Q != []:
            # exploit frontier
            frontier = Q.pop(0)
            frontier_cost= cost_map[frontier]
            maps.set_node(*frontier,state='red',f=frontier_cost)

            # explore frontier
            neighbour_costs = self.get_neighbour_costs_bfs(frontier)

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

        print("cost_map = ", cost_map)


    def get_heuristic_cost(self, x,y):
        goal = self.navigation_map.goal
        # return abs(goal[0]-x)+abs(goal[1]-y)
        return sqrt((goal[0]-x)**2+(goal[1]-y)**2)

    def get_neighbour_costs_astar(self, vertex):
        cost_map = self.cost_map
        action_cost = self.action_cost
        get_heuristic_cost = self.get_heuristic_cost
        ncol = self.navigation_map.ncol
        nrow = self.navigation_map.nrow
        obstacles =self.navigation_map.obstacles

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


    def search_astar(self):
        ### starting astar Algorithm
        maps = self.navigation_map
        get_heuristic_cost = self.get_heuristic_cost

        start = maps.start
        goal = maps.goal

        cost_map  = {start: [0, get_heuristic_cost(*start)]}; self.cost_map = cost_map
        parent_map= {start:None}; self.parent_map = parent_map

        Q = [start]

        fig = maps.plot_map()
        fig.show(True)

        while Q != []:
            # exploit frontier
            frontier   = min(Q, key=lambda x: sum(cost_map[x])) #todo :: use sorting and insertion for speed up
            Q.remove(frontier)
            gcost, hcost= cost_map[frontier]
            maps.set_node(*frontier,state='red',g=gcost, h=hcost, f=gcost+hcost)

            # explore frontier
            neighbour_costs = self.get_neighbour_costs_astar(frontier)
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



if __name__ == "__main__":
    nrow = 10; ncol = 10; start = (0,0); goal = (5,5); obstacles = [(1,2)]
    maps = MAP(nrow, ncol, start, goal, obstacles)
    navigation = Navigate(maps)
    navigation.search_BFS()
