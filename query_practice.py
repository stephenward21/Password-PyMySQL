import pymysql.cursors
import bcrypt

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
							 user='x',
							 password='x',
							 db='Passwords',
							 charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor)


print ("connect successful!!")

try:
 

	with connection.cursor() as cursor:
		def run_query():
		# SQL
			# sql = "SELECT Username FROM accounts "
			sql = "SELECT Password FROM accounts WHERE Username = "'"epwimberly "'
		   
			# Execute query
			cursor.execute(sql)
		   
			print ("cursor.description: ", cursor.description)

			print()

			for row in cursor:
				print(row)

		run_query()
		   
finally:
	connection.close()