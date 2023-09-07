class HandleCSV:
    filename = "C:\Users\User\Downloads\employees.csv"

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            return foo.readlines()

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()

if __name__=="__main__":
    print(__name__)
    print("from utils/info.csv")