#Q1
def merge_and_sort(list1, list2):
    
    merged_list = list1 + list2

    
    
    for i in range(len(merged_list)):
        for j in range(0, len(merged_list) - i - 1):
            if merged_list[j] > merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]
    
    return merged_list
list1 = [3, 1, 4]
list2 = [2, 5, 0]
print(merge_and_sort(list1, list2))



#Q2

def repeat_characters(s, n):
    
    result = ''.join([char * n for char in s])
    return result


s = "abc"
n = 3
print(repeat_characters(s, n))  
