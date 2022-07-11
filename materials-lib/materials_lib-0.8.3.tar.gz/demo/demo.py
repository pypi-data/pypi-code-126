from materials_lib.material import Material

filename = "./data/titanium.toml"
mat = Material(filename)
print(mat.G())
