import numpy as np
from math import *
import arenav0

def dist(x,y,dest):
    a=(x-dest[0])**2
    b=(y-dest[1])**2
    return sqrt(a+b)

def Path(position,destination,data):
    
    final=[position[:]]

    while True:
        pos2=position
        curr=dist(position[0],position[1],destination)
        if curr<2:
            final.append(destination)
            break

        up,down,left,right=curr,curr,curr,curr
        if  position[1]+1<14 and data[position[0]][position[1]+1]==0:
            up=dist(position[0],position[1]+1,destination)
        if position[1]-1>-1 and data[position[0]][position[1]-1]==0:
            down=dist(position[0],position[1]-1,destination)
        if position[0]-1>-1 and data[position[0]-1][position[1]]==0:
            left=dist(position[0]-1,position[1],destination)
        if position[0]+1<14 and data[position[0]+1][position[1]]==0 :
            right=dist(position[0]+1,position[1],destination)

        if left<right:
            if up<left:
                position=[pos2[0],pos2[1]+1]
                new_dist=dist(position[0],position[1],destination)
                new_left,new_right=new_dist,new_dist
                if position[0]-1>-1 and data[position[0]-1][position[1]]==0:
                    new_left=dist(position[0]-1,position[1],destination)
                if position[0]+1<14 and data[position[0]+1][position[1]]==0:
                    new_right=dist(position[0]+1,position[1],destination)

                if new_left<new_dist:
                    if data[position[0]-1,pos2[1]]!=-1:
                        position=[position[0]-1,position[1]]
                elif new_right<new_dist:
                    if data[position[0]+1,pos2[1]]!=-1:
                        position=[position[0]+1,position[1]]

                final.append(position)
            elif down<left:
                position=[pos2[0],pos2[1]-1]
                new_dist=dist(position[0],position[1],destination)
                new_left,new_right=new_dist,new_dist
                if position[0]-1>-1 and data[position[0]-1][position[1]]==0 :
                    new_left=dist(position[0]-1,position[1],destination)
                if position[0]+1<14 and data[position[0]+1][position[1]]==0:
                    new_right=dist(position[0]+1,position[1],destination)

                if new_left<new_dist:
                    if data[position[0]-1,pos2[1]]!=-1:
                        position=[position[0]-1,position[1]]
                elif new_right<new_dist:
                    if data[position[0]+1,pos2[1]]!=-1:
                        position=[position[0]+1,position[1]]

                final.append(position)
            else:
                position=[pos2[0]-1,pos2[1]]
                new_dist=dist(position[0],position[1],destination)
                new_up,new_down=new_dist,new_dist
                if position[1]+1<14 and data[position[0]][position[1]+1]==0:
                    new_up=dist(position[0],position[1]+1,destination)
                if position[1]-1>-1 and data[position[0]][position[1]-1]==0:
                    new_down=dist(position[0],position[1]-1,destination)

                if new_up<new_dist:
                    if data[pos2[0],position[1]+1]!=-1:
                        position=[position[0],position[1]+1]
                elif new_down<new_dist:
                    if data[pos2[0],position[1]-1]!=-1:
                        position=[position[0],position[1]-1]

                final.append(position)

        else:
            if up<right:
                position=[pos2[0],pos2[1]+1]
                new_dist=dist(position[0],position[1],destination)
                new_left,new_right=new_dist,new_dist
                if position[0]-1>-1 and data[position[0]-1][position[1]]==0:
                    new_left=dist(position[0]-1,position[1],destination)
                if position[0]+1<14 and data[position[0]+1][position[1]]==0:
                    new_right=dist(position[0]+1,position[1],destination)

                if new_left<new_dist:
                    if data[position[0]-1,pos2[1]]!=-1:
                        position=[position[0]-1,position[1]]
                elif new_right<new_dist:
                    if data[position[0]+1,pos2[1]]!=-1:
                        position=[position[0]+1,position[1]]
                final.append(position)
            elif down<right:
                position=[pos2[0],pos2[1]-1]
                new_dist=dist(position[0],position[1],destination)
                new_left,new_right=new_dist,new_dist
                if position[0]-1>-1 and data[position[0]-1][position[1]]==0:
                    new_left=dist(position[0]-1,position[1],destination)
                if position[0]+1<14 and data[position[0]+1][position[1]]==0:
                    new_right=dist(position[0]+1,position[1],destination)

                if new_left<new_dist:
                    if data[position[0]-1,pos2[1]]!=-1:
                        position=[position[0]-1,position[1]]
                elif new_right<new_dist:
                    if data[position[0]+1,pos2[1]]!=-1:
                        position=[position[0]+1,position[1]]

                final.append(position)
            else:
                position=[pos2[0]+1,pos2[1]]
                new_dist=dist(position[0],position[1],destination)
                new_up,new_down=new_dist,new_dist
                if position[1]+1<14 and data[position[0]][position[1]+1]==0:
                    new_up=dist(position[0],position[1]+1,destination)
                if position[1]-1>-1 and data[position[0]][position[1]-1]==0:
                    new_down=dist(position[0],position[1]-1,destination)

                if new_up<new_dist:
                    
                    if data[pos2[0],position[1]+1]!=-1:
                        position=[position[0],position[1]+1]
                elif new_down<new_dist:
                    if data[pos2[0],position[1]-1]!=-1:
                        position=[position[0],position[1]-1]

                final.append(position)

    return np.array(final)



if __name__=='__main__':
    position=[0,0]#[int(i) for i in input("Starting Position : ").split()]
    destination=[13,13]#[int(i) for i in input("Destination :").split()]
    arena_main=arenav0.info()
    path1=Path(position,destination,arena_main)
    print(path1)
    print("🍆🍆")

