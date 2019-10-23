from Basic_data_structures.Stack import stack


def par_checker(symbol_string):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    print("top:", open)
    print("symbol: ", close)
    opens = "([{"
    closes = ")]}"
    print("Top index: ", opens.index(open))
    print("Symbol index: ", closes.index(close))
    print("**********************************")

    return opens.index(open) == closes.index(close)


print("\n\nFIRST")
print("Is {{([][])}()} balanced? : ", par_checker('{{([][])}()}'))
print("\n\nSECOND")
print("Is [{()] balanced? : ", par_checker('[{()]'))
