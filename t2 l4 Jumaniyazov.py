
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    op = open(INPUT_FILENAME, "r")
    clos = open(OUTPUT_FILENAME, "w")
    read = csv.DictReader(op)
    arr = []
    for i in read: arr.append(i)
    json.dump(arr, clos, indent = 4)
    clos.close()
    op.close()

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
