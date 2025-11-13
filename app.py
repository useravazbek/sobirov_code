# Bro code cours
# if and else

# age = int(input("how old are you? "))

# if age >= 18:
#        print("You are an adult!")
# elif age == 100:
#        print("You are century old!") 
# elif age < 0:
#        print("You haven't been born yet!")
# else:
#        print("You are child!")


# ( or , and ) Logical operators

# temp = int(input("What is the temperature outside? "))

# if temp >= 0 and temp <= 30:
#        print("The weather is good today!")
#        print("Go outside!")
# elif temp < 0 or temp > 30:
#        print("The weather is bad today!")
#        print("Stay inside!")


# while loop ==?

# while 1==1:
#        print("Help me!")

# name = ""
# while len(name) ==0:
#        name= input("Enter your name: ")
# print("Hello " + name)


# for loop <=>    while loop => unlimited
# for loop => limited

# for i in range(50, 100 + 1, 2):
       # print(i)

# for i in "Avazbek Sobirov":
#        print(i)


# import time

# for second in range(10,0,-1):
#        print(second)
#        time.sleep(1)
# print("Happy New Year!")

# ===> Nested loops <===

# rows = int(input("How many rows:  "))
# columns = int(input("How many columns:  "))
# symbol = input("Enter a symbol to use:  ")

# for i in range(rows):
#        for j in range(columns):
#               print(symbol, end="")
#        print()

# ===> Loop control statements <===

# break = used to terminate the loop || Qiymat unga teng bo'lganda siklni to'xtatadi
# continue = skips to the next iteration of the loop || Qiymat unga teng bo'lganda siklni davom ettiradi
# pass = does nothing, acts as a placeholder || Qiymat unga teng bo'lganda hech narsa qilmaydi
# != teng emas

# while True:
#        name = input("Enter your name: ")
#        if name != "":
#               break

# phone_number = "123-456-7890"

# for i in phone_number:
#        if i == "-":
#               continue
# print(i, end="")

# for i in range(1,25):
#        if i == 13:
#               pass
#        else:
#               print(i)

# ===> List <===

# food = ["pizza", "fasFood", "sushi", "gamburger"]

# food[0] = "coffe"
# food.append("cream") # Element oxiriga qo'shish
# food.remove("sushi") # Elementni o'chirish
# food.pop() # Oxirgi elementni o'chirish
# food.insert(0, "cola") # Elementni ko'rsatilgan index ga qo'shish
# food.sort() # Elementlarni alifbo bo'yicha tartiblash
# food.clear() # Ro'yxatni tozalash
# food.extend(["cola", "fanta"]) # Ro'yxatga boshqa ro'yxatni qo'shish
# food.reverse() # Ro'yxatni teskari tartibda chiqarish


# for x in food:
#        print(x)


# ===> 2D Lists & Nested Lists <===

# drinks = ["coffe", "soda", "tea"]
# dinner = ["pizza", "pasta", "salad"]
# dessert = ["cake", "ice cream"]

# food = [drinks, dinner, dessert]

# # print(food[0][1]) # soda
# print(food)

# collection = single_list 

# list = []
# set = {}
# Tuple = ()

# meva = ["olma", "anor", "banan","shaftoli"]

# # print(dir(meva))
# # print(help(meva))


a = 23
b = 32
print(a + b)