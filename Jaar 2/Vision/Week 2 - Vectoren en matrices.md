---
created: 2026-09-07T10:32
updated: 2026-09-07T14:52
---
# Inhoud

```toc
```

## Vectoren

$$
\vec{a} = \begin{pmatrix} a_{1} \\a_{2} \end{pmatrix} \text{ in } R_{2}
$$

 $$
\vec{a} = \begin{pmatrix} a_{1} \\a_{2} \\ a_{3}  \end{pmatrix} \text{ in } R_{3}
$$

$$
\vec{a} = \begin{pmatrix} a_{1} \\ \vdots \\a_{n} \end{pmatrix} \text{ in } R_{n}
$$

### Eenheidsvectoren

$$
\vec{e_{1}} = \begin{pmatrix} 1 \\ 0 \end{pmatrix},  \text{ in } R_{1}, \vec{e_{2}} = \begin{pmatrix} 0 \\ 1 \end{pmatrix},  \text{ in } R_{2}
$$

$$
\vec{e_{1}} = \begin{pmatrix} 1 \\ 0 \\ 0\end{pmatrix},  \text{ in } R_{1}, \vec{e_{2}} = \begin{pmatrix} 0 \\ 1 \\ 0\end{pmatrix},  \text{ in } R_{2},
\vec{e_{3}} = \begin{pmatrix} 0 \\ 0 \\ 1\end{pmatrix},  \text{ in } R_{3}
$$

### Vectorbewerking

Als $\vec{a} = \begin{pmatrix} a_{1} \\a_{2}\end{pmatrix}$ en $\vec{b} = \begin{pmatrix} b_{1} \\b_{2}\end{pmatrix}$ dan is:

$\vec{a}+ \vec{b} =  \begin{pmatrix} a_{1} + b_1 \\a_{2} + b_{2}\end{pmatrix}$ en $\vec{a} - \vec{b} =  \begin{pmatrix} a_{1} - b_1 \\a_{2} - b_{2}\end{pmatrix}$

Als $\vec{a} = \begin{pmatrix} a_{1} \\a_{2}\end{pmatrix}$ en $c$ is een getal dan is $c\vec{a} = \begin{pmatrix} c \cdot a_{1} \\ c \cdot a_{2}\end{pmatrix}$

Ontbinden: $\vec{a} = \begin{pmatrix} a_{1} \\a_{2}\end{pmatrix}$ is te schrijven als:

$$
\vec{a} = a_{1} \cdot \vec{e} +a_{2} \cdot \vec{e_{2}} = a_{1} \begin{pmatrix}1\\0\end{pmatrix} + a_{2} \begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}a_{1}\\a_{2}\end{pmatrix}
$$

### Vectorlengte en inwendig product

De lengte van een vector is $|\vec{a}|=\sqrt{a_{1}^{2}+ a_{2}^{2}}$

Het inwendig product van twee vectoren is $\vec{a} \cdot \vec{b} = a_{1} \cdot b_{1} + a_{2} \cdot b_{2}$

Er is dus geen vector maar een getal als uitkomst

$\vec{a} \cdot \vec{a} = a_{1}^{2} + a_{2}^{2}= |\vec{a}|^{2}$ dus $|\vec{a}| = \sqrt{\vec{a}\cdot \vec{a}}$

### Hoek tussen vectoren 

$\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cos{\phi}$

Dus,

$\cos{\phi} = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$

### Opbouw matrix

Een $m \cdot n$ matrix heeft *m* rijen (horizontaal) en *n* kolommen (vertikaal)

De getallen in een matrix heten elementen. Het element $a_{ij}$ staat in de $i^{e}$ rij en $j^e$ kolom.

### Bijzondere matrices

Vierkante matrix

$A = \begin{pmatrix}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{pmatrix}$

Eenheidsmatrix

$A = \begin{pmatrix}1&0&0 \\ 0&1&0 \\ 0&0&1\end{pmatrix}$

Getransporteerde matrixen: rijen en kollomen wisselen

$A = \begin{pmatrix}1&2 \\ 3&4\\ 5&6\end{pmatrix}$ geeft $A^{T} = \begin{pmatrix}1 & 3 & 5 \\ 2 & 4 & 6\end{pmatrix}$

### Matrices optellen en scalair vermenigvuldigen

Matrix optellen kan alleen als de matrices de zelfde afmeting hebben

Als $C = A + B$ dan geldt $c_{ij} = a_{ij} + b_{ij}$

Vermenigvuldigen met een getal:
Als $B=\lambda \cdot A$ dan geldt $b_{ij} = \lambda a_{ij}$

### Product van matrix en vector

$M \cdot \vec{v} = \begin{pmatrix} m_11 & m_12 \\ m_21 & m_22\end{pmatrix} \begin{pmatrix}v_{1}\\v_{2}\end{pmatrix} = \begin{pmatrix} m_{11}\cdot v_{1} & m_{12}\cdot v_2 \\ m_{21}\ cdot v_{1} & m_{22} \cdot v_{2}\end{pmatrix}$


### Matrixvermenigvuldigingen

Gegeven $m \cdot n$ matrix A en $n \cdot p$ matrix B
$C = A \cdot B$ geeft matrix met afmeting $m \cdot p$

Matrixvermenigvuldiging is niet commutatief(verwisselbaar):
$A \cdot B \neq B \cdot A$

Als $n = n$ dan is de vermenigvuldiging wel commutatief


