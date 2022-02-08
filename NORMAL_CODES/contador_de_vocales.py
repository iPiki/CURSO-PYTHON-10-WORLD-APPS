vocals=list(str(input("Escriba las vocales: ")))
length=len(vocals)
timer=0
contador=0
contador_e=0
contador_i=0
contador_o=0
contador_u=0
while length-timer !=0:
    for loop in vocals:
        if      loop=="a":
            contador=contador+1
        elif    loop=="e":
            contador_e=contador_e+1
        elif    loop=="i":
            contador_i=contador_i+1
        elif    loop=="o":
            contador_o=contador_o+1
        elif    loop=="u":
            contador_u=contador_u+1
    if loop !="a" and loop !="e" and loop !="i" and loop !="o" and loop !="u":
        print("Una letra no es vocal")
        break
print(f"a={contador}")
print(f"e={contador_e}")
print(f"i={contador_i}")
print(f"o={contador_o}")
print(f"u={contador_u}")