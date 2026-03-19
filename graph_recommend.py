from graph_api import add_node, add_edge, get_recommendations

# People
add_node('Emily',   'Person', {'name': 'Emily'})
add_node('Spencer', 'Person', {'name': 'Spencer'})
add_node('Brendan', 'Person', {'name': 'Brendan'})
add_node('Trevor',  'Person', {'name': 'Trevor'})
add_node('Paxton',  'Person', {'name': 'Paxton'})

# books
add_node('Cosmos',               'Book', {'title': 'Cosmos',               'price': 17.00})
add_node('Database Design',      'Book', {'title': 'Database Design',      'price': 195.00})
add_node('The Life of Cronkite', 'Book', {'title': 'The Life of Cronkite', 'price': 29.95})
add_node('DNA and you',          'Book', {'title': 'DNA and you',          'price': 11.50})

add_edge('Emily',   'Spencer', 'knows')  # edge 10
add_edge('Spencer', 'Emily',   'knows')  # edge 11
add_edge('Spencer', 'Brendan', 'knows')  # edge 12

add_edge('Emily',   'Database Design',      'bought')  # edge 1
add_edge('Spencer', 'Cosmos',               'bought')  # edge 2
add_edge('Spencer', 'Database Design',      'bought')  # edge 3
add_edge('Brendan', 'Database Design',      'bought')  # edge 4
add_edge('Brendan', 'DNA and you',          'bought')  # edge 5
add_edge('Trevor',  'Cosmos',               'bought')  # edge 6
add_edge('Trevor',  'Database Design',      'bought')  # edge 7
add_edge('Paxton',  'Database Design',      'bought')  # edge 8
add_edge('Paxton',  'The Life of Cronkite', 'bought')  # edge 9

recommendations = get_recommendations('Spencer')

print("Book recommendations for Spencer:")
for book in recommendations:
    print(f"  - {book}")