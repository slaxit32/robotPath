
from __future__ import print_function
from colorclass import Color, Windows
from terminaltables import SingleTable

import time
import random
import os

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
	table_data[int(current/10)][int(current%10)]=Color('{autoyellow}O{/autoyellow}')


	table_instance = SingleTable(table_data,title)
	table_instance.inner_heading_row_border = False
	table_instance.inner_row_border = True
	table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center'}

	Windows.enable(auto_colors=True, reset_atexit=True)  # Does nothing if not on Windows.

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
	visited.append(sn)

	t=[]
	for i in nei(cn):
		if(i not in stones):
			t.append(i)

	stack=t+stack
	visited=t+visited

	print("current node ",cn)
	print("stack ",stack)
	print("visited ",visited)
	print()

	print(table("dfs",stones,sn,en,cn,stack,"",""))

	flag=0

	while cn!=en:
		print("stack before ",stack)
		
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

			print(table("dfs",stones,sn,en,cn,stack,travel,""))
			#time.sleep(0.25)

			print("current node ",cn)
			print("stack after ",stack)
			print("visited ",visited)
			print()
			i=cn
		
			print(stack)
			
			
	if(flag!=1):
		print(table("dfs",stones,sn,en,cn,"","",travel))

	

	end = time.time()
	timeTaken=end - start

	if(timeTaken<1):
		print("Time taken ",timeTaken*1000," ms")
	else:
		print("Time taken ",timeTaken," s")


	

def bfs(s,e):

	start = time.time()

	stack=[]
	visited=[]
	travel=[]


	sn=s
	en=e

	cn=sn
	visited.append(sn)

	t=[]
	for i in nei(cn):
		if(i not in stones):
			t.append(i)

	stack=t+stack
	visited=t+visited

	# print("current node ",cn)
	# print("stack ",stack)
	# print("visited ",visited)
	# print()

	print(table("bfs","",sn,en,cn,stack,"",""))

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
			print(table("bfs","",sn,en,cn,stack,travel,""))
			#time.sleep(0.1)
			#os.system('cls' if os.name == 'nt' else 'clear')



			# print("current node ",cn)
			# print("stack after ",stack)
			# print("visited ",visited)
			# print()
			i=cn
			
			#print(stack)
	if(flag!=1):
		print(table("bfs",stones,sn,en,cn,"","",travel))

	end = time.time()
	timeTaken=end - start

	if(timeTaken<1):
		print("Time taken ",timeTaken*1000," ms")
	else:
		print("Time taken ",timeTaken," s")


startNode=random.randint(0,99)
print("Start at ",startNode)
endNode=random.randint(0,99)
print("End at ",endNode)


#ading stones
stones=[2,11]

print(table("Init",stones,0,9,98,"","",""))

#dfs(0,9)
#bfs(0,9)




















# for i in ["Hi", "You", "Fool"]:
#     sys.stdout.write("\r" + i)
#     sys.stdout.flush()
#     time.sleep(1)


# cn=sn
# # print("start node ",sn)
# # stack.append(up(sn))
# # stack.append(ri(sn))
# # stack.append(do(sn))
# # stack.append(le(sn))

# # visited.append(sn)

# # print("stack before",stack)

# # cn=stack.pop(0)
# # print("current node ", cn)

# # print("stack after",stack)
# # print("visited ",visited)



# while cn>=0 and cn<=99:

# 	print()

# 	print("current node ",cn)


# 	l=le(cn)
# 	if l in table_data:
# 		print("added left")
# 		stack.insert(0,l)

# 	d=do(cn)
# 	if d in table_data:
# 		print("added down")
# 		stack.insert(0,d)

# 	# r=ri(cn)
# 	# stack.insert(0,r)

# 	# u=up(cn)
# 	# stack.insert(0,u)


# 	visited.append(cn)


# 	print("stack before",stack)

# 	cn=stack.pop(0)
# 	print("current node ", cn)

# 	print("stack after",stack)
# 	print("visited ",visited)



# 	if(cn=="e"):
# 		cn=stack.pop(0)
# 		cn=stack.pop(0)



