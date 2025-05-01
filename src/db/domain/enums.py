from enum import Enum

class Color(str, Enum):
    red = "red"
    blue = "blue"
    green = "green"
    yellow = "yellow"
    purple = "purple"
    orange = "orange"
    dark = "dark"
    white = "white"

class ImportanceStatus(str, Enum):
    very_urgent = "very_urgent"
    urgently = "urgently"
    not_urgent = "not urgent"