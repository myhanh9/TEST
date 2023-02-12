flag = True
while(flag):
    n = input("Enter number of Fibonacci: , Enter '0' to exit")
    if n.isnumeric() is False:
        print("Please enter a number only!")
    elif int(n) == 0:
        flag = False
    else:
        Fib_list = [1, 1]
        for i in range(int(n)-2):
            Fib_list.append(Fib_list[len(Fib_list)-1] + Fib_list[len(Fib_list)-2])
        print(Fib_list)
