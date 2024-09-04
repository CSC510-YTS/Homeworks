--- original/./HW2/rand.py
+++ fixed/./HW2/rand.py
@@ -1,8 +1,10 @@
 import subprocess
+
 
 def random_array(arr):
     shuffled_num = None
     for i in range(len(arr)):
-        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True)
+        shuffled_num = subprocess.run(
+            ["shuf", "-i1-20", "-n1"], capture_output=True)
         arr[i] = int(shuffled_num.stdout)
     return arr
--- original/./HW2/rand.py
+++ fixed/./HW2/rand.py
@@ -6,7 +6,7 @@
 
 def random_array(arr):
     """
-    This function is to grenarte a random array 
+    This function is to grenarte a random array
     """
     shuffled_num = None
     for i, _ in enumerate(arr):
