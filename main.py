
from __future__ import print_function
from colorclass import Color, Windows
from terminaltables import SingleTable

import time
import random
import os
import math

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')


#------------------------create metrix
w, h = 10,10
table_data = [["" for x in range(w)] for y in range(h)] 

for i in range(0,10):
	for j in range(0,10):
		table_data[i][j]=i*10+j

#-----------------------create metrix end



#table droving funcion
def table(title,stones,start,end,current,serch,path,final):

	for i in stones:
		col=int(i%10)
		row=int(i/10)
		table_data[row][col]=Color('{autoblue}#{/autoblue}')

	for i in serch:
		col=int(i%10)
		row=int(i/10)
		table_data[row][col]=Color('{autogreen}!{/autogreen}')

	for i in path:
		col=int(i%10)
		row=int(i/10)
		table_data[row][col]=Color('{automagenta}-{/automagenta}')

	for i in final:
		col=int(i%10)
		row=int(i/10)
		table_data[row][col]=Color('{autored}*{/autored}')

	table_data[int(start/10)][int(start%10)]=Color("{autored}St{/autored}")
	table_data[int(end/10)][int(end%10)]=Color("{autored}En{/autored}")

	if(current!=""):
		table_data[int(current/10)][int(current%10)]=Color('{autoyellow}O{/autoyellow}')


	table_instance = SingleTable(table_data,title)
	table_instance.inner_heading_row_border = False
	table_instance.inner_row_border = True
	table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center'}

	Windows.enable(auto_colors=True, reset_atexit=True)  # Does nothing if not on Windows.

	print()

	return table_instance.table

def up(node):
	return (int(node/10)-1)*10+int(node%10)

def do(node):
	return (int(node/10)+1)*10+int(node%10)

def le(node):
	return node-1

def ri(node):
	return node+1

def nei(node):

	addStrck=[]

	u=up(node)
	if (u>=0 and u<=99 ):
		addStrck.append(u)

	r=ri(node)
	if (r>=0 and r<=99 and int(r/10)==int(node/10)):
		addStrck.append(r)

	d=do(node)
	if (d>=0 and d<=99):
		addStrck.append(d)

	l=le(node)
	if (l>=0 and l<=99 and int(l/10)==int(node/10)):
		addStrck.append(l)

	return addStrck

def neiShort(node,e):

	addStrck=[]
	dis=[]
	disSort=[]
	outList=[]

	u=up(node)
	if (u>=0 and u<=99 ):
		ud=sdis(u, e)
		dis.append(ud)
		addStrck.append(u)

	r=ri(node)
	if (r>=0 and r<=99 and int(r/10)==int(node/10)):
		rd=sdis(r, e)
		dis.append(rd)
		addStrck.append(r)

	d=do(node)
	if (d>=0 and d<=99):
		dd=sdis(d, e)
		dis.append(dd)
		addStrck.append(d)

	l=le(node)
	if (l>=0 and l<=99 and int(l/10)==int(node/10)):
		ld=sdis(l, e)
		dis.append(ld)
		addStrck.append(l)

	disSort=dis
	disSort=sorted(dis)


	map=[]

	for i in addStrck:
		map.append([])

	cou=0
	for i in dis:
		map[cou].append(i)
		cou+=1

	cou=0
	for i in addStrck:
		map[cou].append(i)
		cou+=1

	map.sort()

	for i in map:
		outList.append(i[1])

	return outList

def checkleaf(node,vis):
	visited=vis
	flag=1
	for i in nei(node):
		if(i not in visited):
			if(i not in stones):
				flag=0
	return flag

def dfs(s,e):

	start = time.time()

	stack=[]
	visited=[]
	travel=[]

	sn=s
	en=e

	cn=sn

	print(table("DFS",stones,sn,en,"",stack,travel,""))

	visited.append(sn)

	t=[]
	for i in nei(cn):
		if(i not in stones):
			t.append(i)

	stack=t+stack
	visited=t+visited

	print(table("DFS",stones,sn,en,cn,stack,travel,""))
	print(cn,stack,"\n")
	
	flag=0

	while cn!=en:
		
		if(len(stack)==0):
			print("\n\n------------------------------No path------------------------------\n\n")
			flag=1
			break
		else:
			cn=stack.pop(0)
			t=[]
			for i in nei(cn):
				if(i not in visited):
					if(i not in stones):
						t.append(i)
						visited.append(i)
			travel.append(cn)
							

			stack=t+stack

			print(table("DFS",stones,sn,en,cn,stack,travel,""))
			print(cn,stack,"\n")
			i=cn
			
			
	if(flag!=1):
		print(table("DFS",stones,sn,en,"","","",travel))


	end = time.time()
	timeTaken=end - start

	if(timeTaken<1):
		print("\nTime taken ",timeTaken*1000," ms")
	else:
		print("\nTime taken ",timeTaken," s")

def bfs(s,e):

	start = time.time()

	stack=[]
	visited=[]
	travel=[]

	sn=s
	en=e

	cn=sn

	print(table("BFS",stones,sn,en,"",stack,travel,""))

	visited.append(sn)

	t=[]
	for i in nei(cn):
		if(i not in stones):
			t.append(i)

	stack=t+stack
	visited=t+visited

	print(table("BFS",stones,sn,en,cn,stack,travel,""))
	print(cn,stack,"\n")



	flag=0

	while cn!=en:
		if(len(stack)==0):
			print("\n\n------------------------------No path------------------------------\n\n")
			flag=1
			break
		else:
			cn=stack.pop(0)
			t=[]
			for i in nei(cn):
				if(i not in visited):
					if(i not in stones):
						t.append(i)
						visited.append(i)
			stack=stack+t
			travel.append(cn)
			print(table("BFS",stones,sn,en,cn,stack,travel,""))

			i=cn
			
			print(cn,stack,"\n")


	if(flag!=1):
		print(table("BFS",stones,sn,en,"","","",travel))
		
	end = time.time()
	timeTaken=end - start

	if(timeTaken<1):
		print("\nTime taken ",timeTaken*1000," ms")
	else:
		print("\nTime taken ",timeTaken," s")

def sdis(a,b):
	x1=int(a/10)
	y1=int(a%10)

	x2=int(b/10)
	y2=int(b%10)

	t=math.sqrt((x2-x1)**2+(y2-y1)**2)

	return t

def greedy(s,e):


	start = time.time()

	stack=[]
	visited=[]
	travel=[]

	sn=s
	en=e

	cn=sn
	visited.append(sn)

	print(table("Greedy",stones,sn,en,"",stack,travel,""))


	t=[]
	for i in neiShort(cn,en):
		if(i not in stones):
			t.append(i)

	stack=t+stack
	visited=t+visited

	print(table("Greedy",stones,sn,en,"",stack,travel,""))
	print(cn,stack,"\n")

	flag=0

	while cn!=en:

		if(len(stack)==0):
			print("\n\n------------------------------No path------------------------------\n\n")
			flag=1
			break
		else:
			cn=stack.pop(0)
			t=[]
			for i in neiShort(cn,en):
				if(i not in visited):
					if(i not in stones):
						t.append(i)
						visited.append(i)
			stack=t+stack
			travel.append(cn)
			print(table("Greedy",stones,sn,en,cn,stack,travel,""))
			print(cn,stack,"\n")

			i=cn
		
			
	if(flag!=1):
		print(table("Greedy",stones,sn,en,"","","",travel))

	end = time.time()
	timeTaken=end - start

	if(timeTaken<1):
		print("\nTime taken ",timeTaken*1000," ms")
	else:
		print("\nTime taken ",timeTaken," s")

def neiCost(node,e,preDis):

	addStrck=[]
	dis=[]

	u=up(node)
	if (u>=0 and u<=99):
		ud=sdis(u, node)
		dis.append(ud)
		addStrck.append(u)

	r=ri(node)
	if (r>=0 and r<=99 and int(r/10)==int(node/10)):
		rd=sdis(r, node)
		dis.append(rd)
		addStrck.append(r)

	d=do(node)
	if (d>=0 and d<=99):
		dd=sdis(d, node)
		dis.append(dd)
		addStrck.append(d)

	l=le(node)
	if (l>=0 and l<=99 and int(l/10)==int(node/10)):
		ld=sdis(l, node)
		dis.append(ld)
		addStrck.append(l)

	map=[]

	for i in addStrck:
		map.append([])


	# #addint total distace to map
	cou=0
	for i in addStrck:
		map[cou].append(sdis(i,e))#distance from i th node to end node
		map[cou].append(sdis(node,i)+preDis)#distance between 2 nodes as cost
		map[cou].append(i)#node
		cou+=1

	cou=0
	for i in map:
		map[cou].insert(0,map[cou][0]+map[cou][1])
		cou+=1


	map.sort()

	return map

def a(s,e):


	start = time.time()

	stack=[]
	visited=[]
	travel=[]

	sn=s
	en=e

	cn=sn

	visited.append(sn)

	print(table("A*",stones,sn,en,"",stack,travel,""))


	t=[]
	td=[]
	for i in neiCost(cn,en,0):
		if(i[3] not in stones):
			td.append(i[3])
			t.append(i)


	stack=t+stack
	visited=td+visited


	print(table("A*",stones,cn,en,cn,visited,"",""))
	print(cn,"\n",stack,"\n")


	flag=0

	while 1:

		if(len(stack)==0):
			print("\n\n------------------------------No path------------------------------\n\n")
			flag=1
			break
		else:
			cn=stack.pop(0)

			curentNodeNode=cn[3]
			currentDistance=cn[2]

			k=neiCost(curentNodeNode, e,currentDistance)

			t=[]
			for i in k:
				if i[3] not in visited:
					if i[3] not in stones:
						t.append(i)
						visited.append(i[3])
				


			stack=t+stack
			travel.append(curentNodeNode)


			#getting stack actual node to drow table
			cou=0
			ss=[]
			for i in stack:	
				ss.append(stack[cou][3])
				cou+=1

			print(table("A*",stones,sn,en,curentNodeNode,ss,travel,""))
			print(cn,"\n",stack,"\n")


			if(curentNodeNode==en):
				break



	if(flag!=1):
		print(table("A*",stones,sn,en,"","","",travel))

	end = time.time()
	timeTaken=end - start

	if(timeTaken<1):
		print("\nTime taken ",timeTaken*1000," ms")
	else:
		print("\nTime taken ",timeTaken," s")



#adding random stones ,start, end
startNode=random.randint(0,99)
print("\n\nStart at ",startNode)
endNode=random.randint(0,99)
print("End at ",endNode)


noOfstones=random.randint(0,99)
print("No of stones ",noOfstones)
stones=[]

for i in range(0,noOfstones):
	sl=random.randint(0,99)
	if (sl!=startNode and sl!=endNode):
		stones.append(sl)

print("Stones locations ",stones)




s=startNode
e=endNode

#dfs(s,e)
#bfs(s,e)
#greedy(s,e)
a(s,e)
















