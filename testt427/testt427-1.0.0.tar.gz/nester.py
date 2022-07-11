"""_summary_ 将list中的非list内容逐个输出
edit by t427
20220708
"""
def print_lol(the_list):
    for list_item in the_list:
        if isinstance(list):
            print_lol(list_item)
        else:
            print(list_item)
            