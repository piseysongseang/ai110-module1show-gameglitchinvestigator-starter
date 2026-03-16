def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

def check_guess(guess, secret):
    """Compare guess to secret and return (outcome, message).

    The outcome can be one of: "Win", "Too High", "Too Low".

    This function is resilient to comparisons between strings and numbers
    by attempting to coerce inputs to integers when possible. If coercion
    fails for either value, it falls back to lexicographic string comparison.
    """

    # Normalize both values for consistent comparisons.
    def _to_int(value):
        if isinstance(value, int):
            return value
        if isinstance(value, float):
            return int(value)
        if isinstance(value, str):
            try:
                return int(value)
            except ValueError:
                try:
                    return int(float(value))
                except ValueError:
                    return None
        return None

    guess_int = _to_int(guess)
    secret_int = _to_int(secret)

    if guess_int is not None and secret_int is not None:
        guess_val, secret_val = guess_int, secret_int
    else:
        guess_val, secret_val = str(guess), str(secret)

    if guess_val == secret_val:
        return "Win", "🎉 Correct!"
# Fix: logic of the hint messages was reversed before, now "Too High" gives a hint to go lower and "Too Low" gives a hint to go higher.
    if guess_val > secret_val:
        return "Too High" , "📉 Go LOWER!"

    return "Too Low" , "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
