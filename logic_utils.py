def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    Harder difficulty = wider range of possible numbers.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        # Allow "42" and "42.0" but reject true text.
        value = int(float(raw))
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    outcome is one of: "Win", "Too High", "Too Low"
    """
    # FIXME: Logic used to break here. The old version had a try/except that
    # caught the int-vs-str TypeError and silently compared them as strings,
    # giving backwards hints. Now both values are ints, so the compare is clean.
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    Winning early is worth more; a wrong guess costs a small penalty.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        return current_score + max(points, 10)

    # Any wrong guess (Too High or Too Low) costs the same.
    return current_score - 5
