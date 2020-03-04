a = 10
print(a)

print(type(a))

b = 10.56
print(b)
x = type(b)
print(x)

a = None
print(a)

print(type(a))

a = True
print(a)

print(type(a))


myStr = "Hello" #çift tırnak
myStr = 'Hello2'#tek tırnak
print(myStr)
print(type(myStr))

ch = 'A'
print(ch)
print(type(ch))


a = 1_000_000 #geçerli
print(a)


a = True

print(5 + a)



myStr = " \"Hello World\" "
print(myStr)
myStr = ' "Hello World" '
print(myStr)

str2 = """Merhaba ben uzun bir stringim
 ve birçok satıra yayılmam gerekiyor.""" #bunun yerine tek tırnak üç tane

print(str2)

#geçerli
str3 = '''Merhaba 'Güzel' "Dunya"'''
str4 = """ Mehaba "Dunya" """


# -> //comment line
'''
/*
Comment block
*/
'''


a = 4
print(id(a))
b = 14
print(id(b))



a = 5
print(id(a), type(a))
a = "Hello"
print(id(a), type(a))


a = 250
b = a

print(a, b)

b = 123

print(a, b)

myList = [10, 20, 30, 40]

myList2 = myList
print(myList)
print(myList2)

myList2[3] = 99

print(myList)
print(myList2)

6 * 2 / 4


x  = 100 % 7
y = 2 + x
print(y) #perşembe


x, y, z = 1, 2, 3

#swap
x = 10
y = 20

c = x
x = y
y = c
print(x,y)

#simultenous assignment swap işlemi
x, y = y, x

print(x,y)


val = int(input("Bir deger giriniz: "))

print(val + 5)


val = eval(input("Deger giriniz"))

print(val + 5)

x, y = eval(input("İki değer Deger giriniz"))
print(x, y)

import time
elapsedTime = time.time()

print(elapsedTime)
#saat göster

