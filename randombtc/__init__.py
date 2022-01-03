from .base import HashSource
from .source_mempoolspace import MempoolSpace
from .functions import *

BLOCKCHAIN_SOURCE = MempoolSpace
ENTROPY_SOUCE = "merkle_root"

generator = BLOCKCHAIN_SOURCE(ENTROPY_SOUCE)
