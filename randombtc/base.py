import hashlib
from typing import *


class HashSource:
    n_sampled: int = 0
    entropy_cache: str = ""

    def __init__(self, source_name):
        self.source_name = source_name

    def __str__(self):
        return f"{self.source_name}: {self.random()}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.random() == other.random()

    def __hash__(self):
        return hash(self.__str__())

    def _int_from_hex_string(self, hex: str) -> int:
        hex = hex.strip("0x")
        hex = "0x" + hex
        return int(hex, 16)

    def _sha256_of_hash(self, hash: str) -> str:
        return hashlib.sha256(hash.encode("utf-8")).hexdigest()

    def _sha256_to_noramlized_float(self, hash: str) -> float:
        fhash = float(self._int_from_hex_string(self._sha256_of_hash(hash)))
        return fhash / (2 ** 256)

    def _entropy_to_random(self, entropy: str) -> float:
        return self._sha256_to_noramlized_float(self._sha256_of_hash(entropy))

    def entropy(self) -> str:
        raise NotImplementedError("entropy() not implemented")

    def random(self, seed: int = 0) -> float:
        entropy = self.entropy()
        self.entropy_cache = entropy

        if seed:
            entropy += str(seed)

        return self._entropy_to_random(entropy)

    def _random_cached(self, seed: int = 0) -> float:
        self.entropy_cache = self.entropy_cache or self.entropy()
        entropy = self.entropy_cache
        if seed:
            entropy += str(seed)
        return self._entropy_to_random(entropy)

    def _sample_once(self) -> float:
        # uses the n_sampled counter as a seed
        self.n_sampled += 1
        return self._random_cached(self.n_sampled)

    def sample(self, k=1) -> List[float]:
        return [self._sample_once() for _ in range(k)]

    def uniform(self, a, b) -> float:
        return a + self.random() * (b - a)

    def randrange(self, start, stop=None, step=1) -> int:
        if stop is None:
            stop = start
            start = 0
        length = stop - start
        assert length > 0
        assert step > 0
        return start + int(self.uniform(0, length) / step)

    def choice(self, seq) -> object:
        return seq[self.randrange(len(seq))]

    def choices(self, population, k=1) -> list:
        return [self.choice(population) for _ in range(k)]
