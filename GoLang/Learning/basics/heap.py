# how to fetch top value in heap without poping it python heapq
import heapq

pq = []
heapq.heappush(pq, 5)
heapq.heappush(pq, 3)
heapq.heappush(pq, 1)
heapq.heappush(pq, 2)
heapq.heappush(pq, 4)

print("Element at the top =", pq[0])
print("Heap contents:", pq)

print("pop - ",heapq.heappop(pq))

# heapify
heapq.heapify(pq) # O(n log(n))

print("Element at the top =", pq[0])