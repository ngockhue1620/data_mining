# import mysql.connector
   
# # tạo đối tượng connection
# myconn = mysql.connector.connect(host = "localhost", user = "root", 
#     passwd = "root", database='bong_da')
   
# # in đối tượng connection ra màn hình
# print(myconn)

from mysql.connector import MySQLConnection, Error
 
# Hàm kết nối
def connect():
    """ Kết nối MySQL bằng module MySQLConnection """
    db_config = {
        'host': 'localhost',
        'database': 'bong_da',
        'user': 'root',
        'password': 'root'
    }
 
    # Biến lưu trữ kết nối
    conn = None
 
    try:
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            return conn
 
    except Error as error:
        print(error)
 
    return conn

conn = connect()
tran_bong = []
ti_le_cua_tran=[]

def get_ti_le(id):
    ti_le=[]
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ti_le where tran_id="+str(id))
    row = cursor.fetchone()
    
    while row is not None:
        ti_le.append(list(row))
        row = cursor.fetchone()
    
    ti_le_cua_tran.append(ti_le)
        



def get_tran():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tran")
 
        row = cursor.fetchone()
 
        while row is not None:
            tran_bong.append(list(row))
            row = cursor.fetchone()
 
    except Error as e:
        print(e)
 
    finally:
        # Đóng kết nối
        cursor.close()
        conn.close()

get_tran()

for i in range(0,len(tran_bong)):
    get_ti_le(tran_bong[i][0])
print(len(tran_bong))
print(len(ti_le_cua_tran))
#du doan cho tran cuoi cùng
tran_du_doan=ti_le_cua_tran[len(tran_bong)-1]

import math

# hai tran cung 1 luc
# for i in range(0,len(tran_bong)):
    
#     if i == len(tran_bong):
#         break
#     else:
#         if tran_bong[i]==21:
#             break
#         else:

#             feature_distance = 0
#             try:        
#                 for j in range(0,len(ti_le_cua_tran[i])):
                    
#                     feature_distance+= math.sqrt( ( float(ti_le_cua_tran[i][j][1])-float(tran_du_doan[j][1]) ) * ( float(ti_le_cua_tran[i][j][1])-float(tran_du_doan[j][1]) ) + ( float(ti_le_cua_tran[i][j][2])-float(tran_du_doan[j][2]) )*( float(ti_le_cua_tran[i][j][2])-float(tran_du_doan[j][2]) ))
#                 tran_bong[i].append(feature_distance)
                
                    
#             except:
#                 print("er")
#     print()


for i in range(0,len(tran_bong)):
    
    if i == len(tran_bong):
        break
    else:
       

        feature_distance = 0
        try:        
            for j in range(0,len(ti_le_cua_tran[i])):
                
                feature_distance+= math.sqrt( ( float(ti_le_cua_tran[i][j][1])-float(tran_du_doan[j][1]) ) * ( float(ti_le_cua_tran[i][j][1])-float(tran_du_doan[j][1]) ) + ( float(ti_le_cua_tran[i][j][2])-float(tran_du_doan[j][2]) )*( float(ti_le_cua_tran[i][j][2])-float(tran_du_doan[j][2]) ))
            tran_bong[i].append(feature_distance)
            
                
        except:
            print("er")
    print()

def get_my_key(obj):
  return obj[6]
tran_bong.sort(key=get_my_key)

for i in range(0,len(tran_bong)):
    print(tran_bong[i])
    print()

