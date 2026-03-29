import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# --- Q1: Organizing Data ---
# Adjusting data based on Student ID: 220011230
st_no_last_2 = 30
data = [
    st_no_last_2 + 200, 147, 296, 230, 215, 150, 171, 215, 211, 228, 155, 236, 267, 192, 204, 
    185, 126, 212, 198, 200, 213, 224, 191, 210, 231, 196, 198, 221, 210, 215, 257, 193, 208, 
    271, 244, 278, 213, 198, 224, 220, 170, 181, 226, 178, 173, 246, 181, 251, 287, 207, 218, 
    217, 284, 158, 250, 249, 226, 234, 208, 225, 210, 260, 137, 139, 205, 189, 222, 245, 219, 
    228, st_no_last_2 + 180, 237, 214, 217, 233, 185, 221, 235, 267, 209
]

print("--- Q1: Descriptive Statistics ---")
print(f"Mean: {np.mean(data):.2f}")
print(f"Median: {np.median(data)}")
print(f"Mode: {stats.mode(data, keepdims=True).mode[0]}")
print(f"Std Dev: {np.std(data, ddof=1):.2f}")
print(f"Skewness: {stats.skew(data):.2f}")
print(f"Kurtosis: {stats.kurtosis(data):.2f}")
print(f"Range: {np.max(data) - np.min(data)}")

# Histogram
plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Material Strength')
plt.show()

# --- Q2: Probability (Hinges) ---
# n=5, p=0.15
n, p = 5, 0.15
prob_1 = stats.binom.pmf(1, n, p)
prob_2_or_less = stats.binom.cdf(2, n, p)
prob_2_or_more = 1 - stats.binom.cdf(1, n, p)

print(f"\n--- Q2: Hinges Probabilities ---")
print(f"P(X=1): {prob_1:.4f}")
print(f"P(X<=2): {prob_2_or_less:.4f}")
print(f"P(X>=2): {prob_2_or_more:.4f}")

# --- Q3: Normal Distribution (HDTV Warranty) ---
# Mean = 36.84, SD = 3.34, Bottom 10%
mu, sigma = 36.84, 3.34
warranty_limit = stats.norm.ppf(0.10, mu, sigma)
print(f"\n--- Q3: HDTV Warranty ---")
print(f"Warranty limit (10% fail): {warranty_limit:.2f} months")

# --- Q4: Hypothesis Testing (IUT Study Time) ---
# Claim: Mean != 3.0, n=50, x_bar=2.9, s=0.5, alpha = (1+0)% = 1%
last_digit = 0
alpha = (1 + last_digit) / 100
mu_0 = 3.0
n_samp = 50
x_bar = 2.9
s_samp = 0.5

z_stat = (x_bar - mu_0) / (s_samp / np.sqrt(n_samp))
p_val = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print(f"\n--- Q4: IUT Hypothesis Test ---")
print(f"Z-statistic: {z_stat:.4f}, P-value: {p_val:.4f}")
print("Result:", "Reject H0" if p_val < alpha else "Fail to reject H0")

# --- Q5: T-Distribution (WX Golf Ltd) ---
# mu=42.3, n=11, x_bar=40.6, s=2.7, alpha=0.10 (One-tailed: Faster)
mu_h0 = 42.3
n_t = 11
x_bar_t = 40.6
s_t = 2.7
t_stat = (x_bar_t - mu_h0) / (s_t / np.sqrt(n_t))
p_val_t = stats.t.cdf(t_stat, df=n_t-1)

print(f"\n--- Q5: WX Golf Assembly ---")
print(f"T-statistic: {t_stat:.4f}, P-value: {p_val_t:.4f}")
print("Result:", "Reject H0 (Method is faster)" if p_val_t < 0.10 else "Fail to reject H0")