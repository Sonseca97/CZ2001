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
    return "No such route"


if __name__ == '__main__':

    flight_10 = {
    'Amsterdam': ['Barcelona', 'London', 'Munich'],
    'Barcelona': ['Amsterdam', 'Istanbul', 'London'],
    'Berlin': ['Geneva', 'Munich', 'Warsaw','London'],
    'Geneva': ['Berlin', 'Vienna','Glasgow'],
    'Glasgow': ['Geneva', 'London'],
    'Munich': ['Amsterdam', 'Berlin'],
    'Istanbul': ['Barcelona'],
    'London': ['Amsterdam', 'Barcelona', 'Berlin', 'Glasgow'],
    'Warsaw': ['Berlin'],
    'Vienna': ['Geneva'],
    }

    flight_15 = {
    'Amsterdam': ['Barcelona', 'London', 'Munich', 'Groningen'],
    'Barcelona': ['Amsterdam', 'Istanbul', 'London'],
    'Berlin': ['Geneva', 'Munich', 'Warsaw','London'],
    'Geneva': ['Berlin', 'Vienna','Glasgow', 'Milan'],
    'Glasgow': ['Geneva', 'London','Zurich'],
    'Munich': ['Amsterdam', 'Berlin', 'Hamburg'],
    'Istanbul': ['Barcelona'],
    'London': ['Amsterdam', 'Barcelona', 'Berlin', 'Glasgow'],
    'Warsaw': ['Berlin', 'Prague'],
    'Vienna': ['Geneva', 'Prague'],
    'Groningen': ['Amsterdam','Hamburg'],
    'Hamburg': ['Groningen', 'Munich'],
    'Zurich': ['Glasgow', 'Milan'],
    'Milan': ['Geneva', 'Zurich'],
    'Prague': ['Warsaw', 'Vienna']
    }

    flight_20 = {
    'Amsterdam': ['Barcelona', 'London', 'Munich', 'Groningen', 'Beijing'],
    'Barcelona': ['Amsterdam', 'Istanbul', 'London'],
    'Berlin': ['Geneva', 'Munich', 'Warsaw','London'],
    'Geneva': ['Berlin', 'Vienna','Glasgow', 'Milan'],
    'Glasgow': ['Geneva', 'London','Zurich'],
    'Munich': ['Amsterdam', 'Berlin', 'Hamburg'],
    'Istanbul': ['Barcelona'],
    'London': ['Amsterdam', 'Barcelona', 'Berlin', 'Glasgow','Singapore'],
    'Warsaw': ['Berlin', 'Prague'],
    'Vienna': ['Geneva', 'Prague'],
    'Groningen': ['Amsterdam','Hamburg'],
    'Hamburg': ['Groningen', 'Munich'],
    'Zurich': ['Glasgow', 'Milan'],
    'Milan': ['Geneva', 'Zurich'],
    'Prague': ['Warsaw', 'Vienna'],
    'Singapore': ['London', 'Bali', 'Bangkok', 'Beijing'],
    'Beijing': ['Amsterdam', 'Singapore'],
    'Bali': ['Singapore', 'Hanoi', 'Bangkok'],
    'Bangkok': ['Singapore', 'Bali', 'Hanoi'],
    'Hanoi': ['Bali', 'Bangkok']
    }
    departure = (input("where is your departure city?")).capitalize()
    arrival = (input("where is your arrival city?")).capitalize()
    #print(time.time())
    #print(bfs_shortest(flight_20, departure, arrival))
    #print(time.time())
    
     if (departure and arrival in flight_10) == True :
        print('You can take flight_10 and the shortest path is as follows:')
        print(bfs_shortest(flight_10, departure, arrival))
        print('flight_10 Running Time:',time.time())   
    else:
        print('No route in flight_10')
        
        
    if (departure and arrival in flight_15) == True :
        print('\n')
        print('You can take flight_15 and the shortest path is as follows:')
        print(bfs_shortest(flight_15, departure, arrival))
        print('flight_15 Running Time:', time.time())   
    else:
        print('No route in flight_15')
        
    
    if (departure and arrival in flight_20) == True :
        print('\n')
        print('You can take flight_20 and the shortest path is as follows:')
        print(bfs_shortest(flight_20, departure, arrival))
        print('Flight_20 Running Time',time.time())
    else:
        print('No route in flight_20')
    
