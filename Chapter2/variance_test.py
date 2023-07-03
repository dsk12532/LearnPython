import numpy as np
import pandas as pd

# Data table of years of study and annual income
# ID | years_of_study | annual_income
data = np.array([[1, 12, 480], [2, 16, 520], [3, 18, 760], [4, 16, 620], [5, 12, 590], [
                6, 10, 370], [7, 14, 690], [8, 16, 950], [9, 12, 610], [10, 12, 480]])

# 2-2 (1)
mean_of_years_of_study = data[:, 1].mean()
print("mean of years of study:", mean_of_years_of_study)

mean_of_annual_income = data[:, 2].mean()
print("mean of annual income:", mean_of_annual_income)

# 2-2 (2)
population_variance_of_years_of_study = data[:, 1].var(ddof=0)
print("population variance of years of study:", population_variance_of_years_of_study)

unbiased_variance_of_years_of_study = data[:, 1].var(ddof=1)
print("unbiased variance of years of study:", unbiased_variance_of_years_of_study)

# 2-3
student_id, years_of_study, salary = data.T

cov_matrix = np.cov(years_of_study, salary)
correlation_matrix = np.corrcoef(years_of_study, salary)

print("Covariance Matrix:")
print(cov_matrix)

print("Correlation Matrix:")
print(correlation_matrix)


# Empirical Analysis
df = pd.read_csv("Chapter2/2_income.csv")

# 2-A
income_mean = df['income'].mean()
print("Mean of income:", income_mean)

income_population_variance = df['income'].var(ddof=0)
print("Unviased variance of income:", income_population_variance)

income_unviaced_variance = df['income'].var(ddof=1)
print("Unviased variance of income:", income_unviaced_variance)

# 2-B
yeduc_mean = df['yeduc'].mean()
print("Mean of yeduc:", yeduc_mean)

yeduc_population_variance = df['yeduc'].var(ddof=0)
print("Unviased variance of yeduc:", yeduc_population_variance)

yeduc_unviaced_variance = df['yeduc'].var(ddof=1)
print("Unviased variance of yeduc:", yeduc_unviaced_variance)

# 2-C

# pandas の cov メソッドには ddof パラメータはないが、内部的には ddof=1 (標本共分散) を使って計算が行われている.
# しかし、母共分散を計算したい場合は、独自の関数を作成して計算することができる.

# def population_cov(df, col1, col2):
#    n = len(df)
#    return (df[col1] * df[col2]).sum() / n - df[col1].mean() * df[col2].mean()
# population_covariance = population_cov(df, 'column1', 'column2')

# この population_cov 関数は、データフレーム df の col1 と col2 列の間の母共分散を計算する.

# 注意すべき点として、通常の状況下では標本共分散（つまり ddof=1）を使うことが一般的であり、母共分散を計算する必要はあまりない.
# この理由は、通常、我々が手にするデータは母集団全体から取得したものではなく、母集団からの標本であるためである.
# したがって、データ分析における共分散の計算では、通常は df.cov() をそのまま使用する.

yeduc_and_income_cov_matrix = df.cov()
print("Yeduc and Income Covariance Matrix:")
print(yeduc_and_income_cov_matrix)

# 2-D
yeduc_and_income_corr_matrix_with_pandas = df.corr(method='pearson')
print("Yeduc and Income Correlation Matrix with Pandas:")
print(yeduc_and_income_corr_matrix_with_pandas)
