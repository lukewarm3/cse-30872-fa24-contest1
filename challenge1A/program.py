#!/usr/bin/env python3
import sys
def program(arr):
    n = len(arr)
    maxHeights = [0 for _ in range(n)]
    maxHeights[-1] = 0

    for i in range(n-2, -1, -1):
        maxHeights[i] = max(maxHeights[i+1], arr[i+1])
    
    output = 0
    for i in range(n):
        if arr[i] > maxHeights[i]:
            output += 1
    
    return output

def main(stream=sys.stdin):
    for line in stream:
        arr = list(map(int, line.strip().split()))
        result = program(arr)

        print(result)

if __name__=='__main__':
    main()