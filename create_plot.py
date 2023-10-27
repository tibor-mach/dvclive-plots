from random import random
from dvclive import Live


with Live() as live:
    for i in range(10):
        live.log_metric("acc", i + random() - 0.5)

        live.next_step()
