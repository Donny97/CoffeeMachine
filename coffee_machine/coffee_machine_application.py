"""File containing CoffeeMachineApplication class"""

import json

from pathlib import Path
from coffee_machine.tasks import CoffeeMachine

class CoffeeMachineApplication:
    """
    Coffee Machine Application main class.

    Args:
        input_file (str): Config file containing beverages configurations.
    
    Returns:
        None
    """
    INPUT_JSON_DIR = Path(__file__).parent.resolve()

    def __init__(self, input_file: str) -> None:
        # Opening and loading input test file

        if input_file is None:
            print('Input file name required. Try Again')
            return None

        input_file_path = CoffeeMachineApplication.INPUT_JSON_DIR / 'assets' / f'{input_file}.json'
        try:
            with open(str(input_file_path)) as file:
                file_data = file.read()
                input_json = json.loads(file_data)
        except Exception as ex:
            print(f'Something wrong with the input. Unable to load the input file {input_file}.json')
            return None

        # Getting CoffeeMachine instance to start processing of all beverages. After the process the machine is reset.
        self.coffee_machine: CoffeeMachine = CoffeeMachine.get_instance(input_json)
        self.coffee_machine.process()
        self.coffee_machine.reset()
