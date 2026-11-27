# import mysql.connector

# conn=mysql.connector.connect(host="localhost" , user="root" , password="Keerthi@1", database="company_db")

# if conn.is_connected():
#     print("MySQL connected successfully")
# conn.close()

# cursor=conn.cursor()
# cursor.execute("SELECT * FROM employees")
# records=cursor.fetchall()

# for row in records:
#     print(row)

# cursor.close()
# conn.close()

# query="SELECT * FROM employees WHERE department = 'IT'"
# cursor.execute(query)
# records=cursor.fetchall()

# for row in records:
#     print(row)

# cursor.close()
# conn.close()

# query="INSERT INTO employees(employee_id,emp_name,department,salary,experience)VALUES(%s,%s,%s,%s,%s)"
# values=(11,"John","IT",48000,3)
# cursor.execute(query,values)
# conn.commit()
# print("Record inserted successfully!")
# cursor.close()
# conn.close()


# query="UPDATE employees SET salary=%s WHERE employee_id=%s"
# values=(50000,1)
# cursor.execute(query,values)
# conn.commit()
# print("record updated successfully")
# cursor.close()
# conn.close()


# query="DELETE FROM employees WHERE employee_id=%s "
# value=(11,)
# cursor.execute(query,value)
# conn.commit()
# print("record deleted successfully")
# cursor.close()
# conn.close()


# cursor.execute("SELECT * FROM employees")
# record=cursor.fetchone()
# print(record)
# cursor.close
# conn.close()


# try:
#     conn=mysql.connector.connect(host="localhost" , user="root" , password="Keerthi@1", database="company_db")

#     if conn.is_connected():
#         print("MySQL connection successfull!")

# except mysql.connector.Error as e:
#     print("Error:",e)

# finally:
#     if "conn" in locals() and conn.is_connected():
#         conn.close()
#         print("connection closed")