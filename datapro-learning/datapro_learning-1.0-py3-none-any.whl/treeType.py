import json
import re
from queue import Queue
from pathlib import Path

class TreeOfType:
  """
  Instantiate a type's tree.
  This tree will used to assignt type to any token.

  :param path: path to tree-type store in json format.
  :type path: str
  """

  def __init__(self):
    self.data = dict()

    default_tree_type = Path('datapro/tree-type.json')
    self.load_tree_type(default_tree_type)
  
  def load_tree_type(self, path):
    '''
      Load new type's tree.

      :param path: path where json file store.
      :type path: str

      :return: The json datastructure as dict
      :rtype: dict
    '''
    filename = Path(path)
    if not filename.exists():
      print("Not found.")
    else :
      with open(filename, 'r') as f :
        tree = json.load(f)
      self.data = tree
      self.generate_code()
  
  def generate_code(self):
    '''
      Generate code for each node. consist of key and data. lower equal A, B, C ..
    '''
    _tree_type = self.data

    q = Queue()
    _tree_type["TOKEN"]['code'] = dict()
    _tree_type["TOKEN"]["code"]["key"] = '@'
    _tree_type["TOKEN"]["code"]["data"] = ''
    q.put("TOKEN")
    
    while not q.empty() :
      now_node = q.get()
      for i, child in enumerate(_tree_type[now_node]['children']) :
        now_key = ord(_tree_type[now_node]["code"]["key"])
        before_data = _tree_type[now_node]["code"]["data"]
        _tree_type[child]["code"] = dict()
        _tree_type[child]["code"]["key"] = chr(now_key+1)
        _tree_type[child]["code"]["data"] = before_data + "." + chr(now_key+1) + str(i+1)
        q.put(child)
    self.data = _tree_type
      
  def fix_format(self, token):
    """
      Fix start and end with only 1 token.

      :param token: token
      :type token: str

      :return: The token after fixed.
      :rtype: str
    """
    if len(token)>2 and token[0]=='^' and token[-1]=='$': return re.escape(token)
    return "^"+re.escape(token)+"$"

  def unfix_format(self, token) :
    """
      Unfix start and end. deleting "^" adn "$".

      :param token: token
      :type token: str

      :return: The token after fixed.
      :rtype: str
    """
    if len(token)>2 and (token[0]!='^' or token[-1]!='$'): return token
    return token[1:-1]

  def revese_escape(self, token) :
    """
      :param token: token
      :type token: str

      :return: The token after fixed.
      :rtype: str
    """
    return re.sub(r'\\(.)', r'\1', token)

  def follow_by(self, token, tokenT):
    """
      Check whather The tokenT is a generalization of the token.

      :param token: Target token.
      :type token: str

      :param tokenT: Target Type of token
      :type tokenT: str

      :return: The result of checking.
      :rtype: bool
    """
    return re.search(self.data[tokenT]["regex"], token)

  def sub_generalize(self, token1,token2): # O(1)
    """
      check whether token2 is a generalization of token1

      :param token1: Token1.
      :type token1: str

      :param token2: Token2
      :type token2: str

      :return: The result of checking.
      :rtype: bool
    """
    dif_level = abs(ord(self.data[token1]["code"]["key"]) - ord(self.data[token2]["code"]["key"]))
    return self.data[token2]["code"]["data"] in self.data[token1]["code"]["data"] and dif_level==1

  def create_tree_type_node(self, token_name, parent, regex):
    """
      Create new node to the type's tree.

      :param token_name: Name of new node.
      :type token_name: str

      :param parent: The parent node.
      :type parent: str

      :param regex: Regular expression of this node.
      :type regex: str
    """
    self.data[token_name] = dict()
    self.data[token_name]["regex"] = regex
    self.data[token_name]["children"] = []
    self.data[token_name]["parent"] = parent
    self.data[token_name]["code"] = dict()
    self.data[token_name]["code"]["key"] = chr(ord(self.data[parent]["code"]["key"]) + 1)
    self.data[token_name]["code"]["data"] = self.data[parent]["code"]["data"] + "." + self.data[token_name]["code"]["key"] + str(len(self.data[parent]["children"]))
    self.data[parent]["children"].append(token_name)

  def assign_type(self, token, grows_tree=False) :
    """
      Assign types to given token.

      :param token: The Target token.
      :type token: str

      :param grows_tree: The state that checkห whether new node can be produced. 
      :type grows_tree: bool

      :return: set of token's types.
      :rtype: set
    """
    # time complexity is O(height of type's tree)
    types = set()
    parent = "TOKEN" # last node that matching.

    _tree_type = self.data

    q = Queue()
    for k in _tree_type["TOKEN"]["children"] :
      q.put(k)

    while not q.empty() :
      now_type = q.get()
      if (now_type not in  _tree_type) : continue
      if re.search( _tree_type[now_type]["regex"], self.revese_escape(token)) :
        types.add(now_type)
        parent = now_type
        for k in _tree_type[now_type]["children"] :
          q.put(k)
    
    if parent=="DIGIT" : # new general type
      len_token = str(len(token))
      new_type = len_token + "_DIGIT"
      if not new_type in _tree_type :
        self.create_tree_type_node(new_type, parent, "^\\d{" + len_token + "}$")
        types.add(new_type)

    if  _tree_type[parent]["regex"] != self.fix_format(parent) and (token not in _tree_type) and grows_tree: # general node
        # constuct new special node
        self.create_tree_type_node(token, parent, self.fix_format(token))
        types.add(token)
    return types

  def print_space(self, k) :
    for i in range(len(k)) :
      if k[i][1]:
        print(" ", end="")
      else :
        print("|", end="")
      for j in range(k[i][0]):
        print(" ", end="")

  def display(self, root="TOKEN", level=0, stack_space=[]):
    """
      show typs's tree structure display.
    """
    if level == 0:
      print("---------- Type's Tree -------------")
      print("TOKEN")
    cnt = 0
    size = len(self.data[root]['children'])
    for child in self.data[root]['children'] :
      if child in self.data :
        self.print_space(stack_space)
        if cnt == size-1 :
          print("└── " + child)
        else :
          print("├── " + child)
        temp = stack_space.copy()
        temp.append([2 + int(len(child)/2), cnt == size-1])
        self.display(child, level+1, temp)
        cnt+=1
    