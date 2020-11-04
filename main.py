import numpy
from scipy import stats
import matplotlib.pyplot as plt

test_names = ['Andy', 'Martin', 'Zahara', 'Vuyo', 'Ziyaad']
test_scores = [12, 99, 65, 85, 42]
x_pos = [i for i, _ in enumerate(test_names)] # Labels
# labelling and visuals
plt.bar(x_pos, test_scores, color="blue")
plt.xlabel("Names")
plt.ylabel("Marks (%)")
plt.title("Python marks for 5 students")
plt.xticks(x_pos, test_names)
plt.show()
