class CatBoxGame:
    def __init__(self, box_count=5):
        self.box_count = box_count
        self.boxes = [True] * self.box_count
        self.turns_count = 0
        self.game_over = False

    def initialize_game(self):
        """Initialize the game by placing cats in all boxes"""
        self.boxes = [True] * self.box_count  # All boxes contain cats
        self.turns_count = 0
        self.game_over = False   
        print("Game initialized! Cats are hiding in all boxes.")
        print("Click on boxes to find the cats!")

    def jumpAnimation(self, from_box, to_box):
        """Move a cat from one box to another adjacent box"""
        if abs(from_box - to_box) == 1:
            print(f"Cat jumped from box {from_box} to box {to_box}")
        else:
            print(f"Error: Cat can only jump to adjacent boxes")

    def get_possible_jumps(self, from_box):
        possible_jumps = []
        if from_box > 0:
            possible_jumps.append(from_box - 1)
        if from_box < self.box_count - 1:
            possible_jumps.append(from_box + 1)
        return possible_jumps

    def victory(self):
        print(f"Congratulations! You found the cat in {self.turns_count} turns!")

    def on_box_click(self, box):
        """Handle player clicking on a box"""
        if self.game_over:
            print("Game is already over! Initialize a new game to play again.")
            return
        
        self.turns_count += 1
        print(f"Checking box {box}...")

        self.boxes[box] = False
        new_boxes = [False] * self.box_count
        for box_index in range(self.box_count):
            if self.boxes[box_index]:
                for jump_to in self.get_possible_jumps(box_index):
                    self.jumpAnimation(box_index, jump_to)
                    new_boxes[jump_to] = True

        self.boxes = new_boxes
        if not any(self.boxes):
            self.victory()
            self.game_over = True
        print(f"Debug - Current box states: {self.boxes}")

# Example usage
if __name__ == "__main__":
    game = CatBoxGame()
    game.initialize_game()
    
    print("\nExample usage:")
    print("To check a box, call: game.on_box_click(box_index)")
    print("Box indices are 0-4 (representing boxes 1-5)")
    print("Example: game.on_box_click(0) checks the first box")
    
    # Example game sequence
    game.on_box_click(1)
    game.on_box_click(2)
    game.on_box_click(3)
    game.on_box_click(1)
    game.on_box_click(2)
    game.on_box_click(3)
