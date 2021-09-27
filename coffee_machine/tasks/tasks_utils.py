from coffee_machine.entities import Machine, CoffeeMachineDetails, Outlet

from typing import Dict


def json_to_coffee_machine_mapper(input_json: Dict) -> CoffeeMachineDetails:
    """
    Map Json data to CoffeeMachineDetails(Machine) class.

    Args:
        input_json(Dict): Input test data.

    Returns:
        CoffeeMachineDetails 
    """
    # Create Machine object and map data to it
    machine = Machine()
    machine_json = input_json['machine']
    machine.ingredient_quantity_map = machine_json['total_items_quantity']
    machine.beverages = machine_json['beverages']
    machine.outlets = Outlet()
    machine.outlets.count = machine_json['outlets']['count_n']

    # Create CoffeeMachineDetails object and assign machine object to its property
    coffee_machine_details = CoffeeMachineDetails()
    coffee_machine_details.machine = machine

    # Return CoffeeMachineDetails object
    return coffee_machine_details