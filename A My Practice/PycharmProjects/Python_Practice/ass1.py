def is_prime(number):
    if number>1:
        flag=True
        for num in range(2,int(number/2)):
            if (number%num)==0:
                flag=False
        return flag
    else:
        return False


num=int(input('Enter Number: '))
if (is_prime(num)):
    print('Number is prime')
else:
    print('Number is not prime')
