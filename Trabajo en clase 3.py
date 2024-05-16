#  segun la escala de calificacion estandar (100,90,80...)
Calificacion=int(input("Ingresa la  ncalificacion:  "))

if Calificacion==100:
    print("Tu calificacion es A")
elif Calificacion>90<100:
    print("Tu calificacion es B")
elif Calificacion>80<90:
    print("Tu calificacion es C")
elif Calificacion>70<80:
    print("Tu calificacion es D")
elif Calificacion>60<70:
    print("Tu calificacion es E")
else:
    print("Tu calificacion es F")