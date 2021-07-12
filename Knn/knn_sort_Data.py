import math

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
{'x':7,'y':4,'label':0,'distance':0},
{'x':8,'y':8,'label':0,'distance':0},
]

def get_my_key(obj):
  return obj['distance']

# sort sai để trộn bộ data
def sort_function(array):
	for i in range(0,len(array)):
		for j in range(1,len(array)):			
			if(array[i]['x']>array[j]['x']):
				temp = array[i]
				array[i]=array[j]
				array[j]=temp
#lấy 80% để làm mẩu train
# tức là lấy 16 phần tử đầu để training 4 phần tử cuối để test

#===#
#function nhận vào 2 giá trị f1,f2 là từng giá trị truyền vào của bộ testing 
def training(f1,f2,k):
	 
	
	# for obj in list:
	# 	obj.distance=math.sqrt( (f1-obj.x)*(f1-obj.x)+(f2-obj.y)*(f2-obj.y) )
	i=0;
	trainingSample=[]
	print("----------------------")
	print(samples)	
	print("----------------------")
	for obj in samples:
		obj['distance']=math.sqrt( (f1-obj['x'])*(f1-obj['x'])+(f2-obj['y'])*(f2-obj['y']) )
		trainingSample.append(obj)
		print("khoan cach tu mau test voi mau thu ",i, " la: ",obj['distance'])
		i+=1
		if(i >= len(samples)*0.8):# nếu tính được trên 80% thì dừng
			print("dung ",i)
			break
	#đặt số lượng nhãn cho từng nhóm là 0		
	nhom0=0
	nhom1=0

	#sort lại các giá trị khoản cách
	trainingSample.sort(key=get_my_key)
	

	# dếm số lượng nhãn để phân lớp
	# cho biến j chạy để đếm đủ j=k thì dừng
	j=1
	for obj in trainingSample:
		print(obj)
		if(obj['label']==1):
			nhom1+=1

		else:
			nhom0+=1
		if(j==k):
			break
		j+=1	
	
	if(nhom0>nhom1):
		print('Mau thu thuoc nhom 0')
		return 0
	else:
		print('Mau thu thuoc nhom 1')
		return 1
	

# ở phần testing lấy từng phần tử của bộ testing tức là lấy 4 phần tử cuối lần lược truyền vào funtion training
confusionMatrix=[[0,0],[0,0]]
def testing():
	a=int(len(samples)*0.8)
	for i in range(a,len(samples)):
		result=training(samples[i]['x'],samples[i]['y'],k)
		#cập nhập bảng confution maxtrix
		# sample[i]['lable'][result] nghĩa là
		# result  = 0 hoặc 1
		# samples[i]['lable'] nghĩa là samples[16]['lable'] property lable của phần tử thứ 16 của mảng
		# samples[1][0],samples[1][1],samples[0][0],samples[0][1]
		confusionMatrix[samples[i]['label']][result]+=1
		





k = int(input("nhap k: "))  
sort_function(samples)
testing()
print("Confusion Matrix Table:")
for i in confusionMatrix:
	print (i)
Accuracy=(confusionMatrix[0][0]+confusionMatrix[1][1])/(int(len(samples)-len(samples)*0.8))*100
print("Model Accuracy is:",Accuracy,"%")
