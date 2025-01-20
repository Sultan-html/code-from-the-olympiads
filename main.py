n, k = map(int, input().split())
numbers = list(map(int, input().split()))

best_sum = float('-inf')
pair = None

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        current_sum = numbers[i] + numbers[j]
        if abs(k - current_sum) < abs(k - best_sum):
            best_sum = current_sum
            pair = (numbers[i], numbers[j])