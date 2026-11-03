---
created: 2026-11-03T13:16
updated: 2026-11-03T14:20
---
# Inhoudsopgave

```toc
```

## Transmissiemedia

Voorbeelden van een medium die gebruikt worden zijn: *Koper*, *Glasvezel*, *Lucht*

### Vergelijken

**Bandbreedte**

### Koper

Afstand
- Maximaal 100 meter
- Voordelig op korte afstanden

Snelheid
- Tot 10 Gb/s
	- Ook mogelijk volgens de standaard: 25 Gb/s en 40 Gb/s

Kwaliteitsverlies
- Overspraak

Om kwaliteitsverlies te voorkomen kan je:
- Afschermen
	-  Door middel van koper
	- Fysiek scheiden
	- Geen open eindjes
- Draaien van draadparen

Ook kan je:
- Coaxiale kabels gebruiken
- Signaalpaden plannen

### Glas

Afstand
- Kilometers
- Voordelig voor lange afstanden

Snelheid
- 10 Gb/s tot 1 Tb/s

Kwaliteitsverlies
- Overspraak is vrijwel onbestaand
- Storing door interne reflecties

Om kwaliteitsverlies te voorkomen kan je:
- Korte bochten voorkoen
- Mechanische stress verminderen
- Kwalitatief goede aansluitingen maken

Afscherming voor overspraak:
- Individuele vezels afschermen van elkaar

#### Aansluitingen

Glasvezels moeten heel specifiek recht op elkaar aangesloten worden en met een zelfde diameter

#### Reflecties

Bij de interne reflecties zal het signaal veranderen i.p.v. een blokgolf zal het meer op een sinusoïde lijken.

### Lucht

Afstand
- Meters t/m kilometers
- Flexibel

Snelheid
- Tot 46 Gb/s

Kwaliteitsverlies
- Overspraak
- Reflecties

Om kwaliteitsverlies te voorkomen kan je:
- Obstakels wegnemen
- Stoorbronnen wegnemen
- Signaal richten

Verder kan je ook:
- Signalen over het spectrum verdelen
- Afschermen voor signalen van buitenaf

#### Signaal en kwaliteitsverlies

**Reflectie**

**Terugkaatsing**

**Buiging**

**Verspreiding**

**Vermindering**


### Welk medium kies je?

1. Temperatuursensor verbinden met een PLC op 3 m afstand in een fabriekshal
	1. Koper
	2. Goedkoop, korte afstand
2. Productielijn in twee hallen, 200 m uit elkaar, hoge datastroom
	1. Glasvezel
	2. Langere afstand, goed voor hoge datastroom
3. Mobiele robot die statusberichten doorstuurt naar centrale server
	1. Lucht
	2. De robot moet mobiel zijn en naar de centrale server verbinden
4. Meetopstelling op labtagel, signaal van sensor naar osciloscoop
	1. Koper
	2. Goedkoop, Korte afstand

---

##  Digitale Codering

Eerder hebben we naar NRZ, NRZ-I, RZ gekeken.

### Manchester Encoding (ME)

Overgang omhoog  = 1
Overgang omlaag = 0

Transmissiesnelheid is af te leiden uit het signaal voor de synchonisatie

### Differential Manchester Encoding (DME)

Dit is soortgelijk aan ME maar dan is er een verschuiving op de tijdsas