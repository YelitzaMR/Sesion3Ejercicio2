textoInicial: str='Importante: Si su IMC es entre 18.5 y 24.9, se encuentra dentro del rango saludable.Si su IMC es entre 25.0 y 29.9, se encuentra dentro del rango de sobrepeso. Si su IMC es 30.0 o superior, se encuentra dentro del rango de obesidad.'
print (textoInicial)
peso= float (input ('Por favor, introduzca su peso en kilos: '))
print (peso)
estatura= float (input ('Por favor, ingrese su estatura en metros: '))
print (estatura)
imc = round(peso/estatura**2,2)
print ('Su índice de masa corportal es:' + str (imc))
