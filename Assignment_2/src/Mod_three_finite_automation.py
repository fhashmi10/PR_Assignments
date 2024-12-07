"""Module to create a MOD 3 FSM """
from src import logger
from src.finite_automation import FiniteAutomation


class ModThreeFiniteAutomation(FiniteAutomation):
    """Class to implement a MOD 3 FSM to compute remainder 
    of an unsigned binary integer divided by 3"""

    def __init__(self):
        # Define transitions for a mod 3 problem
        # Based on δ: Q×Σ→Q as the transition function
        # Key as state
        # Value as dictionary of transitions, where
        # key is input character
        # and value is state to transition to
        # values are based on diagram in assignment
        transitions = {
            0: {'0': 0, '1': 1},
            1: {'0': 2, '1': 0},
            2: {'0': 1, '1': 2}
        }
        # Define initial states for a mod 3 problem
        q_0_state = 0
        try:
            # Initialize super class
            super().__init__(q_0_state, transitions)
        except Exception as e:
            logger.exception("Exception occured: %s", str(e))

    def compute_remainder(self, str_binary: str):
        """
        Returns the remainder
        """
        try:
            if len(str_binary)==0:
                raise ValueError(
                        "Input binary string must not be empty.")
            for char in str_binary:
                self.perform_transition(sigma_input=char)
            return self.get_current_state()
        except Exception as e:
            logger.exception("Exception occured: %s", str(e))
            return None
