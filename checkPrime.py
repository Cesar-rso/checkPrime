def isPrime(n: int) -> bool:
    div = n // 2
    while div > 1:
        if n % div == 0:
            return False
        div -= 1
    return True
    
if __name__ == "__main__":
    try:
        number = int(input("Type number to check if it is prime: "))
        print(isPrime(number))
    except:
        print("Error! You must enter an integer!")
