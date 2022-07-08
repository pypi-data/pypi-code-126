import orm

def up_while_or(node: orm.FTNode) -> orm.FTNode|None:
    """Поднимаемся наверх по дереву пока встречаются ИЛИ гейты или начало дерева отказов"""
    gate = node.Event
    if gate.Symbol == orm.SymbolEnum.OR.value:
        if node.Transfer == orm.TransferEnum.Yes.value or node.FatherNode is None:
            return node
        else:
            result = up_while_or(node.FatherNode)
            if result is None:
                return node
            return result
    return None

def et_propagate(event_tree: orm.EventTree, back_propagate=False, recursive=False)->List[orm.EventTree]:
    
    pass