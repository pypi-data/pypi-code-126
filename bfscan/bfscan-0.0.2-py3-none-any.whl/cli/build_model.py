from Bio import SeqIO
from bfscan.filter import BFScanFilter
from bfscan.model import BFScanModel
from bfscan.utils import read_sequence_file
from bfscan.logo import logo
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.under_sampling import RandomUnderSampler
import numpy as np
import argparse
import os

def main():
    print(logo)
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='*', metavar='FASTAFILE', required=True, help='Input fasta file')
    parser.add_argument('-b', '--background', required=True, help='Input background fasta file')
    parser.add_argument('-f', '--filter', type=str, required=True, help='filter file')
    parser.add_argument('-o', '--output', required=True, help='Output model file')
    parser.add_argument('-r', '--output-report', default=None, help='Output classification report file')
    arguments = parser.parse_args()

    bfscan_filter = BFScanFilter.load(arguments.filter)
    bfscan_model  = BFScanModel(base_estimator=ExtraTreesClassifier(), filter=bfscan_filter)

    X_raw = []
    y_raw = []

    for file in arguments.input:

        file_basename_name = os.path.splitext(os.path.basename(file).strip(".gz"))[0]
        records = (str(record.seq) for record in read_sequence_file(file))

        for record in records:
            X_raw.append([str(record)])
            y_raw.append(file_basename_name)
    
    records = (str(record.seq) for record in read_sequence_file(arguments.background))

    for record in records:
        X_raw.append([str(record)])
        y_raw.append("other")
    
    X_raw = np.array(X_raw)
    y_raw = np.array(y_raw)

    X_ros, y_ros = RandomUnderSampler().fit_resample(X_raw, y_raw)
    X_train, X_test, y_train, y_test = train_test_split(X_ros[:,0], y_ros)
    
    bfscan_model.fit(X_train, y_train)   
    report = classification_report(y_test, bfscan_model.predict(X_test))
    print(report)

    bfscan_model.save(arguments.output)
        
if __name__ == '__main__':
    main()
    



