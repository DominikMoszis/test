#pole neboli the list
#food = ["pizza", "hamburger", "apple", "fish"]

#food[1] = "sushi"

#užitečné funkce

#tato funkce přidá na konec pole daný string
#food.append("ice cream")

#food.remove("sushi")

#vymaže poslední element z pole
#food.pop()

#přidá element na místo které mu přiřadím 
#food.insert(2, "cake")

#seřadí pole v tomto případě podle abecedy
#food.sort()

#vymaže všechna data z pole
#food.clear()

#pole vždy vypsat cyklem
#for i in food:
    #print(i,  end=" ")



#procvičování loopů
#phone_number = "123-3344-2311"
#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end=",")


#for i in range(1,12):
    #if i != 9:
        #pass
        #print(i)

#name = "heloo my name iisb dominik"

#name = name.replace("iisb", "is")
#name = name.replace("heloo", "Hello")
#name = name.__add__(".")
#print(name)

#meal = ["hamburger","pizza","chese"]
#drink = ["soda","pepsi","cocacola"]
#food = [drink, meal]

#meal = ["hamburger","pizza","chese"]
#for i in meal:
#    if i == "pizza":
#        continue
#    print(i)

#tuple = je to něco jako pole, ale nelze měnit jeho elementy uvnitř a narozdíl od pole se používaji () tyto závorky

from pstats import SortKey


student = ("Dominik",17,"male")
#řekne kolik se těchto elementu v poli nází
print(student.count("Dominik"))
#kde se element nachazi
print(student.index("male"))

for i in student:
    print(i)

if "Dominik" in student:
    print("Dominik is here!")

#set => je to něco jako pole, ale je ohraničeno {} a je neindexované a neuspořádané. Tzn, že když to pole vypíšu, 
# tak ae nevypíše podle pořadí, ale random a když je tam více stejných elementů, tak je vypíše a 
# pracuje s nimi jako s jedním

set = {"knife","spoon","fork","fork","spoon"}
dishes = {"bowl","plate","fork","knife"}
#set.add("napkin")
#set.remove("fork")
#set.clear()
#=> update je, že spojí sety dohromady
#set.update(dishes)
#dinner_table = set.union(dishes)
#for i in dinner_table:
#    print(i)

#zjistí co v setu je a v dishes není
#print(set.difference(dishes))

#zjiszí co mají společného
print(set.intersection(dishes))

#dictionary = je to něco jako set, ale je tam key:value

#countries = {'USA':'Washington DC',
#             'Austria':'Wienna',
#             'Norway':'Oslo'}
#countries.update({"Germany":"Berlin"})
#countries.update({"USA":"Las vegas"})
#countries.pop("USA")
#countries.clear()
#když zjišťuji zda je tam nějaký klíč a nejsem si jist zda tam je, či ne použiji metodu get, protože je bezpečnější
#print(countries.get("USA"))
#print(countries.keys())
#print(countries.values())
#print(countries.items())

#for key,value in countries.items():
#    print(key,value)


#name  = "dominik"
#
#if (name[0].islower()):
#    name = name.capitalize()
#print(name)

#name = "dominik MOSZIS!"

#first_name = name[:3].upper()
#ast_name = name[8:].lower()
#vypíše poslední znak => záporné indexování =>jde to pozpátku => -1 je první od konce
#last_character = name[-1]
#print(first_name)
#print(last_name)
#print(last_character)

##funkce
#def hello(name,surname,age):
#    print("ahoj "+name+" "+surname)
#    print("You are "+str(age)+" years old.")

#surname = "Moszis"
#firs_name = "Dominik"
#hello(firs_name,surname,17)


#def mul(number1,number2):
#    return number1 * number2

#x = mul(8,8)
#print(x)

def div(number1,number2):
    return number1 / number2

x = div(8,4)
print(x)
    