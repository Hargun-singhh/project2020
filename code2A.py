# 1. Storage Container Creation Statement
johnsAge = 20

# johnsAge is a Reference Variable
# It holds HashCode for the Data 20

# 2. Container Read Statement
print("Johns Age is:", johnsAge)
print("Johns Age HashCode is:", id(johnsAge))

jenniesAge = 20
print("Jennies Age is:", jenniesAge)
print("Jennies Age HashCode is:", id(jenniesAge))

print("===================")

# 3. Container Updation Statement
johnsAge = 70

print("Johns Age Now is:", johnsAge)
print("Johns Age HashCode Now is:", id(johnsAge))

print("Jennies Age Now is:", jenniesAge)
print("Jennies Age HashCode Now is:", id(jenniesAge))

# 4. Container Copy Statement | Reference Copy
siasAge = jenniesAge
print("===================")

print("Sias Age is:", siasAge)
print("Sias Age HashCode is:", id(siasAge))

# 5. C
del johnsAge

print("Johns Age Now is:", johnsAge)
print("Johns Age HashCode Now is:", id(johnsAge))
