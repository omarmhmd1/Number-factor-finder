def finding_factor(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result

def multiplied_numbers(factors, number):
    multiplied_numbers_list = []
    
    
    for i in range(len(factors)):
        for j in range(i, len(factors)):  
            if factors[i] * factors[j] == number:
                multiplied_numbers_list.append([factors[i], factors[j]])
    
    return multiplied_numbers_list

while True:
    try:
        number = int(input("Enter Your Number (Integer Number): "))
        if number <= 0:
            print("Please enter a positive integer.")
            continue
        factors = finding_factor(number)
        result = multiplied_numbers(factors, number)
        print(f"Pairs of factors whose product is {number}:")
        for pair in result:
            print(pair)
    except ValueError:
        print("Invalid input. Please enter an integer number.")