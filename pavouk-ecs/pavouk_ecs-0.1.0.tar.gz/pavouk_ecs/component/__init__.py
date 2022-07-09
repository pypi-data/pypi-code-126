from pavouk_ecs import log
from pavouk_ecs.id_generator import IDGenerator
from pavouk_ecs.setup import MAX_ENTITIES


LOG = log.getLogger(__name__)


class Components:
    def __init__(self, Type):
        self.Type = Type
        self.size = 0
        self.components = [None for i in range(MAX_ENTITIES)]
        self.entity_id_to_index = {}
        self.index_to_entity_id = {}

    def assign(self, e):
        if e is None:
            LOG.error("Can't assign entity. e={}".format(e))
            return
        if self.size >= len(self.components):
            LOG.error(
                "Can't assign more entities to this component."
                " Not enough space"
            )
            return

        i = self.size
        self.entity_id_to_index[e.id] = i
        self.index_to_entity_id[i] = e.id
        self.components[i] = self.Type()
        self.size += 1
        e.mask = e.mask | IDGenerator.getID(self.Type)
        LOG.debug("Entity {} assigned to {}".format(e, self.components[i]))
        return self.components[i]

    def remove(self, e):
        if e is None:
            LOG.error("Can't remove entity. e={}".format(e))
            return
        removed_index = self.entity_id_to_index[e.id]
        last_index = self.size - 1
        self.components[removed_index] = self.components[last_index]

        last_index_id = self.index_to_entity_id[last_index]
        self.entity_id_to_index[last_index_id] = removed_index
        self.index_to_entity_id[removed_index] = last_index_id

        c = self.components[last_index]
        LOG.debug("Entity {} removed from {}".format(e, c))
        self.components[last_index] = None

        self.size -= 1
        e.mask = IDGenerator.getID(self.Type) ^ e.mask

    def get(self, e):
        if e is None:
            LOG.error("Can't get entity. e={}".format(e))
            return
        i = self.entity_id_to_index.get(e.id)
        if i is not None:
            return self.components[i]

    def get_size(self):
        return self.size

    def __repr__(self):
        return "Type: {}\nComponents: {}\n".format(self.Type, self.components)
