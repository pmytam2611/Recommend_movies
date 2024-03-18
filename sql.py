import pyodbc

# Tạo kết nối với cơ sở dữ liệu SQL Server
def connect():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          r'SERVER=DESKTOP-EQJF9I1\SQLEXPRESS;'
                          'Database=Recommend_Movies;'
                          'UID=sa;'
                          'PWD=sa')
    return conn

# Thực hiện truy vấn
# cursor = connect().cursor()

# sql_insert = "INSERT INTO movie VALUES (?, ?, ?, ?, ?, ?)"
#
# for i in range(1589, 1682):
#     # Prepare the data to be inserted (replace with your actual values)
#     values = (df[i][0], df[i][1], df[i][2], df[i][3], df[i][4], 'poster/' + str(i) + '.PNG')
#
#     cursor.execute(sql_insert, values)
#     conn.commit()

def select():
    sql_select = "SELECT image_path from movie WHERE movie_id=0"
    return sql_select

# # Đóng kết nối
# cursor.close()
# connect().close()
