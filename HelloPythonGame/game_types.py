# Игровые типы данных
from enum import Enum

class GameStates(Enum):
    """Состояние игры"""
    Menu = 1
    Play = 2
    GameOver = 3
    Pause = 4


