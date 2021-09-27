from coffee_machine.stock.stock_manager import StockManager
from coffee_machine.entities import Beverage, CoffeeMachineDetails
from .beverage_maker import BeverageMakerTask
from .tasks_utils import json_to_coffee_machine_mapper

from concurrent.futures import ThreadPoolExecutor
from typing import Dict


class CoffeeMachine:
    """
    Main class depicting Coffee Machine.

    Important Points to remember:
        * The input JSON will not have duplicate beverage names. (Workaround would be to use custom deserialiser. 
        Considering this out of scope for now.
        * The input JSON contains correct input.

    Algorithm:
        * A multithreaded system with n threads is started which represent n outlet coffee machine.
        * It tries to create all the beverages. Preference served to represent multithreaded system and to ensure two drinks do not use same ingredient.
        * Extra Feature include - API for new ingredient addition in our stock, and API for adding new Beverage Requests at any given point of time.

    Used singleton class to simulate a Coffee Machine which can serve parallely without any error, using multi threading.

    Args:
        input_json (Dict): Input data for the machine.

    Returns:
        None
    """

    _coffee_machine: "CoffeeMachine" = None
    _coffee_machine_details: CoffeeMachineDetails = None
    _stock_manager: StockManager = None
    _executor: ThreadPoolExecutor = None

    # This method makes class singleton in nature. It will return CoffeeMachine instance if it already exits else creates one

    @staticmethod
    def get_instance(input_json: Dict) -> "CoffeeMachine":
        if CoffeeMachine._coffee_machine is None:
            CoffeeMachine._coffee_machine = CoffeeMachine(input_json)
        return CoffeeMachine._coffee_machine

    def __init__(self, input_json: Dict) -> None:
        print("Coffee Machine Starts")

        # Mapping input data to coffe machine details class
        self._coffee_machine_details = json_to_coffee_machine_mapper(input_json)
        outlet = self._coffee_machine_details.machine.outlets.count

        # Get outlets count and set number of threads as number of outlets
        self._executor = ThreadPoolExecutor(outlet)

    def process(self) -> None:
        self._stock_manager = StockManager.get_instance()

        # Get Ingredient quantity mapping and add all the ingredients to stock.
        ingredients = self._coffee_machine_details.machine.ingredient_quantity_map
        for key in ingredients.keys():
            self._stock_manager.add_to_stock(key, ingredients.get(key))

        # Start the process for creation of each beverage,
        beverages = self._coffee_machine_details.machine.beverages
        for key in beverages.keys():
            beverage = Beverage(key, beverages.get(key))
            self._coffee_machine.add_beverage_request(beverage)

    def add_beverage_request(self, beverage: Beverage) -> None:
        task = BeverageMakerTask()
        task.beverage_maker_task(beverage)
        self._executor.submit(task.run(), task)

    def stop_machine(self) -> None:
        self._executor.shutdown()

    # Resetting stocks and stopping coffee machine.
    def reset(self) -> None:
        print("Coffee Machine Reset")
        self.stop_machine()
        self._stock_manager.reset_stock()
