"""Module to evaluate different types of models (a binary classification for this assignment)"""
from src import logger


class ModelEvaluator:
    """ModelEvaluator class to evaluate models"""

    def __init__(self, thresholds_data: dict):
        """
        Initializes Model Evaluator with input thresholds data.

        Parameters:
            thresholds_data: a dictionary of TP, TN, FP, FN values for various thresholds
        """
        try:
            if not isinstance(thresholds_data, dict):
                raise ValueError("Input must be a dictionary.")
            if len(thresholds_data) == 0:
                raise ValueError(
                    "Input dictionary must have at least one item.")
            for _, values in thresholds_data.items():
                if not isinstance(values, dict):
                    raise ValueError(
                        "Input dictionary must be a nested dictionary.")
            self.thresholds_data = thresholds_data
        except ValueError as e:
            logger.exception("%s", str(e))
            raise

    def find_best_threshold_for_recall(self, recall_value: float = 0.9) -> float:
        """
        Finds the best threshold that yeilds the best recall with recall>=recall_value 
        recall_value is defaulted to 0.9 when no recall_value is specified.

        Parameters:
            recall_value (float): The minimum recall value to yeild

        Returns: 
            float: The best threshold that provides best recall >=recall_value.
                    Returns None when no threshold exists
        """
        try:
            best_threshold = None
            best_recall = 0

            # Dictionary is sorted by keys,
            # so that the lowest threshold where recall is reached is returned.
            for threshold, confusion_matrix in sorted(self.thresholds_data.items()):
                # Recall forumla is TP/(TP+FN), so lets calculate TP and FN values.
                try:
                    true_positives = confusion_matrix['TP']
                    false_negatives = confusion_matrix['FN']
                except KeyError:
                    logger.exception("Could not find TP and FP for threshold: %s", threshold)
                    return None

                denominator = true_positives + false_negatives
                recall = true_positives/denominator if denominator > 0 else 0
                # Decided to handle zero denominator
                # instead of raising exception to find other best thresholds

                if recall >= recall_value and recall > best_recall:
                    best_recall = recall
                    best_threshold = threshold

            if best_threshold is None:
                logger.warning("No threshold found.")
            else:
                logger.info("Best threshold for recall >= %s is: %s",
                            recall_value, best_threshold)
            return best_threshold

        except Exception as e:
            logger.exception("Error finding best threshold: %s", str(e))
            return None
