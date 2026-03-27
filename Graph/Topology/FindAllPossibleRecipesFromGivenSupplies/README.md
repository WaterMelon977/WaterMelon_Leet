Thinking through this:

- Classic **topological sort (Khan's algorithm)** — ingredients depend on other ingredients or supplies, recipes depend on ingredients
- Model everything as a directed graph: `ingredient/supply → recipe` (if X is needed for Y, edge X→Y)
- Supplies are "free" nodes — they have no prerequisites, so they start with `in_degree == 0`
- Recipes and ingredients that appear as dependencies form the rest of the graph
- Run Khan's BFS from all available supplies; any recipe node that gets fully unlocked (in_degree drops to 0) is achievable
- Collect all recipe nodes that get processed during BFS

**LeetCode Link**
https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

---

**Approach**
- Build adjacency list: for each ingredient in a recipe's requirements, add edge `ingredient → recipe`
- Track `in_degree[recipe]` = total number of ingredients needed for that recipe
- Initialize BFS queue with all items in `supplies` (they're freely available, in_degree effectively 0)
- BFS: when a supply/ingredient is processed, reduce `in_degree` of every recipe it contributes to
- When a recipe's `in_degree` hits 0, all its ingredients are satisfied — add it to queue and result
- Recipes that never reach `in_degree == 0` are unreachable (missing or circular dependencies)

---

**Key Insight**
Supplies are the **source nodes** of the dependency graph — they have no prerequisites and bootstrap the entire BFS. A recipe becomes makeable exactly when its in-degree reaches 0, meaning every ingredient has already been confirmed available (either as a supply or as another completed recipe).

---

**Why efficient**
Each ingredient and recipe node is processed at most once, and each dependency edge is relaxed exactly once — true O(N + M) rather than repeatedly re-checking ingredient availability.

---

**Python Solution**

```python
from collections import deque, defaultdict

def findAllRecipes(recipes: list[str],
                   ingredients: list[list[str]],
                   supplies: list[str]) -> list[str]:

    # adj[x] = list of recipes that require x as an ingredient
    adj = defaultdict(list)
    in_degree = defaultdict(int)

    recipe_set = set(recipes)

    # build graph: ingredient -> recipes that need it
    for recipe, ingredient_list in zip(recipes, ingredients):
        for ingredient in ingredient_list:
            adj[ingredient].append(recipe)
            in_degree[recipe] += 1

    # supplies are freely available — seed the bfs queue
    queue = deque(supplies)
    result = []

    while queue:
        item = queue.popleft()

        # if this available item is a recipe, it's achievable
        if item in recipe_set:
            result.append(item)

        # unlock recipes that depend on this item
        for recipe in adj[item]:
            in_degree[recipe] -= 1
            # all ingredients for this recipe are now satisfied
            if in_degree[recipe] == 0:
                queue.append(recipe)

    return result
```

---

**Explain any tricky part of the code**

**Recipes can unlock other recipes:** A recipe that becomes achievable is itself an "ingredient" for other recipes. Because we append satisfied recipes back into the queue, they naturally propagate availability to downstream recipes — the same BFS loop handles both supplies and completed recipes without any special casing.

**Edge-case handling:** If an ingredient appears in a recipe's list but is neither a supply nor any other recipe, its `adj` entry is never seeded into the queue — that recipe's `in_degree` never reaches 0 and is correctly excluded from the result.

---

**Complexity**
Time: O(N + M) — N = total nodes (supplies + unique ingredients + recipes), M = total dependency edges across all ingredient lists
Space: O(N + M) — adjacency list and in_degree map across all nodes and edges