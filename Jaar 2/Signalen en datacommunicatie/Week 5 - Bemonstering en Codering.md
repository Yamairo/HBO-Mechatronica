---
created: 2026-09-29T13:02
updated: 2026-09-29T14:10
---
# Inhoud

```toc
```

## Bemonstering


> [!quote] Bemonstering of Kwantisering
> **Bemonstering** is een tijd discreet signaal maken
> **Kwantisering** is een waarde-discreet signaal maken

### Tijd-discreet maken

Wiskundig gezien zou voor een simpele sinusgolf meten, het genoeg zijn om met 2 keer de frequentie van de golf te meten. In de praktijk werkt dit niet zo goed.

> [!quote] Hoe vaak kan je bemonsteren en zeker weten dat je alles hebt gezien?
> $f_{bemonstering} > 2f_{signaal}$

## Kwantisatie

### Waarde-discreet maken

Bij het kwantiseren vormt er uiteindelijk ruis.

> [!quote] Hoeveel bits heb je nodig?
> $b = \big|{\log_{2}\frac{max}{stap}}\big|$

### Afronding

> [!quote] Waarom afronden?
> Als er geen afrondig is aangegeven dan zal de afwijking $+$ of $-$ 1 stap zijn. Als er wel afronding is dan zal die $+1/2$ of $-1/2$ zijn

## Codering

### NRZ (Non Return to Zero) Coding

Een hoog signaal (*bv. 5 V*) geeft `1` en een laag signaal (*0 V*) geeft `0`. Kan ook andersom zijn, dus een hoog signaal (*bv. 5 V*) geeft `0` en een laag signaal (*0 V*) geeft `1`

Hierbij is synchonisatie tussen de zender en ontvanger nodig


### NRZ-I (Non Return to Zero Inverted)

Als er een verandering is van de waarde in de blokgrafiek dan is het signaal hoog of  `1`. Als er geen verandering is dan is deze laag of `0`.

Hierbij is synchonisatie tussen de zender en ontvanger nodig

### RZ (Return to Zero) Coding

Een hoog signaal (*bv. 5 V*) geeft `0` en een laag signaal (*0 V*) geeft `1`. Na elk bit wordt er ook een `0` waarde gestuurd. Vandaar de `return`.

Er is **geen** extra synchronisatie nodig. Maar de frequentie moet wel hoger zijn door de extra bits.