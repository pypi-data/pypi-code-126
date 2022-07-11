
import cobra
from typing import Match
def _number_to_chr_safe(numberStr: Match) -> str:
    ascii = int(numberStr.group(1))
    return numberStr.group(1) if (ascii <= 31 or ascii == 127) else chr(ascii)
cobra.io.sbml._number_to_chr = _number_to_chr_safe

import libsbml

cobra_model = cobra.io.read_sbml_model('iJN746_mntx.sbml')

model = cobra.io.load_model('BIOMD0000000586')

#model_file = "BIOMD0000000586_url.xml"
model_file = "00e21d35b6f9e555d9454716b7e618c71a7b4a4f.sbml"
sbml_model = libsbml.readSBML(model_file)
#model = sbml_model.getModel()

cobra_model = cobra.io.read_sbml_model(model_file)

for r in range(model.getNumReactions()):
    rxn = model.getReaction(r)
    for m in range(rxn.getNumModifiers()):
        mod = rxn.getModifier(m)
        print(mod.getId(), "in reaction '" + rxn.getId() + "'")

for s in range(model.getNumSpecies()):
    spc = model.getReaction(s)
    for m in range(spc.getNumModifiers()):
        mod = spc.getModifier(m)
        print(mod.getId(), "in species '" + spc.getId() + "'")

import mergem

#mergem.update_id_mapper()

#model = mergem.load_model("merged_model.sbml")

model1 = mergem.load_model("iEC042_1314.sbml")
model2 = mergem.load_model("iECP_1309.sbml")
#model2 = mergem.load_model("iEC042_1314.sbml")

#model1 = mergem.load_model("e_coli_core.xml")
#model2 = mergem.load_model("e_coli_core.xml")

#model1 = mergem.load_model("Recon3D.sbml")
#model2 = mergem.load_model("iMM1415.sbml")

#model1 = mergem.load_model("iMM1415.sbml")
#model2 = mergem.load_model("iMM1415.sbml")

#model1 = mergem.load_model("RECON1.xml")
#model2 = mergem.load_model("RECON1.xml")

#model1 = mergem.load_model("AU.sbml")
#model2 = mergem.load_model("PT.xml")
#model2 = mergem.load_model("CA.xml")
#model2 = mergem.load_model("MD.xml")

merge_results = mergem.merge([model1, model2])

print(merge_results['jacc_matrix'])
mergem.save_model(merge_results["merged_model"], model1.id + "_" + model2.id + "_merged_model.sbml")


## Profiling
# 76854 ms (52 sec) - v0.10 (0)
# 63061 ms - template_reactions (1)
# 47480 ms - template to merge_model is same model (3)
# 46761 ms - pickles loaded only once at startup (4)
# 46161 ms - template to merge_model converts all metabolite ids (5)
# 44588 ms - simplified map_metabolite_to_mergem_id (7)
# 44196 ms - removed cleanup of models (10)
# 41463 ms - reaction_copy once and reversed ifs (11)
# 39580 ms - metabolites translated at once (13)
# 39492 ms - efficient metabolite_id reversal (16)
# 39790 ms - no conversion of sources to list (18)
# 37745 ms - no reaction copies (19)
# 37228 ms - limited calls to id (20)
# 37594 ms - sources are lists (21)
# 37257 ms - append all lists (26)
# 37411 ms (13 sec) - sources are sets again, so no repeated model ids (29)
# 40585 ms (11 sec) - v13
# 38160 ms (11 sec) - v16
# 39390 ms (11 sec) - v17
# 24860 ms (5.8 sec) - v18 (dictionaries are empty)
# 30940 ms (11 sec) - v20