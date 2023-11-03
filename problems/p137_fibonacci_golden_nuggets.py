def main():
    current = 1
    previous = 0
    for i in range(30):
        old = previous
        previous = current
        current = previous + old
    return current * previous
