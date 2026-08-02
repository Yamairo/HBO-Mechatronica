---
created: 2025-02-19T09:35
updated: 2026-04-23T15:01
---
# Inhoudsopgave
```toc
```

## Eenheden van hoeksnelheid

$1 \text{ rpm} = \frac{2\pi}{60} \text{ rad/s}$
$1 \text{ rpm} \approx 0.1 \text{ rad/s}$

## Hoeksnelheid weten
- Vaantje op de as aantal omwentelingen tellen en timen
- Encoder op de as en timen

![[Pasted image 20260422164014.png]]

## Kracht weten

Kracht meten? 
- Met een veerunster
- Met gewichten belasten tot de beweging stopt (evenwicht)
- Met een krachtsensor

## Koppel weten

Koppel leg je aan met een lier en een gewicht

Koppel meten kan met:
- Een stroommeting
- Een balans vinden met een lier
- Een sensor

## Spanning weten

Spanning aanleggen wordt met een labvoeding of accu gedaan

Spanning meten kan door:
- De labvoeding af te lezen
- Het gebruiken van een multimeter

## Stroom weten

Stroom aanleggen kan met een stroombron maar meestal is het een gevolg uit de weerstand van de opstelling waarop een spanning wordt gelegd.

Stroom begrenzen kan via de labvoeding of door middel van een zekering

Spanning meten kan door:
- De labvoeding af te lezen
- Het gebruiken van een multimeter

## Zwakke plekken elektomotor

1. Teveel kracht op de lagers van de as
2. Oververhitting: Smelten van de isolatie van de draadwindingen

### Oververhitting 

Oververhitting komt doordat er teveel stroom gebruikt wordt
Dit komt gebeurd vaak omdat er teveel koppel/kracht wordt gevraagd
En dan kan de motor zichzelf niet begrenzen.

Voordat dit gebeurd begint de motor vaak moeizamer te draaien en te ruiken.

---

Het voorkomen van oververhitting wordt door **stroombegrenzing** gedaan
Dit kan dmv:
1. Het instellen van de labvoeding
2. Het gebruiken van een zekering
3. De motor controller instellen, meten op shield
4. Het gebruiken van een motor met thermische beveiliging

Het voorkomen van overvehitting kan ook door de koppel te begrenzen
Dit kan dmv:
1. Het mechaniek soepel maken
2. Grenzen te stellen aan gewicht
3. Het gebruiken van het juiste formaat motor

## Kracht op lagers

Er zijn twee soorten kracht op een as:
- Radiaal: loodrecht op de asrichting
- Axiaal: in de asrichting

De krachten op een lager hebben grenzen

Oorzaken van teveel kracht zijn:
1. Te hoge draaisnelheid
2. Verkeerd type overbrenging op as

Je kan dit voor komen door:
1. De draaisnelheid te begrenzen
2. Type overbrenging gebruiken die weinig kracht op de as geeft
3. Niet teveel gewicht direct aan de as te hangen
4. Montage op de as van bv tandwiel
	- Gebruik hierbij geen motor
	- Gebruiken een schroefklem of pers het met beleid
	- Ondersteun hierbij het uiteinde van de as

## Mechanische overbrengingen

### Tandwielkast: planetair

- In het verlengde van de motor-as
- Nauwkeurigheid goed (weinig speling)
- Hoogste rendement
- Kwetsbaar voor gruis, daarom vaak vastgelast
- Lagers dicht bij elkaar: kan weinig radiaalkracht hebben.

## Tandwielkast: gewoon

- As parallel aan de motoras
- As kan wel grotere radiale kracht aan
- Simpel
- Goedkoop
- Enige speling nodig
- Vrij weinig radiale kracht op assen
- Tandwielen: altijd wat rendementsverlies. Want wrijving.

## Wormwieloverbrenging

- Enorme reductie mogelijk
- Goedkoop
- Heel veel wrijving
- Laag rendement
- Blokkeert bij draaien aan andere kant
- De as gaat de hoek om
- Flinke radiale kracht op assen. Dus montage op motor-as riskant.

## Tandriem

- Vrij nauwkeurig, want tandjes en weinig rek
- Rendement vrij OK altijd wat rendementsverlies. Want wrijving.
- Inzetbaar voor nog meer functies
- Constructie nodig om op spanning te houden.

## Wrijvingsoverbrenging (Wrijfwiel)

- Gebruikt wrijving om koppel over te brengen (statische wrijving, die kost geen energie)
- Vaak met rubber
- Alu op alu kan ook: hoog rendement!
- Kan slippen: nuttig als beveiliging tegen overbelasting
- Simpel te bouwen
- Vraagt hoge radiale kracht op assen: constructie nodig om die in te stellen.