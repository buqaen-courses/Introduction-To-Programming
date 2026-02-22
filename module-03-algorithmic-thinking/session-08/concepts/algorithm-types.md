# Algorithm Types: A Comprehensive Classification

## Understanding Algorithm Categories

Algorithms can be classified in multiple ways based on their approach, strategy, or the type of problem they solve. Understanding these categories helps in selecting the right algorithm for specific problems.

## Classification by Approach

### 1. Brute Force Algorithms

**Strategy**: Try all possible solutions until finding the correct one.

**Characteristics:**
- Simple to understand and implement
- Always finds a solution if one exists
- Can be very slow for large problem spaces

**Examples:**
```python
# Password cracking (brute force)
def crack_password(target_hash, charset, max_length):
    for length in range(1, max_length + 1):
        for attempt in generate_combinations(charset, length):
            if hash(attempt) == target_hash:
                return attempt
    return None

# Traveling salesman - try all routes
def tsp_brute_force(cities):
    min_distance = float('inf')
    best_route = None

    for route in permutations(cities):
        distance = calculate_route_distance(route)
        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance
```

**When to use:** Small problem spaces, when correctness is more important than speed.

### 2. Greedy Algorithms

**Strategy**: Make the locally optimal choice at each step with the hope of finding a global optimum.

**Characteristics:**
- Fast and efficient
- Don't always produce optimal solutions
- Work well for certain types of problems

**Examples:**
```python
# Coin change problem
def coin_change_greedy(amount, coins):
    coins.sort(reverse=True)  # Largest first
    result = []

    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin

    return result

# Activity selection (greedy by finish time)
def activity_selection(activities):
    # activities = [(start, finish), ...]
    activities.sort(key=lambda x: x[1])  # Sort by finish time

    selected = [activities[0]]
    last_finish = activities[0][1]

    for activity in activities[1:]:
        if activity[0] >= last_finish:
            selected.append(activity)
            last_finish = activity[1]

    return selected
```

**When to use:** Optimization problems where local choices lead to global optimum.

### 3. Divide and Conquer Algorithms

**Strategy**: Break the problem into smaller subproblems, solve recursively, then combine solutions.

**Characteristics:**
- Recursive approach
- Problems must be divisible
- Often optimal solutions
- Good for parallel processing

**Examples:**
```python
# Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Binary search
def binary_search(arr, target):
    if not arr:
        return -1

    mid = len(arr) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        # Need to adjust index for right half
        result = binary_search(arr[mid+1:], target)
        return mid + 1 + result if result != -1 else -1
```

**When to use:** Problems that can be naturally divided into independent subproblems.

### 4. Dynamic Programming Algorithms

**Strategy**: Break problem into subproblems, solve each subproblem once, store solutions for reuse.

**Characteristics:**
- Optimal substructure (optimal solution uses optimal subsolutions)
- Overlapping subproblems
- Trade space for time
- Often uses memoization or tabulation

**Examples:**
```python
# Fibonacci with memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Longest common subsequence
def lcs(X, Y):
    m, n = len(X), len(Y)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Reconstruct solution
    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str = X[i-1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return len(lcs_str), lcs_str

# 0/1 Knapsack
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

**When to use:** Problems with overlapping subproblems and optimal substructure.

### 5. Backtracking Algorithms

**Strategy**: Try partial solutions, backtrack when they don't work, try different choices.

**Characteristics:**
- Systematic search of solution space
- Build solution incrementally
- Remove solutions that don't work
- Can find all solutions or just one

**Examples:**
```python
# N-Queens problem
def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check this column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check lower diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(board, row):
        if row == n:
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(board, row + 1)
                board[row][col] = '.'  # Backtrack

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return solutions

# Sudoku solver
def solve_sudoku(board):
    def is_valid(num, pos):
        # Check row
        for j in range(9):
            if board[pos[0]][j] == num and j != pos[1]:
                return False

        # Check column
        for i in range(9):
            if board[i][pos[1]] == num and i != pos[0]:
                return False

        # Check 3x3 box
        box_x = pos[0] // 3
        box_y = pos[1] // 3
        for i in range(box_x*3, box_x*3 + 3):
            for j in range(box_y*3, box_y*3 + 3):
                if board[i][j] == num and (i,j) != pos:
                    return False

        return True

    def find_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def solve():
        empty = find_empty()
        if not empty:
            return True

        row, col = empty
        for num in range(1, 10):
            if is_valid(num, (row, col)):
                board[row][col] = num
                if solve():
                    return True
                board[row][col] = 0  # Backtrack

        return False

    solve()
    return board
```

**When to use:** Constraint satisfaction problems, puzzles, combinatorial optimization.

## Classification by Problem Type

### Sorting Algorithms

#### Comparison-Based
```python
# Quick sort (divide and conquer)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Heap sort
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
```

#### Non-Comparison Based
```python
# Counting sort
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1

    count = [0] * range_size
    output = [0] * len(arr)

    # Count occurrences
    for num in arr:
        count[num - min_val] += 1

    # Cumulative count
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Build output
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Radix sort
def radix_sort(arr):
    max_digits = len(str(max(arr)))

    for digit in range(max_digits):
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit_value = (num // (10 ** digit)) % 10
            buckets[digit_value].append(num)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)

    return arr
```

### Search Algorithms

#### Linear Search
```python
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1
```

#### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

#### Hash-Based Search
```python
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
```

## Randomized Algorithms

**Strategy**: Use random choices to simplify or speed up algorithms.

```python
# Quick sort with random pivot
import random

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Random pivot
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Monte Carlo algorithm for primality testing
import random

def is_prime_monte_carlo(n, k=10):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True
```

## Approximation Algorithms

**Strategy**: Find near-optimal solutions when exact solutions are too expensive.

```python
# Traveling salesman approximation (nearest neighbor)
def tsp_nearest_neighbor(cities):
    if not cities:
        return [], 0

    unvisited = set(cities)
    current = cities[0]
    unvisited.remove(current)
    route = [current]
    total_distance = 0

    while unvisited:
        # Find closest unvisited city
        closest = min(unvisited, key=lambda city: distance(current, city))
        total_distance += distance(current, closest)
        route.append(closest)
        current = closest
        unvisited.remove(closest)

    # Return to start
    total_distance += distance(route[-1], route[0])
    route.append(route[0])

    return route, total_distance
```

## Key Takeaways

1. **Different strategies**: Brute force, greedy, divide-and-conquer, dynamic programming, backtracking
2. **Problem-specific**: Choose algorithm based on problem characteristics
3. **Trade-offs**: Time vs space, exact vs approximate solutions
4. **Combinations work**: Many problems benefit from hybrid approaches
5. **Practice matters**: Understanding when to apply different techniques

## Further Reading
- Study algorithm design manuals and textbooks
- Practice on competitive programming platforms
- Learn about advanced data structures
- Explore parallel and distributed algorithms