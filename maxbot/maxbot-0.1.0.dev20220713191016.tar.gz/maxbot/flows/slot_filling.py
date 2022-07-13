import logging
from dataclasses import dataclass, field
from typing import List

logger = logging.getLogger(__name__)

from ..nlu import EntitiesProxy, RecognizedEntity
from ._base import FlowContext, FlowResult
from .scenarios import Expression, Scenario


class SlotFilling:
    def __init__(self, slots, handlers):
        self.slots = [Slot(d) for d in slots]
        self.handlers = [Handler(d) for d in handlers] if handlers else []

    def __call__(self, context, returning=False):
        turn = Turn(self.slots, self.handlers, context, returning)
        return turn()


class Slot:
    def __init__(self, definition):
        self.name = definition.name
        self.check_for = Expression(definition.check_for)
        self.condition = Expression(definition.condition) if definition.condition else None
        self.value = Expression(definition.value) if definition.value else None
        self.prompt = Scenario(definition.prompt) if definition.prompt else None
        self.found = Scenario(definition.found) if definition.found else None
        self.not_found = Scenario(definition.not_found) if definition.not_found else None


class Handler:
    def __init__(self, definition):
        self.condition = Expression(definition.condition)
        self.response = Scenario(definition.response)


@dataclass
class Turn:
    slots: List[Slot]
    handlers: List[Handler]
    context: FlowContext
    returning: bool

    found_slots: list = field(default_factory=list)
    skip_prompt: list = field(default_factory=list)
    want_response: bool = False

    @property
    def enabled_slots(self):
        for slot in self.slots:
            if slot.condition is None or slot.condition(self.context):
                yield slot

    def elicit(self, slot):
        value = slot.check_for(
            self.context, slot_in_focus=(self.context.state.get("slot_in_focus") == slot.name)
        )
        if not value:
            return
        if slot.value:
            value = slot.value(self.context)
        if isinstance(value, (EntitiesProxy, RecognizedEntity)):
            value = value.value
        logger.debug(f"elicit slot {slot.name!r} value {value!r}")
        previous_value = self.context.slots.get(slot.name)
        self.context.slots[slot.name] = value
        self.found_slots.append((slot, {"previous_value": previous_value, "current_value": value}))

    def clear_slot(self, slot):
        self.context.slots.pop(slot.name, None)

    def listen_again(self, slot):
        self.skip_prompt.append(slot)

    def found(self, slot, params):
        for command in slot.found(self.context, **params):
            if command.name == "response":
                self.want_response = True
                break
            if command.name == "prompt_again":
                self.clear_slot(slot)
                break
            if command.name == "listen_again":
                self.clear_slot(slot)
                self.listen_again(slot)
                break
            if command.name == "move_on":
                break
            self.context.commands.append(command)

    def not_found(self, slot):
        for command in slot.not_found(self.context):
            if command.name == "response":
                self.want_response = True
                break
            if command.name == "prompt_again":
                break
            if command.name == "listen_again":
                self.listen_again(slot)
                break
            self.context.commands.append(command)
        else:
            self.listen_again(slot)

    def prompt(self, slot):
        for command in slot.prompt(self.context):
            if command.name == "response":
                self.want_response = True
                break
            if command.name == "listen_again":
                self.listen_again(slot)
                break
            self.context.commands.append(command)
        else:
            self.listen_again(slot)

    def handler(self, handler):
        for command in handler.response(self.context):
            if command.name == "response":
                self.want_response = True
                break
            if command.name == "move_on":
                break
            self.context.commands.append(command)

    def __call__(self):
        # elicit
        for slot in self.enabled_slots:
            self.elicit(slot)
        # found
        for slot, params in self.found_slots:
            if slot.found:
                self.found(slot, params)
        if self.context.state.get("slot_in_focus") and not self.found_slots:
            # slot handlers
            for handler in self.handlers:
                if handler.condition(self.context):
                    self.handler(handler)
                    break
            else:
                if not self.returning:
                    return FlowResult.DIGRESS
                # not found
                catalog = {s.name: s for s in self.enabled_slots}
                slot = catalog[self.context.state.get("slot_in_focus")]
                if slot and slot.not_found:
                    self.not_found(slot)
        if not self.want_response:
            # prompt
            for slot in self.enabled_slots:
                if slot.prompt and self.context.slots.get(slot.name) is None:
                    self.context.state["slot_in_focus"] = slot.name
                    if slot not in self.skip_prompt:
                        self.prompt(slot)
                    break
            else:
                self.context.state["slot_in_focus"] = None
        # result
        if self.want_response:
            self.context.state["slot_in_focus"] = None
        if self.context.state.get("slot_in_focus") is None:
            return FlowResult.DONE
        else:
            return FlowResult.LISTEN
