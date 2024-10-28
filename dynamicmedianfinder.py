import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap for the lower half (invert values to use Python's min-heap as a max-heap)
        self.lower_half = []
        # Min-heap for the upper half
        self.upper_half = []

    def add_number(self, num):
        # Add number to the appropriate heap
        if len(self.lower_half) == 0 or num <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.upper_half, num)

        # Balance the two heaps so that their sizes differ by at most 1
        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))

    def get_median(self):
        # If the heaps are the same size, return the average of the two middle elements
        if len(self.lower_half) == len(self.upper_half):
            return (-self.lower_half[0] + self.upper_half[0]) / 2.0
        # Otherwise, return the middle element from the max-heap (lower_half)
        else:
            return -self.lower_half[0]

# Lecture de l'entrée
n = int(input())  # Nombre de requêtes
median_finder = MedianFinder()

for _ in range(n):
    query = input().split()

    if query[0] == 'add':
        num = int(query[1])
        median_finder.add_number(num)
    elif query[0] == 'get':
        print(f"{median_finder.get_median():.1f}")