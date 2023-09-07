import csv

with open("utils/info.csv", "r") as fobj:
    content = csv.reader(fobj)
    next(content)

    for i in content:
        if int(i[7]) > 4200 and int(i[10]) >= 30 and int(i[10]) <= 110:
            #a = ["hire_date", "full_name"]
            i[5] = i[5][-2:] + i[5][2:-2] + i[5][:2]
            b = {i[5]: [i[1] + " " + i[2]]}
            #c = dict(zip(a, b))
            print(b)
