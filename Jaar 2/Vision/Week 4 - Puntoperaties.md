---
created: 2026-09-07T10:37
updated: 2026-09-21T11:59
---
# Inhoud

```toc
```

## Intro

Puntoperaties veranderen de pixelwaarden zonder dat de afmetingen, geometrie of lokale
Structuur van de afbeelding veranderen. Elke nieuwe pixelwaarde hangt alleen maar af van
De vorige pixelwaarde op dezelfde positie

> [!infobox] Wiskunde weergave
> Wiskundig kun je een puntoperatie zo weergeven.
> De nieuwe waarde hangt alleen maar af van de oude op dezelfde positie
> $$
> \begin{align} \\
> a` = f(a) \\ \\
> I`(u,v) = f(I(u,v)) \\
> \end{align}
> $$

## Inverteren

$I`(u,v) = I_{max} - I(u,v)$

## Omkeerbaar

**Voor**
$I`(u,v) = I(u,v) \cdot 0.5$

$I``(u,v) = I`(u,v) \cdot 2$

**Na**

$I`(u,v) = I(u,v) \cdot 2$

$I``(u,v) = I`(u,v) \cdot 0.5$

Omdat je werkt met integers zijn deze operaties niet omkeerbaar want 


## Contrast en/of helderheid verhogen

$I `(u,v) = I(u,v) \cdot 1.25$

$I `(u,v) = I(u,v) + 15$

## Wat is contrast?
> [!quote] E.H.Weber
>  $$
>  \frac{{I-I_{b}}}{I_{b}}
>  $$
>  Nadeel van deze formule is dat je **oneindig** contrast kan hebben

> [!quote] A.A. Michelson
> $$
> \frac{{I_{max} - I_{min}}}{I_{max} + I_{min}}
> $$
> Nadeel van deze formule is dat als je een pixel **zwart/wit** toevoegd de **min/max** waarde gelijk **0/255** wordt.

> [!quote] RMS (Root Mean Square) Contrast
> Dit is de standaard deviatie van de pixel intensiteit
> $$
> \sqrt{\frac{1}{MN}\sum_{i=0}^{N-1}\sum_{j=0}^{M-1}(I_{ij}-\overline{I})^{2}}
> $$

## Drempelwaarde

$I `(u.v) = \begin{cases}0&\forall &  I(u,v) < d \\  1 & \forall & I(u,v) \geq d\end{cases}$

## Automatisch contrast

$f_{auto} = (a - a_{laag}) \cdot \frac{255}{(a_{hoog}-a_{laag})}$

## Wat is helderheid?

**Intensiteit** wordt uitgedrukt in een waarde
**Helderheid** is een subjectieve ervaring
**Luminatie** is een getal uit het HSL-model

Voor de lessen/tentamens gebruiken we **pixelwaardes**



