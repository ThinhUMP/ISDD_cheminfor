from rdkit import DataStructs

def get_simi_pairwise(fgs1, fgs2):
    tanimoto_coeff = DataStructs.TanimotoSimilarity(fgs1, fgs2)
    return tanimoto_coeff