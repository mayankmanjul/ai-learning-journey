age = int(input("Enter your age: "))
has_email_verified = input("Has email verified? y/n: ")
has_subs = input("Has Subscription? y/n: ")
print("")
if age >=21 and has_email_verified == "y" and has_subs == "y":
    print("Access Granted")
elif age >=21 and has_email_verified == "n" and has_subs == "y":
    print("Reason for Denial: Email not Verified")
elif age >=21 and has_email_verified == "y" and has_subs == "n":
    print("Reason for Denial: have no subscription")
elif age >=21 and has_email_verified == "n" and has_subs == "n":
    print("Reason for Denial: have Email not Verified and have no subscription")
elif age < 21 and has_email_verified == "n" and has_subs == "n":
    print("Reason for Denial: Age is < 21 and have Email not Verified and have no subscription")
elif age < 21 and has_email_verified == "y" and has_subs == "y":
    print("Reason for Denial: Age is < 21")
elif age < 21 and has_email_verified == "n" and has_subs == "y":
    print("Reason for Denial: Age is < 21 and Email not Verified")
elif age < 21 and has_email_verified == "y" and has_subs == "n":
    print("Reason for Denial: Age is < 21 and have no subscription")
else:
    print("Wrong Input")