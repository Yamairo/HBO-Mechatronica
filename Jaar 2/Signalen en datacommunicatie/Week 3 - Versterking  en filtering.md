---
created: 2026-09-15T13:04
updated: 2026-09-18T08:45
---
# Inhoud

```toc
```

## Versterking

### Uitdagingen

- Ruis wordt ook versterkt
- Te veel versterken leidt tot clipping
- Bij hoge vermogens aanzienlijke verliezen en warmteontwikkeling

### OpAmp

> [!infobox] OpAamp
> ![[Pasted image 20260915132021.png]]
> $$V_{out} = A_{0}(V_{+} - V_{-}) \tag{1}$$
> $$
> \begin{align} \\
> &A_{0} = \text{Vergroting} \\
> &V_{+} = \text{Spanning op de positive aansluiting} \\
> &V_{-} = \text{Spanning op de negatieve aansluiting} \\
> \end{align}
> $$

#### Positieve feedback



Bij het aansluiten van $V_{out}$ aan $V_{+}$ zal er een positieve feedback plaatsvinden. Dit is handig om bij een bepaalde drempelwaarde gelijk een hoog signaal te krijgen. Je kan hier dus goed een 1 of 0 waarde krijgen.

#### Negatieve feedback

Wordt een voorspelbare, stabiele, storingsarme, breedbandige, 

### Interverterende versterker

> [!infobox] Interverterende versterker
> ![[Pasted image 20260915140042.png]]
> $$A = -\frac{R_{2}}{R_{1}} \tag{2}$$
> 
> $$V_{uit} = -V_{in} \frac{R_{2}}{R_{1}} \tag{3}$$
> 


## Clipping

> [!Infobox] Clipping
> ![[Pasted image 20260915134124.png]]

### Voorkomen

1. Eigenschappen van ingangsignaal bepalen
2. Eigenschappen van versterker bepalen
3. Versterker of ingangsignaal aanpassen

### Voorbeeld


| Voltage | Distance (cm) |
| ------- | ------------- |
| 2.3V    | 10            |
| 1.4V    | 20            |
| 0.96V   | 30            |
| 0.75V   | 40            |
| 0.62V   | 50            | 

```chart
type: line
labels: [10,20,30,40,50]
series:
  - title: Voltage
    data: [2.3,1.4,0.96,0.75,0.62]
tension: 0.2
width: 80%
labelColors: false
fill: false
beginAtZero: false
bestFit: false
bestFitTitle: undefined
bestFitNumber: 0
```

## Filtering

### Toepassingen

**Scheiden van signalen**

Filters nemen 1 signaal en geven een signaal als output.

### Belangrijke filters


> [![Infobox] Filters 
> ![[Pasted image 20260915135428.png]]

