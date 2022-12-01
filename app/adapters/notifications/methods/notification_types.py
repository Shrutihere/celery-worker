"""
This file is for xyz reason
"""


def title_from_type(type: str):
    """
    This function does xyz
    """

    no_of_vars = (
        3 if type in ["AT1"] else
        2 if type in ["TL3",] else 1
    )  # if the notification has two variables put it here too

    mapping = {
        "TL3": "You have a {} starting at {}",
        "AT1": "You are marked {} for {} in {}"
    }

    return [mapping[type], no_of_vars]


def create_title(first_variable: str, type: str, second_variable: str = "", third_variable: str = ""):
    """
    This function does xyz
    """
    print(1)

    formatstr = title_from_type(type)
    print(formatstr, type[1])

    return (
        formatstr[0].format(first_variable)
        if formatstr[1] == 1 else
        formatstr[0].format(first_variable, second_variable, third_variable)
        if formatstr[1] == 3 
        else formatstr[0].format(first_variable, second_variable)
    )
