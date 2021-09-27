from typing import Dict


class Beverage:
    """
    Class for Beverage entity.

    Args:
        name (str): Name of the beverage.
        ingredient_quantity_map (Dict): Ingredient quantity maping.

    Returns:
        None
    """

    _name = ""
    _ingredient_quantity_map = {}

    def __init__(self, name: str, ingredient_quantity_map: Dict) -> None:
        self._name = name
        self._ingredient_quantity_map = ingredient_quantity_map

    @property
    def name(self) -> str:
        """Name property for Beverage class."""
        return self._name

    @property
    def ingredient_quantity_map(self) -> Dict:
        """Ingredient mapper property for Beverage class."""
        return self._ingredient_quantity_map
