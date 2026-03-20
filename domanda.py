from dataclasses import dataclass
import random

@dataclass
class Domanda(object):
    testo: str
    diff: int
    corretta: bool
    opzioni: str

    def opzioni_random(self):
        random.shuffle(self.opzioni)
        return self.opzioni