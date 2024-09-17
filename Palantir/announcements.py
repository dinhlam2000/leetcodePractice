'''

A company has n employees with a unique ID for each employee from 0 to n - 1.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee. If manager[i] is -1, then the i-th employee is has no manager, and is the root manager of the company. Also, it is guaranteed that the subordination relationships have a single tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Write a function to calculate the number of minutes needed to inform all the employees about the urgent news.


n employees, 0 -> n - 1 (index each employee)

Employee --> Direct Manager 
employeeIth --> directManager[i] only if != -1

ManagerArray = [] --> can only have one -1 and that's the root --> CEO

Head --> CEO --> Employee with no manager --> Employeeith --> DirectManager[ith] == -1 

Employee requires time[i] mins to spread the news 

Sub-informing can only be done when the parent is done

==============================================================================================================

Sample Input 1:
n = 6, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Sample Output 1:
1
Explanation: 
Employee #2 is the manager of all other employees, and it takes him 1 minute to inform all of his subordinates. Therefore, the answer is 1. 

Sample Input 2:
n = 5, manager = [1,3,1,-1,2], informTime = [0, 2, 3, 6, 0]
Sample Output 2:
11
Explanation:
Employee #3 takes 6 minutes to inform employee employee #1, and employee #1 takes 2 minutes to inform employee #0 and #2, and employee #2 takes 3 minutes to inform employee #4. Therefore, the total minutes needed to inform all employees is 11. 


# no cycle graph

1st --> BUild a tree that basically expresses this relationship
Node:
 index: --> find inFormtimeArray[index]
 children --> [Node,Node]
 
2nd --> Once tree constructed

Find the root Node --> and start traversing through each children, each node
start adding the minutes and keep traversing if there are more children

BFS(node):
  --> queue
    chilren
    
n = 6, managers = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]

'''""

# class Node:
#     def __init__(self,children,index):
#         self.children = children
#         self.index = index

# assume valid inputs for now
def findTotalTime(n, managers, informTime):
    indexManager = 0
    managerMap = {}
    for index, man in enumerate(managers):

        if man == -1:
            indexManager = index
            # managerMap[indexManager]
        else:
            if man not in managerMap:
                managerMap[man] = [index]
            else:
                managerMap[man].append(index)
    # print(managerMap)
    print(managerMap)
    return dfs(indexManager, managerMap, informTime)

def dfs(index, managerMap, informTime):
    # print(result)
    # print('traversing', index)
    if index in managerMap:
        children = managerMap[index]
    else:
        children = []
    # no children
    if children == []:
        return informTime[index]
    # 2 --> [0,1,3,4,5] --> children
    #   -> each child --> they have children --> adding the minute
    #.                --> no children. --> return 0
    """
    3(6)
1(2)
0 2(3)
    4   
    """
    # 1 -> [3]
    # 2 --> time = 1 minute
    childrenValue = []

    for child in children:
        # no children
        # print('child =', child, informTime, 'index=',index)
        # print('result', result)
        # print('index', index)
        # if dfs(child, managerMap, informTime, result):
        childrenValue.append(dfs(child,managerMap, informTime))

    return informTime[index] + max(childrenValue)
    # taking in the time of each node that needs to announce
    # max() ??
    # return True


#    n = 5, manager = [1,3,1,-1,2], informTime = [0, 2, 3, 6, 0]
print(findTotalTime(6, [2,2,-1,2,2,2], [0,0,1,0,0,0]))
print(findTotalTime(5, [1,3,1,-1,2], [0, 2, 3, 6, 0]))
print(findTotalTime(7, [1,2,3,4,5,6,-1], [0, 6, 5, 4, 3, 2, 1]))








    # mapping:
    # managerIndex : [indexelement]
    # 2 -> [0,1,3,4,5]
    #
    # 1st --> manager[2]
    # 2nd --> manager[2]

    # step 1 --> construct the tree by adding to this rootNode


