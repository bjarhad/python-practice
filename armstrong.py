
number = input("Enter a number: ")


def is_armstrong(number: str):
    digit = len(str(number))
    total_sum = sum([int(i) ** digit for i in str(number)])
    if total_sum == number :
        return True
    else:
        return False

if is_armstrong(int(number)):
    print('Number is armstrong')
else:
    print('Number is not armstrong')