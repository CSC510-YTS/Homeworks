--- original/./HW2/hw2_debugging.py
+++ fixed/./HW2/hw2_debugging.py
@@ -1,12 +1,14 @@
 import rand
+
 
 def mergeSort(arr):
     if (len(arr) == 1):
         return arr
 
-    half = len(arr)//2
+    half = len(arr) // 2
 
     return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))
+
 
 def recombine(leftArr, rightArr):
     leftIndex = 0
@@ -22,15 +24,14 @@
 
     for i in range(rightIndex, len(rightArr)):
         mergeArr[leftIndex + rightIndex] = rightArr[i]
-    
+
     for i in range(leftIndex, len(leftArr)):
         mergeArr[leftIndex + rightIndex] = leftArr[i]
 
     return mergeArr
 
+
 arr = rand.random_array([None] * 20)
 arr_out = mergeSort(arr)
 
 print(arr_out)
-
-
