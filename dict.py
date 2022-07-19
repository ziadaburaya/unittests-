import numpy
def split_male_female(d: dict) :

    if type(d) is not dict:
        raise TypeError(" split_male_female's parameter must be a dictionary")
        return {}, {}
    male = {}
    female = {}
    for details in d.values():
        if details['sex'] == 'male':
            male[details['name']] = details
        else:
            female[details['name']] = details
    return female, male


def find_median_average(d: dict) :

    if type(d) is not dict:
        raise TypeError("find_median_average's parameter must be a dictionary")
    lst_age = []
    for k in d.keys():
        lst_age.append(d[k]["age"])
    return numpy.mean(lst_age), numpy.median(lst_age)


def print_values_above(d: dict, num: int ) :
    new_lst = []
    for k in d.keys():
        if (d[k]["age"]) > num:
            new_lst.append(d[k]["age"])
    return new_lst


def main():
    data_set = {
        "1232": {"sex": "female", "age": 57, "ID": 17681, "name": "ziad"},
        "21525": {"name": "ahmad", "sex": "male", "age": 22},
        "33212": {"name": "mohamd", "sex": "female", "age": 42},
        "45155": {"name": "osama", "sex": "male", "age": 18}
    }
    female, male = split_male_female(data_set)
    print(female)
    print(male)
    find_median_average(data_set)
    print_values_above(data_set, 6)


main()
