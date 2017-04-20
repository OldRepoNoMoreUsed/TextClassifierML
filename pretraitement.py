"""Module de prétraitement des données.
Utile pour la conversation des noms, adjectif, verbe et adverbe
selon la notation canonique du texte. Puis séparation dans les
dossiers de training ou de test (pos/neg) en respectant un quota
de 80 - 20 (training - test)"""

import os
import random
import shutil

CATEGORIES = ["pos", "neg"]

SOURCES = ["tagged/pos", "tagged/neg"]
TARGET = ["training/pos", "training/neg", "test/pos", "test/neg"]

TAG = ["NOM", "ADJ", "VER", "ADV"]

RATIO = 0.8
POS_NEG_RATIO = 0.5

def review(files, source, target):
    """Decoupe et tri les fichiers données"""
    for file in files:
        with open(str(source) + "/" + str(file), 'r') as opened_file:
            resume = ""
            for line in opened_file:
                if any(word in line for word in TAG):
                    splited_line = line.split("\t")[2]
                    if "|" in splited_line:
                        resume += splited_line.split("|")[0]
                    else:
                        resume += splited_line
        with open(str(target) + "/reviewed_" + str(opened_file), 'w') as out:
            out.write(resume)

if __name__ == '__main__':
    print("Read directories...")
    POSITIVE_FILES = os.listdir(SOURCES[0])
    NEGATIVE_FILES = os.listdir(SOURCES[1])
    print("Counting files...")
    COUNT_POS = len(POSITIVE_FILES)
    COUNT_NEG = len(NEGATIVE_FILES)




