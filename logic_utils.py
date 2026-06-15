def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

# FIXME: Logic breasks here. Hint displayed to the user is switched.
# FIX: When guess is greater than secret, the string returned should be "Too High, Go Lower" and vise versa when the guess is less than the secret.
    try:
        if guess > secret:
            return "Too High", "Go 📉 LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # secret may be passed as a str; convert both to int for numeric comparison
        # FIXME: Logic breasks here. Even numbers are converted to a string. Thus, both the guess and the secret are compared lexiographically instead of numerically.
        # FIX: Both guess and secret should be converted to int before comparison. This ensures that the comparison is accurate and will provide the correct hint to the user.
        g = int(guess)
        s = int(secret)
        if g == s:
            return "Win", "🎉 Correct!"
        if g > s:
            return "Too High", "Go 📉 LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")