def prime_number_checker(num):
    flag=1
    for i in range(2,num,1):
        if(num%i==0):
            flag=0
            break
    return flag

def main():
    print("Please enter a number")
    num = int(input())
    flag=prime_number_checker(num)
    if(flag==1):
        print(num," is a prime")
        print("The value of flag is ", flag)
    else:
       print(num," is not a prime")

#give a space between main and if main
if __name__=="__main__":
    main()