

def main():
    with open("./Data/0079_keylog.txt") as f:
        trials = [int(trial) for trial in f.read().splitlines()]

    trials = sorted(list(set(trials)))

    print(trials)
