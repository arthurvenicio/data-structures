import heapq


def reorganizeString(s: str) -> str:
    char_map = {}
    for char in s:
        char_map[char] = char_map.get(char, 0) + 1
        
    max_heap = [(-freq, char) for char, freq in char_map.items()]
    heapq.heapify(max_heap)
  
    res = []
    
    while len(max_heap) >= 2:
        freq1, char1 = heapq.heappop(max_heap)
        freq2, char2 = heapq.heappop(max_heap)
        
        res.extend([char1, char2])
        
        if freq1 + 1 < 0:
            heapq.heappush(max_heap, (freq1 + 1, char1))
        if freq2 + 1 < 0:
            heapq.heappush(max_heap, (freq2 + 1, char2))
            
    if max_heap:
        freq, char = heapq.heappop(max_heap)
        if -freq > 1:
            return ""
        res.append(char)
        
    return "".join(res)
        
        
reorganizeString("aaabbcc")