def char_to_int(value):
        try:
                int(value)
        except ValueError:
                return -1
        else:
                return int(value)


def to_integer(value):
        num = ""

        if char_to_int(value) != -1:
                return int(value)
        elif (value[0] == "+" or value[0] == "-") and char_to_int(value[1]) != -1:
                num = value[0]
                for i in range(1,len(value)):
                        if char_to_int(value[i]) != -1:
                                num += value[i]
                        else: break
                return int(num)
        elif char_to_int(value[0]) != -1:
                for i in value:
                        if char_to_int(i) != -1:
                                num += i
                        else: break
                return int(num)
        else: return 0
