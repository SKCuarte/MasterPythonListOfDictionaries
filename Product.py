#List of Dictionary (Products)
ld_products = [
{
    "product": "Canned Food",
    "product name": "Argentina Meatloaf",
    "price": "P49.00",
    "quantity": "100pcs",
    "quality": "7/10",
    "supplier": "Argentina"
},

{
    "product": "Shampoo",
    "product name": "Sunsilk Strong & Long Shampoo",
    "price": "P499.00",
    "quantity": "100pcs",
    "quality": "8/10",
    "supplier": "Sunsilk"
},

{
    "product": "Conditioner",
    "product name": "Cream Silk Triple Keratin Serum Conditioner",
    "price": "P299.00",
    "quantity": "100pcs",
    "quality": "9/10",
    "supplier": "Cream Silk"
},

{
    "product": "Face Cleanser",
    "product name": "Pond's Men Energy Charge",
    "price": "P149.00",
    "quantity": "100pcs",
    "quality": "8/10",
    "supplier": "Pond's"
},

{
    "product": "Soap",
    "product name": "Kojie San Men Lightening Face and Body Soap",
    "price": "P79.00",
    "quantity": "100pcs",
    "quality": "9/10",
    "supplier": "Kojie San"
},

{
    "product": "Instant Coffee",
    "product name": "Nescafe Classic",
    "price": "P49.00",
    "quantity": "100pcs",
    "quality": "8/10",
    "supplier": "Nescafe"
},

{
    "product": "Lotion",
    "product name": "Silka Papaya Premium Whitening Lotion",
    "price": "P98.00",
    "quantity": "100pcs",
    "quality": "7/10",
    "supplier": "Silka"
}
]

for product in ld_products:
    print(f"Product: {product['product']}, Product Name: {product['product name']}, Price: {product['price']}, Quantity: {product['quantity']}, Quality: {product['quality']}, Supplier: {product['supplier']}")