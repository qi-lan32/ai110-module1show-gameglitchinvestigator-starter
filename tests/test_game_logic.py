from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Hint message tests ---

def test_hint_correct_message():
    # Correct guess should return the "Correct!" hint message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_hint_too_high_message():
    # Guess above secret should return a "lower" hint message
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High", "📉 Go LOWER!"
    assert "LOWER" in message

def test_hint_too_low_message():
    # Guess below secret should return a "higher" hint message
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low", "📈 Go HIGHER!"
    assert "HIGHER" in message

def test_hint_uses_secret_not_guess():
    # Hint direction must be relative to the secret, not some fixed value
    outcome_high, _ = check_guess(90, 10)   # guess way above secret
    outcome_low,  _ = check_guess(1,  90)   # guess way below secret
    assert outcome_high == "Too High", "📉 Go LOWER!"
    assert outcome_low  == "Too Low", "📈 Go HIGHER!"

def test_hint_boundary_one_above():
    # secret=50, guess=51 → still "Too High"
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High", "📉 Go LOWER!"
    assert "LOWER" in message

def test_hint_boundary_one_below():
    # secret=50, guess=49 → still "Too Low"
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low", "📈 Go HIGHER!"
    assert "HIGHER" in message


# --- Attempt limit tests (via get_range_for_difficulty) ---

ATTEMPT_LIMIT_MAP = {"Easy": 6, "Normal": 8, "Hard": 5}

def test_attempt_limit_easy():
    assert ATTEMPT_LIMIT_MAP["Easy"] == 6

def test_attempt_limit_normal():
    assert ATTEMPT_LIMIT_MAP["Normal"] == 8

def test_attempt_limit_hard():
    assert ATTEMPT_LIMIT_MAP["Hard"] == 5

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 50

def test_range_unknown_difficulty_defaults():
    # An unrecognised difficulty should fall back to 1–100
    low, high = get_range_for_difficulty("Extreme")
    assert low == 1 and high == 100


# --- Error message tests (parse_guess) ---

def test_error_empty_string():
    ok, value, err = parse_guess("")
    assert not ok
    assert value is None
    assert err == "Enter a guess."

def test_error_none_input():
    ok, value, err = parse_guess(None)
    assert not ok
    assert value is None
    assert err == "Enter a guess."

def test_error_non_numeric_string():
    ok, value, err = parse_guess("abc")
    assert not ok
    assert value is None
    assert err == "That is not a number."

def test_error_special_characters():
    ok, value, err = parse_guess("!@#")
    assert not ok
    assert err == "That is not a number."

def test_no_error_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok
    assert value == 42
    assert err is None

def test_no_error_float_string_truncates():
    # Floats are accepted and truncated to int
    ok, value, err = parse_guess("7.9")
    assert ok
    assert value == 7
    assert err is None
