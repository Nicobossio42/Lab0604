N1 = int(input("Ingrese primera nota: "))
N2 = int(input("Ingrese Segunda nota: "))
N3= int(input("Ingrese tercera nota: "))


promedio = (N1+N2+N3) / 3

if promedio>=7:
    print("Promedio", promedio)
elif promedio>=4 and promedio<=7:
    print("Regular")
else:
    print("no habilitado")
