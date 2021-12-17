temperatura1 = float(input(""))
atributo1 = str(input("").upper()).strip()
temperatura2 = float(input(""))
atributo2 = str(input("").upper()).strip()

temp1 = (temperatura1, atributo1)
temp2 = (temperatura2, atributo2)

if atributo1 == atributo2:
    print(f"({temperatura1 + temperatura2}, '{atributo1}')")
else:
    print(f"({temperatura1 + temperatura2 :.4f}, '{atributo2}')")
    
