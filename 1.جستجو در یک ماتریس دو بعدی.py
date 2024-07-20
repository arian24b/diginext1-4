

def search(n: int, numbers: list) -> bool:
    for x in numbers:
        for y in x:
            if y == n:
                return True
            elif y > n:
                return False
    return False


print(search(n=8, numbers=[[1, 3, 5], [7, 8, 10], [12, 15, 18]]))
