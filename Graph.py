# Jonathan Nguyen; #000918228

""" This python file is used to set our graph in order. Our graph will be a
dictionary,with the keys being our initial nodes or "starting point", and another
dictionary with the nodes and distances from our starting point as the value. As for
scalability, given that the distances from each node should theoritically not change 
and given the type of structure we are using to create the graph, this model should scale 
just fine when applied to larger or smaller projects."""


distances = {
    "hub": {"a": 7.2, "b": 3.8, "c": 11.0, "d": 2.2, "t": 1.2, "v": 2.4, "q": 2.0},
    "a": {
        "b": 3.8,
        "c": 11.0,
        "k": 5.3,
        "o": 4.5,
        "i": 6.3,
        "g": 2.8,
        "s": 4.8,
        "f": 1.6,
    },
    "b": {
        "a": 7.1,
        "q": 4.1,
        "i": 1.6,
        "y": 2.8,
        "j": 10.4,
        "p": 5.7,
        "n": 5.6,
        "z": 7.4,
    },
    "c": {"w": 9.7},
    "d": {"r": 1.7, "k": 1.5},
    "e": {"s": 3.5, "a": 3.5},
    "f": {"a": 1.6, "b": 8.6, "c": 8.6, "l": 5.3, "x": 6.1, "s": 4.3, "r": 3.6},
    "g": {"a": 2.8, "b": 6.3, "c": 4.0, "hub": 8.6},
    "h": {"a": 4.8, "b": 5.3, "c": 11.1, "x": 9.5},
    "i": {
        "e": 1.5,
        "b": 6.3,
        "y": 3.2,
        "j": 9.4,
        "p": 6.7,
        "n": 3.7,
        "c": 7.3,
        "o": 4.0,
        "g": 9.3,
    },
    "j": {"a": 7.3, "b": 10.4, "c": 1.0, "p": 8.1, "n": 5.2, "z": 6.8},
    "k": {"n": 2.6, "o": 2.9, "i": 1.1, "g": 4.8},
    "l": {"h": 7.7, "x": 9.5},
    "m": {"g": 1.6, "f": 4.2, "l": 7.3, "o": 1.5},
    "n": {"r": 2.2, "m": 1.3, "p": 6.4, "z": 8.8},
    "o": {"i": 4.0, "f": 5.8, "x": 5.9, "s": 6.4, "l": 6.6, "g": 3.4},
    "p": {"a": 7.4, "b": 5.7, "c": 7.2, "z": 13.6, "l": 7.2},
    "q": {"a": 6.0, "b": 4.1, "d": 0.5, "m": 3.2, "z": 5.2, "t": 3.0},
    "r": {"o": 2.2, "e": 1.1, "x": 5.6, "l": 5.4, "s": 4.4},
    "s": {"y": 1.8, "l": 1.0, "k": 3.7, "o": 6.4, "i": 4.1, "g": 6.7},
    "t": {"b": 3.3, "u": 2.0},
    "u": {"a": 10.9, "b": 5.0, "c": 7.4},
    "v": {"x": 1.7, "c": 6.1},
    "w": {"p": 7.5, "j": 0.4},
    "x": {"z": 1.3, "a": 10.0, "b": 6.1, "c": 6.4, "h": 9.5, "hub": 2.4},
    "y": {"a": 4.4, "b": 2.8, "c": 10.1},
    "z": {"a": 13.0, "b": 7.4, "c": 10.1, "hub": 3.6},
}

# The next thing we need to do is determine which trucks the packages need to
# go into based on the time they are due. This will move us to the Trucks.py file
