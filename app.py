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




# random>>> tasodifiy son yoki belgilarni tanlash uchun ishlatiladi
# random funksiyasi 0 bilan 1 orasidagi sonlarga bittasini tanlab beradi
# randrange ma'lum oraliqdagi butub sonlarni tanlab beradi (start,stop,step)
### stop-1 gacha qabul qiladi
# randit() bu funksiya a va b oraliqdagi tasodifiy tanlab beradi (a,b)
#  bunda b ni ham qabul qiladi


# import random
# for i in range():
#     x = random.randint(i)
#     print(x)




# ======================================

# fuits = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
# print(dir(fuits))
# print(help(fuits))
# print(len(fuits))
# print("piple" in fuits)

# fuits[0] = "avocado"
# fuits.append("piple")
# fuits.remove("apple")
# fuits.insert(1, "grape")
# fuits.sort()
# fuits.reverse()
# fuits.clear()

# print(fuits.index("apple"))
# print(fuits.count("apple"))


# for fur in fuits:
#     print(fur)


# mevalar = {"olma", "anor", "banan","shaftoli", "uzum"}
# print(dir(mevalar))
# print(help(mevalar))
# print(len(mevalar))
# print("piple" in mevalar)

# mevalar.add("piple")
# mevalar.remove("olma")
# mevalar.pop()
# mevalar.clear()

# print(mevalar)


# mevalar = ("olma", "anor", "banan","shaftoli", "uzum")
# print(dir(mevalar))
# print(help(mevalar))
# print(len(mevalar))
# print("piple" in mevalar)

# print(mevalar.index("olma"))

# print(mevalar.count("olma"))


# print(mevalar)

# for meva in mevalar:
#     print(meva)


# ================SHOPPOING CART PROGRAM======================
# pishirq = []
# meva = []
# sabzavot = []
# total = 0

# while True:
#        food = input("Olmoqchi bo'lgan maxshulotni kiriting (q chiqish): >>> ")
#        if food.lower() == "q":
#               break
#        else:
#               price = float(input(f"Summani kiriting dollarda {food}: $"))
#               pishirq.append(food)
#               meva.append(price)

# print("----- YOUR SHOPPING CART -----")

# for food in pishirq:
#        print(food, end=" ")

# for price in meva:
#        total += price

# print()
# print(f"Sizning to'liq summangiz: ${total}")




# ================== new code =====================

ismlar = ["Ali", "Vali", "Guli", "Soli"]
familiyalar = ["Karimov", "Sobirov", "Ahmedov", "Toshpulatov"]
shariflar = ["O'g'li", "Qizi"]

toliq_ism = [ismlar, familiyalar, shariflar]

ismlar[0] = "Anvar"
print(ismlar)