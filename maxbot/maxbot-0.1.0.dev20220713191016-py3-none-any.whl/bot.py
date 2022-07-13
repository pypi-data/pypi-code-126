import logging

logger = logging.getLogger(__name__)

from .flows import DialogTree, FlowComponent, FlowContext, FlowResult
from .nlu import Nlu
from .schemas import Definitions
from .storage import SQLAlchemyStore


class MaxBot:
    def __init__(self, definitions: Definitions):
        self.definitions = definitions
        self.store = SQLAlchemyStore(definitions.services.sqlalchemy)
        self.nlu = Nlu.from_definitions(definitions)
        self.flow = FlowComponent("ROOT", DialogTree(definitions.dialog))

    def __call__(self, event):
        logger.debug(f"event {event}")
        intents, entities = self.nlu(event.message)
        with self.store(event) as variables:
            context = FlowContext(
                event, intents, entities, variables.user, variables.slots, variables.flow, list()
            )
            result = self.flow(context)
            if result == FlowResult.DONE:
                variables.slots.clear()
            elif result == FlowResult.LISTEN:
                pass
            else:
                raise RuntimeError(f"Unexpected result {result}")
            return context.commands
