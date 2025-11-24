#Pascal's Triangle problem with the recursive method.
#Pascal's Triangle is recursively defined by a simple rule: each number in the triangle is the sum of the two numbers directly above it.
def pascal(row,col):
   if (col == 1):return 1
   if (row == col):return 1
   #we use the recursive method
   return pascal(row - 1, col - 1) + pascal(row - 1, col)

rows = int(sys.argv[1])
for r in range(1, rows + 1):
 print(" ")
 for c in range (1, r+1):
     value = pascal(r,c)
     print (value, end = " ")
 print(" ")
