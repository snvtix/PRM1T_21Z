with open("splot.txt", "r+", encoding = "utf-8") as file:
    a = file.read()
    x = "."
    y = "*"
    z = ""
    b = a.count(x)
    c = a.count(y)
    print("liczba zdan w tekscie: ", b)
    print("liczba gwiazdek w tekscie: ", c)

    d = a.replace(y,z,c)

with open("zadanie3.txt", "r+", encoding = "utf-8") as file:
    file.write(d)



