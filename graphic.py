import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('bd.db')
cursor = conn.cursor()

year1, year2 = int(input()), int(input())

x = [i for i in range(year1, year2)]
cursor.execute(f"SELECT temperature FROM stations WHERE year = {year1}")
y = cursor.fetchall()

plt.plot(x, y)
plt.show()

print(y)



