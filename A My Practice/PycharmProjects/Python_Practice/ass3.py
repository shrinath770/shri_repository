class SumToZero:
    def calculate(self,arr):
        result,i = [],0
        while i < (arr.__len__()):
            first = arr[i]
            j = i + 1
            while j < (arr.__len__()):
                second = arr[j]
                k = j + 1
                while k < (arr.__len__()):
                    third = arr[k]
                    if (first + second + third) == 0:
                        result.append([first, second, third])
                    k += 1
                j += 1
            i += 1
        print(result)


#count = int(input('How Many No in Array: '))
#array = [int(input()) for i in range(count)]

array = [-25, -10, -7, -3, 2, 4, 8, 10]
obj1=SumToZero()
print(f'Elements that sum to zero:')
obj1.calculate(array)
