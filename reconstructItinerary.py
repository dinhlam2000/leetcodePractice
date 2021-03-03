#have a map for the ticket [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#map should be like "JFK" : [destination,destination] destination should be in lexiorder
#have a stack and push the destination to the stack when you reach a deadend or when you use up is emptycldear
#the stack will contain the order backward

def findItinerary(tickets):
    airlineTicket = {}
    stack = []

    tickets.sort(key=lambda x: x[1])

    for value in tickets:
        if value[0] not in airlineTicket:
            airlineTicket[value[0]] = [value[1]]
        else:
            airlineTicket[value[0]].append(value[1])

    result = []
    def findPath(startPoint):
        while startPoint in airlineTicket and airlineTicket[startPoint] != []:
            destination = airlineTicket[startPoint].pop(0)
            findPath(destination)
        result.append(startPoint)
    findPath("JFK")

    return reversed(result)

if __name__ == "__main__":

    flights = [["JFK","C"],["C","JFK"],["JFK","B"]]
    import pdb; pdb.set_trace()
    a = findItinerary(flights)
    print(a)