if __name__ == '__main__':

    def sub_lists (l):
        lists = [[]]
        for i in range(len(l) + 1):
            for j in range(i):
                lists.append(l[j : i])
        return lists

    l1 = []

    userInput = input("Enter sequence of values: ")

    for input in userInput:
        if input != " ":
            l1.append(input)

    print(sub_lists(l1))

