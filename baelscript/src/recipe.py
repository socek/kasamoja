from baelfire.recipe import Recipe
from bael.project.recipe import ProjectRecipe


class BaelScriptRecipe(Recipe):

    def gather_recipes(self):
        self.add_recipe(ProjectRecipe())
