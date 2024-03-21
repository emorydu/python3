from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip", "w") as zip_file:
    [zip_file.write(p) for p in Path("../../PrimitiveTypes").rglob("*.*") if p.is_file()]


with ZipFile("files.zip") as zip_file:
    print(zip_file.namelist())
    info = zip_file.getinfo(zip_file.namelist()[0])
    print(info.file_size)
    print(info.compress_type)
    print(info.compress_size)
    zip_file.extractall("extract")

