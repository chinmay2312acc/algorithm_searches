list1 = [88,46,25,11,18,12,22]

        
        
def quick_sort(list1) :
    left_list =[]
    mid_list =[]
    right_list =[]
    
    if len(list1)<=1:
        return list1
    else :
        pivot = list1[len(list1)-1]
        
        for i in range(len(list1)) :
            if list1[i] < pivot :
                left_list.append(list1[i])
                
            elif list1[i] > pivot :
                right_list.append(list1[i])
            
            else :
                mid_list.append(list1[i])
            
    
    return quick_sort(left_list) + mid_list+ quick_sort(right_list)
    

print(quick_sort(list1))