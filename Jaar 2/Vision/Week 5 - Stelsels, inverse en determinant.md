---
created: 2026-09-07T10:37
updated: 2026-09-28T11:41
---
# Inhoud

```toc
```

## Inverse van een vierkante matrix

$$
\begin{align}
A \cdot B = I \\
B = I \cdot A^{-1}
\end{align}
$$

> [!example] Matrix regels
> -  Matrix B is de inverse van matrix A als:
> $$
> A \cdot B = B \cdot A = I
> $$
> - $B = A^{-1} \text{ en } A = B^{-1}$ 

 ## Stelsels lineaire vergelijkingen

### Stelsels met 2 variabelen

$$
\begin{align}
y_{1} = 2.5x - 3 \\
y_{2} = -0.5x + 6
\end{align}
$$

```_system
f(x) = 2.5x - 3
h(x) = -0.5x + 6
```

$$
\begin{align}
\begin{cases}
5x -2y = 6 \\
x + 2y = 12 \\
\end{cases}
\end{align}
$$

Hieruit volgt x =3 en y = 4.5 dit is hetzelfde als uit de grafiek.

### Stelsels met 3 variabelen

Gegeven het volgende stelsel:

$$
\begin{align}
\begin{cases}
x + y + z = 6 \\
2x - y + z = 3 \\
x + 2y - z = 2 \\
\end{cases}
\end{align}
$$

Wat zijn de waarden van $x, y, z$

Dit kan door de variabelen te definiëren met de andere gegeven variabelen maar kost veel tijd. Daarom gaan we dit met matrixen doen.



> [!example]  Stelsen omschrijven naar Matrix
> $$
> A \cdot \vec{x} = \vec{b}
> $$
> Met $A$: coëfficientmatrix (deze stelt het systeem voor) 
> $\vec{x}$: onbekendenvector (zoals bijvoorbeeld reactiekrachten) 
> $\vec{b}$: constantenvector (zoals bijvoorbeeld externe belastingen)
> 
> *Voorbeeld Opgave*
> 
> Los op in matrixvorm
> $$\begin{align}
> 2x+3y = 1 \\
> x=6y = 2
> \end{align}$$
> Matrixvorm
> $$\begin{align}
> \begin{bmatrix}
> 2 & 3 \\
> 1 & -6
> \end{bmatrix}
> \begin{pmatrix}
> x \\
> y
> \end{pmatrix}
> = 
> \begin{pmatrix}
> 1 \\
> 2
> \end{pmatrix}
> \end{align}$$
> 
> Werk uit:
> 
> $$\begin{align} \left[ \begin{array}{cc|c} 2 & 3 & 1 \\ 1 & -6 & 2 \end{array} \right] \end{align}$$
> 	

$$
\begin{bmatrix}
1 & 1 & 1 \\
2 & -1 & 1 \\
1 & 2 & -1 \\
\end{bmatrix}
\begin{pmatrix}
x \\
y \\
z\\
\end{pmatrix}
=
\begin{pmatrix}
6 \\
3 \\
2 \\
\end{pmatrix}
$$

$$
\begin{align} \left[ \begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 2 & -1 & 1 & 3 \\ 1 & 2 & -1 & 2 \end{array} \right] \end{align}
$$

Dit geeft 

$$\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
1 \\ 2 \\ 3 \\
\end{pmatrix}
$$

## Determinant voor stelsels van vergelijkingen

Als de determinant van de vergelijking bestaat, dan bestaat de inverse ook. Als de determinant niet bestaat, dan bestaat de inverse ook niet.

