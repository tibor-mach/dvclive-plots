from random import random
from dvclive import Live


with Live() as live:
    for i in range(10):
        live.log_metric("acc", i + random() - 0.5)

        live.next_step()

    y_true = [0, 0, 1, 1]
    y_pred = [1, 0, 1, 0]

    live.log_sklearn_plot(
        kind="confusion_matrix",
        labels=y_true,
        predictions=y_pred,
        name="confusion_matrix.json",
        )
