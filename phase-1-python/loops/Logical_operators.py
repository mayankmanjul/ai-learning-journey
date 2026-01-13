age = int(input("Enter your age: "))
has_id = input("Have voter id? y/n: ")
print("")
if age >= 18 and has_id == "y":
    print("Eligible for vote")
else:
    print("Not Eligible")