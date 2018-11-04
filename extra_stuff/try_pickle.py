import pickle
import sys

with open("dictionary.pickle","rb") as input_file:
    e = pickle.load(input_file,encoding="latin1")

print(e)
