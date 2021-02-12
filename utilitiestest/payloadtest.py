def Payload_AddBook(isbn,aisle):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John testing"
    }
    return body
