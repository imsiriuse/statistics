# this script is computing the probability of >8 sons
# coming back from world war II to mother in Russia.

import math

returned_children = 8
avg_children = 6
# N. Savchenko in his study about russia demographics
# found that in the 1939 census there were 838 men for 1000 woman
# https://iq.hse.ru/en/news/177669270.html
# mw_ratio = man/woman
mw_ratio = 0.838

# total population in russia in 1939
# https://en.wikipedia.org/wiki/Demographics_of_the_Soviet_Union
total_population = 168524000
# average life expectancy in russia in 1939 was 45 years for woman
# if the childbearing age is 15-45, then the estimated generations
# in this society is 3 thus:grandmothers, mothers and children

# number of mothers in russian population
# assuming that all adult woman are mothers
# 1gen + 2gen + 3gen = total_population
# gen = woman + men
# gen = woman + woman * mw_ratio
# gen = woman * (1 + mw_ratio)
# grandmothers * (1 + mw_ratio) + mothers * (1 + mw_ratio) + children = total_population
# children = mothers * avg_children
# grandmothers * avg_children = mothers * (1 + mw_ratio)
# grandmothers =  mothers * (1 + mw_ratio) / avg_children
# (1 + mw_ratio) * (mothers * (1 + mw_ratio)) / avg_children + mothers * (1 + mw_ratio) + mothers * avg_children = total_population
# mothers * ((1 + mw_ratio)*(1 + mw_ratio)/avg_children + (1 + mw_ratio) + avg_children) = total_population
mothers = total_population / ((1 + mw_ratio)*(1 + mw_ratio)/avg_children + (1 + mw_ratio) + avg_children)
grandmothers = mothers * (1 + mw_ratio) / avg_children
adult_woman = mothers + grandmothers
print("Adult women: ", adult_woman)

# probability of the child being drafted
man_soldiers = 34500000
woman_soldiers = 800000
all_soldiers = man_soldiers + woman_soldiers
# P(draft|woman) = woman_soldiers / soldiers
# P(draft|man) = man_soldiers / soldiers
# P(man) = mw_ratio / (mw_ratio + 1)
# P(woman) = 1 / (wm_ratio + 1)
# P(draft) = P(draft|woman) * P(woman) + P(draft|man) * P(man)
Pdw = woman_soldiers / all_soldiers
Pdm = man_soldiers / all_soldiers
Pm = mw_ratio / (mw_ratio + 1)
Pw = 1 / (mw_ratio + 1)
Pd = Pdw * Pw + Pdm * Pm
print("P(draft): ", Pd)

# probability of the child being drafted and returning
dead_soldiers = 8700000
# P(return) = (all_soldiers - dead_soldiers) / all_soldiers
# P(return|draft) = P(return) * P(draft)
# avg_returning_children = P(return|draft) * avg_children //(for 1 mother)
avg_returning_children = Pd * ((all_soldiers - dead_soldiers) / all_soldiers) * avg_children
print("Avg returning children: ", avg_returning_children)

# probability of having 8 or more children
# using normal distribution
# estimate that sigma is 1/4 of the mean
sigma = avg_children / 4
# compute the probability of having exactly 8 children
z_score = (returned_children - avg_children) / sigma
# compute the probability of having more than 8 children
cumulative_probability = 1 - 0.5 * (1 + math.erf(z_score / math.sqrt(2)))
mothers_with_enough_children = adult_woman * cumulative_probability
print("Mothers with enough children: ", mothers_with_enough_children)

# probability of returning more than 8 children
# using normal distribution
# estimate that sigma is 1/4 of the mean
sigma = avg_returning_children / 4
# compute the probability of returning exactly 8 children
z_score = (returned_children - avg_children) / sigma
# compute the probability of returning more than 8 children
cumulative_probability = 1 - 0.5 * (1 + math.erf(z_score / math.sqrt(2)))
returns_occured = mothers_with_enough_children * cumulative_probability

print("Number of mothers that had ", returned_children, "or more children returned: ", returns_occured)
print("Probability of happening: 1 :" , adult_woman / returns_occured)
























