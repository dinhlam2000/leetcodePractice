#add the courses to a map with weight, where its weight is how many times it was mapped to
#then go through the map and get the heaviest key out and append that key to result
#then delete that key
#then result should contain that

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a map that shows all the prereq that goes from a -> b

        # and therefore, the course b must be taken first before we can take a
        # b can only be taken if there's no prereq to it, meaning it's not in the map
        # or all of the pre reqs have already been taken for b, meaning it's in the map, but there's an
        # empty array for the value ---> array being the value that contains all the pre reqs that it needs to take
        # KEYS == course ---> VALUE === ALL THE PREREQ CLASS for the that course

        # eventually perform a dfs for each course and if there's a cycle return False
        # if we can take all the courses, then ultimately we return True

        mapCourses = {}
        visited = [False] * (numCourses)
        for req in prerequisites:
            classA = req[0]
            classB = req[1]
            if classA not in mapCourses:
                mapCourses[classA] = [classB]
            else:
                mapCourses[classA].append(classB)
        # {1 -> [0]}
        for i in range(numCourses):
            if not (self.canTake(mapCourses, i, visited)):
                return False
        return True

    def canTake(self, mapCourses, course, visited):
        # check the cyclic map
        if course in mapCourses and visited[course] == True:
            return False
        if course not in mapCourses:
            return True

        preReqs = mapCourses.get(course, [])
        visited[course] = True
        for req in preReqs:
            if not self.canTake(mapCourses, req, visited):
                return False
        del mapCourses[course]
        return True
