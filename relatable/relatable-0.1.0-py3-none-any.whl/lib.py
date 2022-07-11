import re


ID_PATTERN = re.compile(r"[id_[0-9]+]")


def make_relational_schema(docs):
    tables = []
    remaining_docs = [insert_index(docs, 0)]
    i = 1
    while len(remaining_docs) > 0:
        docs = remaining_docs.pop(0)
        new_table, more_docs = tabulate(docs)
        more_docs = [insert_index(docs, i + j) for j, docs in enumerate(more_docs)]
        i += len(more_docs)
        tables.append(new_table)
        remaining_docs.extend(more_docs)
    return tables


def insert_index(docs, i):
    return [{f"[id_{i}]": j, **d} for j, d in enumerate(docs)]


def tabulate(docs):
    if all(check_no_dicts(d) for d in docs):
        list_fields = get_list_fields(docs)
        more_docs = [extract_list_field(docs, k) for k in list_fields]
        return docs, more_docs
    else:
        for d in docs:
            flatten_one_level(d)
        return tabulate(docs)


def check_no_dicts(d):
    return all(type(v) is not dict for v in d.values())


def get_list_fields(docs):
    return set(k for d in docs for k, v in d.items() if type(v) is list)


def extract_list_field(docs, k):
    updated_docs = []
    for d in docs:
        if k in d.keys():
            v = d.pop(k)
            id_d = {x: y for x, y in d.items() if re.fullmatch(ID_PATTERN, x)}
            for v_ in v:
                updated_docs.append({**id_d, k: v_})
    return updated_docs


def remove_list_fields(docs, list_fields):
    for d in docs:
        for k in list_fields:
            if k in d.keys():
                del d[k]


def flatten_one_level(d):
    for k in list(d.keys()):
        v = d[k]
        if type(v) is dict:
            for k_, v_ in v.items():
                d[f"{k}.{k_}"] = v_
            del d[k]
