# Hacktech2021 (Weird Chess)

## Inspiration
Combining popular "roguelike" games that have upgrades and a difficulty increase with chess. The upgrades became, well, upgrades, and the difficulty increase comes with the larger board as you increase in level each time.

## What it does
This is a chess-style game that follows most of the rules of chess.
1. There is no check or checkmate, the goal is to take the opponent's king.
2. The winner of a match gets to choose from one of three upgrades, a "straight" upgrade, diagonal upgrade, and "knight" upgrade, which will be applied to one type of their pieces at random.
3. Each match you play, the board expands.

Upgrades:

Straight Upgrade:
- This allows the piece to move one square vertically or horizontally in any direction.
- Can be applied to knights and bishops.

Diagonal Upgrade:
- This allows the piece to move one square diagonally in any direction.
- Can be applied to knights and rooks.

"Knighted" Upgrade:
- This allows the piece to move like a knight.
- Can be applied to kings, queens, rooks, and bishops.

## How we built it
We used `pygame` for our graphics and event handling, and due to the nature of the Sprite class, we were able to handle all of the game logic internally, only having to touch graphics logic when converting coordinates from game coords to screen coords.

## Challenges we ran into
The `generate_moves` method in Piece was at first written in such a way that it tried to return a non-existent attribute when it was first called. Google led us to believe that it was an issue with tabs vs. spaces, and when that was fixed we kept looking around until we eventually found the problematic return statement.

The AI was a bit tricky to make work, we couldn't get the movements to weight properly so eventually we just went with what we could.

Beyond that, there were some formulas that we had to figure out that took a minute, but the rest was *fairly* straightforward.

## Accomplishments that we're proud of
The upgrades system turned out really well and works great!
We were able to build the entire chess logic structure without any third parties libraries

## What we learned
- I (Ryan) learned a lot more about subclassing as while I'd used it some before, not extensively like this.
- Don't make all commits "initial commit"

## What's next for Weird Chess
Codebase refactor
- A lot of the code can be cleaned up, but we just haven't had time to worry about that on the offchance that we break something and it takes an hour to fix.

AI Improvement
- The current AI is only slightly better than random, and it needs improved.

## [See It!](https://youtu.be/Fzd6dWUqJpA)