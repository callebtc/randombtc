import randombtc as random

if __name__ == "__main__":
    print(f"Seed: {random.entropy()}")
    print(f"Random float: {random.random()}")
    chose_from = ["a", "b", "c", "d", "e", "f", "g", "h"]
    print(f"Random choice from list {chose_from}: {random.choice(chose_from)}")
    print(f"Sample (k=5): {random.sample(k=5)}")
