#9.	Haz un programa que calcule el IMC (índice de masa corporal), solicitándole al usuario 
#tu altura y peso
peso= input("escribe tu peso en kilos ")
estatura= input("escribe tu estatura en cm ")
imc= round(float (peso)/ float (estatura)**2,2)
print ("tu imc es ", str (imc))
