class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        s = 0
        e = len(matrix) - 1
        row = -1
        ##this is for finding row
        ## check last ones to see if in between
        while (s <= e):
            m = int((s+e)/2)
            lastOfRow = matrix[m][-1]
            firstOfRow = matrix[m][0]
            ##if is first row, can't check one before, so smarter to check first and last of row
            ##checking here if equal at the start saves memory because don't have to have the loop or anything in mem later, but is slower than just checking the smart way as in the other file
            if (lastOfRow == target):
                return True
            elif (firstOfRow == target):
                return True
            elif (firstOfRow < target and lastOfRow > target):
                row = m
                break
            #this row is too big
            elif (firstOfRow > target):
                e = m - 1
            #this row is too small
            elif (lastOfRow < target):
                s = m + 1
        if (row == -1):
            return False
        l = 0
        r = len(matrix[row]) - 1
        
        while (l <= r):
            m = int((l+r)/2)
            if (matrix[row][m] > target):
                r = m - 1
            elif (matrix[row][m] < target):
                l = m + 1
            else:
                return True
        return False
        
