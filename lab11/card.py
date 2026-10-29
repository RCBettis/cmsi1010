from dataclasses import dataclass
@dataclass (frozen=True)
class Card:
    suit: str
    rank: int

def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")
def __str__(self):
        match self.suit:
            case "S": suit_str = "♠"
            case "H": suit_str = "♥"
            case "D": suit_str = "♦"
            case _: suit_str = "♣"
        match self.rank:
            case 1: rank_str = "A"
            case 11: rank_str = "J"
            case 12: rank_str = "Q"
            case 13: rank_str = "K"
            case _: rank_str = str(self.rank)
        return f"{rank_str}{suit_str}"

print(Card("Hearts", 3))
