from collections import deque

def requests_in_queue(wait):
    n = len(wait)
    queue = deque(wait)  # queue stores the waiting times
    time = 0
    result = []
    
    while queue:
        # Add the current number of requests in the queue
        result.append(len(queue))

        queue.popleft()
        
        # Increment the time
        time += 1

        # Process the first request in the queue (FIFO)
        
        # After processing, remove any expired requests (those whose time <= current time)
        queue = deque([w for w in queue if w > time])
    
    # Add the final state when the queue becomes empty
    result.append(0)
    
    return result



wait = [3, 4, 2, 1]
wait2 = [2,2,3,1]
print(requests_in_queue(wait))  # Output: [4, 2, 0]
print(requests_in_queue(wait2))  # Output: [4, 2, 1, 0]
print(requests_in_queue( [2,2,3,1,1,1,5,3,3,10,7]))
print(requests_in_queue([3,1,2,1])) # 4, 1 ,0



