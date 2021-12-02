def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True


def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''

     # this tests the condition that is implied by the definition
     # i.e. that m has to be a square matrix
     if(not(is_square(m))): # if matrix is not square
          return False      # return False

     if len(m) < 2 or len(m[0]) < 2:
          return False

     elements = []
     for i in range(len(m)):
          for j in range(len(m[i])):
               elements.append(m[i][j])

     # Check if numbers 1 to len(m)^2 are in square
     for i in range(1, len(m)**2):
          if i not in elements:
               return False
          

     # Check if rows, columns, diagonals all have equal sums

     sumElements = 0
     testSumRows = 0
     testSumCols = 0
     testSumDiag1 = 0
     testSumDiag2 = 0

     # Initialize sum
     for i in range(len(m[0])):
          sumElements += m[0][i]

     # Check sum of rows and columns
     for i in range(len(m)):
          for j in range(len(m[i])):
               testSumRows += m[i][j]
               testSumCols += m[j][i]
               if i == j:
                    testSumDiag1 += m[i][j]
               if i + j == len(m)-1:
                    testSumDiag2 += m[i][j]
          if testSumRows != sumElements or testSumCols != sumElements:
               return False
          testSumCols = 0
          testSumRows = 0
               
     if sumElements != testSumDiag1 or sumElements != testSumDiag2:
         return False
    
     testSumDiag1 = 0
     testSumDiag2 = 0

     return True


