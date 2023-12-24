import csv


def read_data():
    with open('employee_birthday.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(row)
            line_count += 1
        print(f'Processed {line_count} lines.')

        print(csv_reader.restkey)


class CSV:
    def __init__(self, file):
        self.file = file
        with open(self.file, 'r') as self.csv_file:
            self.csv_reader = csv.reader(self.csv_file)
            self.line_count = 0

            for row in self.csv_reader:
                self.line_count += 1

    def dataRows(self) -> list:
        with open(self.file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            data = [row for row in csv_reader]
        return data

    def dataColumns(self) -> list:
        data = self.dataRows()
        result = []
        for i in range(0, len(data[0])-1):
            r = []
            for j in range(0, self.line_count):
                r.append(data[j][i])
            result.append(r)

        return result


print(CSV("employee_birthday.txt").dataColumns())

