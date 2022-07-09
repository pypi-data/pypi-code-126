class IDGenerator:
    next_id = 1
    type_to_id = {}

    @staticmethod
    def getID(Type):
        if Type not in IDGenerator.type_to_id:
            IDGenerator.type_to_id[Type] = IDGenerator.next_id
            IDGenerator.next_id <<= 1
        return IDGenerator.type_to_id[Type]
