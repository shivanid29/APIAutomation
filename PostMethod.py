import requests
import json
from utilitiestest.configuration import *
from utilitiestest.urldetails import *
from utilitiestest.Resources import *
from utilitiestest.payloadtest import *

adding_book = requests.post(NeededUrl() + Actiontobetaken.Add_Books, json=Payload_AddBook(), headers={"Content-Type": "application/json"})

print(adding_book)
print(adding_book.json())
response_book = adding_book.json()
BookId = response_book["ID"]
print("This is the bookid that was added", BookId)

get_bookdetails = requests.get("http://216.10.245.166/Library/GetBook.php?AuthorName=John testing",
                               headers={"Content-Type": "application/json"})

print(get_bookdetails.json())

delete_book = requests.post("http://216.10.245.166/Library/DeleteBook.php", json={
    "ID": BookId
}, headers={"Content-Type": "application/json"})

print(delete_book.json())
# print(delete_book.text)
assert "successfully" in delete_book.text
