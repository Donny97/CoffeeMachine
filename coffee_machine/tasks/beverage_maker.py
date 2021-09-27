"""This class represents an atomic task to make any Beverage. Uses Runnable interface to support multithreading."""

from threading import Thread

from coffee_machine.stock.stock_manager import StockManager
from coffee_machine.entities.beverage import Beverage


class BeverageMakerTask(Thread):
    """Beverage Maker Task class whose objects will act as threads."""

    _beverage = None

    def beverage_maker_task(self, beverage: Beverage) -> None:
        """
        Set beverage to be prepared next.

        Args:
            beverage (Beverage): Beverage object to be prepared next.
        
        Returns: 
            None
        """
        self._beverage = beverage

    def run(self) -> None:
        """
        Run the task thread for preparing the beverage.

        Returns:
            None
        """
        if StockManager.get_instance().check_and_update_stock(self._beverage):
            print(f"{self._beverage.name} is prepared")

    def __str__(self) -> str:
        """Return string representation of the class."""
        return self._beverage.name
