
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def add_node(name, type, properties=None):
    """
    Stores a node as a Redis Hash.
    Key: node:{name}
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
    Key: edges:{name1}
    Members: "{name2}|{type}"
    """
    r.sadd(f"edges:{name1}", f"{name2}|{type}")