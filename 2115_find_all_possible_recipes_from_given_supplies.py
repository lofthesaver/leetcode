from typing import List
from collections import deque # queue

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        # 1. Create dictionary of initial_supplies and initial_recipes
        # Initial recipes stores all the recipes that can be created using initial supplies - these are the starting nodes
        initial_supplies = set(supplies)
        initial_recipes = set()

        # Create dictionary with key = recipe, value = ingredients
        ingredient_dict = {}
        for i, recipe in enumerate(recipes):
            ingredient_dict[recipe] = ingredients[i]

        # Initiate adjacency list
        adjList = {}
        for recipe in recipes:
            adjList[recipe] = []
            for ingredient in ingredient_dict[recipe]:
                adjList[ingredient] = []

        # Find recipes that can be made using only the initial supplies
        for recipe in recipes:
            if all(ingredient in initial_supplies for ingredient in ingredient_dict[recipe]):
                initial_recipes.add(recipe)


        # For all other recipes, create an edge that links the supply that is NOT in initial_supplies to itself,
        # using an adjList
        for recipe in recipes:

            # If this recipe is not creatable using only the initial supplies, then create an edge needed_ingredient -> current_recipe
            if recipe not in initial_recipes:
                
                # Loop through all ingredients not in supplies
                for ingredient in ingredient_dict[recipe]:
                    if ingredient not in initial_supplies:
                        adjList[ingredient].append(recipe)
        
        # Start the search from all initial_recipes, then explore all its edges, adding all recipes to the supplies and continue
        # until all edges have been explored
        curr_supplies = initial_supplies.copy()
        queue = deque()

        # Add all initial recipes to current supplies, and add all recipes to queue
        for recipe in initial_recipes:
            curr_supplies.add(recipe)
            queue.append(recipe)


        # BFS traverse through all neighbors of the initial recipes, adding to current supplies if it can be created
        visited = set()
        while queue:
            curr_recipe = queue.popleft()

            # Check if this recipe can be created
            if all(ingredient in curr_supplies for ingredient in ingredient_dict[curr_recipe]):
                curr_supplies.add(curr_recipe)

            # If recipe has already been explored, then skip
            if curr_recipe in visited:
                continue
                
            # Add this recipe to visited
            visited.add(curr_recipe)

            # Add neighbors to queue
            for next_recipe in adjList[curr_recipe]:
                queue.append(next_recipe)
        
        # Return all the recipes in supplies that were not in initial supplies
        res = []
        for recipe in curr_supplies:
            if recipe not in initial_supplies:
                res.append(recipe)

        return res

        
# Test Cases
# print(Solution().findAllRecipes(recipes = ["burger","bread","sandwich"], ingredients = [["sandwich","meat","bread"],["yeast","flour"],["bread","meat"]], supplies =["yeast","flour","meat"]))
# print(Solution().findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast"]))
# print(Solution().findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))
# print(Solution().findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]))
# print(Solution().findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))
# print(Solution().findAllRecipes(recipes = ["1", "2"], ingredients = [["2"],["1"]], supplies = ["yeast","flour","meat"]))