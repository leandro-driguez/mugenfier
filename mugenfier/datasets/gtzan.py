import tarfile
from copy import deepcopy
from mugenfier.utils import is_valid_split
import os

SETS = ['test', 'train', 'val']

GENRES = ['blues', 'classical', 'country', 'disco', \
    'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']


class GTZAN:

    def __init__(self, path: str):
        self.path = path
        self.split = dict()
        self.descompress()

    def descompress(self):
        if self.path.endswith('.tar.gz'):
            tar = tarfile.open(self.path, 'r:gz')
            tar.extractall(
                ''.join(self.path.split('/')[:-1])   
            )
            tar.close()

    def set_split(self, split: dict):
        
        if is_valid_split(split):
            self.split = deepcopy(split)

    def __getitem__(self, key: tuple):
        try:
            i, j = key
        except:
            raise Exception("Incorrect key for index")

        # index by dataset['test', 'jazz']
        if (i in SETS and j in GENRES) or \
            (j in SETS and i in GENRES):
            
            if j in SETS and i in GENRES:
                i, j = j, i
            

        # index by dataset['jazz', 93]
        if (i in GENRES and j >= 0 and j < 100) or \
            (j in GENRES and i >= 0 and i < 100):
            ...
