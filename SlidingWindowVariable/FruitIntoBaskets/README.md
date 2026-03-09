# Insert Leetcode Link
[https://leetcode.com/problems/fruit-into-baskets/](https://leetcode.com/problems/fruit-into-baskets/)

## Approach

- Track the last two fruit types instead of a frequency map.

Maintain:
- `last_fruit` → most recent fruit type
- `second_last_fruit` → the other fruit type
- `last_fruit_count` → number of consecutive `last_fruit`

- If the current fruit matches either type, extend the window.
- Otherwise, start a new window consisting of the last streak of `last_fruit` plus the current fruit.
- Update the two fruit types accordingly.

## Key Insight
The window only needs to remember two fruit types and the length of the last streak, which is enough to reconstruct the valid window when a third type appears.

## Why efficient?
It avoids dictionary operations and uses only constant variables while still scanning the array once.

## Python Solution
```python
def totalFruit(self, fruits: List[int]) -> int:
    last_fruit = -1
    second_last_fruit = -1
    last_fruit_count = 0
    current_window = 0
    max_window = 0

    for fruit in fruits:
        if fruit == last_fruit or fruit == second_last_fruit:
            current_window += 1
        else:
            current_window = last_fruit_count + 1

        if fruit == last_fruit:
            last_fruit_count += 1
        else:
            last_fruit_count = 1
            second_last_fruit = last_fruit
            last_fruit = fruit

            max_window = max(max_window, current_window)

        return max_window
```

## Complexity
Time: O(n) each fruit is processed once
Space: O(1) only a few variables are used
