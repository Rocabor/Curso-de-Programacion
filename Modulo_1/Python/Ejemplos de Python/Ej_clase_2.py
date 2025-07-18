"""
num_a=int(input("ingrese primer numero: ".upper()))
num_b=int(input("ingrese segundo numero: ".upper()))
if num_a==num_b:
    print(f"a={num_a} y b= {num_b} son iguales".upper()) 
elif num_a<num_b:
    print(f"el numero b={num_b} es mayor que a={num_a}".upper())
else:
    print(f"el numero a= {num_a} es mayor que b={num_b}".upper())"""


var_a= int(input("ingrese valor a: ".upper()))
var_b= int(input("ingrese valor b: ".upper()))
var_c= int(input("ingrese valor c: ".upper()))
if var_a==var_b and var_a==var_c:
    print(f"a={var_a} b= {var_b} y c={var_c} son iguales".upper()) 
elif var_a>var_b and var_a>var_c:
    print(f"el numero a={var_a} es mayor que b={var_b} y que c={var_c}".upper())
elif var_b>var_a and var_b>var_c:
    print(f"el numero b={var_b} es mayor que a={var_a} y que c={var_c}".upper())
else:
    print(f"el numero c={var_c} es mayor que a={var_a} y que b={var_b}".upper())

"""
calificacion= int(input("ingrese calificacion: ".upper()))
if calificacion >= 90:
    print(f"grado de calificacion: A".upper()) 
elif calificacion>=80 and calificacion <=89:
    print(f"grado de calificacion: B".upper()) 
elif calificacion>=70 and calificacion <=79:
    print(f"grado de calificacion: C".upper()) 
elif calificacion>=60 and calificacion <=69:
    print(f"grado de calificacion: D".upper()) 
else:
    print(f"grado de calificacion: F".upper()) """

"""
signo= int(input("ingrese numero: ".upper()))
if signo>0:
    print(f"el numero es positivo:".upper())
elif signo <0:
     print(f"el numero es negativo:".upper())
else:
      print(f"el numero es 0:".upper())   """


