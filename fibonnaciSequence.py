def print_fibonacci(user_input):
    x = int(user_input)
    fib_list = []
    print("0: 0")
    print("1: 1")
    fib_list.append(0)
    fib_list.append(1)
    for i in range(2, x):
        prev_2 = fib_list[i-2]
        prev_1 = fib_list[i-1]
        fib_list.append(prev_2 + prev_1)
        print(str(i) + ": " + str(fib_list[i]))



user = input("How many fibonacci numbers do you want? ")
if user.isdigit() and (int(user) >= 2):
    print_fibonacci(int(user))

else:
    print("error")
