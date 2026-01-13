age = int(input("Enter your age: "))
email_verified = input("Has email verified? (y/n): ")
subscription = input("Has subscription? (y/n): ")

reasons = []

if age < 21:
   reasons.append("Age is less than 21")

if email_verified != "y":
    reasons.append("Email not verified")

if subscription != "y":
    reasons.append("No active subscription")

if not reasons:
    print("Access Granted")
else:
    print("Access Denied:")
    for reason in reasons:
        print("-", reason)
