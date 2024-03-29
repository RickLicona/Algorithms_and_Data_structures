def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list)-1)


def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point-1)
        quick_sort_helper(a_list, split_point+1, last)


def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            print("*******************")
            print("Left: ", left_mark)
            print("Right: ", right_mark)
            left_mark = left_mark + 1
            print("C1")
            print(a_list)

        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            print("*******************")
            print("Right:", right_mark)
            print("C2")
            right_mark = right_mark - 1
            print(a_list)

        if right_mark < left_mark:
            print("*******************")
            print("Left: ", left_mark)
            print("Right: ", right_mark)
            done = True
            print("C3")
            print(a_list)

        else:
            print("*******************")
            print("Left: ", left_mark)
            print("Right: ", right_mark)
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
            print("C4")
            print(a_list)


    print("C5")
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print("\n \nFinal List:", a_list)