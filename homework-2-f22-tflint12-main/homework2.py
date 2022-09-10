def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats

    # Write your code here

    temp = 0
    if b == h:
        print("b and h are the same value")
        hist = [0]
        return hist

    if b > h:
        temp = b
        b = h
        h = temp

    if n == 0:
        hist = [0]
        return hist

    w = (h-b) / n

    hist = [0] * n

    i = 0
    k = 0
    while i != len(hist):
        bin_bottom = b + i * w
        bin_top = b + (i + 1) * w
        for k in range(0, len(data), 1):
            if b < data[k] < h:
                if data.index(data[k]) == k:
                    if bin_bottom <= data[k] < bin_top:
                        hist[i] += 1
        i += 1

    return hist
    # return the variable storing the histogram
    # Output should be a list

    pass


def happybirthday(name_to_day, name_to_month, name_to_year):
    #name_to_day, name_to_month and name_to_year are dictionaries
    
    # Write your code here

    # return the variable storing date_to_all
    # Output should be a dictionary
    
    pass

