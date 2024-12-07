"""Module to test ModThreeFiniteAutomation.
This will only be a function call without unit tests """
from src import logger
from src.Mod_three_finite_automation import ModThreeFiniteAutomation


class TestModThreeFiniteAutomation():
    """Class to test ModThreeFiniteAutomation methods."""

    def run(self):
        """
        Run tests for ModThreeFiniteAutomation methods.
        """
        logger.info(
            "********************Scenario: 1101 ********************")
        self.test_mod_three_compute_remainder('1101')
        logger.info(
            "********************Scenario: 1110 ********************")
        self.test_mod_three_compute_remainder('1110')
        logger.info(
            "********************Scenario: 1111 ********************")
        self.test_mod_three_compute_remainder('1111')
        logger.info(
            "********************Scenario: 110 ********************")
        self.test_mod_three_compute_remainder('110')
        logger.info(
            "********************Scenario: 1010 ********************")
        self.test_mod_three_compute_remainder('1010')
        logger.info(
            "********************Scenario: 0000 ********************")
        self.test_mod_three_compute_remainder('0000')

    def run_negative_tests(self):
        """
        Run negative tests for ModThreeFiniteAutomation methods.
        """
        logger.info(
            "********************Scenario: blank string ********************")
        self.test_mod_three_compute_remainder('')

    def test_mod_three_compute_remainder(self, str_binary):
        """
        Test the compute_remainder method of ModThreeFiniteAutomation
        """
        try:
            mod_three_fa = ModThreeFiniteAutomation()
            remainder=mod_three_fa.compute_remainder(str_binary)
            logger.info("Remainder for binary string %s: %s",str_binary,remainder)
        except Exception as e:
            # not stopping at exception as
            # some test cases are expected to return exception
            logger.exception("Scenario failed: %s", str(e))


if __name__ == "__main__":
    test_mod_three_fa = TestModThreeFiniteAutomation()
    test_mod_three_fa.run()
    # commenting out negative test to avoid showing exceptions on intial run
    # test_mod_three_fa.run_negative_tests()
