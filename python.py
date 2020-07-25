value = (input("Enter a value you want to convert: "))

if value == "km":
    value_km = input("Enter amount of km you want to convert into miles: ")
elif value == "mile":
    value_mile = input("Enter amount of miles you want to convert into km: ")
else:
    print("Type the correct form")

def convert_km (value_km):
  return value_km * 1.60934
