# samples=[
# {x:4,y:3},
# {x:7,y:4},
# {x:5,y:6},
# {x:4,y:6},
# ]

# print(samples[1].x)

# import json

# # some JSON:
# x =  '[{ "name":"John", "age":30, "city":"New York"},{ "name":"John", "age":30, "city":"New York"}]'

# # parse x:
# y = json.loads(x)

# for i in y:
# 	print(i['name']);
# # the result is a Python dictionary:
# print(y)
# import math
# class sample: 
#     def __init__(self, x, y,label): 
#         self.x = x 
#         self.y = y
#         self.label =label
# def get_my_key(obj):
#   return obj['size']  
# # creating list       
# list = [] 
  
# # appending instances to list 
# list.append(sample(4,3,1))
# list.append(sample(7,4,1))
# list.append(sample(5,6,1))
# list.append(sample(4,6,0))
# list.append(sample(5,8,0))
# list.append(sample(7,6,0))
# list.append(sample(9,7,0))
# list.append(sample(8,5,0))
# list.append(sample(4,1,1))
# list.append(sample(3,7,1))
# list.append(sample(4,4,0))
# list.append(sample(7,8,0))
# list.append(sample(4,10,0))
# list.append(sample(5,4,0))
# list.append(sample(3,7,1))
# list.append(sample(6,5,1))
# list.append(sample(6,2,1))
# list.append(sample(6,6,0))
# list.append(sample(7,4,0))
# list.append(sample(8,8,0))
import math
def get_my_key(obj):
  return obj['distance']
samples=[
{'x':4,'y':3,'label':1,'distance':0},
{'x':7,'y':4,'label':1,'distance':0},
{'x':5,'y':6,'label':1,'distance':0},
{'x':4,'y':6,'label':0,'distance':0},
{'x':5,'y':8,'label':0,'distance':0},
{'x':7,'y':6,'label':0,'distance':0},
{'x':9,'y':7,'label':0,'distance':0},
{'x':8,'y':5,'label':0,'distance':0},
{'x':4,'y':1,'label':1,'distance':0},
{'x':3,'y':7,'label':1,'distance':0},
{'x':4,'y':4,'label':0,'distance':0},
{'x':7,'y':8,'label':0,'distance':0},
{'x':4,'y':10,'label':0,'distance':0},
{'x':5,'y':4,'label':0,'distance':0},
{'x':3,'y':7,'label':1,'distance':0},
{'x':6,'y':5,'label':1,'distance':0},
{'x':6,'y':2,'label':1,'distance':0},
{'x':6,'y':6,'label':0,'distance':0},
{'x':7,'y':4,'label':1,'distance':0},
{'x':8,'y':8,'label':0,'distance':0},
]
f1=7
f2=5  
k = int(input("nhap k: "))  
# for obj in list:
# 	obj.distance=math.sqrt( (f1-obj.x)*(f1-obj.x)+(f2-obj.y)*(f2-obj.y) )
i=1;

for obj in samples:
	obj['distance']=math.sqrt( (f1-obj['x'])*(f1-obj['x'])+(f2-obj['y'])*(f2-obj['y']) )
	print("khoan cach tu mau test voi mau thu ",i, " la: ",obj['distance'])
	i+=1
nhom0=0
nhom1=0
samples.sort(key=get_my_key)
for obj in samples:
	print(obj)
j=1
for obj in samples:

	if(obj['label']==1):
		nhom1+=1
		#print(nhom1)

	else:
		nhom0+=1
	if(j==k):
		print("ok")
		break
	j+=1
	print(j)	
if(nhom0>nhom1):
	print('Mau thu thuoc nhom 0')
else:
	print('Mau thu thuoc nhom 1')			