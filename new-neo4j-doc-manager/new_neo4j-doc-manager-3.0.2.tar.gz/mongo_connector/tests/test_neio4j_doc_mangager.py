# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 下午3:55
# @Author  : kyq
# @Software: PyCharm

from py2neo import Graph,NodeMatcher

def nodeExist(name):
    matcher = NodeMatcher(graph)
    m = matcher.match().where(actorName=name).first()
    if m is None:
       return False
    else:
       return m

def creat_relationship(id,doubanid,a):
    doubanId = "{" + "doubanId:'{}'".format(id) + "}"
    director_doubanId = "{" + "doubanId:'{}'".format(doubanid) + "}"
    statement = 'MATCH (director{a}), (actor{b}) CREATE (director)-[r:Acted_in {c}]->(actor)'.format(a=director_doubanId, b=doubanId,c=a)
    return statement

graph = Graph('http://192.168.3.215:7474/db/data')
tx = graph.begin()
creat_director_list = [
    {'_id': '23423464322341', 'doubanId': '1354570', 'post': '导演', 'actorName': '郭虎', 'actorPic': 'https://img1.doubanio.com/view/celebrity/raw/public/p1519793013.48.jpg', 'roleName': '导演 Director', '_ts': 1},
    {'_id': '23423464322341', 'doubanId': '1374579', 'post': '导演', 'actorName': '白鹿', 'actorPic': 'https://img9.doubanio.com/view/celebrity/raw/public/p1495863041.05.jpg', 'roleName': '导演 Director', '_ts': 1},
    # {'_id': '1234564', 'doubanId': '1355646', 'post': '导演', 'actorName': '于中中','actorPic': 'https://img1.doubanio.com/view/celebrity/raw/public/p1519793015.48.jpg','roleName': '导演 Director', '_ts': 1},
    # {'_id': '1234564', 'doubanId': '1355648', 'post': '导演', 'actorName': '吴建新','actorPic': 'https://img1.doubanio.com/view/celebrity/raw/public/p1519793018.48.jpg','roleName': '导演 Director', '_ts': 1},
]
creat_actor_list = [
    {'_id': '23423464322341', 'doubanId': '1360678', 'post': '演员', 'actorName': '任嘉伦', 'actorPic': 'https://img9.doubanio.com/view/celebrity/raw/public/p1604728756.56.jpg', 'roleName': '周生辰', '_ts': 1},
    # {'_id': '1234564', 'doubanId': '1374579', 'post': '演员', 'actorName': '白鹿', 'actorPic': 'https://img9.doubanio.com/view/celebrity/raw/public/p1495863041.05.jpg', 'roleName': '路招摇', '_ts': 1},
    # {'_id': '1234564', 'doubanId': '1401137', 'post': '演员', 'actorName': '李宜儒','actorPic': 'https://img9.doubanio.com/view/celebrity/raw/public/p1537497086.55.jpg', 'roleName': '宏晓誉', '_ts': 1},

]

creat_list = [
  {"CREATE (:Actor {parameters})":{'_id': '23423464322341', 'doubanId': '1360678', 'post': '演员', 'actorName': '任嘉伦', 'actorPic': 'https://img9.doubanio.com/view/celebrity/raw/public/p1604728756.56.jpg', 'roleName': '周生辰', '_ts': 1}},
  {"CREATE (:Actor {parameters})":{'_id': '23423464322341', 'doubanId': '1354570', 'post': '导演', 'actorName': '郭虎', 'actorPic': 'https://img1.doubanio.com/view/celebrity/raw/public/p1519793013.48.jpg', 'roleName': '导演 Director', '_ts': 1}},
  {"CREATE (:Actor {parameters})":{'_id': '23423464322341', 'doubanId': '1374579', 'post': '导演', 'actorName': '白鹿', 'actorPic': 'https://img9.doubanio.com/view/celebrity/raw/public/p1495863041.05.jpg', 'roleName': '导演 Director', '_ts': 1}},
  # {"CREATE (:Actor {parameters})":{'_id': '1234564', 'doubanId': '1374579', 'post': '演员', 'actorName': '白鹿', 'actorPic': 'https://img9.doubanio.com/view/celebrity/raw/public/p1495863041.05.jpg', 'roleName': '路招摇', '_ts': 1}},
  # {"CREATE (:Actor {parameters})":{'_id': '1234564', 'doubanId': '1355646', 'post': '导演','actorName': '于中中','actorPic': 'https://img1.doubanio.com/view/celebrity/raw/public/p1519793015.48.jpg','roleName': '导演 Director', '_ts': 1}},
  # {"CREATE (:Actor {parameters})":{'_id': '1234564', 'doubanId': '1355648', 'post': '导演', 'actorName': '吴建新','actorPic': 'https://img1.doubanio.com/view/celebrity/raw/public/p1519793018.48.jpg','roleName': '导演 Director', '_ts': 1}},
  # {"CREATE (:Actor {parameters})":{'_id': '1234564', 'doubanId': '1401137', 'post': '演员', 'actorName': '李宜儒','actorPic': 'https://img9.doubanio.com/view/celebrity/raw/public/p1537497086.55.jpg', 'roleName': '宏晓誉', '_ts': 1}},

]
actor_list = []
director_list = []
for creat in creat_list:
    for statement in creat.keys():
        name = creat[statement]['actorName']
        role_name = creat[statement]['roleName']
        ret = nodeExist(name)
        if ret==False:
            tx.run(statement, {"parameters": creat[statement]})
        else:
            m = ret
            if '导演' in role_name:
                director_list.append(m)
            else:
                actor_list.append(m)

if director_list!=[]:
    for director in director_list:
        for creat_actor in creat_actor_list:
            id = creat_actor['doubanId']
            id_ = m['doubanId']
            type = "{" + "type:'{}'".format(0) + "}"
            statement = creat_relationship(id,id_,type)
            tx.run(statement)

    for director in creat_director_list:
        for actor in creat_actor_list:
            id = director['doubanId']
            id_ = actor['doubanId']
            type = "{" + "type:'{}'".format(1) + "}"
            tx.run(creat_relationship(id, id_,type))

if actor_list != []:
    for actor in actor_list:
        for director in creat_director_list:
            id = director['doubanId']
            id_ = m['doubanId']
            type = "{" + "type:'{}'".format(0) + "}"
            tx.run(creat_relationship(id, id_,type))

    for director in creat_director_list:
        for actor in creat_actor_list:
            if m['doubanId'] != actor['doubanId']:
                id = director['doubanId']
                id_ = actor['doubanId']
                type = "{" + "type:'{}'".format(1) + "}"
                tx.run(creat_relationship(id, id_,type))

if actor_list== [] and director_list==[]:
    for director in creat_director_list:
        for actor in creat_actor_list:
            id = director['doubanId']
            id_ = actor['doubanId']
            type = "{" + "type:'{}',count=1".format(1) + "}"
            tx.run(creat_relationship(id, id_,type))
tx.commit()