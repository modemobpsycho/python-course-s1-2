def can_contact(n, thresholds):
    max_threshold = max(thresholds)

    if max_threshold >= n - 1:
        return "Yes"

    threshold_counts = {}
    for threshold in thresholds:
        if threshold not in threshold_counts:
            threshold_counts[threshold] = 0
        threshold_counts[threshold] += 1

    for count in threshold_counts.values():
        if count >= 3:
            return "No"

    return "Yes"


t = int(input())

for _ in range(t):
    n = int(input())
    thresholds = list(map(int, input().split()))

    result = can_contact(n, thresholds)
    print(result)
