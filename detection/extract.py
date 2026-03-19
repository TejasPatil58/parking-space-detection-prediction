import zipfile

with zipfile.ZipFile("pklot-dataset.zip", 'r') as zip_ref:
    zip_ref.extractall("detection/dataset")
print("Extraction Done!")