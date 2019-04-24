class Operaciones():

    def __init__(self):
        pass

    def suma(self, val1, val2):
        return float(val1) + float(val2)

    def resta(self, val1, val2):
        return float(val1) - float(val2)

    def multiplicacion(self, val1, val2):
        return float(val1) * float(val2)

    def division(self, val1, val2):
        return float(val1) / float(val2)

    def signo(self, val):
        return str(float(val)*-1)

    def countingSort(self, arr, exp1):

        n = len(arr)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = (int(arr[i]) / exp1)
            count[(index) % 10] += 1

        # Change count[i] so that count[i] now contains actual
        #  position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

            # Build the output array
        i = n - 1
        while i >= 0:
            index = (int(arr[i]) / exp1)
            output[count[(index) % 10] - 1] = arr[i]
            count[(index) % 10] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

            # Method to do Radix Sort

    def radixSort(self, arr):
        max1 = max(arr)
        exp = 1
        while int(max1) / exp > 0:
            self.countingSort(arr, exp)
            exp *= 10