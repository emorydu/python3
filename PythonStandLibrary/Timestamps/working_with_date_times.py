import time
from datetime import datetime


dt = datetime(2024, 3, 11)
print(dt)

dt = datetime.now()
print(dt)
print(datetime.strptime("2024/3/11", "%Y/%m/%d"))

another_dt = dt
dt = datetime.fromtimestamp(time.time())
print(dt.year)
print(dt.month)
print(dt.day)
print(dt)

print(another_dt > dt)
print(another_dt < dt)
print(another_dt == dt)

dt = datetime.now()
dtf = dt.strftime("%Y-%m-%d")
print(dtf)

