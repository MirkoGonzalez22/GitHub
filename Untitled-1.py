class Restaurant:
    name = "0"
    category = "0"
    rating = 0.0
    delivery = False

# Instancia de la clase Restaurant y asignación de atributos
bobs_burguers = Restaurant()
bobs_burguers.name = "Bob's Burguers"
bobs_burguers.category = "American Diner"
bobs_burguers.rating = 4.7
bobs_burguers.delivery = False

# Imprimir los atributos de bobs_burguers
print(vars(bobs_burguers))
