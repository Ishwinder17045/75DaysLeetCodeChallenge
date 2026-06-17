class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
    
        n = len(stockPrices)

        if n <= 1:
            return 0

        stockPrices.sort()

        lines = 1

        dx = stockPrices[1][0] - stockPrices[0][0]
        dy = stockPrices[1][1] - stockPrices[0][1]

        for i in range(2, n):
            ndx = stockPrices[i][0] - stockPrices[i - 1][0]
            ndy = stockPrices[i][1] - stockPrices[i - 1][1]

            if dy * ndx != ndy * dx:
                lines += 1
                dx, dy = ndx, ndy
            else:
                dx, dy = ndx, ndy

        return lines