def gridlandMetro(n, m, k, track):
    track_map = {}
    
    for r, c1, c2 in track:
        if r not in track_map:
            track_map[r] = []
        track_map[r].append((c1, c2))
    
    total_occupied = 0
    
    for r in track_map:
        track_map[r].sort()
        merged_intervals = []
        
        for start, end in track_map[r]:
            if not merged_intervals or merged_intervals[-1][1] < start:
                merged_intervals.append((start, end))
            else:
                merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], end))
        
        for start, end in merged_intervals:
            total_occupied += (end - start + 1)
    
    return n * m - total_occupied

# Example usage:
n = 4
m = 4
k = 3
track = [(2, 2, 3), (3, 1, 4), (4, 4, 4)]
print(gridlandMetro(n, m, k, track))  # Output: 9
