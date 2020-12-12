import csv

movies = [
    {"name": "The Matrix", "director": "Wachowskis"},
    {"name": "Shawshank Redemption", "director": "Tim Something"},
    {"name": "Okja", "director": "Swedish Director"},
]


def write_to_output(output):
    with open("file.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "director"])
        writer.writeheader()
        writer.writerows(output)


def read_from_file():
    with open("file.csv", "r") as f:
        reader = csv.DictReader(f)
        # for line in reader:
        #     print(f"Name: {line['name']}\tDirector: {line['director']}")
        return list(reader)


write_to_output(movies)
read_from_file()
