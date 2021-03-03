#just sort the result using the distance formula function

def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:


    result = sorted(points, key=lambda x: (x[0] ** 2 + x[1] ** 2) ** .5)
    return result[0:K]
