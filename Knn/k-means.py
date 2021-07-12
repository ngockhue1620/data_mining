# ý tưởng của thuật toán là
# ví dụ có 10 điểm , ta muốn phân 10 điểm dữ liệu này thành 2 cụm
# trước tiên chung ta phỉa đi tìm tâm của 2 cụm này
# sau đó tính khoản cách đến 10 điểm kia , điểm nào gần tâm cụm nào hơn thì thuộc cụm đó
# cách tìm tâm , thì chọn đại 2 điểm trong 10 điểm đó là tâm đầu tiên để tính
# nhưng để ra kết quả nhanh hơn thì nên chon 2 điểm đầu cuối (2 điểm có giá trị nhỏ nhất)

from random import random
import math
# ở đây mình random ra dữ liệu và nó bé hơn 10
# như ri thì không chọn được 2 điểm nhỏ nhất mà thôi kệ (nhát sort quá)
data=[
	
	{'a':int(random()*10),'b':int(random()*10)},
	{'a':int(random()*10),'b':int(random()*10)},
	{'a':int(random()*10),'b':int(random()*10)},
	{'a':int(random()*10),'b':int(random()*10)},
	{'a':int(random()*10),'b':int(random()*10)},
	{'a':int(random()*10),'b':int(random()*10)},
	{'a':int(random()*10),'b':int(random()*10)},
	{'a':int(random()*10),'b':int(random()*10)},
	{'a':int(random()*10),'b':int(random()*10)},
	{'a':int(random()*10),'b':int(random()*10)}
	
]
tam1 = data[0] # cum 1
tam2 = data[len(data)-1] # cum 2

def caculateDistance(obj,tam):
    #tính khoản cách từ tâm đến các điểm

    return math.sqrt( (tam['a']-obj['a'])**2 + (tam['b']-obj['b'])**2 )  

gia_tri_1 =""
gia_tri_2 =""

for i in data:
    print(i)

while True:
    diem_thuoc_cum_1=""
    diem_thuoc_cum_2=""

    x1 = 0
    y1 = 0

    x2 = 0
    y2 = 0
    for i in range(0,len(data)):
        if caculateDistance(data[i],tam1)<caculateDistance(data[i],tam2):
            diem_thuoc_cum_1+=str(i)
            x1+=data[i]['a']
            y1+=data[i]['b']
        else:
            diem_thuoc_cum_2+=str(i)
            x2+=data[i]['a']
            y2+=data[i]['b']
    # cập nhập tâm bằng trung bình cộng các giá trị a,b (x,y) của các điểm
    x1=x1/(len(diem_thuoc_cum_1))
    y1=y1/(len(diem_thuoc_cum_1))

    tam1 ={'a':x1,'b':y1}

    x2=x2/(len(diem_thuoc_cum_2))
    y2=y2/(len(diem_thuoc_cum_2))

    tam2 ={'a':x2,'b':y2}
    print()
    print("tam 1",tam1)
    print("cac diem thuoc tam 1",diem_thuoc_cum_1)
    print()
    print("tam 2",tam2)
    print("cac diem thuoc tam 2",diem_thuoc_cum_2)

    if gia_tri_1!=diem_thuoc_cum_1:
        gia_tri_1=diem_thuoc_cum_1
        gia_tri_2=diem_thuoc_cum_2
    else:
        break



