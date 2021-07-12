import math

f = open("G:\\z-ky2-nam3\\Slides-DataMining\\code\\Knn\\Data_Iris-Two-Cross\\iris.dat")

c = f.readlines()
# Read data from file iris.dat => 4 feature , 3 label
# f.readlines to read a line in file iris.dat , one line is a sample
# one line is a string , use split() method to remove space
# result is an array , example [1.22,21.4,1.5,3.4,1,0,0]
# add the result to array samples
samples=[]

for i in c:
	item=i.split()
	#add distance
	
	item.append(0)
	samples.append(item)
# have a element is wrong at the end of the array samples	
del samples[len(samples)-1]
# mix data with algorithm sort but the algorithm must wrong to mix data
print(len(samples))
for i in range(0,len(samples)-1):
	for j in range(0,len(samples)-1):
		if(samples[i][i%5]>samples[j][2]):
			temp = samples[i]
			samples[i]=samples[j]
			samples[j]=temp

# chose 80% to training
def training(obj):

	for i in range(0,int(len(samples)*0.8)):
		# minus 4 because a sample have len = n
		# but 4 last element is 3 feature and distance 
		distance=0
		a=int(len(samples[i])-4)
		for j in range(0,a):
			distance+=(obj[j]- float(samples[i][j]) ) * (obj[i] float(samples[i][j]) )
		samples[i][a+3]=math.sqrt(distance)
training()
for i in samples:
	print(i)