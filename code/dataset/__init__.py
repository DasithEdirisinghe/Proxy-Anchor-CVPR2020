from .cars import Cars
from .cub import CUBirds
from .SOP import SOP
from .import utils
from .base import BaseDataset
from .rabot import Rabot


_type = {
    'cars': Cars,
    'cub': CUBirds,
    'SOP': SOP,
    'rabot': Rabot
}

def load(name, root, mode, transform = None):
    return _type[name](root = root, mode = mode, transform = transform)
    
