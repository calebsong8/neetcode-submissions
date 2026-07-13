class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(float(num))

    def findMedian(self) -> float:
        sort_arr = sorted(self.arr)
        if len(sort_arr) == 0:
            return None
        elif len(sort_arr) == 1:
            return sort_arr[0]
        elif len(sort_arr) % 2 == 0:
            mid = len(sort_arr) / 2 - 1
            return (sort_arr[int(mid)] + sort_arr[int(mid + 1)]) / 2
        else:
            return sort_arr[int((len(sort_arr) // 2))]

        