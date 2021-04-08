def main():
    num_list = []
    n = int(input("please enter the number:"))
    for i in range(n):
        x = int(input('enter the number'+str(i+1)+'of'+str(n)+": "))
        num_list.append(x)
    for i in range(n):
        print(num_list[i])

    num_list.sort()
    print(num_list)

main()