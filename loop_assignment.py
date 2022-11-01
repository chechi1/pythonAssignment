

#Even numbers between 1 -30 while loop
print("even numbers between 1 and 30")
a = 0
while(a<=30):
    if(a%2 == 0):
     print (a)
    a=a+1

#odd numbers between 1 - 30 while loop
print("odd numbers between 1 and 30")
a = 0
while (a<=30):
 if a % 2!= 0:
  print(a)
 a=a+1

#even numbers between 1 - 30 for loop
print("even numbers between 1 -30 ")

for a in range (2,29,2):
        print(a)

#odd numbers between 1 - 30 for loop
print("odd numbers between 1 -30 ")

for a in range (1, 30, 1):
        print(a)

        


#Ahmed's Financial Statement

budget = int(input("What is your budget? "))
marketingCost = int(0.25 * budget)
operationalExpenses = int(0.5 * budget)
totalExpenses = int(marketingCost + operationalExpenses)
customerAcquisition = int(0.25 * budget)
customers = int(customerAcquisition / 5)

print("-----------Ahmed's Financial Statement---------------------")
print(f" Number of Customers acquired {customers}")
print(f" Ahmed's total costs          {totalExpenses}")
print(f" Marketing Expenses           {marketingCost}")
print(f" Opex                         {operationalExpenses}")
print("-----------------------------------------------------------")

