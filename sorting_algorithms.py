########################################
#GUI for Sorting Algorithm Visualizer  #
#File to hold all of the sorting       #
#algorithm classes                     #
#Author: Macinto5h                     #
########################################
import math

class Sort:
    def sort(self, Application, list):
        print("ERROR: Superclass sort method invoked, must override")
    # def __init__(self,Application):
        # self.sort(Application, Application.array)
#todo: BeadSort
#todo: BinaryTreeSort
#todo: BitonicSorter
#todo: BlockSort
#todo: BucketSort
#todo: BurstSort

class BubbleSort(Sort):
    def sort(self, Application, list):
        length = len(list)
        for index_0 in range(length):
            for index_1 in range(length-1,index_0,-1):
                if (list[index_1-1] > list[index_1]):
                    temp = list[index_1]
                    list[index_1] = list[index_1-1]
                    Application.update_canvas(temp,list[index_1],index_1)
                    list[index_1-1] = temp
                    Application.update_canvas(list[index_1],list[index_1-1],index_1-1)

class CocktailSort(Sort):
    def sort(self, Application, list):
        swapped = True
        while (swapped == True):
            swapped = False
            for i in range(len(list)-2):
                if (list[i] > list[i+1]):
                    temp = list[i]
                    list[i] = list[i+1]
                    Application.update_canvas(temp,list[i],i)
                    list[i+1] = temp
                    Application.update_canvas(list[i],list[i+1],i+1)
                    swapped = True
            if (swapped == False):
                break
            for i in range(len(list)-2,0,-1):
                if (list[i] > list[i+1]):
                    temp = list[i]
                    list[i] = list[i+1]
                    Application.update_canvas(temp,list[i],i)
                    list[i+1] = temp
                    Application.update_canvas(list[i],list[i+1],i+1)
                    swapped = True
#todo: CombSort
#todo: CountingSort
#todo: CubeSort
#todo: CycleSort
#todo: FlashSort
#todo: FranceschinisMethods
class GnomeSort(Sort):
    def sort(self, Application, list):
        index = 0
        while (index < len(list)):
            if (index == 0 or list[index] >= list[index-1]):
                index += 1
            else:
                temp = list[index]
                list[index] = list[index-1]
                Application.update_canvas(temp,list[index],index)
                list[index-1] = temp
                Application.update_canvas(list[index],list[index-1],index-1)
                index -= 1
#todo: Heapsort
#TODO: InPlaceMergeSort
class InsertionSort(Sort):
    def sort(self, Application, list):
        length = len(list)
        for index in range(1, length):
            k = list[index]
            i = index-1
            while(i >= 0 and list[i]>k):
                old_value = list[i+1]
                new_value = list[i]
                list[i+1]=list[i]
                Application.update_canvas(old_value,new_value,i+1)
                i = i - 1
            old_value = list[i+1]
            list[i+1] = k
            Application.update_canvas(old_value,k,i+1)
#todo: IntroSort
#todo: LibrarySort
class MergeSort(Sort):
    def merge(self, Application, list, p, q, r):
        left_length = q-p+1
        right_length = r-q
        l = 0
        ri = 0
        left_list = []
        right_list = []
        for index in range(p, q+1, 1):
            left_list.append(list[index])
        for index in range(q+1, r+1, 1):
            right_list.append(list[index])
        for index in range(p, r+1, 1):
            old_value = list[index]
            if (l == left_length):
                list[index] = right_list[ri]
                ri += 1
            elif (ri == right_length or left_list[l]<=right_list[ri]):
                list[index] = left_list[l]
                l += 1
            else:
                list[index] = right_list[ri]
                ri += 1
            Application.update_canvas(old_value,list[index],index)
    def merge_sort(self, Application, list, p, r):
        if (p < r):
            q = (p+r)//2
            self.merge_sort(Application, list, p, q)
            self.merge_sort(Application, list, q+1, r)
            self.merge(Application,list,p,q,r)

    def sort(self, Application, list):
        self.merge_sort(Application, list, 0, len(list)-1)
#todo: OddEvenSort
#todo: PostmanSort
#todo: Quicksort
#class QuickSort:
    #def sort(self, Application, list):
    #add stuff here
    #def __init__(self,Application):
#todo: PatienceSorting
#todo: PigeonholeSort
class RadixSortLSD(Sort):
    def sort(self,Application,list):
        maxValue = max(list)
        i = 0
        #10 is the base value since values of the list are in decimal
        while 10 ** i <= maxValue:
            list = self.buckets_to_list(self.list_to_buckets(list,i),Application,list)
            i += 1

    def list_to_buckets(self,array,iteration):
        buckets = [[] for x in range(10)]
        for i in array:
            digit = (i // (10 ** iteration)) % 10
            buckets[digit].append(i)
        return buckets

    def buckets_to_list(self,buckets,Application,list):
        numbers = []
        index = 0
        for bucket in buckets:
            for j in bucket:
                numbers.append(j)
                Application.update_canvas(list[index],j,index)
                index += 1
        return numbers
#todo: RadixSortMSD
class SelectionSort(Sort):
    def sort(self, Application, list):
        length = len(list)
        for i in range(length):
            m = list[i] #smallest value variable
            j = i + 1
            swap_index = i
            while (j < length):
                if (list[j] < m):
                    m = list[j]
                    swap_index = j
                j += 1
            Application.update_canvas(list[swap_index],list[i],swap_index)
            list[swap_index] = list[i]
            Application.update_canvas(list[i], m, i)
            list[i] = m
class ShellSort(Sort):
    def sort(self, Application, list):
        gap = len(list)//2
        while (gap > 0):
            for i in range(gap,len(list)):
                temp = list[i]
                j = i
                while j >= gap and list[j-gap] > temp:
                    Application.update_canvas(list[j],list[j-gap],j)
                    list[j] = list[j-gap]
                    j -= gap
                Application.update_canvas(list[j],temp,j)
                list[j] = temp
            gap //= 2
#todo: SimplePancakeSort
#todo: SmoothSort
#todo: SortingNetwork
#todo: SpaghettiSort
#todo: SpreadSort
#todo: StoogeSort
class StoogeSort(Sort):
    def sort(self, Application, list):
        self.stoogeSortHelper(Application, list, 0, len(list) - 1)

    def stoogeSortHelper(self, Application, list, i, j):
        if (list[i] > list[j]):
            tmp = list[i]
            Application.update_canvas(list[i],list[j],i)
            list[i] = list[j]
            Application.update_canvas(list[j],tmp,j)
            list[j] = tmp
        
        if ((j - i + 1) > 2):
            # t = -(-(j - i + 1) // 3) 
            t = (j - i + 1) // 3
            self.stoogeSortHelper(Application, list, i, j - t)
            self.stoogeSortHelper(Application, list, i + t, j)
            self.stoogeSortHelper(Application, list, i, j - t)   
#todo: StrandSort
#todo: TimSort
#todo: TournamentSort
#todo: UnShuffleSort