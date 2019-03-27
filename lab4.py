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
    flight = {
    'Amsterdam': ['Barcelona', 'London', 'Munich', 'Paris'],
    'Barcelona': ['Amsterdam', 'Istanbul', 'London', 'Paris'],
    'Berlin': ['Geneva', 'Munich', 'Warsaw'],
    'Geneva': ['Berlin', 'Vienna'],
    'Glasgow': ['Groningen', 'London'],
    'Groningen': ['Glasgow', 'London'],
    'Hamburg': ['Munich', 'Warsaw'],
    'Istanbul': ['Barcelona', 'London', 'Paris', 'Warsaw'],
    'London': ['Amsterdam', 'Barcelona', 'Berlin', 'Glasgow', 'Groningen'],
    'Munich': ['Amsterdam', 'Berlin', 'Hamburg', 'Vienna'],
    'Paris': ['Amsterdam', 'Barcelona', 'Istanbul'],
    'Vienna': ['Geneva', 'Munich'],
    'Warsaw': ['Berlin', 'Hamburg', 'Istanbul']
    }
    start = input("where are you from? ")
    destination = input("where are you going? ")
    print(bfs_shortest(flight, start, destination))


