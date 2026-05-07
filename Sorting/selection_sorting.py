'''Sorting techniques in a single class'''



from typing import List
from datetime import datetime


ls = [8,3,6,4,7,3,2,5]


class Sorting:
    def selection_sort(self,ls : List):
        for i in range(len(ls)):
            min_index =i
            for j in range(i,len(ls)):
                # print(2)
                if(ls[j]<ls[min_index]):
                    min_index = j
            ls[min_index],ls[i] = ls[i],ls[min_index]
        return ls
    def bubble_sort(self,ls:List):
        for i in range(len(ls)):
            for j in range(len(ls)-i-1):
                if(ls[j]>ls[j+1]):
                    ls[j],ls[j+1] = ls[j+1],ls[j]
        return ls
    def insertion_sort(self,ls:List[int]) ->List[int]:
        # for i in range(1,len(ls)):
        #     for j in range(i,0,-1):
        #         if(ls[j] <ls[j-1]):
        #             ls[j-1],ls[j] = ls[j],ls[j-1]
        #         else:
        #             break

        for i in range(len(ls)):
            k=i-1
            key=ls[i]

            while(key<ls[k] and k >=0):
                ls[k],ls[k+1] = ls[k+1],ls[k]
                k -=1
        return ls















s = Sorting()
print(s.selection_sort(ls))
print(s.bubble_sort(ls))
print(s.insertion_sort(ls))
# t1  = datetime.now().time()
# t2 = datetime.now().time()
# print(t1)