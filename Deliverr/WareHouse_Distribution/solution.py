import copy
import pdb; pdb.set_trace()
def find_houses(orders, warehouses, result):
    orders_copy = copy.deepcopy(orders)
    warehouses_copy = copy.deepcopy(warehouses)
    warehouse = []
    if orders_copy and sum(orders_copy.values()) != 0:
        for index, each_warehouse in enumerate(warehouses_copy):
            name = each_warehouse['name']
            inventory = each_warehouse['inventory']
            # check if there's a warehouse that contains all of it first
            if check_everything_inventory(inventory, orders):
                return [{'name': name, 'inventory' : orders}]
            #find all the possible combinations of distributing the warehouses
            else:
                partially_purchased = check_availability(inventory, orders_copy)
                #found some items within that inventory
                if partially_purchased != {}:
                    warehouse.append({'name': name, 'inventory' : partially_purchased})

                #recursively call this method but exluding the current warehouse
                find_houses(orders, warehouses[index+1:], result)

    #do this for all the warehouses
    i = 1
    while i < len(warehouses):
        find_houses(orders, warehouses[0:i] + warehouses[i + 1:], result)
        i += 1

    orders_copy = dict(filter(lambda x: x[1] != 0, orders_copy.items()))
    if warehouse and orders_copy == {} and warehouse not in result:
        result.append(warehouse)




    return result

def check_availability(inventory, items):
    result =[]
    for item, amount in items.items():
        if item in inventory:
            if amount > inventory[item]:
                items[item] = items[item] - inventory[item]
            else:
                items[item] = 0
                inventory[item] = amount
            result.append(item)
    return dict(filter(lambda x: x[0] in result and x[1] != 0 , inventory.items()))


def check_everything_inventory(inventory, items):
    all_item = 0
    for item, amount in items.items():
        if item in inventory:
            if inventory[item] >= amount:
                all_item += 1
                continue
            else:
                return False

    return all_item == len(items)

def helper(orders,warehouses):
    result = find_houses(orders,warehouses,[])
    try:
        minimum_length = min(list(map(lambda x: len(x), result)))
        lowest_length_result = list(filter(lambda x: len(x) == minimum_length, result))
        return lowest_length_result[-1]
    except:
        return []




if __name__== '__main__':
    print('hello')

    input1a, input1b = {'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 1}}]
    # Output: [{owd: {apple: 1}}]

    input2a, input2b = {'apple': 10}, [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
    # Output: [{owd: {apple: 5}}, {dm: {apple: 5}}]

    input3a, input3b = {'apple': 11}, [{'name': 'ad', 'inventory': {'apple': 5}}, {'name': 'b', 'inventory': {'apple': 5}}, {'name': 'c', 'inventory': {'apple': 10}}]
    # Output: [{'name': 'ad', 'inventory': {'apple': 5}}, {'name': 'c', 'inventory': {'apple': 6}}]

    input4a, input4b = {'apple': 23}, [{'name': 'bca', 'inventory': {'apple': 5}}, {'name': 'aa', 'inventory': {'apple': 5}}, {'name': 'sdf', 'inventory': {'apple': 10}}, {'name': 'd', 'inventory': {'apple': 11}}]
    # Output: [{'name': 'bca', 'inventory': {'apple': 5}}, {'name': 'sdf', 'inventory': {'apple': 10}}, {'name': 'd', 'inventory': {'apple': 8}}]

    input5a, input5b = {'apple': 11}, [{'name': 'bca', 'inventory': {'apple': 5}}, {'name': 'aa', 'inventory': {'apple': 5}}, {'name': 'sdf', 'inventory': {'apple': 12}}, {'name': 'd', 'inventory': {'apple': 15}}]
    # Output: [{'name': 'sdf', 'inventory': {'apple': 11}}]

    input6a, input6b = {'apple': 10}, [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 10}}]
    # Output: [{dm: {apple: 10}}]


    #NOT ENOUGH
    # Input: {apple: 1}, [{name: owd, inventory: {apple: 0}}]
    # Output: []
    #
    # Input: {apple: 2}, [{name: owd, inventory: {apple: 1}}]
    # Output: []

    input7a, input7b = {'apple': 5, 'banana': 5, 'orange': 5}, [ { 'name': 'owd', 'inventory': { 'apple': 4, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'apple': 1, 'banana': 5, 'orange': 10 }}]
    # [{'name': 'owd', 'inventory': {'apple': 4, 'orange': 5}}, {'name': 'dm', 'inventory': {'apple': 1, 'banana': 5}}]

    input8a, input8b = {'apple': 10, 'banana': 5, 'orange': 10}, [ { 'name': 'owd', 'inventory': { 'apple': 4, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'apple': 7, 'banana': 5, 'orange': 10 }}, { 'name': 'dxx', 'inventory': { 'apple': 17, 'banana': 15, 'orange': 10 }}]


    result1 = helper(input1a, input1b)
    print(result1)

    result2 = helper(input2a,input2b)
    print(result2)

    result3 = helper(input3a,input3b)
    print(result3)

    result4 = helper(input4a,input4b)
    print(result4)

    result5 = helper(input5a,input5b)
    print(result5)

    result6 = helper(input6a,input6b)
    print(result6)

    result7 = helper(input7a,input7b)
    print(result7)

    result8 = helper(input8a,input8b)
    print(result8)

