#defiing variables and using them within a string
name = "jaydeep"
age = 42
job = "Linde plc"
print("my name is subhajit, I'm 37 years old & I work for Linde")
print("my name is " + name + " I'm " + str(age) + " years old & I work for " +
      job + ".")
#using backslash for adding a new line and using a quotation mark within a string
print("my name is subhajit. \n my age is 37")
print("he once said that \"we will reach at the top of our game..\"")
#few important functions ;
name = "Subhajit Kundu"
name1 = name.upper()
name2 = name.lower()
print("uppercase name : " + name1 + " and lower case name : " + name2)
print(name[5])
print(name2.index("k"))
print(name2.replace("subha", "abhi").replace("kundu", "chatterjee"))
#working with numbers :
var = -5
print(abs(var))
print(pow(var,2))
var = 2.78
print(round(var))
#importing external libraries
import math as m
print(m.pi)

#taking inouts from user :
name = input("what is you name?")
print("hello "+name+"!")

