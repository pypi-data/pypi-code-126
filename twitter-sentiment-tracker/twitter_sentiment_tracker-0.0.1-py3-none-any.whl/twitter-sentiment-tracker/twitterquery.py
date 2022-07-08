'''
This method constructs a query_param string for twitter api
INPUT: keywords_ops- list of lists. Each element in the outer list represent a condition separated by the 'OR' operator from the other elements. Each element in the 
        inner lists represents a condition separated by the 'AND' operator from the other elements in the same list.
        lang- list that stores language abbreviations that represent which languages tweets may be, with an empty list representing any language
OUTPUT: query_params- dictionary recognmized as a valid query format by the Twitter web API v2
RESULT: Twitter API v2 can be accessed in order to retrieve tweet data on keywords over a given interval
'''
def make_query(keywords_ops, lang):
    
    #remove list entries that contain no meaningful characters or contain forbidden characters
    keywords_ops = [[i for i in sublist if i.strip() != '' and "\\" not in  i and ":" not in i] for sublist in keywords_ops]
    #remove empty sublists
    keywords_ops = [sublist for sublist in keywords_ops if sublist]
    rule_list = []
    
    #list of legal twitter language abbreviations
    lang_list = ['en','ar','bn','cs','da','de','el','es','fa','fi','fil','fr','he','hi','hu','id','it','ja','ko','msa','nl','no','pl','pt','ro','ru','sv','th','tr','uk','ur','vi','zh-c','zh-tw']  
    temp_string = ""
    first = True #boolean that represents whether current sublist is the first in the list
    first_lang = True #boolean that represents whether the current language abbr. is the first to be added to the temp_string
    
    #construct twitter query string in correct syntax
    for possible_match in keywords_ops:
        if not first:
             temp_string += "OR "
        temp_string += "("
        for partial_match in possible_match:
            if temp_string != "(" and temp_string != "OR (":
                temp_string += " "
            if not "-" in partial_match:
                temp_string += "\"" + partial_match + "\""
            else:
                temp_string += partial_match 
        for abbr in lang:
            if abbr in lang_list:
                if first_lang:
                    temp_string += " ("
                if not first_lang:
                    temp_string += " OR "
                temp_string += "lang:" + str(abbr) 
                first_lang = False
        #checks if parenthesis for language filter need to be closed
        if not first_lang:
            temp_string += ")"
        temp_string += ")"
        rule_list.append(temp_string)
        temp_string = ""
        first = False
        first_lang = True
        
    # construct a ruleset from all rules
    rules = " ".join(rule_list)
    query_params = {'query': rules}
    
    return query_params 