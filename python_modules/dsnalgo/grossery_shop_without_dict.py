def get_number_of_buckets(item_list, strength):
    total = 0
    
    sorted_item_list = sorted(item_list)
    print sorted_item_list
    for index, item in enumerate(sorted_item_list):
        x=1
        print index, item
        if sorted_item_list[index] == sorted_item_list[index+1]:
           x=x+1


total = get_number_of_buckets(["a", 'b', 'c', "d", "a", "b"], 1)

