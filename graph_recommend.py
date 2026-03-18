from graph_api import add_node, add_edge, get_recommendations

# People
add_node('Bob',     'Person', {'name': 'Bob'})
add_node('Emily',   'Person', {'name': 'Emily'})
add_node('Billy',   'Person', {'name': 'Billy'})
add_node('Arshia',  'Person', {'name': 'Arshia'})
add_node('Shireen', 'Person', {'name': 'Shireen'})
add_node('Rob',     'Person', {'name': 'Rob'})

# Books
add_node('The Odyssey',    'Book', {'title': 'The Odyssey',    'price': 17.00})
add_node('Database Design','Book', {'title': 'Database Design','price': 195.00})
add_node('Bible',          'Book', {'title': 'Bible',          'price': 29.95})
add_node('Marvel Comic',   'Book', {'title': 'Marvel Comic',   'price': 11.50})

# Knows edges
add_edge('Arshia',  'Emily',   'knows')
add_edge('Emily',   'Arshia',  'knows')
add_edge('Arshia',  'Shireen', 'knows')

# Bought edges
add_edge('Arshia',  'The Odyssey',    'bought')
add_edge('Arshia',  'Database Design','bought')
add_edge('Emily',   'Database Design','bought')
add_edge('Emily',   'Bible',          'bought')
add_edge('Shireen', 'Marvel Comic',   'bought')
add_edge('Shireen', 'The Odyssey',    'bought')
add_edge('Bob',     'Bible',          'bought')
add_edge('Billy',   'Marvel Comic',   'bought')
add_edge('Rob',     'Database Design','bought')

# Recommendations for Arshia
recommendations = get_recommendations('Arshia')

print("Book recommendations for Arshia:")
for book in recommendations:
    print(f"  - {book}")