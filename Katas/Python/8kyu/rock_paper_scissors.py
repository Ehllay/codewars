def rps(p1, p2):
    rps = ["rock", "paper", "scissors"]

    if p1 == p2:
        return "Draw!"

    elif p1 == rps[(rps.index(p2) + 2) % len(rps)]:
        return "Player 2 won!"

    return "Player 1 won!"
