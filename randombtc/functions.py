from .base import HashSource
from .source_mempoolspace import MempoolSpace
from .__init__ import generator


def random():
    return generator.random()


def uniform(a, b) -> float:
    return generator.uniform(a, b)


def entropy():
    return generator.entropy()


def choice(seq):
    return generator.choice(seq)


def choices(population, k=1):
    return generator.choices(population, k)


def sample_once():
    return generator.sample_once()


def sample(k):
    return generator.sample(k)


def get_timestamp():
    return generator.get_timestamp()
