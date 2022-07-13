import logging
from functools import cached_property

logger = logging.getLogger(__name__)

from ..errors import BotError, YamlSnippet
from ._base import FlowComponent, FlowResult
from .scenarios import Expression, Scenario
from .slot_filling import SlotFilling


class NodeStack:
    def __init__(self, stack, tree):
        self.stack = stack
        self.tree = tree

    def push(self, node, transition):
        self.remove(node)
        self.stack.append([node.label, transition])

    def pop(self):
        if self.stack:
            label, transition = self.stack.pop()
            return self.tree.catalog[label], transition
        return None, None

    def peak(self):
        if self.stack:
            label, transition = self.stack[-1]
            return self.tree.catalog[label], transition
        return None, None

    def remove(self, node):
        label = node.label
        found = False
        for label, transition in self.stack[:]:
            if label == node.label:
                self.stack.remove([label, transition])
                found = True
        return found

    def clear(self):
        self.stack.clear()


class DialogTree:
    def __init__(self, definition):
        self.tree = Tree(definition)

    def __call__(self, context):
        stack = NodeStack(context.state.setdefault("node_stack", []), self.tree)
        turn = Turn(self.tree, stack, context)
        return turn()


class Turn:
    def __init__(self, tree, stack, context):
        self.tree = tree
        self.stack = stack
        self.context = context

    def __call__(self):
        node, transition = self.stack.peak()
        if node:
            logger.debug(f"peak {node} transition={transition}")
            if transition == "followup":
                return self.focus_followup(node)
            elif transition == "slot_filling":
                return self.trigger(node)
            else:
                raise ValueError(f"Unknown focus transition {transition!r}")
        else:
            return self.root_nodes()

    def root_nodes(self):
        for node in self.tree.root_nodes:
            if node.condition(self.context):
                return self.trigger(node)
        else:
            return FlowResult.DONE

    def focus_followup(self, parent_node):
        for node in parent_node.followup:
            if node.condition(self.context):
                self.stack.remove(parent_node)
                return self.trigger(node)
        else:
            return self.digression(parent_node)

    def command_followup(self, parent_node):
        logger.debug(f"followup {parent_node}")
        for node in parent_node.followup:
            if node.condition(self.context):
                return self.trigger_maybe_digressed(node)
        else:
            logger.warning(f"No followup node matched {parent_node}")
            return FlowResult.LISTEN

    def command_listen(self, node):
        if node.followup:
            self.stack.push(node, "followup")
            return FlowResult.LISTEN
        else:
            return self.return_after_digression()

    def command_jump_to(self, from_node, command):
        logger.debug(f"jump_to {command}")
        jump_to_node = self.tree.catalog.get(command.node)
        if jump_to_node is None:
            raise BotError(f"Unknown jump_to node {command.node!r}")
        if command.transition == "response":
            return self.trigger_maybe_digressed(jump_to_node)
        elif command.transition == "condition":
            return self.jump_to_condition(jump_to_node)
        else:
            raise BotError(f"Unknown jump_to transition {command.transition!r}")

    def jump_to_condition(self, jump_to_node):
        for node in jump_to_node.me_and_right_siblings:
            if node.condition(self.context):
                return self.trigger_maybe_digressed(node)
        else:
            logger.warning(f"No node matched {jump_to_node}")
            return self.return_after_digression()

    def digression(self, digressed_node):
        logger.debug(f"digression from {digressed_node}")
        for node in self.tree.root_nodes:
            if node == digressed_node:
                continue
            if node.condition(self.context, digressing=True):
                return self.trigger_maybe_digressed(node)
        else:
            if digressed_node.followup_allow_return:
                return self.return_after_digression()
            else:
                return FlowResult.LISTEN

    def return_after_digression(self):
        node, transition = self.stack.pop()
        if node:
            logger.debug(f"return_after_digression {node} {transition}")
            if transition == "slot_filling":
                return self.trigger(node, returning=True)
            elif transition == "followup":
                if node.followup_allow_return:
                    return self.trigger(node, returning=True)
                else:
                    return self.return_after_digression()
            else:
                raise ValueError(f"Unknown focus transition {transition!r}")
        else:
            return FlowResult.DONE

    def trigger_maybe_digressed(self, node):
        if self.stack.remove(node):
            return self.trigger(node, returning=True)
        else:
            return self.trigger(node)

    def trigger(self, node, returning=False):
        logger.debug(f"trigger {node}, returning={returning}")
        if node.slot_filling:
            result = node.slot_filling(self.context, returning)
            if result == FlowResult.DONE:
                self.stack.remove(node)
                return self.response(node, returning)
            elif result == FlowResult.LISTEN:
                self.stack.push(node, "slot_filling")
                return FlowResult.LISTEN
            elif result == FlowResult.DIGRESS:
                return self.digression(node)
            else:
                raise ValueError(f"Unknown flow result {result!r}")
        else:
            return self.response(node, returning)

    def response(self, node, returning):
        for command in node.response(self.context, returning=returning):
            if command.name == "jump_to":
                return self.command_jump_to(node, command)
            if command.name == "listen":
                return self.command_listen(node)
            if command.name == "end":
                self.stack.clear()
                self.context.flow_vars.clear()
                return FlowResult.DONE
            if command.name == "followup":
                return self.command_followup(node)
            self.context.commands.append(command)
        else:
            return self.command_listen(node)


class Tree:
    def __init__(self, definition):
        self.catalog = {}
        self.root_nodes = [self.create_node(d) for d in definition]

    def create_node(self, definition, parent=None):
        if not definition.label and (definition.followup or definition.slot_filling):
            raise BotError("Stateful node must have a label", YamlSnippet.format(definition))
        node = Node(definition, self, parent)
        if definition.label:
            if definition.label in self.catalog:
                raise BotError(
                    f"Duplicate node label {definition.label!r}",
                    YamlSnippet.format(definition.label),
                )
            self.catalog[definition.label] = node
        return node


class Node:
    def __init__(self, definition, tree, parent):
        self.label = definition.label
        self.definition = definition
        self.parent = parent
        self.tree = tree
        self.condition = Expression(definition.condition)
        self.response = Scenario(definition.response)
        self.followup = [tree.create_node(d, self) for d in definition.followup]
        self.slot_filling = None
        if definition.slot_filling:
            self.slot_filling = FlowComponent(
                definition.label,
                SlotFilling(
                    definition.slot_filling,
                    definition.slot_handlers,
                ),
            )

    @cached_property
    def me_and_right_siblings(self):
        siblings = self.parent.followup if self.parent else self.tree.root_nodes
        index = siblings.index(self)
        return siblings[index:]

    @cached_property
    def followup_allow_return(self):
        policy = self.definition.settings.after_digression_followup
        if policy == "allow_return":
            return True
        elif policy == "never_return":
            return False
        else:
            raise ValueError(f"Unknown returning policy {policy!r}")

    @cached_property
    def title(self):
        if self.label:
            return f"{self.label!r}"
        elif self.parent:
            return f'{self.parent.title} -> "{self.definition.condition!r}"'
        else:
            return f'"{self.definition.condition!r}"'

    def __str__(self):
        return self.title
