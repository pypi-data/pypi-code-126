def get_similar_compounds_structure(
    compounds_of_interest, compounds, n=10, distance="tanimoto"
) -> dict:
    """
    The get_similar_compounds_structure function takes a list of compounds and returns the most similar compounds based on structure.
    The function takes in four arguments:

        1) A list of compound names (compounds_of_interest),
        2) A dataframe containing all the other compounds (compounds), and
        3) An integer n that specifies how many similar compounds to return. The default is 10.
        4) A distnace

    The function returns a dictionary with three keys: "InChi", "number" and "similarity". Number corresponds to the index number for each compound, while similarity contains their similarity score.

    :param compounds_of_interest: Used to Specify the compounds for which similar compounds are to be found.
    :param compounds: Used to Get the structure of all compounds in the database.
    :param n=10: Used to Specify how many similar compounds we want to find.
    :param distance="Tanimoto": Used to Specify the similarity metric to be used.
    :return: A dictionary with the following keys:.

    :doc-author: Julian M. Kleber
    """
    raise NotImplementedError(
        "Either implement with RDKit or just convert a fingerprint to a dataframe"
    )
    for i in range(len(compounds_of_interest)):
        compound = compounds_of_interest[i]
        similarity = calculate_similarity(compound, compounds, n=10)
        compounds["number"] = i
        compounds["similarity"] = similarity
        compounds["InChI"] = inchi
    return compounds
