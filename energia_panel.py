import numpy as np

I_sc = [[0, 0], [200, 0.5], [400, 1.2], [600, 1.5], [800, 2], [1000, 2.5]]
V_oc = [[i, 100] for i in range(0, 26)] + [[30, 90], [35, 75], [40, 60]] + [[i, 40] for i in range(45, 151)]

x = [i[0] for i in V_oc]
y = [i[1] for i in V_oc]

"""
import numpy as np
import matplotlib.pyplot as plt
# Plot a straight diagonal line with ticked style path
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, label="Line")


ax.legend()

plt.show()
"""
def get_mn(x1, y1, x2, y2):
    m = (y2 - y1)/(x2 - x1)
    n = y2 - m * x2
    return m, n

def get_value(x, values):
    for idx in range(len(values) - 1):
        current, next = values[idx], values[idx + 1]
        current_t, next_t = current[0], next[0]
        #print(current_t, next_t)
        if current_t <= x < next_t:
            current_v, next_v = current[1], next[1]
            m, n = get_mn(current_t, current_v, next_t, next_v)
            value = m * x + n
            return value


## Irradiancia
summer = [0, 0,	0, 0, 0, 0, 8.8859,	68.12461333, 291.52129, 526.21198, 729.51397, 890.3392, 981.3667467, 995.6460633, 942.40046, 822.6537267, 644.1712933, 427.1989567, 201.1726167, 30.59198, 0, 0, 0, 0]
fall =   [0, 0, 0, 0, 0, 0, 0, 3.830516667, 123.16564, 378.7462167, 553.6018267, 689.1563767, 754.28945, 779.2412667, 729.61491, 634.26789, 475.9197767, 301.93824, 78.68181333, 0.85624 ,0, 0, 0, 0]
winter = [0, 0, 0, 0, 0, 0,	0, 0, 16.70059333, 232.8532133, 361.69518, 450.30034, 479.5454933, 507.8528767, 485.37603, 434.8992833, 328.1666367, 220.7518533, 3.39585333, 0, 0, 0, 0, 0]
spring = [0, 0, 0, 0, 0, 0,	6.411916667, 72.16724667, 271.8452, 460.4412033, 624.6427133, 754.1921367, 809.2682333, 809.1165633, 738.4447633, 622.3184933, 465.28004, 273.0013433, 107.74166, 5.557056667, 0, 0, 0, 0]

irr_typical_days = [summer, fall, winter, spring]


## Temperatura

summer = [16.66799, 16.03647333, 15.42200333, 14.93718, 14.56888, 14.00155, 14.28533667, 15.62754667, 17.83690333, 20.32003667, 22.83341667, 25.17112333, 26.91431667, 28.16884333, 28.76132333, 28.35928667, 27.55235, 26.51037667, 25.11953, 23.12648667, 21.04744, 19.51417, 18.34668333, 17.43480667]
fall =   [12.68455333, 12.12553667, 11.60707, 11.16800667, 10.83918667, 10.58893667, 10.14373333, 10.35446333, 11.55782, 13.72287333, 16.30155667, 18.62228333, 20.66222667, 22.12987667, 23.02603333, 23.05518333, 22.26307333, 20.86164667, 18.91437, 17.11253333, 15.82919667, 14.80844333, 13.91496, 13.22944]
winter = [7.571626667, 7.21006, 6.896653333, 6.591713333, 6.32097, 6.103143333, 5.9396, 5.525186667, 6.030076667, 7.691563333, 9.68753, 11.77819333, 13.55514333, 15.02605, 15.87455, 16.03531667, 15.41590333, 13.87986, 12.02218, 10.71321667, 9.807963333, 9.103983333, 8.523153333, 8.007173333]
spring = [11.22041, 10.65799, 10.17517667, 9.716236667, 9.34276, 8.9439, 8.767786667, 9.72994, 11.74203667, 14.17875333, 16.49450333, 18.6219, 20.39092667, 21.63087, 22.20581333, 22.14179667, 21.48144667, 20.32521, 18.71178333, 16.64095, 14.93355, 13.66322, 12.76220667, 11.95249]

temp_typical_days = [summer, fall, winter, spring]

V, I = [], []

def get_values(typical_seasons, response_values):
    result = []
    for season in typical_seasons:
        values = []
        for value in season:
            irr = get_value(value, response_values)
            values.append(irr)
        result.append(values)

    return np.array(result)
I = get_values(irr_typical_days, I_sc)
V = get_values(temp_typical_days, V_oc)
P = V * I

print(I.shape)
print(V.shape)
print(P.shape)

days_per_season = 120

E = P * days_per_season

E_per_season = E.sum(1)
print(f'Energía por estación: {E_per_season}')
print(f'Energía anual: {np.round(E_per_season.sum()/1000, 4)} [kWh]')

