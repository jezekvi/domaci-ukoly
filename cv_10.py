"""
from pyproj import Transformer

wgs2jtsk = Transformer.from_crs(4326,5514)
jtsk2wgs = Transformer.from_crs(5514,4326)

out = wgs2jtsk.transform(50,15)

print(out)
print(jtsk2wgs.transform(*out))
"""
def read_int(prompt):
    return int(input(prompt))

def read_float(prompt):
    pass

def print_dict(adict):
    pass