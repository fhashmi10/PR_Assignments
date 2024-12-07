"""Module to test Model Evaluator.
This will only be a function call without unit tests """
from src import logger
from src.model_evaluator import ModelEvaluator

# Input Data Structure - Reason for choosing dictionary
# ************************************************************************************************************************************************************************************-
# A list of tuples could've been used as well to benefit from the fact that it's ordered.
# list of tuples - [(10, 80, 5, 5),(8, 82, 8, 2),..]
# However you wouldn't know what is what just by looking at the data

# A dictionary was chosen as data structure will be more clear to understand by just looking at the data.
# We can sort dictionary by keys in code to make sure its ordered.
# dictionary - {0.01:{'TP':10,'TN':80,'FP':5,'FN':5}, }
# ************************************************************************************************************************************************************************************-


class TestModelEvaluator():
    """Class to test ModelEvaluator methods."""

    def run(self):
        """
        Run tests for ModelEvaluator methods.
        """
        logger.info(
            "********************Scenario: Best Threshold Found ********************")
        thresholds_data = {0.1: {'TP': 10, 'TN': 80, 'FP': 5, 'FN': 5},
                           0.2: {'TP': 20, 'TN': 75, 'FP': 10, 'FN': 7},
                           0.3: {'TP': 30, 'TN': 70, 'FP': 5, 'FN': 8},
                           0.4: {'TP': 40, 'TN': 65, 'FP': 10, 'FN': 9},
                           0.5: {'TP': 50, 'TN': 60, 'FP': 5, 'FN': 8},
                           0.6: {'TP': 60, 'TN': 55, 'FP': 10, 'FN': 5},
                           0.7: {'TP': 70, 'TN': 50, 'FP': 5, 'FN': 3},
                           0.8: {'TP': 80, 'TN': 45, 'FP': 10, 'FN': 11},
                           0.9: {'TP': 90, 'TN': 40, 'FP': 5, 'FN': 10}}
        self.test_best_threshold_for_recall(thresholds_data)

        logger.info(
            "********************Scenario: Best Threshold Not Found********************")
        thresholds_data = {0.1: {'TP': 10, 'TN': 80, 'FP': 5, 'FN': 50},
                           0.2: {'TP': 20, 'TN': 75, 'FP': 10, 'FN': 70},
                           0.3: {'TP': 30, 'TN': 70, 'FP': 5, 'FN': 80},
                           0.4: {'TP': 40, 'TN': 65, 'FP': 10, 'FN': 90},
                           0.5: {'TP': 50, 'TN': 60, 'FP': 5, 'FN': 80},
                           0.6: {'TP': 60, 'TN': 55, 'FP': 10, 'FN': 50},
                           0.7: {'TP': 70, 'TN': 50, 'FP': 5, 'FN': 70},
                           0.8: {'TP': 80, 'TN': 45, 'FP': 10, 'FN': 70},
                           0.9: {'TP': 90, 'TN': 40, 'FP': 5, 'FN': 70}}
        recall_value = 0.9
        self.test_best_threshold_for_recall(thresholds_data, recall_value)

        logger.info(
            "********************Scenario: Zero FN and TP: No Exception ********************")
        thresholds_data = {0.1: {'TP': 0, 'TN': 75, 'FP': 10, 'FN': 0},
                           0.2: {'TP': 20, 'TN': 75, 'FP': 10, 'FN': 7},
                           0.3: {'TP': 30, 'TN': 70, 'FP': 5, 'FN': 8},
                           0.4: {'TP': 40, 'TN': 65, 'FP': 10, 'FN': 9},
                           0.5: {'TP': 50, 'TN': 60, 'FP': 5, 'FN': 8},
                           0.6: {'TP': 60, 'TN': 55, 'FP': 10, 'FN': 5},
                           0.7: {'TP': 70, 'TN': 50, 'FP': 5, 'FN': 3},
                           0.8: {'TP': 80, 'TN': 45, 'FP': 10, 'FN': 11},
                           0.9: {'TP': 90, 'TN': 40, 'FP': 5, 'FN': 10}}
        recall_value = 0.9
        self.test_best_threshold_for_recall(thresholds_data, recall_value)

        logger.info(
            "********************Scenario: Best Threshold Different Recall value********************")
        thresholds_data = {0.1: {'TP': 10, 'TN': 80, 'FP': 5, 'FN': 5},
                           0.2: {'TP': 20, 'TN': 75, 'FP': 10, 'FN': 7},
                           0.3: {'TP': 30, 'TN': 70, 'FP': 5, 'FN': 8},
                           0.4: {'TP': 40, 'TN': 65, 'FP': 10, 'FN': 9},
                           0.5: {'TP': 50, 'TN': 60, 'FP': 5, 'FN': 8},
                           0.6: {'TP': 60, 'TN': 55, 'FP': 10, 'FN': 5},
                           0.7: {'TP': 70, 'TN': 50, 'FP': 5, 'FN': 3},
                           0.8: {'TP': 80, 'TN': 45, 'FP': 10, 'FN': 11},
                           0.9: {'TP': 90, 'TN': 40, 'FP': 5, 'FN': 10}}
        recall_value = 0.6
        self.test_best_threshold_for_recall(thresholds_data, recall_value)

    def run_negative_test(self):
        """
        Run negative tests for ModelEvaluator methods.
        """
        logger.info(
            "********************Scenario: Blank dictionary********************")
        thresholds_data = {}
        recall_value = 0.9
        self.test_best_threshold_for_recall(thresholds_data, recall_value)

        logger.info(
            "********************Scenario: Dictinary Not Nested ********************")
        thresholds_data = {0.1: 10,
                           0.2: {'TP': 20, 'TN': 75, 'FP': 10, 'FN': 7},
                           0.3: {'TP': 30, 'TN': 70, 'FP': 5, 'FN': 8},
                           0.4: {'TP': 40, 'TN': 65, 'FP': 10, 'FN': 9},
                           0.5: {'TP': 50, 'TN': 60, 'FP': 5, 'FN': 8},
                           0.6: {'TP': 60, 'TN': 55, 'FP': 10, 'FN': 5},
                           0.7: {'TP': 70, 'TN': 50, 'FP': 5, 'FN': 3},
                           0.8: {'TP': 80, 'TN': 45, 'FP': 10, 'FN': 11},
                           0.9: {'TP': 90, 'TN': 40, 'FP': 5, 'FN': 10}}
        recall_value = 0.9
        self.test_best_threshold_for_recall(thresholds_data, recall_value)

    def test_best_threshold_for_recall(self, thresholds_data: dict, recall_value: float = 0.9):
        """
        Test the find_best_threshold_for_recall method.
        """
        try:
            model_evaluator = ModelEvaluator(thresholds_data)
            model_evaluator.find_best_threshold_for_recall(recall_value)
        except Exception as e:
            # not stopping at exception as
            # some test cases are expected to return exception
            logger.exception("Scenario failed: %s", str(e))


if __name__ == "__main__":
    test_model_evaluator = TestModelEvaluator()
    test_model_evaluator.run()
    # commenting out negative test to avoid showing exceptions on intial run
    # test_model_evaluator.run_negative_test()
