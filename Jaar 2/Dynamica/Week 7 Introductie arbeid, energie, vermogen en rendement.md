---
created: 2026-10-12T13:01
updated: 2026-10-12T14:18
---
# Inhoud

```toc
```

## Definities

> [!quote] Arbeid
$$U = \int{ F }ds \tag{1}$$

> [!quote] Arbeid
> $$
> U = F \cos\theta s \tag{2}
> $$

> [!quote] Mechanish rendement ($\epsilon$)
> $$
> \epsilon = \frac{P_{uit}}{P_{in}} \tag{3}
> $$

### Oefenopdracht 1

- Bepaal het maximale vermogen dat de motor moet leveren

$P_{max.mechanisch} = F \cdot V_{max}$
$\sum{F} = m \cdot a$
$F_{m} - F_{z} = 2000 \cdot \frac{25}{30}$

$F_{z} = \frac{2000 \cdot 9.81}{\sqrt{101}}$
$F_{m} = 2000\left( \frac{9.81}{\sqrt{ 101 }} + \frac{25}{30} \right) = 3618.9 \pu{ N }$

$P_{motorg, echt} = \frac{3618.9\cdot{25}}{0.8} = 113.1 \pu{kW}$


- Bepaal het geleverd gemiddeld vermogen

$P_{motor,gem} = \frac{112.1}{2} = 56.5 \pu{ kW }$

## Arbeids-energievergelijking

$$
T_{2} = T_{1} + \sum{U_{1-2}} \tag{4}
$$
$$
T_{2} + E_{z,2} + E_{v,2} = T_{1} + E_{z,1} + E_{v,1} + \sum{U_{nc,1-2}} \tag{5}
$$

> [!quote] Kinetische energie
> $$
> T = \frac{1}{2}mv^{2}\tag{6}
> $$

> [!quote]  Potentiële energie
> $$E_{z} = mgh \tag{7}$$

> [!quote] Potentiële veerenergie
> $$E_{v} = \frac{1}{2}kx^{2} \tag {8}$$
> 

###  Oefenopdracht 2


|         | Begin                  | Eind                   |
| ------- | ---------------------- | ---------------------- |
| T       | 0                      | $\frac{1}{2}m(0.15)^2$ |
| $E_{z}$ | $m \cdot 9.81 \cdot 5$ | 0                      |
| $E_{v}$ |                        | NVT                    |
$$
\begin{align}
U_{nc,schuin} &= -F_{\omega} \cdot l \\
 \\
\sin(20\degree) &= \frac{5}{l} \\
l &= \frac{5}{\sin(20\degree)} \approx 14.6 \pu{ m } \\
 \\
F_{\omega} &= F_{N} \mu = F_{N} \cdot 0.1\\
F_{N} &= m \cdot 9.81 \cos(20\degree) \\
 \\
\text{Dus, } \\
U_{nc,schuin} &= -0.1 \cdot m \cdot 9.81 \cdot \cos(20\degree) \cdot \frac{5}{\sin(20\degree)} \\
 \\
U_{nc,recht} &= -F_{\omega} \cdot d = -0.25 \cdot m \cdot 9.81 \cdot d \\
\end{align}
$$


### Oefenopdracht 3

|         | Begin                                   | Eind                   |
| ------- | --------------------------------------- | ---------------------- |
| T       | 0                                       | $\frac{1}{4}\cdot v^2$ |
| $E_{z}$ | $3 \cdot 9.81 \cdot 2 = 58.92 \pu{ J }$ | 0                      |
| $E_{v}$ | $400 \pu{ J }$                          | $100 \pu{ J }$         |
$$
\begin{align}
\frac{3}{2} v^{2} = 400 + 58.92 - 100 \\
v^{2} = 1435.68 \\
v = 37.8903681692

|   |   |   |
|---|---|---|
||   ||
||||
||||
||||
||||

|   |   |   |   |
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
\end{align}
$$