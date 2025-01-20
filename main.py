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

if pair:
    print(f"Пара чисел: {pair[0]} и {pair[1]}")
    print(f"Их сумма: {best_sum}")
else:
    print("Пара не найдена")

numbers.sort()
left, right = 0, len(numbers) - 1
best_sum = float('-inf')
pair = None

while left < right:
    current_sum = numbers[left] + numbers[right]
    if abs(k - current_sum) < abs(k - best_sum):
        best_sum = current_sum
        pair = (numbers[left], numbers[right])
    
    if current_sum < k:
        left += 1
    else:
        right -= 1

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
left,