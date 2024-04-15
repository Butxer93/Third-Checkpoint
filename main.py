# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

name = "Ibon es mi nombre" #String
age = 30 #Number
snakes = ["Boa", "Pitón", "Culebra venenosa", "Víbora Rayada"] #List
is_coding = True #Boolean

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

grabbed_name = name[0:3]
print(grabbed_name)

# Exercise 3: Use an index to grab the first element from your list.

first_snake = snakes[0]
print(first_snake)

# Exercise 4: Create a new number variable that adds 10 to your original number.

new_number = age + 10
print(new_number)

# Exercise 5: Use an index to get the last element in your list.

last_snake = snakes[-1]
print(last_snake)

# Exercise 6: Use split to transform the following string into a list. 

names = 'harry,alex,susie,jared,gail,conner'
splitted_list = names.split(',')
print(splitted_list)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

just_name = name.split()[0]
upper = just_name.upper()
new_name = upper + name[4:]
print(new_name)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

phrase = f"{name}, tengo {age} años y soy de Bilbo."
print(phrase)

# Exercise 9: Print “hello world”.

print("hello world")

# Además necesito que me crees una cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".

sentence = 'Hola programadores, ¿Qué tal va el año?'
sentence = sentence.replace('Hola', 'Adios')
print(sentence)