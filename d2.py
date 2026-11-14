
import heapq

# Create Node
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Generate Huffman Codes
def huffman(node, code=""):
    if node.char is not None:
        print(node.char, ":", code)
        return

    huffman(node.left, code + "0")
    huffman(node.right, code + "1")


# Main Program
text = input("Enter text: ")

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print("\nCharacter Frequencies:")
for ch, f in freq.items():
    print(ch, ":", f)

# Create Min Heap
heap = [Node(ch, f) for ch, f in freq.items()]
heapq.heapify(heap)

# Build Huffman Tree
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    new = Node(None, left.freq + right.freq)
    new.left = left
    new.right = right

    heapq.heappush(heap, new)

print("\nHuffman Codes:")
if heap:
    huffman(heap[0])


# Time Complexity: O(n + k log k)
# Space Complexity: O(k)
# n = number of characters in input text
# k = number of unique characters
