# A1 — Guessing Game (cloud-ready, no core-logic changes)

# The possible hints the game can return
enum Hint { HIGHER, LOWER, CORRECT }

# Pure game logic: compare guess against the secret and return a typed hint
def judge(secret: int, guess: int) -> Hint {
    if guess < secret { return Hint.HIGHER; }
    if guess > secret { return Hint.LOWER; }
    return Hint.CORRECT;
}

with entry {
    # --- Demo values (keep static for Step-5) ---
    # You can change these two ints to show different outcomes.
    let secret = 57;
    let guess  = 72;

    # Run one round and print the result
    let hint = judge(secret, guess);

    print("Secret:", secret, "Guess:", guess, "Hint:", hint);
}
