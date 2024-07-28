# this script is computing probability of
# contacting other civilization in our galaxy
# in 1000 years. Based on Drake's equation

# DRAKE EQUATION (extended)
# N = Ro * fp * ne * fL * fi * fc * L
# N - number of possible contactable civilizations in our galaxy
# Ro - average rate of sun like star formation in our galaxy
# fp - fraction of stars with planetary systems
# ne - average number of planets that could support life per star with planetary system
# fL - fraction of planets that could support life that actually develop life
# fi - fraction of planets with life that develop intelligent life
# fc - fraction of civilizations that develop technology that releases detectable signs of their existence into space
# L - length of time civilizations release detectable signals into space

# drake's solution (1961)
# Ro = 1/year
# fp = 0.2
# ne = 1
# fL = 1
# fi = 0.01
# fc = 1
# L = 10 000 years
N = 1 * 0.2 * 1 * 1 * 0.01 * 1 * 10000
print("Number of possible contactable civilizations in our galaxy by Drake in 1961: ", N)

# solution 2024 (optimistic approach)
# Ro
# https://ar5iv.labs.arxiv.org/html/2211.05573
# 1.65 to 2.7 solar masses per year
# https://ui.adsabs.harvard.edu/abs/2001JRASC..95...32L/abstract
# Most stars (76%) are in the main sequence, 24% are white dwarfs, and the rest (0.6%) are on the giant branch
# star have to be on main sequence of hr diagram
Ro = ((1.65 + 2.7) / 2) * 0.76

# fp
# now we know that almost every star has planetary system
fp = 1

# ne
# exoplanets discovered
# https://spaceexplored.com/2024/04/10/how-many-exoplanets-are-there-discovered/
# 5602 exoplanets discovered in 4166 planetary systems
# https://en.wikipedia.org/wiki/List_of_potentially_habitable_exoplanets
# 55 potentially habitable exoplanets
ne = 55 / 5062

# fL
# for to life to develop planet has to have few favorable conditions
# it has to have tilt
# it has to have stable moon
# it has to have magnetic field
# it has to have tectonic activity
# these are very optimistic probabilities based on our solar system
# real probability would be much lower
ftilt = 2/8
fmoon = 1/4
fmagnetic = 2/4
ftectonic = 1/4
fL = ftilt * fmoon * fmagnetic * ftectonic

# there is an information that which Drake didn't know
# that there is an habitable zone in galaxy
# star have to be 22800 - 29500 light years from center of galaxy
# https://en.wikipedia.org/wiki/Galactic_habitable_zone
# radius of galaxy is 52000 light years
# number of stars in habitable zone
# non-habitable zone surface
nhzs = (3.14 * (29500 - 22800)) ** 2
# all galaxy surface
ags = 3.14 * 52000 ** 2
# fraction of stars in habitable zone
fhz = nhzs / ags

# fi
# this is probability that intelligent life will develop
# I suppose that creatures have to be able to use fire
# so it has to be not a ocean world
# it can't be ice giant, hot jupiter or lava world
# so it has to be rocky planet
# the distribution of planets is like this
# hot jupiters 30%
# ice giants 15%
# ocean worlds 20%
# lava worlds 10%
# rocky planets 25%
fi = 0.25

# fc
# we will use very optimistic approach
# that every civilization will develop technology
fc = 1

# L
# civilizations lifespan by history (already extinct)
egypt = 3000
sumer = 1200
indus = 900
babylon = 1200
greece = 800
rome = 1200
byzantium = 1100
mayans = 2000
ottomans = 600
L = (egypt + sumer + indus + babylon + greece + rome + byzantium + mayans + ottomans) / 9
# assuming that technology can be transfered between civilizations
# i will use 10x longer lifespan
L = L * 10

N = Ro * fp * ne * fL * fhz * fi * fc * L

print("Number of possible contactable civilizations in our galaxy by me in 2024: ", N)

# communication probability in 1000 years
R = 1000
# galaxy radius
Rg = 52000
# galaxy thickness
Tg = 1000
# habitable zone radius
Rh = (29500 + 22800) / 2
# galaxy volume
Vg = 3.14 * Rg ** 2 * Tg
# habitable zone volume
Vh = Vg - ((3.14 * Rh ** 2) * Tg)
# signal range volume
Vsr = (3/4) * 3.14 * R ** 3
# probability of contacting civilization in 1000 years
P = N * (Vsr / Vh)
print("Probability of contacting other civilization in our galaxy in 1000 years is: 1:", 1/P)

# communication probablity is very low
# probability of winning lottery is 1:13000000
# and someone won it
# but we have only one chance to contact other civilization
# and there were many tickets bought
# contact is impossible
# WE ARE ALONE
