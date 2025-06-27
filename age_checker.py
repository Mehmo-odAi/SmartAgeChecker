# Smart Age Checker Project by Mehmood

# Step 1: User se age input lena
age = int(input("Please enter your age: "))

# Step 2: Check karna ke user kis category mein aata hai
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
