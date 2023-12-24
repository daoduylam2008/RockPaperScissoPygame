import csv


def read_data(file):
    with open(file, mode='r') as csv_file:
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


class CSV_txt:
    def __init__(self, file):
        self.file = file
        with open(self.file, 'r') as self.csv_file:
            self.csv_reader = csv.reader(self.csv_file)
            self.line_count = 0

            for row in self.csv_reader:
                self.line_count += 1

    def readDataRows(self) -> list:
        with open(self.file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            data = [row for row in csv_reader]
        return data

    def readDataColumns(self) -> list:
        data = self.readDataRows()
        result = []
        for i in range(0, len(data[0])-1):
            r = []
            for j in range(0, self.line_count):
                r.append(data[j][i])
            result.append(r)

        return result

