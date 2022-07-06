"""
test_ppi.txt train_ppi.txt 
encode:ac, dpc, ct, cksaap, ara2vec, dmi2vec, esm ,pdb2dpc

python RF.py -test=test.txt -train=train.txt -encode="ac,ct,cksaap,..." -out=/tmp/rf.txt

"""
import numpy as np
from Bio import SeqIO
from zzd.feature_encode.feature_combine import feature_combine
from sklearn.svm import SVC

def load_data(ppi_file,seqs_file,features):
    """
    pass
    """
    ppis = np.genfromtxt(ppi_file,str)
    X,Y = np.array(ppis[:,:2],str), np.array(ppis[:,2],int)
    seqs = {i.id:str(i.seq) for i in SeqIO.parse(seqs_file,'fasta')}
    encode = feature_combine(features,features,seqs)
    return encode.encode(X),Y

def ppi_svm(test_file,train_file,seqs_file,feature_encode,n_jobs=-1,**argv):
    """
    test_file:for pred
    train_file:fro train
    seqs_file: fasta sequence
    feature: AC,DPC,CT,CKSAAP,ESM,ara2vec,dmi2vec
    """
    x_train, y_train = load_data(train_file,seqs_file,feature_encode)
    x_test, y_test = load_data(test_file,seqs_file,feature_encode)

    model =  SVC(probability=True,class_weight="balanced",verbose=0,C=6.3, gamma=15.8)
    model.fit(x_train,y_train)
    
    y_test_pred = model.predict_proba(x_test)[:, 1]
    return y_test_pred

if __name__ == "__main__":
    test_file = "../../../atppi/B2_train_and_test/p1n10_10folds/test_0.txt"
    train_file = "../../../atppi/B2_train_and_test/p1n10_10folds/train_0.txt"
    seqs_file = "../../../atppi/B1_ppis_and_seqs/ppis_ara_and_eff.fasta"
    pred = ppi_svm(test_file,train_file,seqs_file,feature_encode=['dpc'],pca=False)
