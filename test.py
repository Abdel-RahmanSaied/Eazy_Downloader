# def getRow(rowIndex):
#     currow = []
#
#     # 1st element of every row is 1
#     currow.append(1)
#
#     # Check if the row that has to
#     # be returned is the first row
#     if (rowIndex == 0):
#         return currow
#
#     # Generate the previous row
#     prev = getRow(rowIndex - 1)
#
#     for i in range(1, len(prev)):
#         # Generate the elements
#         # of the current row
#         # by the help of the
#         # previous row
#         curr = prev[i - 1] + prev[i]
#         currow.append(curr)
#     currow.append(1)
#     # Return the row
#     return currow
# n = 4
# arr = getRow(n)
# print(arr)
# # for i in range(len(arr)):
# #
# #     if (i == (len(arr) - 1)):
# #         print(arr[i])
# #     else:
# #         print(arr[i], end=", ")


# def StockPicker(arr):
#     cost = 0
#     maxcost = 0
#
#     mini = arr[0]
#     for i in range(len(arr)):
#         mini = min(mini, arr[i])
#         cost = arr[i] - mini
#         maxcost = max(maxcost, cost)
#     return maxcost
#
# print(StockPicker([14,20,4,12,5,11]))
#     # n = len(price);
#     #
#     # print(maxProfit(price, 0, n - 1));


# def MaximalSquare(strArr):
#     l = list([[int(x) for x in s] for s in strArr])
#     row = len(strArr)
#     col = len(strArr[0])
#     F = min(row, col)
#
#     for f in range(F, 0, -1):  # descending searching
#         for i in range(0, row - f + 1):  # from row to row (filter goes from upper to bottom)
#             # if f == row, do this for loop only once
#             # i is the row index of the matrix
#             for j in range(0, col - f + 1):  # from column to column (filter goes from left to right)
#                 # if f == col, do this loop only once
#                 # j is the column index of the matrix
#                 # strArr[i][j] is the upper left corner of the submatrix
#                 multiply = 1
#
#                 # l[m][n] is the elements of the submatrix
#                 for m in range(i, f + i):
#                     for n in range(j, f + j):
#                         multiply *= l[m][n]
#                 ## after all the multiply operator:
#                 if multiply == 1:
#                     return f * f
#     return 0
#
# input = ["1011", "0011", "0111", "1111"]
# print(MaximalSquare(input))


# class Solution():
# class Solution:
def maximalRectangle( matrix:list) -> int:
    def getMaxAreaHisto(histogram):
        n = len(histogram)
        left_lim = [0]*n
        right_lim = [0]*n
        left_lim[0] = -1
        right_lim[n-1] = n
        max_histo_area = 0

        for i in range(1, n):
            pointer = i-1
            while (pointer >= 0) and (histogram[pointer] >= histogram[i]):
                pointer = left_lim[pointer]
            left_lim[i] = pointer

        for i in range(n-2, -1, -1):
            pointer = i+1
            while (pointer < n) and (histogram[pointer] >= histogram[i]):
                pointer = right_lim[pointer]
            right_lim[i] = pointer

        for i in range(n):
            height = histogram[i]
            width = right_lim[i] - left_lim[i] - 1
            max_histo_area = max(max_histo_area, height*width)

        return max_histo_area

    def getHistoArea(rows):
        cols = len(rows[0])
        histogram = [0]*cols
        for row in rows:
            for col in range(cols):
                histogram[col] = 0 if row[col] == '0' else (
                    1 + histogram[col])
        return getMaxAreaHisto(histogram)

    max_area = 0
    rows = len(matrix)
    if rows < 1:
        return 0

    for r in range(rows):
        max_area = max(max_area, getHistoArea(matrix[:r+1]))
    return max_area


print(maximalRectangle(["101", "111", "001"]))