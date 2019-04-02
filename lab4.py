import time

def bfs_shortest(graph, start, destination):
    if(start == destination):
        return "you don't need to take flight!"
    visited = []
    queue = [[start]]
    while(queue):
        path = queue.pop(0)
        vertex = path[-1]
        if vertex not in visited:
            for neighbour in graph[vertex]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if(neighbour == destination):
                    return new_path
            visited.append(vertex)


if __name__ == '__main__':

    flight_10 = {
    'Amsterdam': ['Barcelona', 'London', 'Munich'],
    'Barcelona': ['Amsterdam', 'Istanbul', 'London'],
    'Berlin': ['Geneva', 'Munich', 'Warsaw'],
    'Geneva': ['Berlin', 'Vienna'],
    'Glasgow': ['Groningen', 'London'],
    'Groningen': ['Glasgow', 'London', 'Zurich'],
    'Hamburg': ['Munich', 'Warsaw'],
    'Munich': ['Hamburg', 'Amsterdam', 'Berlin'],
    'Istanbul': ['Barcelona', 'London', 'Warsaw'],
    'London': ['Amsterdam', 'Barcelona', 'Berlin', 'Glasgow', 'Groningen'],
    }

    flight_15 = {
    'Amsterdam': ['Barcelona', 'London', 'Munich', 'Paris'],
    'Barcelona': ['Amsterdam', 'Istanbul', 'London', 'Paris'],
    'Berlin': ['Geneva', 'Munich', 'Warsaw'],
    'Geneva': ['Berlin', 'Vienna'],
    'Glasgow': ['Groningen', 'London'],
    'Groningen': ['Glasgow', 'London', 'Zurich'],
    'Hamburg': ['Munich', 'Warsaw'],
    'Helsinki': ['Zurich'],
    'Istanbul': ['Barcelona', 'London', 'Paris', 'Warsaw'],
    'London': ['Amsterdam', 'Barcelona', 'Berlin', 'Glasgow', 'Groningen'],
    'Munich': ['Amsterdam', 'Berlin', 'Hamburg', 'Vienna'],
    'Paris': ['Amsterdam', 'Barcelona', 'Istanbul'],
    'Vienna': ['Geneva', 'Munich'],
    'Warsaw': ['Berlin', 'Hamburg', 'Istanbul'],
    'Zurich': ['Groningen','Helsinki']
    }

    flight_20 = {
    'Amsterdam': ['Barcelona', 'London', 'Munich', 'Paris', 'Prague'],
    'Barcelona': ['Amsterdam', 'Istanbul', 'London', 'Paris'],
    'Berlin': ['Geneva', 'Munich', 'Warsaw'],
    'Beijing': ['Milan'],
    'Geneva': ['Berlin', 'Vienna'],
    'Glasgow': ['Groningen', 'London'],
    'Groningen': ['Glasgow', 'London', 'Zurich'],
    'Hamburg': ['Munich', 'Warsaw'],
    'Helsinki': ['Zurich'],
    'Istanbul': ['Barcelona', 'London', 'Paris', 'Warsaw'],
    'London': ['Amsterdam', 'Barcelona', 'Berlin', 'Glasgow', 'Groningen', 'Stockholm'],
    'Milan': ['Beijing', 'Paris'],
    'Munich': ['Amsterdam', 'Berlin', 'Hamburg', 'Vienna'],
    'Madrid': ['Paris', 'Zurich'],
    'Paris': ['Amsterdam', 'Barcelona', 'Madrid', 'Milan','Istanbul', 'Stockholm'],
    'Prague': ['Amsterdam', 'Vienna'],
    'Stockholm': ['London', 'Paris'],
    'Vienna': ['Geneva', 'Munich', 'Prague'],
    'Warsaw': ['Berlin', 'Hamburg', 'Istanbul'],
    'Zurich': ['Groningen','Helsinki','Madrid'],
    }
    print(time.time())
    print(bfs_shortest(flight_20, 'Amsterdam', 'Helsinki'))
    print(time.time())
