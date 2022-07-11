from sys import path
# from os.path import dirname, join, abspath
# path.append(abspath(join(dirname(__file__), '..')))

print(path)
from materials_lib.material import Material

mat = Material("Titanium")
print(mat.G())
