
def get_similar_compounds(compounds_of_interest, compounds, n=10, distance="Tanimoto")->dict:
    """
    The get_similar_compounds function takes a list of compounds and returns the n most similar compounds.
    The similarity is calculated by calculating the cosine distance between two compound vectors.
    
    :param compounds_of_interest: Used to specify the compounds that we want to find similar compounds for.
    :param compounds: Used to Store the similarity scores for each compound.
    :param n=10: Used to Specify the number of similar compounds to return.
    :return: A dictionary with the following keys:.
    
    :doc-author: Trelent
    """
    

    for compound in compounds_of_interest: 
        similarity = calculate_similarity(compound, compounds, n=10)
        compounds["number"] = 
        compounds["similarity"] = similarity
        compounds["InChI"] = inchi
    return compounds


def get_similar_compounds_structure(compounds_of_interest, compounds, n=10, distance="Tanimoto")->dict: 
    """
    The get_similar_compounds_structure function takes a list of compounds and returns the most similar compounds based on structure.
    The function takes in three arguments: 
        1) A list of compound names (compounds_of_interest), 
        2) A dataframe containing all the other compounds (compounds), and 
        3) An integer n that specifies how many similar compounds to return. The default is 10.  
        4.) A distnace
         The function returns a dictionary with three keys: "InChi", "number" and "similarity". Number corresponds to the index number for each compound, while similarity contains their similarity score.
    
    :param compounds_of_interest: Used to Specify the compounds for which similar compounds are to be found.
    :param compounds: Used to Get the structure of all compounds in the database.
    :param n=10: Used to Specify how many similar compounds we want to find.
    :param distance="Tanimoto": Used to Specify the similarity metric to be used.
    :return: A dictionary with the following keys:.
    
    :doc-author: Trelent
    """
    
    for compound in compounds_of_interest: 
        similarity = calculate_similarity(compound, compounds, n=10)
        compounds["number"] = 
        compounds["similarity"] = similarity
        compounds["InChI"] = inchi
    return compounds