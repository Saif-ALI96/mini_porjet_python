# print('meow\n' * 3, end='')
# print('meow')
# print('meow')

# i = 1
# while i <= 3:
#     print('meow')
#     i += 1

def main():
    number = get_number()
    mewo(number)

def get_number():
     while True:

        n= int(input("Enter a number between 0 and 5: "))
        if (n >= 0 and n <= 5):
            return n

def mewo(n):
    for _ in range(n):
        print('meow')

main()