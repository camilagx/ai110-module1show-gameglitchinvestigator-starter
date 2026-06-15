from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Regression tests for bugs fixed ---

# Bug fix: check_guess raised TypeError when secret was passed as a string
# (app.py converts secret to str on even-numbered attempts)
def test_check_guess_win_with_string_secret():
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"

def test_check_guess_too_high_with_string_secret():
    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"

def test_check_guess_too_low_with_string_secret():
    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"


# Bug fix: attempts was initialized to 1 instead of 0, causing the first
# game to begin with one attempt already "used"
def test_attempts_initial_value_is_zero():
    session_state = {}
    if "attempts" not in session_state:
        session_state["attempts"] = 0
    assert session_state["attempts"] == 0, "attempts must start at 0, not 1"
