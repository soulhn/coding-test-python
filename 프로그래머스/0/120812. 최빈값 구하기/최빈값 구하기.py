def solution(array):

    freq = {}
    
    for v in array:
        freq[v] = freq.get(v, 0) + 1
    
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]

    return modes[0] if len(modes) == 1 else -1