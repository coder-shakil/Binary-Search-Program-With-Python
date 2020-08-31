def BinarySearch (list1,key):
  low= 0
  high= len(list1)-1
  Found = False
  k = "We Got The Key "

  while low<= high and not Found:
      mid = (low+high)//2
      if key==list1[mid]:
        return k

      elif key > list1[mid]:
        low = mid+1

      else :
        high = mid-1
 
  else : 
      print("We didn't find any key :")

list1 =[15,52,31,41,54]

key = int(input("Enter Your Key :"))
print(BinarySearch(list1,key))
