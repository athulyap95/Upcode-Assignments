# Write python code to sort products data from https://fakestoreapi.com/products?limit=5 based rating.
Products = [
    {"id":1,"title":"Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops","price":109.95,
     "description":"Your perfect pack for everyday use and walks in the forest.",
     "category":"men's clothing","image":"url",
     "rating":{"rate":3.9,"count":120}},

    {"id":2,"title":"Mens Casual Premium Slim Fit T-Shirts","price":22.3,
     "description":"Slim-fitting style.",
     "category":"men's clothing","image":"url",
     "rating":{"rate":4.1,"count":259}},

    {"id":3,"title":"Mens Cotton Jacket","price":55.99,
     "description":"Great outerwear jackets.",
     "category":"men's clothing","image":"url",
     "rating":{"rate":4.7,"count":500}},

    {"id":4,"title":"Mens Casual Slim Fit","price":15.99,
     "description":"Casual slim fit.",
     "category":"men's clothing","image":"url",
     "rating":{"rate":2.1,"count":430}},

    {"id":5,"title":"John Hardy Women's Bracelet","price":695,
     "description":"From our Legends Collection.",
     "category":"jewelery","image":"url",
     "rating":{"rate":4.6,"count":400}}
]

# Sorting by rating using loops
n = len(Products)

for i in range(n):
    for j in range(i + 1, n):
        if Products[i]["rating"]["rate"] < Products[j]["rating"]["rate"]:
            Products[i], Products[j] = Products[j], Products[i]

# Print sorted products
for product in Products:
    print(product["title"], "→ Rating:", product["rating"]["rate"])
