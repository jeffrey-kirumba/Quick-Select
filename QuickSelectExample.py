from typing import List

def comparedistance(points: List[List[int]], points1: int, points2: int) -> bool:
    d1 =  points[points1][0] * points[points1][0] + points[points1][1] * points[points1][1] #find distance of first point 
    d2 =  points[points2][0] * points[points2][0] + points[points2][1] * points[points2][1]#find distance of second point
    return d2>d1
    
def swap(points: List[List[int]],index1: int, index2: int) -> List[List[int]]:  #helper function used to swap indexes 
   #s1, s2 = s2, s1
    if(index1 == index2):
        return points
    else:
        points[index1], points[index2] = points[index2], points[index1]
        return points
    
def quickselect(points: List[List[int]], start: int, end: int, K: int):
    if(start >= end): #if the list only has one pair of points
        return
    pivot = start #initialize pivot's index at the start so that each point can be compared 
    i = start
    while i < end: #from start to end
        if (comparedistance(points,i,end) == True): #if the distance of this index is less than the choosen pivot's
            points = swap(points, i, pivot) # swap the points
            pivot+=1
        i+=1     
    points = swap(points, pivot, end) #put the pivot in its index
    maybe_k = pivot - start + 1 # the number of elements on the left half plus the pivot
    if(maybe_k == K): #The Kth number was found, return function
        return 
    if(maybe_k < K):
        return quickselect(points, pivot+1, end, K-(maybe_k)) #recurse the right side
    if(maybe_k > K):
        return quickselect(points, start, pivot-1, K) #recurse the left side

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        end = len(points) - 1 #last index in points
        start =0 #first index in points
        result =[[]] #initialize list of list with no values
        quickselect(points, start, end, K) #call the recursive funciton
        i =0
        while i < K: #loop up until the last Kth number
            result.insert(i,points[i]) #add each index to the result
            i+=1
        result.pop(i) #Pop the last empty index
        return result #Return Kth closest points to the origin

#https://leetcode.com/jeffreykirumba/
#My code was accepted by leetcode
