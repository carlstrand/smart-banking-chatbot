#!/usr/bin/python 
import pymysql
import cgi, cgitb 
import sys
import os
import config
class customer:
	global cid,username,fname,lname,middle_name,email,password,contact,postal_add,perm_add,city,state,country,pincode,dob,gender
	def customer_details(self,user):
		sql="select * from customers where email='%s'"%user
		conn,cursor=config.connect_to_database()
		try:
			cursor.execute(sql)
			results=cursor.fetchall()
			for row in results:
				self.cid=row[0]
				self.username=row[1]
				self.fname=row[2]
				self.lname=row[3]
				self.email=row[4]
				self.password=row[5]
				self.contact=row[6]
				self.postal_add=row[7]
				self.perm_add=row[8]
				self.city=row[9]
				self.state=row[10]
				self.country=row[11]
				self.middle_name=row[12]
				self.pincode=row[13]
				self.dob=row[14]
				self.gender=row[15]
		except:
			print("Error")
		conn.close()
				
def get_any_value(user,f):
	c=customer()
	c.customer_details(user)
	if f=="cid":
		return c.cid
	elif f=="username":
		return c.username
	elif f=="fname":
		return c.fname
	elif f=="lname":
		return c.lname
	elif f=="middle_name":
		return c.middle_name
	elif f=="email":
		return c.email
	elif f=="password":
		return c.password
	elif f=="contact":
		return c.contact
	elif f=="postal_add":
		return c.postal_add
	elif f=="perm_add":
		return c.perm_add
	elif f=="city":
		return c.city
	elif f=="state":
		return c.state
	elif f=="country":
		return c.country
	elif f=="pincode":
		return c.pincode
	elif f=="dob":
		return c.dob
	elif f=="gender":
		return c.gender
	else: 
		return 0;