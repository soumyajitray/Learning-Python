import math

class solution(object):

    # def combination(self,n, r):
    #     return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

    def pascals_trianglecombined(self, rows):
        # result = []
        # for count in range(rows):
        #     row = []
        row = []
        for element in range(rows + 1):

            combination = int(
                (math.factorial(rows)) / ((math.factorial(element)) * math.factorial(rows - element)))
            row.append(combination)
        print(row)

        return row

obj = solution()
obj.pascals_trianglecombined(5)