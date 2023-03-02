import math
import time

'''
The ArrayList class simulates a fixed array in Python, ala ArrayList in Java.
Here we specify a growth function when we create the ArrayList.
You may not modify any of the code here, but you may add additional code that does not affect the functioning of this code.
'''


class ArrayList:
    def __init__(self, growfn):
        '''Initializes the empty ArrayList with the specified growth function.'''
        self.size = 0;
        self.used = 0;
        self.array = []
        self.grow = growfn;

    def get(self, index):
        if index < self.size:
            return self.array[index]
        # exception handling
        return None

    def add(self, value):
        if self.used == self.size:
            newSize = self.grow(self.size)
            if newSize <= self.size:
                # exception handling
                return
            newArray = self.array[:] + [None for i in range(self.size, newSize)]
            self.array = newArray
            self.size = newSize
        self.array[self.used] = value
        self.used = self.used + 1
        return None

    def is_called(self):
        if self.used == self.size:
            return True
        else:
            return False


'''
Growth Functions
Here is the basic growth function.
You should add those from the assignment afterwards.
'''


def double(size):
    if size == 0:
        return 1
    return size + size


'''
Additional growth functions for the solution.
Three that were included in the assignment.
'''


def addsqrt(size):
    if size == 0:
        return 1
    return size + math.ceil(math.sqrt(size))


def addlog(size):
    if size == 0:
        return 2
    return size + math.ceil(math.log(10, size))


def nplus100(size):
    if size == 0:
        return 100
    return size + 100


def addhalf(size):
    if size == 0:
        return 1
    return size + (math.ceil(size / 2))


def doublehalf(size):
    if size == 0:
        return 1
    return size + (size + (math.ceil(size / 2)))


'''
The analyzePerformance function accepts three parameters:
* a list of N values for which results should be returned.
* a growth function that returns the new size of the array given the old size.
* the number of tries used to average the time.
The analyzePerformance function returns a list of values, one for each value of N.  
Each of the  values in the list is a dictionary {"grow": ..., "N":..., "seconds":..., "sizes":...} containing:
* the growth function 
* the value of N
* the decimal number of seconds required to add N elements to a new Array averaged over the specified number of tries.
* the list of sizes the array grows through while adding the N elements
Do not include the creation of the initial ArrayList object in the time.
'''


def analyzePerformance(nList, gfn, tries):
    data = []
    for i in nList:
        timerData = []
        for n in range(tries):
            tempArr = []
            listDict = dict(grow=gfn, N=0, seconds=0, sizes=[])
            listDict['N'] = i
            # Create fancy list
            array = ArrayList(gfn)

            # Start Timer
            start = time.perf_counter()

            # Loop though nList
            for j in range(0, i):
                array.add(j)
                if array.is_called():
                    tempArr.append(array.size)
            if tempArr[-1] != array.size:
                tempArr.append(array.size)

            # Stop Timer
            finish = time.perf_counter()

            # Calculate time taken and add to 'seconds' list
            timeTaken = finish - start
            timerData.append(timeTaken)
            averageTime = sum(timerData) / tries
            listDict['seconds'] = averageTime

        # Add grow sizes to list and return data
        listDict['sizes'] = tempArr
        data.append(listDict)
    return data


'''
Here is a sample main program for your testing purposes.
We will use a different main program to call your analyze function with various lists and growth functions of our choice.
You might graphs the values returned for the various functions to compare their actual versus expected behavior.
'''


def main():
    for resultDouble in analyzePerformance([10, 100], double, 13):
        print(resultDouble)
    # for resultSquareRoot in analyzePerformance([10, 100], addsqrt, 13):
    #     print(resultSquareRoot)
    # for resultSquareRootLogN in analyzePerformance([10, 100], addlog, 13):
    #     print(resultSquareRootLogN)
    # for resultNPlus100 in analyzePerformance([1000], nplus100, 13):
    #     print(resultNPlus100)
    # for resultHalf in analyzePerformance([10, 100], addhalf, 13):
    #     print(resultHalf)
    # for resultDoubleHalf in analyzePerformance([10, 100], doublehalf, 13):
    #     print(resultDoubleHalf)


if __name__ == '__main__':
    main()
