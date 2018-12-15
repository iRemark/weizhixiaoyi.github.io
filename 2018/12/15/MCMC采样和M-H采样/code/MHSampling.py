import random
from scipy.stats import norm
import matplotlib.pyplot as plt


def norm_dist_prob(theta):
    y = norm.pdf(theta, loc=3, scale=2)
    return y


def plot_res(pi):
    plt.scatter(pi, norm.pdf(pi, loc=3, scale=2))
    num_bins = 50
    plt.hist(pi, num_bins, normed=1, facecolor='red', alpha=0.7)
    plt.show()


def mh_sampling():
    # sampling
    t = 0
    T = 5000
    pi = [0 for i in range(T)]
    sigma = 1
    while t < T - 1:
        t = t + 1
        pi_star = norm.rvs(loc=pi[t - 1], scale=sigma, size=1, random_state=None)
        alpha = min(1, (norm_dist_prob(pi_star[0]) / norm_dist_prob(pi[t - 1])))

        u = random.uniform(0, 1)

        if u < alpha:
            pi[t] = pi_star[0]
        else:
            pi[t] = pi[t - 1]

    # plot
    plot_res(pi)


if __name__ == '__main__':
    mh_sampling()