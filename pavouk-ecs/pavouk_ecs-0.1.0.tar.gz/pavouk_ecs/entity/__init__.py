from dataclasses import dataclass


@dataclass
class Entity:
    id: int
    mask: int = 0
    dead: bool = False

    def add_mask(self, mask):
        self.mask = self.mask | mask

    def remove_mask(self, mask):
        self.mask = mask ^ self.mask

    def has_mask(self, mask):
        return mask & self.mask == mask

    def set_dead(self):
        self.dead = True

    def is_dead(self):
        return self.dead
