"""Module de prétraitement des données.
Utile pour la conversation des noms, adjectif, verbe et adverbe
selon la notation canonique du texte. Puis séparation dans les
dossiers de training ou de test (pos/neg) en respectant un quota
de 80 - 20 (training - test)"""

import os
import random
import shutil

def select_random_training_file(dir_path):
    """Choisi les fichiers qui feront parti du corpus d'entrainement"""
    training_files = []
    while len(training_files) < 400:
        choose_file = random.choice(os.listdir(dir_path))
        if choose_file not in training_files:
            training_files.append(choose_file)
    return training_files

def create_dir():
    """Crée l'arborescence de dossier utile"""
    shutil.rmtree("TestText")
    shutil.rmtree("TrainingText")
    os.makedirs("TrainingText/neg")
    os.makedirs("TrainingText/pos")
    os.makedirs("TestText/neg")
    os.makedirs("TestText/pos")
    print("TrainingText directories create")
    print("TestText directories create")


def fill_dir(dir_path, training_files):
    for f in training_files:
        t = "tagged/neg/" + str(f)
        print(t)
        shutil.copy2(t, "TrainingText/neg/")

if __name__ == "__main__":
    create_dir()
    print("Select file for training")
    negative_files = select_random_training_file("tagged/neg/")
    print("Selected negative files: " + str(negative_files))
    fill_dir("truc", negative_files)
    positive_files = select_random_training_file("tagged/pos/")
    print("\nSelected positive files: " + str(positive_files))



