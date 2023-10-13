print("JAYAMOL REMESAN")
print("--SJC22MCA-2031--")
print("--20MCA241--DATA SCIENCE LAB--")
print("**************************************************")

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]


if len(list1) == len(list2):

    result = []


    for i in range(len(list1)):
        sum_element = list1[i] + list2[i]
        result.append(sum_element)

    print("Resultant list after adding elements:", result)
else:
    print("Lists are of different lengths. Cannot perform element-wise addition.")