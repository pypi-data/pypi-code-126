import os
import MDAnalysis as mda
import LigPrepper as lp
try:
    from openbabel import openbabel
except:
    print(">>> Warning:\n"
          "            Could not find OpenBabel!!! SMILES2MOL2 and SMILES2PDBQT are not available!\n"
          ">>> To install openbabel:\n"
          "            conda install -c conda-forge openbabel")

def RunVina(vinabin, receptor, ligand, config):
    command = vinabin+' --config '+config+' --receptor '+receptor+' --ligand '+ligand+' --out ./output/'+ligand+' > ./log/'+str(ligand)[0:-6]+'.log'
    os.system("%s" % command)

def pdbqt2sdf(ligand):
    obConversion = openbabel.OBConversion()
    obConversion.SetInAndOutFormats("pdbqt","sdf")
    mol = openbabel.OBMol()
    obConversion.ReadFile(mol, "%s.pdbqt"%(str(ligand)[0:-6]))
    obConversion.WriteFile(mol, "%s.sdf"%(str(ligand)[0:-6]))

def protpdb2pdbqt(protpdb):
    obConversion = openbabel.OBConversion()
    obConversion.SetInAndOutFormats("pdb", "pdbqt")
    obConversion.AddOption("p")
    obConversion.AddOption("r")
    mol = openbabel.OBMol()
    obConversion.ReadFile(mol, "%s.pdb"%(str(protpdb)[0:-4]))
    obConversion.WriteFile(mol, "%s.pdbqt"%(str(protpdb)[0:-4]))

