#exceptions => když chci něco zakázat v programu jako např. když chci aby do inputu psali pouze čísla a kdyžb nepíšou něco jiného, tak 
#jim to naíše třeba, že to není číslo a že to mají změnit
try:        #try normálně provádí kód, ale když narazí na chybu, tak přeskočí zbytek kódu a začne provádět kód od řádku s exception
    number1 = int(input("Enter a number to devide: "))
    number2 = int(input("Enter a number to devide by: "))
    result = number1 / number2
    print(result)
except ZeroDivisionError:
    print("You can't devide by zero! Idiot!")   #zerrodivisionerror => kontrluje zda se nedělí nulou
except ValueError:
    print("Enter only numbers please!")     #valueerror => kontroluje zda místo čísla nenapsal někdo písmeno
except Exception:
    print("Something went wrong :(")

