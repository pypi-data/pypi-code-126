import KratosMultiphysics

def Factory(settings, Model):
    if not isinstance(settings, Parameters):
        raise Exception("expected input shall be a Parameters object, encapsulating a json string")
    return CheckAndPrepareSelfweightModelProcess(Model, settings["Parameters"])

## All the processes python should be derived from "Process"
class CheckAndPrepareSelfweightModelProcess(KratosMultiphysics.Process):
    """Prepare the computing model part.

    The computing model part is created if it does not exist. Nodes and elements
    from the domain sub model parts are added to the computing model part.
    Conditions are added from the processes sub model parts.
    """
    def __init__(self, main_model_part, Parameters ):
        KratosMultiphysics.Process.__init__(self)
        self.main_model_part = main_model_part

        self.mechanical_model_part_name  = Parameters["mechanical_model_part_name"].GetString()
        self.mechanical_domain_sub_model_part_list = Parameters["mechanical_domain_sub_model_part_list"]
        self.mechanical_loads_sub_model_part_list = Parameters["mechanical_loads_sub_model_part_list"]
        self.body_domain_sub_model_part_list = Parameters["body_domain_sub_model_part_list"]
        self.body_domain_sub_sub_model_part_list = Parameters["body_domain_sub_sub_model_part_list"]
        self.loads_sub_model_part_list = Parameters["loads_sub_model_part_list"]
        self.loads_sub_sub_model_part_list = Parameters["loads_sub_sub_model_part_list"]

    def Execute(self):

        ## Construct the mechanical model part:
        mechanical_parts = []
        for i in range(self.mechanical_domain_sub_model_part_list.size()):
            mechanical_parts.append(self.main_model_part.GetSubModelPart(self.mechanical_domain_sub_model_part_list[i].GetString()))
        self.main_model_part.CreateSubModelPart(self.mechanical_model_part_name)
        mechanical_model_part = self.main_model_part.GetSubModelPart(self.mechanical_model_part_name)
        mechanical_model_part.ProcessInfo = self.main_model_part.ProcessInfo
        mechanical_model_part.Properties = self.main_model_part.Properties
        mechanical_model_part.Set(KratosMultiphysics.ACTIVE)
        print("Adding Nodes to Mechanical Model Part")
        list_of_ids = set()
        for part in mechanical_parts:
            for node in part.Nodes:
                list_of_ids.add(node.Id)
        mechanical_model_part.AddNodes(list(list_of_ids))
        print("Adding Elements to Mechanical Model Part")
        list_of_ids = set()
        for part in mechanical_parts:
            for elem in part.Elements:
                list_of_ids.add(elem.Id)
        mechanical_model_part.AddElements(list(list_of_ids))
        # Mechanical Conditions
        print("Adding Conditions to Mechanical Model Part")
        mechanical_conditions = []
        for i in range(self.mechanical_loads_sub_model_part_list.size()):
            mechanical_conditions.append(self.main_model_part.GetSubModelPart(self.mechanical_loads_sub_model_part_list[i].GetString()))
        list_of_ids = set()
        for part in mechanical_conditions:
            for cond in part.Conditions:
                list_of_ids.add(cond.Id)
        mechanical_model_part.AddConditions(list(list_of_ids))
        print("Adding Mechanical Sub Sub Model Parts")
        # Sub sub model parts
        # Body - Joints
        for i in range(self.body_domain_sub_model_part_list.size()):
            body_sub_model_part = self.main_model_part.GetSubModelPart(self.body_domain_sub_model_part_list[i].GetString())
            mechanical_model_part.CreateSubModelPart(self.body_domain_sub_sub_model_part_list[i].GetString())
            body_sub_sub_model_part = mechanical_model_part.GetSubModelPart(self.body_domain_sub_sub_model_part_list[i].GetString())
            list_of_ids = set()
            for node in body_sub_model_part.Nodes:
                list_of_ids.add(node.Id)
            body_sub_sub_model_part.AddNodes(list(list_of_ids))
            list_of_ids = set()
            for elem in body_sub_model_part.Elements:
                list_of_ids.add(elem.Id)
            body_sub_sub_model_part.AddElements(list(list_of_ids))
        # Arc-length
        for i in range(self.loads_sub_model_part_list.size()):
            load_sub_model_part = self.main_model_part.GetSubModelPart(self.loads_sub_model_part_list[i].GetString())
            mechanical_model_part.CreateSubModelPart(self.loads_sub_sub_model_part_list[i].GetString())
            load_sub_sub_model_part = mechanical_model_part.GetSubModelPart(self.loads_sub_sub_model_part_list[i].GetString())
            list_of_ids = set()
            for node in load_sub_model_part.Nodes:
                list_of_ids.add(node.Id)
            load_sub_sub_model_part.AddNodes(list(list_of_ids))
        print(mechanical_model_part)
