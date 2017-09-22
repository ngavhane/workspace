
def get_number_of_buckets(item_list, strength):
    total = 0
    item_dict = {}
    for item in item_list:
        if item in item_dict:
            item_dict[item] = item_dict[item] + 1
        else:
            item_dict[item] = 1
    print item_dict
    
    for name, value in item_dict.iteritems():
        if value % strength == 0:
            total = total + value/strength
        else:
            total = total + value/strength + 1
    return total
total = get_number_of_buckets(["a", 'b', 'c', "d", "a", "b"], 1)
print total
