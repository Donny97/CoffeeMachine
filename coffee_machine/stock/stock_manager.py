"""
This is a thread-safe singleton implementation for an stock management system.
This class takes care of handling all the ingredient stock.
"""

from typing import Dict
from coffee_machine.entities.beverage import Beverage

class StockManager:
    """
    Main class for managing the ingredients stock.
    
    Returns:
        None
    """

    stock: Dict = {}
    __shared_instance = None
 
     # This method makes class singleton in nature. It will return StockManager instance if it already exits else creates one
    @staticmethod
    def get_instance():
        if StockManager.__shared_instance is None:
            StockManager.__shared_instance = StockManager()
        return StockManager.__shared_instance

    def check_and_update_stock(self, beverage: Beverage) -> bool:
        """
        Check and update the stock map for the required ingredients.

        Args:
            beverage (Beverage): Beverage object to be prepared.

        Returns:
            bool: True if beverage can be prepared, else False.
        """
        required_ingredient_map = beverage.ingredient_quantity_map
        is_possible = True

        # Check if we have the required ingredients.
        for ingredient in required_ingredient_map.keys():
            ingredient_stock_count = StockManager.get_instance().stock.get(ingredient, -1)
            if ingredient_stock_count == -1 or ingredient_stock_count == 0:
                print(f"{beverage.name} cannot be prepared because {ingredient} is not available")
                is_possible = False
                break
            elif required_ingredient_map.get(ingredient) > ingredient_stock_count:
                print(f"{beverage.name} cannot be prepared because {ingredient} is not sufficient")
                is_possible = False
                break

        #  Update the stock map according to the ingredients used for preparing beverage.
        if is_possible:
            for ingredient in required_ingredient_map.keys():
                existing_stock = StockManager.get_instance().stock.get(ingredient, 0)
                StockManager.get_instance().stock[ingredient] = existing_stock - required_ingredient_map.get(ingredient)

        return is_possible

    def add_to_stock(self, ingredient: str, quantity: int) -> None:
        """
        Add the ingredient and its quantity to stock map.

        Args:
            ingredient (str): Ingredient to add.
            quantity (int): Quantity of ingredient.

        Returns:
            None 
        """
        existing_stock = StockManager.get_instance().stock.get(ingredient, 0)
        StockManager.get_instance().stock[ingredient] = existing_stock + quantity

    def reset_stock(self) -> None:
        """Clear the stock map and reset the manager."""
        StockManager.get_instance().stock.clear()