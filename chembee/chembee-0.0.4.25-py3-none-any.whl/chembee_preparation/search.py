def get_similar_compounds(
    compounds_of_interest, compounds, n=10, distance="tanimoto"
) -> dict:
    """
    The get_similar_compounds function takes a list of compounds and returns the n most similar compounds.
    The similarity is calculated by calculating a user defined distance metric between two compound vectors.
    The function works on arbitrary data and features. It could also take in vectorized fingerprints. The function
    is written as such that it could return the most similar compounds that are the same as the search compounds. You
    would have to exclude them manually. Still, the function is experimental and if you feel handling the exlusion of
    of identical compounds inside of this function is neccessary, please file an issue, or feature request.

    :param compounds_of_interest: Used to specify the compounds that we want to find similar compounds for.
    :param compounds: Used to store the similarity scores for each compound.
    :param n=10: Used to specify the number of similar compounds to return. Specify n='all' if you want to return all coumpounds
    :return: A dictionary containing the jsonified result, ready to use in web tech like MongoDB, Flask, React, etc.

    :doc-author: Julian M. Kleber
    """

    AD = ApplicabilityDomain(verbose=True)
    sims = AD.analyze_similarity(
        base_train=compounds_of_interest,
        base_test=compounds,
        similarity_metric=distance,
    )
    if n == "all":
        result = sims.to_json()
    else:
        result = sims.head(n).to_json()
    return result


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
