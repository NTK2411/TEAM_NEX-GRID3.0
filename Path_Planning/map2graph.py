import arenav0
import numpy as np

def graphfunction1(info):
    d={}
    # count_corner = 0
    # count = 0
    for y in range(info.shape[0]):
        for x in range(info.shape[1]):
            if info[y][x] == 0:
                
                d[coord_con_str([y,x])] = {}
                for i in (-1,0,1):
                    for j in (-1,0,1):
                        
                        if not(i == 0 and j == 0):
                            if (i+x) in range(info.shape[0]) and (j+y) in range(info.shape[1]):
                                if info[y+j,x+i] != -1:
                                    if (i * j == 0):
                                            d[coord_con_str([y,x])][coord_con_str([y+j,x+i])] = 1#info[y+j,x+i]
                                    else:
                                        # print(f"{x,y}  {i,j}")
                                        if info[y+j,x] != -1 and info[y,x+i] != -1:
                                            d[coord_con_str([y,x])][coord_con_str([y+j,x+i])] = 1.414#info[y+j,x+i]
    

    return d

def see_dictionary(d):
    print ("{:<10} {:<10}".format('Start', 'End'))
    for key, value in d.items():
        print (f"{key}:{value}")

def coord_con_int(posi):

    y = ((int(posi[1]))*10)+(int(posi[2]))
    x = ((int(posi[3]))*10) + (int(posi[4]))
    return y,x

def coord_con_str(yx):
    x = yx[0]##actually y
    y = yx[1]##actually x
    if (len(str(x)) < 2 and len(str(y)) < 2):
        posi = ('d'+'0' + str(x) + '0' + str(y))
    elif (len(str(x)) < 2 and len(str(y)) == 2):
        posi = ('d'+'0' + str(x) + str(y))
    elif (len(str(x)) == 2 and len(str(y)) < 2):
        posi = ('d'+str(x) + '0' + str(y))
    elif (len(str(x)) == 2 and len(str(y)) == 2):
        posi = ('d'+str(x) + str(y))
    return posi #(y,x)


#####################
def path_dijkstra(graph,start,goal):
    # see_dictionary(graph)
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph.copy()
    infinity = 999999
    track_path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:

        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:

            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0,currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print("Path is not reachable")
            break
    if shortest_distance[goal] != infinity:
        # print("Shortest distance is " + str(shortest_distance[goal]))
        # print("Optimal Path is " + str(track_path))
        pass
    
    position = [coord_con_int(start)[0],coord_con_int(start)[1]]
    final = [position[:]]#np.array(coord_con_int(start))#[position[:]]#
    for _ in track_path:
        position = [coord_con_int(_)[0],coord_con_int(_)[1]]
        # final = np.vstack([final,position])
        final.append(position)
    # see_dictionary(graph)
    return track_path,int(shortest_distance[goal]),final
#####################

if __name__ == "__main__":
    arena_main=arenav0.info()
    dict_main = graphfunction1(arena_main)
    see_dictionary(dict_main)
    # start = coord_con_str([0,0])
    # end = coord_con_str([13,13])
    # _, _, p = path_dijkstra(dict_main,start,'d0001')
    # print(p)
