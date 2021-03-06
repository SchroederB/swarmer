from src import api_wrapper as api
import networkx as nx

def assign_package(graph, packages_divided, nodes_groups, new_packages):
    for new_package in new_packages:
        for i in range(0, 2):
            if (graph.index(new_package.coordinates)+1) in nodes_groups[i]:
                packages_divided[i].append(new_package)
                break
    print("LA",packages_divided)
    return packages_divided


def assign_package_wrapper(new_packages, graph, packages_divided=list()):
    if packages_divided == list():
        packages_divided.append(list())
        packages_divided.append(list())
        packages_divided.append(list())
    nodes_groups = list()
    nodes_groups.append([3, 2, 8])
    nodes_groups.append([5, 7])
    nodes_groups.append([6, 4, 9])
    super_list = assign_package(graph, packages_divided, nodes_groups, new_packages)
    return super_list

import src.PathSolving.path_solver as ps
def optimal_path(G, targets):
   targets = [ps.get_point_or_idx(package.coordinates[:2]) for package in targets]
   total_cost = list()
   shortest_path = list()
   min_cost = 0

   if len(targets) == 1:
       return nx.dijkstra_path(G, 1, targets[0])

   if len(targets) == 2:
       total_cost.append(nx.dijkstra_path_length(G, 1, targets[0]) + nx.dijkstra_path_length(G, targets[0], targets[1]))
       min_cost = total_cost[0]
       min_path = 0
       total_cost.append(nx.dijkstra_path_length(G, 1, targets[1]) + nx.dijkstra_path_length(G, targets[1], targets[0]))
       if (min_cost>total_cost[1]):
           min_cost = total_cost[1]
           min_path = 1

       if min_path == 0:
           sublist1 = nx.dijkstra_path(G, targets[0], targets[1])
           del sublist1[0]
           shortest_path = [nx.dijkstra_path(G, 1, targets[0]) + sublist1]

       if min_path == 1:
           sublist1 = nx.dijkstra_path(G, targets[1], targets[0])
           del sublist1[0]
           shortest_path = [nx.dijkstra_path(G, 1, targets[1]) + sublist1]
       return shortest_path

   elif len(targets) == 3:
       print("Targest: ",targets)
       print("Paths: ",nx.dijkstra_path_length(G, 1, targets[0]))
       total_cost.append(nx.dijkstra_path_length(G, 1, targets[0]) + nx.dijkstra_path_length(G, targets[0], targets[1]) + nx.dijkstra_path_length(G, targets[1], targets[2]))
       min_cost = total_cost[0]
       min_path = 0
       total_cost.append(nx.dijkstra_path_length(G, 1, targets[0]) + nx.dijkstra_path_length(G, targets[0], targets[2]) + nx.dijkstra_path_length(G, targets[2], targets[1]))
       if (min_cost>total_cost[1]):
           min_cost = total_cost[1]
           min_path = 1
       total_cost.append(nx.dijkstra_path_length(G, 1, targets[1]) + nx.dijkstra_path_length(G, targets[1], targets[0]) + nx.dijkstra_path_length(G, targets[0], targets[2]))
       if (min_cost>total_cost[2]):
           min_cost = total_cost[2]
           min_path = 2
       total_cost.append(nx.dijkstra_path_length(G, 1, targets[1]) + nx.dijkstra_path_length(G, targets[1], targets[2]) + nx.dijkstra_path_length(G, targets[2], targets[0]))
       if (min_cost>total_cost[3]):
           min_cost = total_cost[3]
           min_path = 3
       total_cost.append(nx.dijkstra_path_length(G, 1, targets[2]) + nx.dijkstra_path_length(G, targets[2], targets[0]) + nx.dijkstra_path_length(G, targets[0], targets[1]))
       if (min_cost>total_cost[4]):
           min_cost = total_cost[4]
           min_path = 4
       total_cost.append(nx.dijkstra_path_length(G, 1, targets[2]) + nx.dijkstra_path_length(G, targets[2], targets[1]) + nx.dijkstra_path_length(G, targets[1], targets[2]))
       if (min_cost>total_cost[5]):
           min_cost = total_cost[5]
           min_path = 5

       if min_path == 0:
           sublist1 = nx.dijkstra_path(G, targets[0], targets[1])
           sublist2 = nx.dijkstra_path(G, targets[1], targets[2])
           del sublist1[0]
           del sublist2[0]
           shortest_path = [nx.dijkstra_path(G, 1, targets[0]) + sublist1 + sublist2]

       if min_path == 1:
           sublist1 = nx.dijkstra_path(G, targets[0], targets[2])
           sublist2 = nx.dijkstra_path(G, targets[2], targets[1])
           del sublist1[0]
           del sublist2[0]
           shortest_path = [nx.dijkstra_path(G, 1, targets[0]) + sublist1 + sublist2]
       if min_path == 2:
           sublist1 = nx.dijkstra_path(G, targets[1], targets[0])
           sublist2 = nx.dijkstra_path(G, targets[0], targets[2])
           del sublist1[0]
           del sublist2[0]
           shortest_path = [nx.dijkstra_path(G, 1, targets[1]) + sublist1 + sublist2]
       if min_path == 3:
           sublist1 = nx.dijkstra_path(G, targets[1], targets[2])
           sublist2 = nx.dijkstra_path(G, targets[2], targets[0])
           del sublist1[0]
           del sublist2[0]
           shortest_path = [nx.dijkstra_path(G, 1, targets[1]) + sublist1 + sublist2]
       if min_path == 4:
           sublist1 = nx.dijkstra_path(G, targets[2], targets[0])
           sublist2 = nx.dijkstra_path(G, targets[0], targets[1])
           del sublist1[0]
           del sublist2[0]
           shortest_path = [nx.dijkstra_path(G, 1, targets[2]) + sublist1 + sublist2]
       if min_path == 5:
           sublist1 = nx.dijkstra_path(G, targets[2], targets[1])
           sublist2 = nx.dijkstra_path(G, targets[1], targets[2])
           del sublist1[0]
           del sublist2[0]
           shortest_path = [nx.dijkstra_path(G, 1, targets[2]) + sublist1 + sublist2]
       return shortest_path

import os
def get_my_work(my_index, packages_divided):
    G = nx.read_gpickle(os.getcwd()+'/coordinates/our_map.mp')
    if len(packages_divided[my_index]) < 3:
        my_work=packages_divided[my_index]
        packages_divided[my_index] = list()
    else:
        my_work=packages_divided[my_index][0:3]
        for i in range(0, 3):
            packages_divided[my_index].pop()

    #optimal_path = list()
    optimal_pathT = optimal_path(G, my_work)
    return my_work, optimal_pathT

'''
from src.PathSolving import path_solver as ps

execute_it=True

swarm = api.Swarm(swarm_id="Swarmer", server_id="http://10.4.14.248:5000/api")
#248, 28, 37

arena = swarm.get_arena()
#print("ARENA:\n",arena)

print(swarm.buildings )
buildingOne = swarm.buildings[0]
buildingOne = arena["buildings"][0]

drone_ids = swarm.droneIDs

droneOne = api.Drone(droneID=drone_ids[1], swarm=swarm)
#droneOne.connect()
#droneOne.disconnect()

try:
    registered= swarm.register(arena=2)
except Exception as err:
    print("Was already Registered")

source_node=[2.2, 1.6]
packages = [swarm.get_package() for x in range(20)]

packages_divided = assign_package_wrapper(packages)
'''



