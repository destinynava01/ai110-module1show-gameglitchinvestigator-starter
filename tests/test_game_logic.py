import os
import pytest
from logic_utils import check_guess

APP_PATH =os.path.join(os.path.dirname(__file__), "..", "app.py")

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_tells_player_to_go_lower():
    # Regression: the hint was inverted and said "Go HIGHER!" for a guess above the secret
    _, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_tells_player_to_go_higher():
    # Regression: the hint was inverted and said "Go LOWER!" for a guess below the secret
    _, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_hint_boundaries():
    # Off-by-one guesses should still point the right way
    assert "LOWER" in check_guess(51, 50)[1]
    assert "HIGHER" in check_guess(49, 50)[1]


def _button(at, label_part):
    return next(b for b in at.button if label_part in b.label)


def test_new_game_resets_state_after_game_over():
    # Regression: New Game left status as "won"/"lost", so the app stayed stuck on game over
    AppTest = pytest.importorskip("streamlit.testing.v1").AppTest

    at = AppTest.from_file(APP_PATH).run()
    at.session_state["status"] = "lost"
    at.session_state["history"] = [1, 2, 3]
    at.session_state["score"] = -15
    at.session_state["attempts"] = 8
    at.run()
    assert at.error  # game over message is shown

    _button(at, "New Game").click().run()

    assert at.session_state["status"] == "playing"
    assert at.session_state["history"] == []
    assert at.session_state["score"] == 0
    assert at.session_state["attempts"] == 0
    assert not at.error  # no longer stuck on game over


def test_new_game_secret_respects_difficulty_range():
    # Regression: New Game always picked from 1-100, ignoring the selected difficulty
    AppTest = pytest.importorskip("streamlit.testing.v1").AppTest

    at = AppTest.from_file(APP_PATH).run()
    at.sidebar.selectbox[0].select("Easy").run()
    for _ in range(30):
        _button(at, "New Game").click().run()
        assert 1 <= at.session_state["secret"] <= 20
