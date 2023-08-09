#dodawanie
def add (a,b):
    return a + b

#odejmowanie
def substract (a, b):
    return a - b

#mnozenie
def multiply(a, b):
    return a * b

#dzielenie
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielic przez 0"
    
#Pytamy uzytkownika o dwie zmienne 
a = float (input ("Podaj wartosc a: "))
b = float (input ("Podaj wartosc b: "))

#wybieramy znak operacji 
operation = input ("Wybierz znak operacji (+, - , * , /): ")

#wybor operacji
if operation == "+":
    result = add(a,b)
elif operation == "-":
    result = substract (a,b)
elif operation == "*":
    result = multiply(a,b)
elif operation == "/":
    result = divide (a, b)
else:
    result = "Nieznana operacja"


print ("Wynik operacji: ", result)