import json
import yaml
from book import Book
from utils import convert_to_dicts, dict_to_xml

if __name__ == "__main__":
    print("Kia ora, Please type as prompted by the command line")
    book_index = 0
    print("How many books do you want to add?")
    times = input()
    # Check input
    while not times.isnumeric():
        print("Error message: pelase type a number")
        times = input()

    book_num = int(times)
    book_list = []

    while book_index < book_num:
        print("Now start add book {} ...".format(book_index + 1))
        print("Please type book title")
        title = input().strip()
        print("Please type book authors, separate multiple authors with commas")
        authors = input().strip()
        print("Please type book ISBN number. e.g. 978-0-87779-855-2")
        isbn = input().strip()
        print("Please type book publisher")
        publisher = input().strip()
        print("Please type book copyright. e.g. 2020")
        copyright = input().strip()
        print("Please type book categories, separate multiple category with commas")
        categories = input().strip()
        book_index += 1
        book = Book(title, authors, isbn, publisher, copyright, categories)
        book_list.append(book)

    print("What kind of file do you want to save? JSON/YAML/XML")
    print("To choose file format, please type JSON or YAML or XML")
    file_extension = input().lower()

    file_extension_list = ["json", "xml", "yaml"]

    # Check file format input whether valid
    while file_extension not in file_extension_list:
        print("Error message: File format is not in one of those JSON, YAML or XML")
        file_extension = input().lower()

    # accept sort
    print("What kind of field do you want to sort by? Title/Authors/Copyright")
    print("To choose sort field, please type TITLE or AUTHORS or COPYRIGHT")
    sort_field = input().lower()
    sort_field_list = ["title", "authors", "copyright"]

    # Check sort field input whether valid
    while sort_field not in sort_field_list:
        print(
            "Error message: Sort field is not in one of those TITLE, AUTHORS or COPYRIGHT"
        )
        sort_field = input().lower()

    book_list_dict = convert_to_dicts(book_list)
    book_list_dict = sorted(book_list_dict, key=lambda x: x[sort_field], reverse=False)

    if file_extension == "json":
        file_name = "book.json"
        book_json = json.dumps(
            book_list_dict, default=lambda o: o.__dict__, sort_keys=True, indent=4
        )
        with open(file_name, "w") as file_object:
            file_object.write(book_json)

    elif file_extension == "xml":
        file_name = "book.xml"

        book_xml = "<xml>"
        for i in book_list_dict:
            book_xml += "<book>"
            book_xml += dict_to_xml(i)
            book_xml += "</book>"
        book_xml += "</xml>"

        with open(file_name, "w") as file_object:
            file_object.write(book_xml)

    elif file_extension == "yaml":
        file_name = "book.yaml"
        book_yaml = yaml.dump(book_list_dict)
        with open(file_name, "w") as file_object:
            file_object.write(book_yaml)
