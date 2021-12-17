temperatura1 = float(input(""))
atributo1 = str(input("").upper()).strip()
temperatura2 = float(input(""))
atributo2 = str(input("").upper()).strip()

temp1 = (temperatura1, atributo1)
temp2 = (temperatura2, atributo2)

if atributo1 == atributo2 and temperatura1 > temperatura2:
        print(temp1)
elif atributo1 == atributo2 and temperatura1 < temperatura2:
    print(temp2)
else:
    if atributo1 == "C":
        temp1_f = (temperatura1 * (9/5)) + 32
        if temp1_f > temperatura2:
            print(temp1)
        else:
            print(temp2)
    if atributo1 == "F":
        temp1_C = (temperatura1 - 32) * (5/9)
        
        if temp1_C > temperatura2:
            print(temp1)
        else:
            print(temp2)

