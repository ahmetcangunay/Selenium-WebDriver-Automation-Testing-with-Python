loans = ["Fast loan", "Special for those who get their salary from Halkbank",
         "Happy retired consumer loan"]
print(loans)
print(loans[0])
print(loans[1])
print(loans[2])

print(len(loans))

loans[0] = "Quick Loan"
print(loans)

for loan in loans:
    print(loan)

for i in range(len(loans)):
    print(loans[i])

for i in range(3, 10):
    print(i)

for i in range(0, 11, 2):
    print(i)
