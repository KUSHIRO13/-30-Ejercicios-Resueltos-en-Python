"""
► Enunciado:

Escribir un programa que pregunte el nombre y apellido del usuario. Luego de ser introducidos los datos muestre por pantalla la cadena ¡Hola {nombre} {apellido}, gusto en conocerte!, donde:

{nombre} y {apellido} son los valores introducidos.
"""

nombre = input("Cual es tu nombre?: ")
apellido = input("Cual es tu apellido?: ")

print(f"Hola {nombre} {apellido}, gusto en conocerte!")