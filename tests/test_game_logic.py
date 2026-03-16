import os
import sys

# Ensure the repository root is on sys.path so test imports work reliably.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_check_guess_handles_string_numbers():
    # Strings that represent numbers should compare numerically
    assert check_guess("10", "20")[0] == "Too Low"
    assert check_guess("30", "20")[0] == "Too High"
    assert check_guess("50", "50")[0] == "Win"


def test_check_guess_falls_back_to_string_comparison():
    # If values can't be coerced to numbers, compare lexicographically
    assert check_guess("b", "a")[0] == "Too High"
    assert check_guess("a", "b")[0] == "Too Low"


def test_parse_guess_invalid_inputs():
    assert parse_guess(None) == (False, None, "Enter a guess.")
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess("not a num") == (False, None, "That is not a number.")


def test_parse_guess_decimal_values():
    ok, value, err = parse_guess("3.14")
    assert ok is True
    assert value == 3
    assert err is None


def test_update_score_win_and_penalties():
    # Winning gives points based on attempt number, but never below 10
    assert update_score(0, "Win", 0) == 90
    assert update_score(0, "Win", 9) == 10

    # Too high alternates between +5 and -5 depending on attempt parity
    assert update_score(0, "Too High", 1) == -5
    assert update_score(0, "Too High", 2) == 5

    # Too low always penalizes
    assert update_score(0, "Too Low", 1) == -5


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Unknown") == (1, 100)
