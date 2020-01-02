#!/usr/bin/python
import mysql.connector
import pandas as pd
import numpy as np


df = pd.read_excel("numero.xlsx") # nombre archivo pendiente

# si es diferente de cero eliminar 

for i in df.index:
	if i == 0:
		a = np.array([df['id'][i]]);
	else:
		a = np.append(a, df['id'][i])



# Connect
db = mysql.connector.connect( user='root', password='root', host='localhost', database='recargasatc', port=3306 )
cursor = db.cursor()

cont = 1
for i in a:
	if i != 0:
		cont += 1
		print(" update numero set regionNumero_id = 2 where id =  "+str(i))
		print(cont)
		cursor.execute(" update numero set regionNumero_id = 2 where id =  "+str(i))
		db.commit()
		print(cursor.rowcount, "record(s) deleted")


db.close()