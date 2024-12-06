# Human Readable!

sorted_col1 = sorted(
    [int(i) 
        for I, i in enumerate(open("data/1.txt", "r").read().split()) 
        if (I == 0 or I %2 == 0)
    ]
)
sorted_col2 = sorted(
    [int(i) 
        for I, i in enumerate(open("data/1.txt", "r").read().split()) 
        if (I != 0 and I %2 == 1)
    ]
)
distances = [
    abs(sorted_col1[i] - sorted_col2[i])
        for i in range(len(sorted_col1))
]

distances_sum = sum(distances)
print(distances_sum)

# One-Liner!

print(sum([abs(sorted([int(i) for I, i in enumerate(open("data/1.txt", "r").read().split()) if (I == 0 or I %2 == 0)])[i] - sorted([int(i) for I, i in enumerate(open("data/1.txt", "r").read().split()) if (I != 0 and I %2 == 1)])[i]) for i in range(len(sorted([int(i) for I, i in enumerate(open("data/1.txt", "r").read().split()) if (I == 0 or I %2 == 0)])))]))