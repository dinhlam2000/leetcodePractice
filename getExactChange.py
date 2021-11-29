def canGetExactChange(targetMoney, denominations):
    # Write your code here

    # denominitaions can it ever contain 1? cannot contain 1
    # unlimited amount of coins in our denominations list?
    # targetMoney ever be negative <---- NO

    # [5,10, 20] --> targetMoney == 200
    import pdb; pdb.set_trace()
    if targetMoney == 0:
        return True
    if targetMoney < 0:
        return False

    for denomination in denominations:
        if canGetExactChange(targetMoney - denomination, denominations):
            return True

    return False



canGetExactChange(75, [4,17,29])

