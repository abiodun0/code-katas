
# print transpose_rows([[1,2,3,4],
#                       [2,3,1,3],
#                       [3,1,2,3]])`
# This should return `[[1,2,3],
#                       [2,3,1],
#                       [3,1,2],[4,3,3]```
# (edited)

# [1:44]
#  ```print transpose_rows([['cricket', 'football', 'tennis'], ['golf']])
# This should return `[['cricket',golf'],
#                       ['football'],
#                       ['golf']

def invertedMatrix(input_array):
    # check for the hieght and the width of the array
    w = len(input_array)
    h = len(input_array[0])

    # build a matrix from the result
    # result = [['not_needed' for x in range(w)] for x in range(h)]
    result = []
    #loop through the outer array
    for i in range(h):
        #loop through the inner array
        result.insert(i,[])
        for j in range(w):
            try:
                #assign the inverse of the input array to the new array -> the meat of the algorithm
                result[i].insert(j,input_array[j][i])
            except IndexError:
                pass
        # Clear unused indexes after the assignment of a partciular row
        # result[i] = [j for j in result[i] if j != 'not_needed']
    #Return the results after the loop
    return result

print(invertedMatrix([[1,2,3,4],[2,3,1,3],[3,1,2,3]]));
print(invertedMatrix([['cricket', 'football', 'tennis'], ['golf']]))