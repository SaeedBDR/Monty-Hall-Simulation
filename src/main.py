import random


def monty_hall(switch: bool) -> bool:
    """
    Run a single simulation of the Monty Hall problem.

    Parameters
    ----------
    switch : bool
        If True, the player will switch their initial choice after the host opens a door.
        If False, the player will keep their original choice.

    Returns
    -------
    bool
        True if the player wins the car, False otherwise.
    """
    # Initialize doors: two goats and one car
    doors = ["Goat", "Goat", "Car"]
    random.shuffle(doors)

    # Player's initial choice
    player_choice = random.randint(0, 2)

    # Host opens a goat door that is not chosen by the player
    host_opens = random.choice(
        [i for i in range(3) if i != player_choice and doors[i] == "Goat"]
    )

    # Player switches to the remaining closed door (if switch=True)
    if switch:
        player_choice = [
            i for i in range(3) if i != player_choice and i != host_opens][0]

    return doors[player_choice] == "Car"


def simulate_monty_hall(trials: int = 10000) -> tuple[int, int]:
    """
    Run multiple Monty Hall simulations and count winning outcomes
    for both strategies (switching and not switching).

    Parameters
    ----------
    trials : int, optional
        Number of simulations to run. Default is 10000.

    Returns
    -------
    tuple[int, int]
        A tuple containing:
        - number of wins without switching
        - number of wins with switching
    """
    wins_without_switch = sum(monty_hall(False) for _ in range(trials))
    wins_with_switch = sum(monty_hall(True) for _ in range(trials))

    return wins_without_switch, wins_with_switch

       



