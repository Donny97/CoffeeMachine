from typing import Dict
from .outlet import Outlet

class Machine:
    """Machine Base class"""

    _outlets: Outlet = None
    _ingredient_quantity_map = {}
    _beverages = {}

    @property
    def beverages(self) -> Dict:
        """Beverages property for Machine class."""
        return self._beverages

    @beverages.setter
    def beverages(self, beverages_map: Dict) -> None:
        """
        Setter for Beverages property.
        
        Args:
            beverages_map (Dict): Beverages map to set.

        Return:
            None
        """
        self._beverages = beverages_map

    @property
    def ingredient_quantity_map(self) -> Dict:
        """Ingredient quantity property for Machine class."""
        return self._ingredient_quantity_map

    @ingredient_quantity_map.setter
    def ingredient_quantity_map(self, ingredient_map: Dict) -> None:
        """
        Setter for Ingredient Quantity property.
        
        Args:
            ingredient_map (Dict): ingredient map to set.

        Return:
            None
        """
        self._ingredient_quantity_map = ingredient_map

    @property
    def outlets(self) -> Outlet:
        """Outlets property for Machine class."""
        return self._outlets

    @outlets.setter
    def outlets(self, outlets: Outlet) -> None:
        """
        Setter for Outlets property.
        
        Args:
            outlets (Outlet): Outlet object to set.

        Return:
            None
        """
        self._outlets = outlets


class CoffeeMachineDetails:
    """Class for Coffee Machine details. Provides machine object as property."""
    
    _machine = None

    @property
    def machine(self) -> Machine:
        """Machine property for CoffeeMachineDetails class."""
        return self._machine

    @machine.setter
    def machine(self, machine: Machine) -> None:
        """
        Setter for Machine property.
        
        Args:
            machine (Machine): Machine object to set.

        Return:
            None
        """
        self._machine = machine