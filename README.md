# randombtc 🎲

> a random number generator that everybody can agree on

### Features

- One random number roughly every 10 minutes.
- Same random number for everyone in the universe.
- Ranges between 0 and 1.

### Install

```bash
git clone https://github.com/callebtc/randombtc
pip install randombtc/
```

### Use

```python
import randombtc as random

# Get the entropy
print(f"Seed: {random.entropy()}")

# Get a random float between 0 and 1
print(f"Random float: {random.random()}")

# Chose a random entry from a list
chose_from = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(f"Random choice from list {chose_from}: {random.choice(chose_from)}")

# Sample many more numbers without having to wait for the next block
print(f"Sample (k=5): {random.sample(k=5)}")

```

### What?!

`randombtc` is a Python library for generating random numbers using the common syntax. The special thing about `randombtc` is that it takes the Bitcoin blockchain as a source for its entropy. What does that mean?

Every random number generator needs some source of randomness. In the most primitive cases, this is often just the current time of your computer which is then put into a hash function which is then used to generate a random number. A better approach would be to use "real" randomness, such as sampling random data from your computer's peripherals and environment such noise from your microphone, keystrokes, cpu temperature, etc. These are all efforts to improve the randomness of a random number generator.

An interesting application of random number generators is in online multiplayer games or in online gambling where multiple parties need to agree on a random number generated. An example is an online roulette game, where the server (the house) and the client (the player) need to agree on what the outcome of the next round was without one having the advantage of knowing in advance of the other, and thus being able to abuse the game's mechanics. This is also known as "provable fairness". These protocols typically require some sort of exchange beforehand: both parties generate random numbers and use hashing functions. This works well as long as you can be sure that both, server and client, have good random number generators.

`randombtc` is an attempt at solving the above problem without requiring the exchange of data between parties. It does this by using the immutable bitcoin blockchain which everyone on the internet can agree on (secured by proof of work). It basically uses the blockchain as a source of randomness. That means that if you want to make a dice game between two users, they can both look at the blockchain to determine what the outcome of the dice roll is for this round.

However, one drawback of this method is that we can only sample new entropy whenever a new block is created, which is roughly every 10 minutes. The library offers a simple workaround to sample many random numbers based on a single block, however, these will all be pre-computable from the first random number, which is based on the blockchain's state.

Does it make any sense to have such a library? I don't know. Is it just for fun and giggles? Maybe.

### Warning

Do not use this to settle a high-stakes bet (on the order of the block reward) against a miner. [They can manipulate](https://ethereum.stackexchange.com/questions/94945/can-we-use-block-hash-as-verifiable-randomness-for-the-off-chain-lottery) the statistics of the block hash to a certain degree.

### Blockchain data

Currently, the library uses the block hash or the Merkle root of the current block as a source of entropy. The data is fetched from [mempool.space](https://mempool.space).

One interesting fact about using the block hash as a source of entropy is that its entropy decreases as the hash rate of the bitcoin mining network increases since the increased difficulty leads to an increasing number of zeroes in the most significant digits of the block hash.

However, a random number generator that gets more insecure when Bitcoin gets more secure is stupid! That's why you can also use the Merkle root (by default) as a source of entropty.
