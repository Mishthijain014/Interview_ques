def n_queens(n):
    cols= set()
    diag1 = set()
    diag2 = set()

    def backtracking(row):
        if row == n:
            return 1
        
        count = 0

        for col in range(n):
            if (col in cols or
                (row - col) in diag1 or
                (row + col) in diag2):
                continue

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            count += backtracking(row+1)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return count

    return backtracking(0)
    

print(n_queens(4))

# time complexity = O(N!)
# space complexity = O(N)

