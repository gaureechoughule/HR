import csv

with open("utils/info.csv", "r") as fobj:
    content = csv.reader(fobj)
    next(content)

    for i in content:
        if int(i[7]) > 9000:
            # print(i)
            a = ["full_name", "email", "phone_no"]
            b = i[1] + " " + i[2], i[3], i[4].replace(".", "")
            c = dict(zip(a, b))
            print(c)
