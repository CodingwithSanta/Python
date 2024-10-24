def dup(numbers):
    seen = set()
    for  num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return None
numbers = [1,2,3,4,5,4]
print("Duplicate Number:",dup(numbers))