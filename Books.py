# Books List of Dictionaries
ld_books = [
{
    "id": "1",
    "title": "A Tale of Two Cities",
    "author": "Charles Dickens",
    "release": "1859",
    "sold": "200+ million",
},

{
    "id": "2",
    "title": "Le Petit Prince",
    "author": "Antoine de Saint0-Exupery",
    "release": "French",
    "sold": "200 million",
},

{
    "id": "3",
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "release": "1988",
    "sold": "150 million",
},

{
    "id": "4",
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "release": "1997",
    "sold": "120 million",
},

{
    "id": "5",
    "title": "And Then There Were None",
    "author": "Agatha Christie",
    "release": "1939",
    "sold": "100 million",
},

{
    "id": "6",
    "title": "Dream of the Red Chamber",
    "author": "Cao Xueqin",
    "release": "1791",
    "sold": "100 million",
},

{
    "id": "7",
    "title": "The Hobbit",
    "author": "J. R. R. Tolkein",
    "release": "1937",
    "sold": "100 million",
}
]

for book in ld_books:
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Release: {book['release']}, Sold: {book['sold']}")