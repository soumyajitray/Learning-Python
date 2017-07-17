import math

class solution(object):

    def combination(self,n, r):
        return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

    def pascals_triangle(self,rows):
        result=[]
        for count in range(rows):
            row = []
            for element in range(count + 1):
                row.append(self.combination(count, element))
            print(row)

        return result

    def pascals_trianglecombined(self,rows):
        result=[]
        for count in range(rows):
            row = []
            for element in range(count + 1):
                combination=int ((math.factorial(count)) / ((math.factorial(element)) * math.factorial(count - element)))
                row.append(combination)
            print(row)
        result.append(row)
        return result


obj=solution()
obj.pascals_trianglecombined(5)