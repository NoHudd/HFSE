"""Test isolation for the process-wide event bus.

`event_bus` and `state_manager` are module-level singletons, so anything a test
leaves subscribed keeps reacting to every later test's events. That is not
theoretical: a GameSession that is never closed leaves its engine on
COMMAND_ENTERED, so a later test's `quit` runs twice — once in its own engine and
once in the stale one — and the stale engine's GAME_QUIT flips a flag the live
test is asserting on.

This fixture restores the bus to whatever it looked like before each test, so a
leak inside one test cannot change the outcome of another. It deliberately does
not fail on leaks: several tests share a session across a module on purpose, and
the leaks that actually matter are pinned directly by test_restart_leak.py.
"""
from __future__ import annotations

import pytest

from src.events import event_bus
from src.game_states import GameState
from src.state_manager import state_manager


@pytest.fixture(autouse=True)
def _isolate_event_bus():
    before = {etype: list(cbs) for etype, cbs in event_bus._listeners.items()}
    yield
    event_bus._listeners.clear()
    event_bus._listeners.update({etype: list(cbs) for etype, cbs in before.items()})
    event_bus.clear_history()


@pytest.fixture(autouse=True)
def _reset_game_state():
    """Leave the shared StateManager where each test found it."""
    before = state_manager.current_state
    yield
    if state_manager.current_state != before:
        state_manager.set_state(before, emit_event=False)
    if state_manager.current_state not in (GameState.MENU, GameState.PLAYING):
        state_manager.set_state(GameState.MENU, emit_event=False)
