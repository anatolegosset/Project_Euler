from collections import deque


def sequence():
    modulus = 10**6
    values = deque()
    for k in range(1, 56):
        new_val = (100003 - 200003 * k + 300007 * k * k * k) % modulus
        yield new_val
        values.append(new_val)
    while True:
        new_val = (values[-24] + values[-55]) % modulus
        yield new_val
        values.append(new_val)
        values.popleft()


def main():
    seq = sequence()
    mapping = [{i} for i in range(10**6)]
    count = 0
    for caller in seq:
        called = next(seq)
        if called == caller:
            continue
        if called not in mapping[caller]:
            if len(mapping[caller]) < len(mapping[called]):
                called, caller = caller, called
            mapping[caller].update(mapping[called])
            for friend in mapping[called]:
                mapping[friend] = mapping[caller]
            print(len(mapping[called]))
        count += 1
        if len(mapping[524287]) >= 990000:
            print(count)
            break


if __name__ == "__main__":
    main()
