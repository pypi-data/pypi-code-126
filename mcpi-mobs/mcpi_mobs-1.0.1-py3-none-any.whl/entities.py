"""
Classes for making quick NBT representations of entities.
"""
from amulet_nbt import *


class Entity:
    """Base of all entities"""
    def __init__(
        self,
        id_: TAG_Int,
        pos: TAG_List,
        motion: TAG_List,
        rot: TAG_List,
        fall_distance: TAG_Float,
        fire: TAG_Short,
        air: TAG_Short,
        on_ground: TAG_Byte,
    ):
        """
        Initialize through arguments, all must be TAG_...s, see amulet_nbt documentation:
            https://github.com/Amulet-Team/Amulet-NBT
        
        """
        self.id = id_
        self.pos = pos
        self.motion = motion
        self.rot = rot
        self.fall_distance = fall_distance
        self.fire = fire
        self.air = air
        self.on_ground = on_ground

    @staticmethod
    def from_dict(dict_: dict):
        """
        Initialize through a dict, must have all entity properties, all must be tags too, see __init__ docstring.
        """
        return Entity(
            dict_["id"],
            dict_["Pos"],
            dict_["Motion"],
            dict_["Rotation"],
            dict_["FallDistance"],
            dict_["Fire"],
            dict_["Air"],
            dict_["OnGround"],
        )

    def as_compound(self):
        return TAG_Compound(
            {
                "id": self.id,
                "Pos": self.pos,
                "Motion": self.motion,
                "Rotation": self.rot,
                "FallDistance": self.fall_distance,
                "Fire": self.fire,
                "Air": self.air,
                "OnGround": self.on_ground,
            }
        )


class Mob(Entity):
    def __init__(
        self,
        # Entity fields
        id_: TAG_Int,
        pos: TAG_List,
        motion: TAG_List,
        rot: TAG_List,
        fall_distance: TAG_Float,
        fire: TAG_Short,
        air: TAG_Short,
        on_ground: TAG_Byte,
        # Mob fields
        attack_time: TAG_Short,
        death_time: TAG_Short,
        health: TAG_Short,
        hurt_time: TAG_Short,
        age: TAG_Int,
        sheared: TAG_Byte,
        color: TAG_Byte,
    ):

        super().__init__(id_, pos, motion, rot, fall_distance, fire, air, on_ground)

        self.attack_time = attack_time
        self.death_time = death_time
        self.health = health
        self.hurt_time = hurt_time
        self.age = age

        # Sheep properties
        self.sheared = sheared
        self.color = color

    @staticmethod
    def from_dict(dict_: dict):
        return Mob(
            dict_["id"],
            dict_["Pos"],
            dict_["Motion"],
            dict_["Rotation"],
            dict_["FallDistance"],
            dict_["Fire"],
            dict_["Air"],
            dict_["OnGround"],
            # Mob fields
            dict_["AttackTime"],
            dict_["DeathTime"],
            dict_["Health"],
            dict_["HurtTime"],
            dict_["Age"],
            dict_["Sheared"],
            dict_["Color"],
        )

    def as_compound(self):
        return TAG_Compound(
            {
                "id": self.id,
                "Pos": self.pos,
                "Motion": self.motion,
                "Rotation": self.rot,
                "FallDistance": self.fall_distance,
                "Fire": self.fire,
                "Air": self.air,
                "OnGround": self.on_ground,
                "AttackTime": self.attack_time,
                "Health": self.health,
                "HurtTime": self.hurt_time,
                "Age": self.age,
                "Sheared": self.sheared,
                "Color": self.color,
            }
        )


class Item(Entity):
    def __init__(
        self,
        # Entity fields
        id_: TAG_Int,
        pos: TAG_List,
        motion: TAG_List,
        rot: TAG_List,
        fall_distance: TAG_Float,
        fire: TAG_Short,
        air: TAG_Short,
        on_ground: TAG_Byte,
        # Item fields
        age: TAG_Short,
        health: TAG_Short,
        item: TAG_Compound,
    ):
        super().__init__(id_, pos, motion, rot, fall_distance, fire, air, on_ground)

        self.age = age
        self.health = health
        self.item = item

    @staticmethod
    def from_dict(dict_: dict):
        return Item(
            dict_["id"],
            dict_["Pos"],
            dict_["Motion"],
            dict_["Rotation"],
            dict_["FallDistance"],
            dict_["Fire"],
            dict_["Air"],
            dict_["OnGround"],
            dict_["Age"],
            dict_["Health"],
            dict_["Item"],
        )

    def as_compound(self):
        return TAG_Compound(
            {
                "id": self.id,
                "Pos": self.pos,
                "Motion": self.motion,
                "Rotation": self.rot,
                "FallDistance": self.fall_distance,
                "Fire": self.fire,
                "Air": self.air,
                "OnGround": self.on_ground,
                "Age": self.age,
                "Health": self.health,
                "Item": self.item,
            }
        )


class ItemData:
    """
    Represents item data
    """

    def __init__(self, id_: TAG_Short, damage: TAG_Short, count: TAG_Byte):
        self.id = id_
        self.damage = damage
        self.count = count

    @staticmethod
    def from_dict(dict_: dict):
        return ItemData(dict_["id"], dict_["Damage"], dict_["Count"])

    def as_compound(self):
        return TAG_Compound({"id": self.id, "Damage": self.damage, "Count": self.count})
