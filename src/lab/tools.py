def get_championships(driver_name) -> int:
    """Get the number of championships won by a Formula 1 driver.

    Arguments:
        driver_name: The name of the Formula 1 driver.

    Returns:
        The number of championships won by the driver, or 0 if the driver is not in the list.
    """
    championships = {
        "Michael Schumacher": 7,
        "Lewis Hamilton": 7,
        "Juan Manuel Fangio": 5,
        "Alain Prost": 4,
        "Sebastian Vettel": 4,
        "Ayrton Senna": 3,
        "Nelson Piquet": 3,
        "Niki Lauda": 3,
        "Jackie Stewart": 3,
        "Jim Clark": 2,
    }

    return championships.get(driver_name, 0)


functions = {
    "get_championships": get_championships,
}
