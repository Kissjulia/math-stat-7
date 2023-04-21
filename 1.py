# Даны две  независимые выборки. Не соблюдается условие нормальности
#
# x1  380,420, 290
#
# y1 140,360,200,900
#
# Сделайте вывод по результатам, полученным с помощью функции
import numpy as np
import scipy.stats as stats
x1=np.array([380,420,290])
y1=np.array([140,360,200,900])
alpha=0.05
stats.mannwhitneyu(x1, y1)
# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)
# pvalue > alfa (0,05) статистически значимых различий нет, H0 не отвергаем