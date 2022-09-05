class Solution:
    def maximumRows(self, mat, cols):
        m, n = len(mat), len(mat[0])
        row = [set() for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    row[i].add(j)

        ans = 0
        for item in combinations(list(range(n)), cols):
            cur = set(list(item))
            cnt = 0
            for i in range(m):
                if len(row[i].intersection(cur)) == len(row[i]):
                    cnt += 1
            if cnt > ans:
                ans = cnt
        return ans