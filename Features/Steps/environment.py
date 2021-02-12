import requests




def after_scenario(context, scenario):
    delete_book = requests.post("http://216.10.245.166/Library/DeleteBook.php", json={
        "ID": context.BookId
    }, headers={"Content-Type": "application/json"})

    print(delete_book.json())
    # print(delete_book.text)
    assert "successfully" in delete_book.text
