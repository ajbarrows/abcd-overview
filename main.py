import numpy as np
import matplotlib.pyplot as plt

from math import gamma
from fMRI.abcd_hrf import *


def plot_hrf():
    plt.plot(abcd_hrf())
    plt.savefig('./fMRI/img/abcd_hrf.png', bbox_inches='tight')



if __name__ == "__main__":
    plot_hrf()