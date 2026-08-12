# Recursion Practice — Year 10 Python

You know functions, loops, and lists. Recursion is just a function that calls **itself** to solve a smaller version of the same problem.

## The 3-step checklist for every problem

1. **Base case** — the simplest input, where you know the answer without calling the function again (this is what stops the recursion).
2. **Recursive case** — how to break the problem into a smaller version of itself, plus one step of work.
3. **Trust it** — assume the recursive call already works correctly for the smaller input; you just need to combine it correctly.

If you ever get stuck, try tracing the function by hand for a tiny input (like `n = 2` or `n = 3`) on paper before you touch the keyboard.

---

## Problem 1: Countdown (warm-up)

Write `countdown(n)` that prints every number from `n` down to `1`, then prints `"Blastoff!"`. It should print nothing and return once `n` reaches `0`.

```python
def countdown(n):
    # Your code here
    pass

countdown(5)
```

Expected output:
```
5
4
3
2
1
Blastoff!
```

---

## Problem 2: Sum from 1 to N

Write `sum_to_n(n)` that **returns** the sum of all whole numbers from `1` to `n`.

```python
def sum_to_n(n):
    # Your code here
    pass

print(sum_to_n(5))  # 15
```

---

## Problem 3: Factorial

Write `factorial(n)` that returns `n!` (n factorial). Recall `0! = 1` and `n! = n * (n-1)!`.

```python
def factorial(n):
    # Your code here
    pass

print(factorial(5))  # 120
```

---

## Problem 4: Power

Write `power(base, exp)` that returns `base` raised to the power `exp`, where `exp` is a non-negative whole number. Don't use `**` or `pow()` — do it recursively.

```python
def power(base, exp):
    # Your code here
    pass

print(power(2, 5))  # 32
print(power(3, 0))  # 1
```

---

## Problem 5: Sum of Digits

Write `sum_of_digits(n)` that returns the sum of the digits of a positive whole number. Hint: `n % 10` gives the last digit, and `n // 10` chops it off.

```python
def sum_of_digits(n):
    # Your code here
    pass

print(sum_of_digits(1234))  # 10
```

---

## Problem 6: Reverse a String

Write `reverse_string(s)` that returns the string reversed. Don't use `s[::-1]` — build it recursively instead.

```python
def reverse_string(s):
    # Your code here
    pass

print(reverse_string("hello"))  # "olleh"
```

---

## Problem 7: Is it a Palindrome?

Write `is_palindrome(s)` that returns `True` if the string reads the same forwards and backwards, `False` otherwise. (Assume no spaces or capitals to worry about.)

```python
def is_palindrome(s):
    # Your code here
    pass

print(is_palindrome("racecar"))  # True
print(is_palindrome("python"))   # False
```

---

## Problem 8: Sum of a List

Write `sum_list(lst)` that returns the sum of all numbers in a list, using recursion instead of `sum()` or a loop.

```python
def sum_list(lst):
    # Your code here
    pass

print(sum_list([1, 2, 3, 4, 5]))  # 15
print(sum_list([]))               # 0
```

---

## Problem 9: Find the Maximum

Write `find_max(lst)` that returns the largest value in a non-empty list, recursively (no `max()` allowed).

```python
def find_max(lst):
    # Your code here
    pass

print(find_max([3, 7, 2, 9, 4]))  # 9
```

---

## Problem 10: Count Occurrences

Write `count_occurrences(lst, target)` that returns how many times `target` appears in `lst`.

```python
def count_occurrences(lst, target):
    # Your code here
    pass

print(count_occurrences([1, 3, 1, 5, 1, 2], 1))  # 3
```

---

## Bonus Challenge: Fibonacci

Write `fibonacci(n)` that returns the `n`th Fibonacci number, where `fibonacci(0) = 0`, `fibonacci(1) = 1`, and every number after is the sum of the two before it.

```python
def fibonacci(n):
    # Your code here
    pass

print(fibonacci(10))  # 55
```

Once it works, try `fibonacci(35)` and see how long it takes. Ask yourself: why is it so slow, and what does that tell you about calling a recursive function twice inside itself?

---
---

# Solutions

Try each problem yourself first — the whole point of recursion is building the instinct for base case + recursive case. Peek only to check your work.

```python
def countdown(n):
    if n == 0:
        print("Blastoff!")
        return
    print(n)
    countdown(n - 1)


def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])


def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = find_max(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max


def count_occurrences(lst, target):
    if len(lst) == 0:
        return 0
    is_match = 1 if lst[0] == target else 0
    return is_match + count_occurrences(lst[1:], target)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

