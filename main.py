def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

if __name__ == "__main__":
    a = 10
    b = 5

    print("Division:", divide(a, b))

