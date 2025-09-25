# A1 — Guessing Game (cloud-ready without changing core logic)

enum Hint { HIGHER, LOWER, CORRECT }

def judge(secret: int, guess: int) -> Hint {
    if guess < secret { return Hint.HIGHER; }
    if guess > secret { return Hint.LOWER; }
    return Hint.CORRECT;
}

with entry {
    # Demo round (static values so it runs identically locally and in the cloud)
    let secret = 57;
    let guess  = 72;

    let hint = judge(secret, guess);

    print("Secret:", secret, "Guess:", guess, "Hint:", hint);
}
