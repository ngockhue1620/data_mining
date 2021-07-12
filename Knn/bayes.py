# 0  => class +
# 1 =>  class -

data=[
	
	{'a':0,'b':0,'c':0,'label':0},
	{'a':0,'b':0,'c':1,'label':1},
	{'a':0,'b':1,'c':1,'label':1},
	{'a':0,'b':1,'c':1,'label':1},
	{'a':0,'b':0,'c':1,'label':0},
	{'a':1,'b':0,'c':1,'label':0},
	{'a':1,'b':0,'c':1,'label':1},
	{'a':1,'b':0,'c':1,'label':1},
	{'a':1,'b':1,'c':1,'label':0},
	{'a':1,'b':0,'c':1,'label':0}
	
]

test ={'a':0,'b':1,'c':0,'label':-1}

def get_P_Class_Plus():
    dem=0
    # 0 class +
    for i in data:
        if(i['label']==0):
            dem+=1
    return dem

# xác xuất của từng class
# tính xác xuất của 1 class trong bộ dữ liệu
P_Class_Plus_In_Dataset  = get_P_Class_Plus()
P_Class_Minus_In_Dataset = len(data) - P_Class_Plus_In_Dataset

#   lần lược là các đặc trưng A,B,C của class +
#    A,B,C
#   [0,0,0],

#   lần lược là các đặc trưng A,B,C của class -
#   [0,0,0]
Result_Maxtrix=[

        [0,0,0],
        [0,0,0]
    ]

def set_Value_To_Result_Maxtrix():
    for i in data:
        # 0 class +
        # nếu phần tử thứ i là lớp +
        if(i['label']==0):
            # nếu test['a']==i['a'] 
            # nghĩa là có thêm 1  đặc trưng A của lớp + cho ra +
            
            if( test['a']==i['a'] ):                
                Result_Maxtrix[0][0]+=1
            
            # nếu test['b']==i['b'] 
            # nghĩa là có thêm 1  đặc trưng A của lớp + cho ra +
            if( test['b']==i['b'] ):                
                Result_Maxtrix[0][1]+=1

            # nếu test['c']==i['c'] 
            # nghĩa là có thêm 1  đặc trưng A của lớp + cho ra +

            if( test['c']==i['c'] ):                
                Result_Maxtrix[0][2]+=1
        else:
            if( test['a']==i['a'] ):                
                Result_Maxtrix[1][0]+=1
            
            # nếu test['b']==i['b'] 
            # nghĩa là có thêm 1  đặc trưng A của lớp + cho ra +
            if( test['b']==i['b'] ):                
                Result_Maxtrix[1][1]+=1

            # nếu test['c']==i['c'] 
            # nghĩa là có thêm 1  đặc trưng A của lớp + cho ra +

            if( test['c']==i['c'] ):                
                Result_Maxtrix[1][2]+=1

set_Value_To_Result_Maxtrix()
giả
# xác xuất để mẩu test thuộc lớp + = P (X | Class = “+”) * P (Class = “+”) 
# bằng xác xuất của các đặc trưng trong X(data/mẫu thử) cho ra lớp công
# nhân với xác xuất lớp cộng xuất hiện trong bộ dữ liệu
# => P(X | class = "+") * P(Class = "+") 
#       = 
#    P ( A = 0 | Class ="+" ) * P ( B = 1 | Class ="+" ) * P ( C = 0 | Class ="+" )
# xác xuất lớp + = xác xuất lớp công xuất hiện trong bộ data 
#   nhân với 
# (xác xuất của đặc trưng A (có giá trị bằng tổng sô lần đặc trưng A thuộc lớp + bằng với giá trị của đặc trưng A trong mẫu thử 
#   chia cho
# số mẩu thử là lớp cộng)
#   nhân với 
#( xác xuất của đặc trưng B (có giá trị bằng tổng sô lần đặc trưng B thuộc lớp + bằng với giá trị của đặc trưng B trong mẫu thử 
#   chia cho
# số mẩu thử là lớp cộng)
#   nhân với 
# (xác xuất của đặc trưng C (có giá trị bằng tổng sô lần đặc trưng C thuộc lớp + bằng với giá trị của đặc trưng C trong mẫu thử 
#   chia cho
# số mẩu thử là lớp cộng)

#P_Class_Plus = (P_Class_Plus_In_Dataset/len(data)) * (Result_Maxtrix[0][0]/P_Class_Plus_In_Dataset) * (Result_Maxtrix[0][1]/P_Class_Plus_In_Dataset) * (Result_Maxtrix[0][2]/P_Class_Plus_In_Dataset)
# rút gọn
P_Class_Plus =( P_Class_Plus_In_Dataset/len(data) )*(Result_Maxtrix[0][0]*Result_Maxtrix[0][1]*Result_Maxtrix[0][2])/(P_Class_Plus_In_Dataset**3)

# tương tự cho lớp -
P_Class_Minus =( P_Class_Minus_In_Dataset/len(data) )*(Result_Maxtrix[1][0]*Result_Maxtrix[1][1]*Result_Maxtrix[1][2])/(P_Class_Minus_In_Dataset**3)

# sau khi có sác xuất , tiến hành phân lớp
# xác xuất nào lớp hơn thì mẫu thuộc lớp đó
print("Xác Xuất Của lớp + là :" ,P_Class_Plus)
print("Xác Xuất Của lớp - là :" ,P_Class_Minus)
print("Mẫu Thử Thuộc Lớp -" if P_Class_Minus>P_Class_Plus else"Mẫu thử thuộc lớp +")


# hén không phải là 1 bài toán phân lớp
# không đưa ra kết quả dựa trên model


# đây là quá trình khai phá dữ liệu dựa vào bộ dữ liệu có sẳn
# để dự đoán cho tương lai

# không vì sẻ có nhiều dữ liệu nhiểu làm ảnh hưởng 
# đến quá trình phân tích

# dựu vào 
# có 2 lớp là lớp giàu ngeo
# có 3 đặc trưng , là đi xe chi , 

# dùng KNN để phân lớp 
# trích xuất đặc trưng 

#     chọn ra dữ liệu trong kho dữ liêu

#     feaurte  là chọn la những đặc tính trội


