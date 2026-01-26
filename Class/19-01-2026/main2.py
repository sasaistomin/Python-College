hour = int(input("Enter Hour: "))

if hour >= 0 and hour <= 10:
    print("Moning")
elif hour > 10 and hour <= 16:
    print("Day")
else:
    print("Naut")