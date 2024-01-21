import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('bd.db')
cursor = conn.cursor()

year, month, hour = int(input("year: ")), int(input("Month: ")), int(input("hour: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    x = [i for i in range(1, 32)]
elif month in [4, 6, 9, 11]:
    x = [i for i in range(1, 31)]
elif month == 2 and year % 4 == 0:
    x = [i for i in range(1, 30)]
else:
    x = [i for i in range(1, 29)]

cursor.execute(f"SELECT temperature FROM stations WHERE year = {year} and month = {month} and hour = {hour}")
y = cursor.fetchall()

print(len(x), x)
print(len(y), y)




plt.plot(x, y)
plt.show()


