# falling gracefully

# n = 10
# try:
#     res = n / 1
# except ZeroDivisionError:
#     print("Can't be divided by zero!")
# finally:
#     print('always run')


# exit process 

# a=4
# b=9
# print(b-a)

def get_int():
    try: 
        x=int(input('Enter the value: '))
    except ValueError:
        print('Please enter numerical value')
    finally:
        print('closed')






