####################################################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS
###############################################

# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comprehesions

from more_itertools.more import divide
from openpyxl.styles.builtins import output




###############################################
# FONKSİYONLAR (FUNCTİONS)
###############################################

#####################
# Fonksiyon Okuryazarlığı
#####################

print("a", "b")
print("a", "b", sep="")

#####################
# Fonksiyon Tanımlama
#####################

def calculate(x):
    print(x*2)

calculate(5)

# İki argümanlı/parametreli bir fonksiyon tanımlayalım.

def summer(arg1, arg2):
    print(arg1+arg2)

summer(7, 8)

summer(8, 7)

summer(arg2=8, arg1=7)

#####################
# Docstring
#####################

def summer(arg1, arg2):
    print(arg1 + arg2)

def summer(arg1, arg2):
    """
sum of two numbers
    :param arg1: int, float
    :param arg2: int, float
    :return:
    int, float
    """
    print(arg1 + arg2)

summer(1, 3)

#####################
# Fonksiyonların Statement/Body Bölümü
#####################

# def function_name(parameters/arguments):
#      statements (function body)

def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")

say_hi()

def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")

say_hi("miuul")

def multiplication(a, b):
    c = a * b
    print(c)

multiplication(10, 9)

# girilen değerleri bir liste içinde saklayacak fonksiyon.

list_store = []

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1, 8)
add_element(18, 8)
add_element(180, 10)

#####################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
#####################

divide(1, 2)

def divide(a, b):
    print(a / b)

divide(10)

def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")

say_hi("mrb")

#####################
# Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?
#####################

# varm, moisture, charge

(56 + 15) / 80
(17 + 45) / 70
(52 + 45) / 80

def calculate(varm, moisture, charge):
    print((varm + moisture)/charge)

calculate(98, 12, 78)

#####################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
#####################

def calculate(varm, moisture, charge):
    print((varm + moisture)/charge)

#calculate(98, 12, 78) * 10 #nonetype hatası verir

def calculate(varm, moisture, charge):
    return(varm + moisture)/charge

calculate(98, 12, 78) * 10

a = calculate(98, 12, 78)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

type(calculate(98, 12, 78))

varm, moisture, charge, output = calculate(98, 12, 78)

#####################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
#####################

def calculate(varm, moisture, charge):
    return int((varm + moisture)/charge)

calculate(90, 12, 12) * 10

def standardization(a, p):
    return a * 10 / 100 * p * p

standardization(45, 1)

def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 12)

def all_calculation(varm, moisture, charge, a, p):
   print(calculate(varm, moisture, charge))
   b = standardization(a, p)
   print(b * 10)

all_calculation(1, 3, 5, 19, 12)

#####################
# Lokal & Global Değişkenler (Local & Global Variables)
#####################

list_store = [1, 2]

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1, 9)

#####################################################
# KOŞULLAR ( CONDITIONS)
######################################################


# True-False'u hatırlayalım.
1 == 1
1 == 2

# if
if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 11

if number == 10:
    print("number is 10")

number = 10
number = 20

def number_check(number):
    if number == 10:
        print("number is 10")

    number_check(12)

########################
# else
####################################

def number_chech(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


number_check(12)

######################################
# elif
############################

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check(6)

###############################################
# DÖNGÜLER (LOOPS)
########################################
# for loop

students = ["John","Mark","Venessa","Mariam"]

students[0]
students[1]
students[2]

for student in students:
    print(student)

for student in students:
    print(student.upper())
