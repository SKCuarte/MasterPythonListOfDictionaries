# Employee List of Dictionaries
ld_employee = [
{
    "id": "1",
    "name": "David Wallace",
    "job title": "CFO",
    "shift": "9am to 5pm",
    "salary": "30,000"
},

{
    "id": "2",
    "name": "Charles Miner",
    "job title": "Vice President",
    "shift": "9am to 5pm",
    "salary": "22,000"
},

{
    "id": "3",
    "name": "Michael Scott",
    "job title": "Regional Manager",
    "shift": "9am to 5pm",
    "salary": "10,000"
},

{
    "id": "4",
    "name": "Jim Halpert",
    "job title": "Sales Representative",
    "shift": "9am to 6pm",
    "salary": "8,000"
},

{
    "id": "5",
    "name": "Pam Halpert",
    "job title": "Sales Representative",
    "shift": "9am to 5pm",
    "salary": "8,000"
},

{
    "id": "6",
    "name": "Dwight Schrute",
    "job title": "Sales Representative",
    "shift": "9am to 5pm",
    "salary": "8,000"
},

{
    "id": "7",
    "name": "Angela Martin",
    "job title": "Senior Accountant",
    "shift": "9am to 5pm",
    "salary": "8,000"
}
]

for employee in ld_employee:
    print(f"ID: {employee['id']}, Name: {employee['name']}, Job Title: {employee['job title']}, Shift: {employee['shift']}, Salary: {employee['salary']}")