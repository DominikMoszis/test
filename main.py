print( "Hello world!" )
first_name = "Dominik"
last_name = "Moszis"
full_name = first_name +" "+last_name
print("Jmenuji se "+full_name)
x = "2"
print("10 = 5 * "+x)
#tento kód pod tím vypisuje datový typ proměnné, což je vtomto případě STRING
print(type(first_name))

#integer se píše bez uvozovek
age = 17
age += 1
print("My age is: "+str(age))
print(type(age))

#desetinná čísla neboli float se píšou bez uvozovek a s tečkou mezi
height = 185.2
print("Moje výška je: "+str(height)+" cm")
print(type(height))

#boolean je datatype který umí je true a false
#hodí se u IF, ELSE atd.
human = False
print("Are you a human: "+str(human))
print(type(human))

#muliple assigment
name, age, attractive = "Dominik", 17, True
print (" ")
print(name)
print(age)
print(attractive)

spongebob = patrick = sue = 30

print(patrick)
print(spongebob)
print(sue)

name, first_surname, age = "Dominik", "Mojzis", 17
print("Dobrý den, jmenuji se "+name+" "+first_surname+" a je mi "+str(age)+" let.")
print(type(age))

#string methods
name = "Dominik"

#tato metoda stringu vypíše počet znaků ve stringu
print(len(name))

#tato metoda stringu vypíše kde se nachází daný znak v tomto případě i
#vypíše to v jakém pořadí je
print(name.find("i"))

#první písmen velké
print(name.capitalize())

#vše velké
print(name.upper())

#vše malé
print(name.lower())

#zjistí jestli ve stringu jsou písmena => false, nebo čísla => true
print(name.isdigit())

#jestli je string pouze z abecedy (mezery se počítají také!!)
print(name.isalpha())

#zjistí kolik znaků, na teré se zeptám je ve stringu
print(name.count("i"))

#vymění v tomto případě i za jiný string v tomto případě a
print(name.replace("i","a"))

#vypíše to tolikrát kolikrát to vynásobím
print(name*10)


#input
#name = input("What is your name: ")
#age = input("How old are you: ")
#age = int(age) + 1
#print("Hello "+name+"!")
#print("You are "+str(age)+" years old.")

import math

x = math.pi
print(round(x))

#zaokrounhlení nahoru
print(math.ceil(x))

#zaokrounhlení dolu
print(math.floor(x))

#absolutní hodnota
print(abs(x))

#dá dané číslo na druhou, nebo na kolikátou napíšu jako druhé číslo za proměnnou
print(pow(x, 2))

#nějaké číslo na druhou se rovná proměnná a vypíše to to číslo ve floatu
print(math.sqrt(x))

#minimum a maximum z pole či více proměnných
x = (1, 3, 2)
print(max(x))
y = 1
c = 3
z = 2
print(min(y, c, z))

name = "Dominik Mojzis"
firsr_name = name[:7]
second_name = name[8:]
print(firsr_name)
print(second_name)
funky_name = name[::2]
print(funky_name)
reversed_name = name[::-1]
print(reversed_name)

website = "https://google.com"
website1 = "https://wikipedia.com"
slice = slice(8,-4)
print(website[slice])
print(website1[slice])