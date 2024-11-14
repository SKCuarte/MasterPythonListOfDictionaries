# Restaurant List of Dictionaries
ld_resto = [
{
    "id": "1",
    "name": "Antonio's",
    "owner": "Tony Boy",
    "cuisine type": "Fine Dining",
    "reservation": "Yes",
},

{
    "id": "2",
    "name": "Jollibee",
    "owner": "JFC",
    "cuisine type": "Fast Food",
    "reservation": "Yes",
},

{
    "id": "3",
    "name": "Olive Garden",
    "owner": "Darden Restaurants, Inc.",
    "cuisine type": "Casual Dining",
    "reservation": "No",
},

{
    "id": "4",
    "name": "Laza Food Plaza",
    "owner": "N/A",
    "cuisine type": "Cafeteria",
    "reservation": "No",
},

{
    "id": "5",
    "name": "The Alley",
    "owner": "Vikings",
    "cuisine type": "Buffet",
    "reservation": "Yes",
},

{
    "id": "6",
    "name": "Five Guys",
    "owner": "Five Guys Holdings, Inc.",
    "cuisine type": "Fast Casual",
    "reservation": "Yes",
},

{
    "id": "7",
    "name": "Mexikombi",
    "owner": "N/A",
    "cuisine type": "Food Trucks",
    "reservation": "No",
}
]

for resto in ld_resto:
    print(f"ID: {resto['id']}, Name: {resto['name']}, Owner: {resto['owner']}, Cuisine Type: {resto['cuisine type']}, Reservation: {resto['reservation']}")