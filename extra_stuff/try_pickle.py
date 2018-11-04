import pickle
import sys

print sys.getdefaultencoding()
print type(open("dictionary.pickle","rb"))
with open("dictionary.pickle","rb") as input_file:
    e = pickle.load(input_file)

print e
