"""Module to create a generic FSM (finite state machine) class"""
from src import logger


class FiniteAutomation:
    """Generic class to handle FSM problems"""
    """A finite automaton (FA) is a 5-tuple (Q, Σ, q0, F, δ), where
        Q is a finite set of states;
        Σ is a finite input alphabet;
        q0 ∈ Q is the initial state;
        F ⊆ Q is the set of accepting/final states; and
        δ: Q×Σ→Q is the transition function."""

    def __init__(self, q_0_state, transitions: dict):
        """
        Initializes the FSM.

        Parameters:
            q_0_state: Initial state.

            transitions: A nested dictionary with - 
                        key=current state, 
                        value=dictionary with key as input and value as resulting state.            
        """
        try:
            # Set current state as initial state
            self.current_state = q_0_state
            # Enforcing transitions as dictionary based on further handling in this module
            if not isinstance(transitions, dict):
                raise ValueError("transitions must be a dictionary.")
            if len(transitions) == 0:
                raise ValueError(
                    "transitions dictionary must have at least one item.")
            for _, values in transitions.items():
                if not isinstance(values, dict):
                    raise ValueError(
                        "transitions dictionary must be a nested dictionary.")
            self.transitions = transitions

        except ValueError as e:
            logger.exception("%s", str(e))
            raise

    def perform_transition(self, sigma_input):
        """
        Performs transition to a state based on input

        Parameters:
            sigma_input: Finite input character
        """
        try:
            # check if the input character is valid for the current state
            if sigma_input in self.transitions[self.current_state]:
                # Get the transition state value and set to current state (performing transition)
                self.current_state = self.transitions[self.current_state][sigma_input]
            else:
                raise ValueError(
                    "Invalid input %s for current state %s.", sigma_input, self.current_state)
        except ValueError as e:
            logger.exception("%s", str(e))
            raise

    def get_current_state(self):
        """
        For easier access to current state of FSM.
        """
        return self.current_state
