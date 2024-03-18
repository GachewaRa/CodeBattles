def mean(numbers):
    sum = 0
    
    for num in numbers:
        sum += num
    mean = sum / len(numbers)
    return mean