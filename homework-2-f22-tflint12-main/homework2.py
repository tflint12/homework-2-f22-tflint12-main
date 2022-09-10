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

    w = (h - b) / n

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
    # name_to_day, name_to_month and name_to_year are dictionaries
    # Write your code here
    date_to_all = {}
    the_age = []
    the_day = []
    the_month = []
    the_year = []
    the_name = []
    tuple_list = []
    for keys in name_to_year.keys():
        the_age.append(2022 - name_to_year[keys])
        the_day.append(name_to_day[keys])
        the_month.append(name_to_month[keys])
        the_year.append(name_to_year[keys])
        the_name.append(keys)

    i = 0
    temp = 0
    for i in range(len(the_day)):
        for j in range(len(the_day)):
            if the_day[i] == the_day[j]:
                if the_age[i] < the_age[j]:
                    temp = the_age[i]
                    the_age[i] = the_age[j]
                    the_age[j] = temp
                    temp = 0
                    temp = the_day[i]
                    the_day[i] = the_day[j]
                    the_day[j] = temp
                    temp = 0
                    temp = the_month[i]
                    the_month[i] = the_month[j]
                    the_month[j] = temp
                    temp = 0
                    temp = the_year[i]
                    the_year[i] = the_year[j]
                    the_year[j] = temp
                    temp = 0
                    temp = the_name[i]
                    the_name[i] = the_name[j]
                    the_name[j] = temp
    i = 0
    for i in range(len(the_year)):
        tuple_list.append((the_name[i], (the_month[i], the_year[i], the_age[i])))

    for i in range(len(the_day)):
        date_to_all[the_day[i]] = tuple_list[i]

    return date_to_all


    # for key in  name_to_day.keys():

    # return the variable storing date_to_all
    # Output should be a dictionary

    # pass
