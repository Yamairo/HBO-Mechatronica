---
created: 2026-09-08T12:59
updated: 2026-09-08T14:23
---
# Inhoud

```toc
```

## Signalen
### Wat zijn signalen?

Een elektrisch signaal brengt informatie over door de spanning, stroom of frequentie te veranderen.

## Weergave

### Fourierreeks
#### Eigenschappen van een sinus

```_graph
a = 1
b = 2
c = pi
D = 2
y1 = a sin(b(x-c)+D)
```

#### Basis

Elk signaal kan gerepresenteerd worden door een optelling van sinussen

Hier is een voorbeeld te zien van 2 sinussen die opgeteld zijn.

```_graph
a = 1
b = 2
c = pi
D = 2
y = a sin(b(x-c)+D) +2a sin(3b(x-2c)+D)
```

#### Benadering

Je kan door het optellen van sinussen specifieke signalen benaderen. Om sommige signalen te bereiken zijn een oneindig aantal sinussen nodig.

#### Tijd, frequentie en intenssiteit

Soms is het nodig om van Tijddomein $\rightarrow$ Frequentiedomein te gaan. Om ruis uit de sinusoptelling te halen

### Weergave van signalen

#### Constante tijd

Een constante waarde in het tijddomein levert een piek bij 0 in het frequentiedomein.

```_graph
y = 2
```

```_graph
x = 0
```

####  Fourriertransformatie

Het wisselen van het domein wordt dmv fouriertransformatie

$X(f) =\int{x(t)e^{j\cdot{2\pi ft}}dt}$

$x(f) = \int_{\infty}^{-\infty}X(f)e^{-j{2\pi ft}}df$

#### Spectogram/Wateval

Een spectogram is een plot, dat een frequentieverandering over de tijd laat zien.

> [!note] Waterval 
> ![[Pasted image 20260908134923.png]]

---

## Kans op ruis

### Gaussische Ruis

> [!note] Gaussion Disturbance
>  ![[Pasted image 20260908135713.png]]

#### Standaard deviate

> [!note] Gaussion Distribution
> ![[Pasted image 20260908135818.png]]

### Ruis in het frequentiedomein

> [!note] Tijd-as wordt frequentie-as
> ![[Pasted image 20260908140128.png]]

### Decibellen

Het werken met $\\pu{dB}$ is erg handig wanneer er gelijkteidig met grote én kleinee getallen wordt gewerkt.

> [!note] Verschil tussen logaritmische schaal t.o.v. lineair
> ![[Pasted image 20260908140316.png]]

Om x naar decibel om te zetten gebruiken we:
$x_{dB} = 10\log_{10}x$

$x = 10^{x_{db}/10}$

### Valkuilen

1. Niet $\log_{10}$ gebruiken
2. Vergeten om $\pu{dB}$ erbij te zetten
3. Vermenigvuldigen en delen in plaats van optellen en aftrekken
4. $\pu{ dB }$ is eenheidsloosen relatief
5. De verschillen tussen $\pu{ dBa }$, $\pu{ dBW }$ ... Enz. Te zien.

### SNR (Signal-to-Noise-Ratio)

$SNR = \frac{P_{signaal}}{P_{ruis}}$

> [!info]
> ![[Pasted image 20260908141528.png]]

$SNR_{dB} = P_{signaal_{dB}} - P_{ruis_{dB}}$

> [!note] SNR in Decibel
> ![[Pasted image 20260908141456.png]]

## Versterking

### Gain

$Versterking = \frac{P_{out}}{P_{in}}$

### Uitdagingen

- Ruis wordt ook versterkt
- Te veel versterken leidt tot clipping
-  Bij hge vermogens zijn er veel verlizen en komt er meer warmte vrij (Niet belangrijk voor de toets)
