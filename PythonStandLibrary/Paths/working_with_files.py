from pathlib import Path
from time import ctime
import shutil

path = Path("paths.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
print(ctime(path.stat().st_ctime))
# print(path.read_text())
# print(path.read_bytes())


with open("paths.py") as file:
    ...

# path.write_text()
# path.write_bytes()

source = Path("paths.py")
target = Path() / "paths.py.copy"
# target.write_text(source.read_text())

shutil.copy(source, target)


