import statistics

n = 0
c = 1
estatura_minima_m = 1.60
estatura_minima_h = 1.70

mujeres_admitidos = 0
mujeres_no_admitidos = 0

hombre_admitidos = 0
hombre_no_admitidos = 0

edad_mujeres_admitidas = []
estatura_hombre_admitidos = []


while True:
    aspirantes = int(input("numero de aspirantes: "))
    if aspirantes >= 1 and aspirantes <= 100 : 
        break

while aspirantes > n :
    print("numero del aspirante " +  str(c))
    genero = str(input("Genero del aspirante , M para mujer , H para hombre: "))
    edad = int(input("edad del aspirante: "))
    ec = str(input("Estado civil, S para soltero, C para casado : "))
    estatura = float(input("Estatura :"))
    if genero == "m" or genero == "M":
        if ec == "S" or ec == "s":
            if edad >=  20 and edad <= 25:
                if estatura >= estatura_minima_m :
                    edad_mujeres_admitidas.append(edad)
                    mujeres_admitidos += 1
                else: mujeres_no_admitidos += 1
            else:
                mujeres_no_admitidos +=1        
        else:
            mujeres_no_admitidos += 1
    if genero == "H" or genero == "h":
        if ec == "S" or ec == "s":
            if edad >= 18 and edad <= 24:
                if estatura >= estatura_minima_h:
                    estatura_hombre_admitidos.append(estatura)
                    hombre_admitidos += 1
                else:
                    hombre_no_admitidos += 1
            else:
                hombre_no_admitidos += 1
        else:
            hombre_no_admitidos += 1
    n += 1
    c +=1
if len(estatura_hombre_admitidos) >= 1 : 
    promedios_estatura_hombre = statistics.mean(estatura_hombre_admitidos)
    print("promedio de estatura hombre :" ,round(promedios_estatura_hombre))
if len(edad_mujeres_admitidas) >= 1:
    promedios_edad_mujer = statistics.mean(edad_mujeres_admitidas)
    print("promedio de edad mujeres :", round(promedios_edad_mujer))
no_admitidos = hombre_no_admitidos + mujeres_no_admitidos
resultado = no_admitidos * 100 / aspirantes

print("mujeres admitidas : " ,mujeres_admitidos ,"mujeres no admitidas :", mujeres_no_admitidos)
print("hombre admitidos : ", hombre_admitidos ,"hombre no admitidos :" , hombre_no_admitidos)
print("promedio de no admitidos ",round(resultado), "%")