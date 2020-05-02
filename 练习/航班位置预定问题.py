class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (n + 1)
        for l, r, seat in bookings:
            res[l-1] += seat
            res[r] -= seat
        for i in range(1, n):
            res[i] += res[i-1]
        print(res)
        return res[:-1]


if __name__ == '__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    s = Solution()
    s.corpFlightBookings(bookings, n)
