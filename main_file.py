import db_add
import db_query

data = (1970, 1, 1)
db_query.query(data)

f = open('27612.dat', 'r')
data = []
counter = 1
for s in f.readlines():
    temp = s.split()
                #год,      месяц,   день,    час,      напр ветра,       осадки,           темпер-ра,          влажность
    data.append([temp[5], temp[6], temp[7], temp[10], float(temp[39]), float(temp[47]), float(temp[-31]), float(temp[-15])])
    db_add.add_inf(counter, temp)
    counter += 1
print(*data[:10], sep="\n")

