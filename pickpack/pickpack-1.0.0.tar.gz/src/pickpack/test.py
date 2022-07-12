#! /usr/bin/env python3

from anytree import Node, RenderTree, find
from pickpack import pickpack

title = 'Please choose an option: '

def count_leaves(node:Node, acc: int = 0):
    if node.children:
        for child in node.children:
            acc += count_leaves(child)
    else:
        acc += 1
    return acc

def count_nodes(node:Node, acc: int = 0):
    if node.children:
        for child in node.children:
            acc += count_nodes(child)
    return acc + 1

k = Node("K")
j = Node("J", children= [k])
i = Node("I", children= [j])
h = Node("H")
g = Node("G")
f = Node("F")
e = Node("E")
d = Node("D", children= [g, e])
c = Node("C", children= [f])
b = Node("B", children= [d, c])
a = Node("A", children=[b])
root = Node("", children=[a, h, i])




# print(count_leaves(root))
# print(count_nodes(root))

# options = Tree([a,h,i])
options = RenderTree(root)

# def match_index(index:int, n:Node):
#     return n.index == index
# for index, option in enumerate(options):
#     option.node.index = index
#     # print(str(index) + " " + option.node.name)

# options = [{'label': 'parent', 'children': [{'label': 'option2', 'id':"werwr"}, {'label': 'option4', 'id':"hgjhf"}], 'id':"asjkadhkas"}, {'label': 'option3', 'id':"gfrhgr"}]

def get_nodes(option):
    children = option.get('children')
    if children is not None:
        children_list: list[Node] = []
        for child in children:
            children_list.append(get_nodes(child))
        return Node(option.get('label'), children=children_list, id=option.get('id'))
    else:
        return Node(option.get('label'), children=None, id=option.get('id'))
    # print("we're in!")
    # children = option.get('children')
    # print(option)
    
    # if children is None:
    #     return option.get('label')
    # else:
    #     for item in children:
    #         return get_label(item)


# def get_leaves_only(node:Node, leaves: list[Node] = None) -> list[Node]:
#     if leaves is None:
#         leaves = []
    
#     if node.children:
#         for child in node.children:
#             leaves = get_leaves_only(child, leaves)
#     else:
#         if node not in leaves:
#             leaves.append(node)
#     return leaves

# print(get_leaves_only(root))
# for pre, fill, node in RenderTree(root):
#      print("%s%s" % (pre, node.name))

# nodes = []
# for option in options:
#     print(option)
#     nodes.append(get_nodes(option))
# print(nodes)
# for n in nodes:
#     print(n.children)

selected = pickpack(options, title, indicator='*', multiselect=True, root_name="Select/\n all", min_selection_count=1, output_format="nodeonly", indicator_parentheses=True)
print(selected)

# print(options.node)
# print(find(root, filter_= lambda n : match_index(3, n)))
