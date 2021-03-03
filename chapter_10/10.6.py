# try:
#     a = int(input())
# except ValueError:
#     print("Enter the number!")
#     a = int(input())
# try:
#     b = int(input())
# except ValueError:
#     print("Enter the number!")
#     b = int(input())

# print(a+b)


try:
    a = int(input())
    b = int(input())
except ValueError:
    print("Enter the number!")
else:
    print(a+b)
