# University List of Dictionaries
ld_uni = [
{
    "id": "1",
    "name": "Cal-Tech",
    "location": "California",
    "quality": "10/10",
    "rate": "3%",
},

{
    "id": "2",
    "name": "Harvard University",
    "location": "Massachusetts",
    "quality": "10/10",
    "rate": "3%",
},

{
    "id": "3",
    "name": "Princeton University",
    "location": "New Jersey",
    "quality": "10/10",
    "rate": "4%",
},

{
    "id": "4",
    "name": "Stanford",
    "location": "California",
    "quality": "10/10",
    "rate": "4%",
},

{
    "id": "5",
    "name": "Brown University",
    "location": "Rhode Island",
    "quality": "10/10",
    "rate": "5%",
},

{
    "id": "6",
    "name": "MIT",
    "location": "Massachusetts",
    "quality": "10/10",
    "rate": "5%",
},

{
    "id": "7",
    "name": "University of Chicago",
    "location": "Chicago",
    "quality": "10/10",
    "rate": "5%",
},
]

for uni in ld_uni:
    print(f"ID: {uni['id']}, Name: {uni['name']}, Location: {uni['location']}, Quality: {uni['quality']}, Rate: {uni['rate']}")