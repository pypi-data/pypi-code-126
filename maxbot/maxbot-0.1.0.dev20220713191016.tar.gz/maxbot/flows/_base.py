from dataclasses import dataclass, replace
from enum import Enum
from typing import Callable, Optional

from ..channels import ChannelEvent
from ..nlu import EntitiesContext, IntentsContext


class FlowResult(Enum):

    DIGRESS = "digress"
    LISTEN = "listen"
    DONE = "done"


@dataclass(frozen=True)
class FlowContext:

    event: ChannelEvent
    intents: IntentsContext
    entities: EntitiesContext
    user: dict
    slots: dict
    flow_vars: dict
    commands: list
    state: Optional[object] = None


@dataclass(frozen=True)
class FlowComponent:

    name: str
    flow: Callable[[FlowContext], FlowResult]

    def __call__(self, context, digression_result=None):
        state = context.flow_vars.setdefault(self.name, {})
        context = replace(context, state=state)
        if digression_result is None:
            result = self.flow(context)
        else:
            result = self.flow(context, digression_result)
        if result == FlowResult.DONE:
            context.flow_vars[self.name] = None
        return result
