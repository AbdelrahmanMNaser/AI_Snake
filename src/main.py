import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.core.game import Game

def main():
    if __name__ == "__main__":
        game = Game()
        game.run()

main()