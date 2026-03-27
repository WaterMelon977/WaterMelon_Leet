"""
LeetCode #2115: Find All Possible Recipes from Given Supplies

https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
"""

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