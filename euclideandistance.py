import math  
# Example points in 3-dimensional space...  
x = (5, 6, 7)  
y = (8, 9, 9)  
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))  
print("Euclidean distance from x to y: ",distance) 
- See more at: http://www.w3resource.com/python-exercises/math/python-math-exercise-79.php#sthash.hcOSDm1J.dpuf
