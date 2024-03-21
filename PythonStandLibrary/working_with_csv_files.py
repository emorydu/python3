import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])


with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader))
    # print([row for row in reader])
    for row in reader:
        print(row)
