# Game state
BOX_COUNT = 5
boxes = [True] * BOX_COUNT
turns_count = 0
game_over = False

def initialize_game():
    """Initialize the game by placing cats in all boxes"""
    global boxes, turns_count, game_over
    boxes = [True] * BOX_COUNT  # All boxes contain cats
    turns_count = 0
    game_over = False
    
    print("Game initialized! Cats are hiding in all boxes.")
    print("Click on boxes to find the cats!")

def jump(from_box, to_box):
    """Move a cat from one box to another adjacent box"""
    global boxes
    
    if abs(from_box - to_box) == 1:
        print(f"Cat jumped from box {from_box} to box {to_box}")
    else:
        print(f"Error: Cat can only jump to adjacent boxes")

def get_possible_jumps(from_box):
    possible_jumps = []
    if from_box > 0:
        possible_jumps.append(from_box - 1)
    if from_box < BOX_COUNT - 1:
        possible_jumps.append(from_box + 1)
    return possible_jumps

def victory():
    print(f"Congratulations! You found the cat in {turns_count} turns!")

def onBoxClick(box):
    """Handle player clicking on a box"""
    global turns_count, boxes, game_over
    
    if game_over:
        print("Game is already over! Initialize a new game to play again.")
        return
    
    turns_count += 1
    print(f"Checking box {box}...")

    newBoxes = [False] * BOX_COUNT
    for box_index in range(BOX_COUNT):
        if boxes[box_index]:
            for jump_to in get_possible_jumps(box_index):
                jump(box_index, jump_to)
                newBoxes[jump_to] = True

    boxes = newBoxes
    boxes[box] = False
    if not any(boxes):
        victory()
        game_over = True
    print(f"Debug - Current box states: {boxes}")

# Start the game when the script runs
if __name__ == "__main__":
    initialize_game()
    
    # Example of how to use the game:
    print("\nExample usage:")
    print("To check a box, call: onBoxClick(box_index)")
    print("Box indices are 0-4 (representing boxes 1-5)")
    print("Example: onBoxClick(0) checks the first box")
    onBoxClick(1)
    onBoxClick(2)
    onBoxClick(3)
    onBoxClick(1)
    onBoxClick(2)
    onBoxClick(3)
