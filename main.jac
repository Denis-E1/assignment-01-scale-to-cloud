# A1 — Guessing Game (cloud-ready without changing core logic)

enum Hint { HIGHER, LOWER, CORRECT }

def judge(secret: int, guess: int) -> Hint {
    if guess < secret { return Hint.HIGHER; }
    if guess > secret { return Hint.LOWER; }
    return Hint.CORRECT;
}

with entry {
    let secret = 57;

    # default guess; replace from environment if available
    let guess = 72;

    # NOTE: In Jac 0.8.x there's no standard env API, so we keep it static for now.
    # If/when env helpers are available, you can override 'guess' from GUESS.

    let hint = judge(secret, guess);
    print("Secret:", secret, "Guess:", guess, "Hint:", hint);
}
