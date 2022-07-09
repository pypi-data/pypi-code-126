from pavouk_ecs import log
from pavouk_ecs.entity import Entity
from pavouk_ecs.setup import MAX_ENTITIES


LOG = log.getLogger(__name__)


def available_ids():
    return [i for i in range(MAX_ENTITIES)]


class EntityManager:
    def __init__(self):
        self.entities = []
        self.availables_ids = []
        self._clear()

    def create(self):
        if len(self.availables_ids) <= 0:
            LOG.error("Entity creation error. Not enough available ids")
            return

        e = Entity(self.availables_ids.pop(0))
        self.entities.append(e)
        LOG.debug("Entity created: {}".format(e))
        return e

    def remove(self, e):
        if e is None:
            return
        LOG.debug("Removing entity: {}".format(e))
        self.availables_ids.append(e.id)
        self.entities.remove(e)
        LOG.debug("Entity removed: {}".format(e))

    def remove_all(self):
        LOG.debug("Removing all entities.")
        self._clear()
        LOG.debug("All entities removed.")

    def get_entities_with_mask(self, mask):
        return [e for e in self.entities if e.has_mask(mask)]

    def _clear(self):
        self.entities = []
        self.availables_ids = available_ids()

    def __repr__(self):
        return "Entities: {}\nIDS: {}".format(
            self.entities, self.availables_ids)
