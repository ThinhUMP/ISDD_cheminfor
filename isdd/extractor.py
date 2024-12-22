from rdkit import Chem
from rdkit.Chem import AllChem

def smile_to_mol(smile):
    mol = Chem.MolFromSmiles(smile)
    if mol == None:
        raise ValueError(f"Invalid SMILES: {smile}")
    return mol

def get_morgan_fgs(mol, radius=2, nbits=2048):
    fgs = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=nbits)
    return fgs