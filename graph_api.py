import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def add_node(name, type, properties=None):
    """
    Stores a node as a Redis Hash.
    Fields: type, plus any properties (e.g. name, title, price)
    """
    key = f"node:{name}"
    r.hset(key, "type", type)
    if properties:
        for k, v in properties.items():
            r.hset(key, k, v)


def add_edge(name1, name2, type):
    """
    Stores a directed edge from name1 -> name2.
    Uses a Redis Set per node to track outgoing edges.
    """
    r.sadd(f"edges:{name1}", f"{name2}|{type}")

def get_adjacent(name, node_type=None, edge_type=None):
    """
    Returns the names of all nodes reachable from `name` via a direct edge.
    """
    raw_edges = r.smembers(f"edges:{name}")
    results = []

    for entry in raw_edges:
        neighbour, etype = entry.rsplit("|", 1)

        # Filter by edge type if requested
        if edge_type is not None and etype != edge_type:
            continue

        # Filter by node type if requested
        if node_type is not None:
            stored_type = r.hget(f"node:{neighbour}", "type")
            if stored_type != node_type:
                continue

        results.append(neighbour)

    return results

def get_recommendations(name):
    """
    Returns books bought by people that `name` knows but that `name`
    has not already bought.
    """
    friends = get_adjacent(name, edge_type='knows')
    already_owns = set(get_adjacent(name, node_type='Book', edge_type='bought'))

    recommended = set()
    for friend in friends:
        friend_books = get_adjacent(friend, node_type='Book', edge_type='bought')
        recommended.update(friend_books)

    return list(recommended - already_owns)