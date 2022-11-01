from sqlite3 import SQLITE_RECURSIVE


#FullName = "Siri" #Pascal casing
#fullname = "Siri" #Camel casing
full_name = "Ahmed" #Snake casing

Age = "36"
Gender = "M"
Stipend = "600"
#Comparison Operator
#if FullName == fullname:
print("the names are the same")
print("the names are not the same")
#Logical Operator
if (full_name == "Siri" and Gender == "F"):
        print("TRUE")
if (full_name == "Siri" or Gender == "F"):
        print("TRUE - AND")
if (full_name == "Siri" or Gender == "M"):
        print("TRUE _ OR")
if (full_name == "Ahmed" and Gender == "M"):
        print("TRUE")




#print (f"Hello {full_name}! Your age is {Age} and your stipend is GHS {Stipend}") Long way
#print("Hello" + full_name + "Your age is"  +  Age)
#print("Hello" + full_name + "Your age is"  +  str(Age))
