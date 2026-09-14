---
created: 2026-09-07T10:37
updated: 2026-09-14T11:50
---
# Inhoud

```toc
```

## Beeldhoek

$$\alpha = 2 \arctan{\frac{d}{2f}} \tag{1}$$


## Contrast

**Contrast**
*Het bereik van pixelwaarden die gebruikt worden in een afbeelding*
*Het verschil tussen de maximale en minimale pixelwaarden*

**Dynamisch bereik**
*Het aantal verschillende gebruikte pixelwaarden in een*

![[Pasted image 20260914113808.png]]

```chart
type: bar
labels: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
series:
  - title: Grijstinten(4 bit)
    data: [5,1,4,8,0,0,12,1,4,5,2,5,10,3,3,2,6]
tension: 0.2
width: 100%
labelColors: true
fill: false
beginAtZero: false
bestFit: false
bestFitTitle: undefined
bestFitNumber: 0
```



### Verhogen contrast
![[Pasted image 20260914114932.png]]

```chart
type: bar
labels: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
series:
  - title: Grijstinten(4 bit)
    data: [0,10,21,0,0,0,0,0,0,0,19,14,0,0]
tension: 0.2
width: 100%
labelColors: true
fill: false
beginAtZero: false
bestFit: false
bestFitTitle: undefined
bestFitNumber: 0
```