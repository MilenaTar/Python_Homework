import sqlite3
import os
import json

#1

path = "C:/Users/Home/Desktop"
database = os.path.join(path,"film.db")
try:
    conn = sqlite3.connect(database)
except Exception as e:
    print(e)

curs = conn.cursor()
starts =  """SELECT film_id FROM film """
curs.execute("""SELECT title FROM film WHERE title LIKE 'B%' """)
conn.commit()
r = curs.fetchall()
print(r)

#2
curs.execute("""SELECT MAX(length) FROM film """)
conn.commit()
a = curs.fetchall()
print(a)

#3
curs.execute(""" SELECT * FROM film""")
conn.commit()
data = curs.fetchall()
with open("json_for_sqlite.json", "w") as file:
  json.dump(data, file)



#4
curs.execute("""SELECT title, release_year, rate  from film WHERE release_year > 2010 AND  (rate > 3 AND rate<5)""")
conn.commit()
data2 = curs.fetchall()

new_table = """ CREATE TABLE IF NOT EXISTS new_table (title text,
                                                      release_year integer,
                                                      rate integer); 
                                                      """

curs.execute(new_table)
conn.commit()


for i in range(len(data2)):
    v1 = data2[i][0]
    v2 = data2[i][1]
    v3 = data2[i][2]
    inserting_new_table = """ INSERT INTO new_table (title, release_year,rate)
                                                VALUES(?,?,?);"""   

    curs.execute(inserting_new_table,(v1,v2,v3))
    conn.commit()


