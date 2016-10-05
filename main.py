
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

	sl=0
	el=99

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


	sl=0
	el=99

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



	# print(addStrck)
	# print("dis ",dis)
	disSort=dis
	disSort=sorted(dis)
	# print("dissort ",disSort)

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
	# print("map ",map)	


	for i in map:
		outList.append(i[1])

	# print(outList)

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

	# print("current node ",cn)
	# print("stack ",stack)
	# print("visited ",visited)
	# print()

	# print(table("dfs",stones,sn,en,cn,stack,"",""))

	flag=0

	while cn!=en:
		#print("stack before ",stack)
		
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

			#time.sleep(0.25)

			# print("current node ",cn)
			# print("stack after ",stack)
			# print("visited ",visited)
			# print()
			i=cn
		
			# print(stack)
			
			
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


	# print("current node ",cn)
	# print("stack ",stack)
	# print("visited ",visited)
	# print()

	#print(table("bfs","",cn,en,cn,stack,"",""))

	flag=0

	while cn!=en:
		# print("stack before ",stack)
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

			#time.sleep(0.1)
			#os.system('cls' if os.name == 'nt' else 'clear')



			# print("current node ",cn)
			# print("stack after ",stack)
			# print("visited ",visited)
			# print()
			i=cn
			
			#print(stack)
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

	# print("current node ",cn)
	# print("stack ",stack)
	# print("visited ",visited)
	# print()

	#print(table("Greedy","",sn,en,cn,stack,"",""))
	print(table("Greedy",stones,sn,en,"",stack,travel,""))

	flag=0

	while cn!=en:
		#print("stack before ",stack)
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
			#time.sleep(0.1)
			#os.system('cls' if os.name == 'nt' else 'clear')



			# print("current node ",cn)
			# print("stack after ",stack)
			# print("visited ",visited)
			# print()
			i=cn
			
			#print(stack)
	if(flag!=1):
		print(table("Greedy",stones,sn,en,"","","",travel))

	end = time.time()
	timeTaken=end - start

	if(timeTaken<1):
		print("\nTime taken ",timeTaken*1000," ms")
	else:
		print("\nTime taken ",timeTaken," s")

# startNode=random.randint(0,99)
# print("Start at ",startNode)
# endNode=random.randint(0,99)
# print("End at ",endNode)


#ading stones
stones=[24,34,44,54,64,74,4,14]


#dfs(0,55)
#bfs(0,55)
#greedy(0,55)





















