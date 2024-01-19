from sklearn.metrics import (accuracy_score, recall_score,
                             precision_score, matthews_corrcoef, roc_auc_score)
import numpy as np


class Metrics:
    def __init__(self, y_true: np.ndarray, y_pred: np.ndarray, y_prob: np.ndarray) -> None:
        self.y_true = y_true
        self.y_pred = y_pred
        self.y_prob = y_prob

    def get_metrics(self) -> dict[str, float]:
        accuracy_val = accuracy_score(self.y_true, self.y_pred)
        recall_val = recall_score(self.y_true, self.y_pred)
        precision_val = precision_score(self.y_true, self.y_pred)
        specificity_val = recall_score(self.y_true, self.y_pred, pos_label=0)
        mcc_val = matthews_corrcoef(self.y_true, self.y_pred)
        roc_auc_value = roc_auc_score(self.y_true, self.y_prob)

        metrics_dict = {
            'accuracy': accuracy_val,
            'recall': recall_val,
            'precision': precision_val,
            'specificity': specificity_val,
            'mcc': mcc_val,
            'roc_auc': roc_auc_value
        }

        return metrics_dict
