---
created: 2026-06-17T15:10
updated: 2026-06-17T16:50
---
# Samenvatting T 2 – Actuatoren, Motoren en Sensoren

# Elektromotoren

## Elektrisch vermogen

$$
P_e = U \cdot I
$$

- $P_e$ = elektrisch vermogen (W)
- $U$ = spanning (V)
- $I$ = stroom (A)

## Mechanisch vermogen

$$
P_m = T \cdot \omega
$$

- $T$ = koppel (N·m)
- $\omega$ = hoeksnelheid (rad/s)

## Rendement

$$
\eta = \frac{P_m}{P_e}
$$

Hieruit volgt:

$$
P_e = \frac{P_m}{\eta}
$$

En voor de stroom:

$$
I = \frac{P_e}{U}
$$

# PMDC-motor

## Snelheidsconstante

$$
\omega = k_\omega \cdot U_i
$$

## Koppelconstante

$$
T = k_T \cdot I
$$

Dus:

$$
I = \frac{T}{k_T}
$$

## Inductiespanning

$$
U_i = U - R_i I
$$

---

# Overbrengingen

## Koppeloverdracht

$$
\frac{T_2}{T_1} = \frac{\eta}{R}
$$

Waarbij:

- $T_1$ = ingaand koppel
- $T_2$ = uitgaand koppel
- $\eta$ = rendement
- $R$ = overbrengingsverhouding

Omschrijven:

$$
T_2 = T_1 \cdot \frac{\eta}{R}
$$

Rendement berekenen:

$$
\eta = \frac{T_2 \cdot R}{T_1}
$$

---

# Pneumatiek

## Cilinderkracht

Theoretische kracht:

$$
F_{th} = p \cdot A
$$

Effectieve kracht:

$$
F_{eff} = F_{th}(1 - \text{wrijvingspercentage})
$$

## Oppervlak van een dubbelwerkende cilinder

$$
A = \frac{\pi}{4}(d_1^2 - d_2^2)
$$

Waar:
- $d_1$ = zuigerdiameter
- $d_2$ = diameter zuigerstang

---

# Stromingsleer

## Continuïteitsvergelijking

$$
A_1 v_1 = A_2 v_2
$$

Bij ronde leidingen:

$$
v_2 = v_1 \left(\frac{d_1}{d_2}\right)^2
$$

---

## Oppervlak van een buis

$$
A = \frac{\pi d^2}{4}
$$

---

## Volumedebiet

$$
q_v = A \cdot v
$$

---

## Reynoldsgetal

$$
Re = \frac{\rho v d}{\eta}
$$

Laminaire stroming:

$$
Re < 2300
$$

---

## Wet van Bernoulli (stilstaand water)

Wanneer $v = 0$:

$$
p_1 = p_2 + \rho g h
$$

Let op:
- Rekenen in **Pascal (Pa)**
- Pas aan het einde eventueel omzetten naar **bar**

---

# LR-schakeling

## Karakteristieke tijd

$$
\tau = \frac{L}{R}
$$

Of

$$
L = \tau R
$$

Na ongeveer:

$$
t = 3\tau
$$

Is de spanning of stroom ongeveer **95%** van de eindwaarde.

---

# Belangrijke eigenschappen van actuatoren

## PMDC-motor

✅ Goedkoop

✅ Eenvoudige aansturing

✅ Lichtgewicht

❌ Borstels slijten

❌ Geeft vonken (niet geschikt voor explosiegevaar)

**Toepassingen:** speelgoed, melkopschuimer, kleine robotica

---

## BLDC-motor

✅ Geen borstels

✅ Lange levensduur

✅ Hoge toerentallen mogelijk

✅ Geschikt voor clean rooms

❌ Duurder

❌ Motorcontroller vereist

**Toepassingen:** drones, tandartsboor, industriële aandrijvingen

---

## Asynchrone motor

✅ Robuust

✅ Hoog rendement

✅ Geschikt voor continu bedrijf

✅ Vaak direct op netspanning

❌ Minder geschikt voor kleine batterijtoepassingen

**Toepassingen:** pompen, compressoren, ventilatoren

---

## Stappenmotor

✅ Zeer nauwkeurige positionering

✅ Positioneren zonder encoder mogelijk

❌ Minder geschikt voor hoge snelheden

**Toepassingen:** 3 D-printers, CNC-machines

---

# Pneumatiek

## Voordelen

- Geschikt voor explosiegevaarlijke omgevingen.
- Werkt goed bij vocht en hitte.
- Relatief goedkoop.
- Perslucht is een veilige energiedrager.

## Nadelen

- Minder nauwkeurig positioneren.
- Lagere krachten dan hydrauliek.
- Compressor nodig.

---

# Hydrauliek

## Voordelen

- Zeer hoge krachten mogelijk.
- Energie relatief eenvoudig op te slaan.
- Hoge vermogensdichtheid.

## Nadelen

- Olie veroudert.
- Kans op lekkages.
- Meer onderhoud.

---

# Sensoren

## Resistieve sensor (potentiometer)

✅ Goedkoop

✅ Eenvoudig

❌ Slijt door mechanisch contact

---

## Capacitieve sensor

✅ Detecteert metaal én niet-metaal

✅ Detecteert vloeistoffen

❌ Gevoelig voor vocht en vuil

---

## Inductieve sensor

✅ Betrouwbaar

✅ Contactloos

✅ Ongevoelig voor vuil

❌ Detecteert alleen metalen

---

## LVDT

✅ Hoge nauwkeurigheid

✅ Werkt ook op isolerende materialen

❌ Mechanisch contact

❌ Kan slijten

❌ Kan kwetsbare producten beschadigen

---

# Feiten om te onthouden

## BLDC

- Geen borstels.
- Lange levensduur.
- Geschikt voor clean rooms.
- Kan zeer hoge toerentallen halen.

## PMDC

- Commutator keert stroomrichting in rotor om.
- Borstels produceren stof en vonken.
- Weekijzeren kern verhoogt het koppel.

## Lagerbelasting beperken door

- Lagere draaisnelheid.
- Minder radiale krachten.
- Weinig gewicht aan de as.

## Waarom een tandwielkast?

- Motorsnelheid is vaak te hoog.
- Motorkoppel is vaak te laag.

---

# Ezelsbruggetjes

- **Vermogen = spanning × stroom**
  $$
  P = UI
  $$

- **Mechanisch vermogen = koppel × hoeksnelheid**
  $$
  P = T\omega
  $$

- **Hydrauliek → hoge kracht**

- **Pneumatiek → goedkoop en explosieveilig**

- **PMDC → goedkoop maar borstels**

- **BLDC → sneller, duurder en onderhoudsarm**

- **Inductieve sensor → alleen metaal**

- **Capacitieve sensor → ook kunststof en vloeistoffen**

- **LVDT → contactsensor met hoge nauwkeurigheid**

- **Kleinere buis → hogere stroomsnelheid**

- **Na $3\tau$ zit een LR-systeem op ongeveer 95% van de eindwaarde.**
# Samenvatting – Sensoren (voor Obsidian)

# Keuzehulp per sensor

| Sensor | Detecteert | Contact? | Opmerkingen |
|---------|------------|-----------|-------------|
| **Potentiometer** | Positie/verplaatsing | ✅ Ja | Slijt, goedkoop |
| **Capacitieve sensor** | Metaal, kunststof, hout, vloeistoffen | ❌ Nee | Gevoelig voor vocht en vuil |
| **Inductieve sensor** | Alleen metaal | ❌ Nee | Zeer robuust, ongevoelig voor vuil |
| **Optische encoder** | Positie, snelheid, hoek | ❌ Nee | Zeer hoge resolutie |
| **Optische ToF (time-of-flight)** | Afstand en detectie | ❌ Nee | Werkt met lichtpulsen |
| **Ultrasone sensor** | Afstand en detectie | ❌ Nee | Werkt met geluidsgolven |
| **Eindschakelaar** | Aanwezig/niet aanwezig | ✅ Ja | Goedkoop, slijtage mogelijk |
| **LVDT** | Lineaire verplaatsing | ✅ Ja | Hoge nauwkeurigheid, slijt |

---

# Belangrijkste eigenschappen

## Potentiometer

✅ Meet positie

✅ Goedkoop

❌ Mechanisch contact

❌ Slijtage

❌ Niet geschikt voor zeer hoge resoluties

---

## Capacitieve sensor

✅ Detecteert metaal én niet-metaal

✅ Detecteert kunststof, hout en vloeistoffen

✅ Contactloos

❌ Gevoelig voor vocht

❌ Gevoelig voor vuil

❌ Typisch klein meetbereik (enkele centimeters)

---

## Inductieve sensor

✅ Detecteert alleen metalen

✅ Contactloos

✅ Werkt goed in natte en vuile omgevingen

✅ Zeer betrouwbaar

❌ Detecteert geen kunststof of hout

❌ Klein meetbereik

---

## Optische encoder

✅ Meet positie

✅ Meet snelheid

✅ Meet hoeksnelheid

✅ Zeer hoge resolutie (tot micrometers)

✅ Groot meetbereik mogelijk

❌ Relatief duur

---

## Optische reflectieve sensor (Time-of-Flight)

✅ Contactloze afstandsmeting

✅ Geschikt voor objectdetectie

✅ Geschikt voor grotere afstanden

❌ Kan beïnvloed worden door reflectie of kleur

---

## Ultrasone sensor

✅ Contactloze afstandsmeting

✅ Ongevoelig voor kleur

✅ Geschikt voor grotere objecten

❌ Minder geschikt voor kleine objecten

❌ Heeft een minimale meetafstand

---

## Eindschakelaar

✅ Zeer goedkoop

✅ Betrouwbare detectie

✅ Geschikt voor deurschakelaars

❌ Alleen aan/uit-detectie

❌ Mechanisch contact → slijtage

---

## LVDT (Linear Variable Differential Transformer)

✅ Zeer nauwkeurige positiemeting

✅ Detecteert ook isolerende materialen

✅ Hoge resolutie

❌ Mechanisch contact

❌ Kan slijten

❌ Kan kwetsbare producten beschadigen

---

# Wanneer kies je welke sensor?

## Detectie van metaal

- Inductieve sensor ⭐
- Capacitieve sensor (kan ook)

---

## Detectie van kunststof

- Capacitieve sensor ⭐
- Optische ToF
- Ultrasoon

---

## Detectie van vloeistoffen

- Capacitieve sensor ⭐

---

## Positie of verplaatsing met hoge nauwkeurigheid

- Optische encoder ⭐
- LVDT

---

## Hoeksnelheid van een motoras

- Optische encoder ⭐
- Inductieve sensor (met tandwiel/tanden)

---

## Afstand meten

### Met licht (Time-of-Flight)

$$
t = \frac{2d}{c}
$$

Waar:

- $t$ = tijd heen en terug (s)
- $d$ = afstand (m)
- $c = 3.00 \times 10^8$ m/s (lichtsnelheid)

Afstand berekenen:

$$
d = \frac{ct}{2}
$$

---

### Met ultrasoon

$$
t = \frac{2d}{v}
$$

Waar:

- $v = 343\ \text{m/s}$ (geluidssnelheid in lucht)

Afstand:

$$
d = \frac{vt}{2}
$$

**Let op:** de puls gaat **heen én terug**, dus altijd delen door 2 of vermenigvuldigen met 2.

---

# Lineaire incrementele encoder

Afstand tussen twee sleuven:

$$
\Delta x = \frac{L}{N}
$$

Waar:

- $L$ = lengte encoder
- $N$ = aantal sleuven

Snelheid:

$$
v = f \cdot \Delta x
$$

Of gecombineerd:

$$
v = f \cdot \frac{L}{N}
$$

Waar:

- $f$ = frequentie (Hz)

---

# Rekstroken (Strain Gauges)

## Gauge factor

$$
K = \frac{\Delta}{\varepsilon}
$$

Waar:

- $K$ = gauge factor
- $\Delta$ = relatieve weerstandsverandering
- $\varepsilon$ = rek

---

## Relatieve weerstandsverandering

$$
\Delta = K \cdot \varepsilon
$$

---

## Absolute weerstandsverandering

$$
\Delta R = \Delta \cdot R_0
$$

Waar:

- $R_0$ = nominale weerstand

---

## Rek bepalen uit een meting

$$
\varepsilon = \frac{\Delta}{K}
$$

---

# Ezelsbruggetjes

- **Inductief = alleen metaal.**
- **Capacitief = bijna alles (ook kunststof en vloeistoffen).**
- **Optische encoder = positie en snelheid met hoge resolutie.**
- **Time-of-Flight = afstand meten met licht.**
- **Ultrasoon = afstand meten met geluid.**
- **Eindschakelaar = alleen aan/uit-detectie.**
- **LVDT = nauwkeurige lineaire positie, maar met contact.**
- **Bij ToF en ultrasoon gaat het signaal altijd heen én terug → factor 2 niet vergeten.**
- **Encoder:**
  $$
  v = f \cdot \frac{L}{N}
  $$
- **Rekstrook:**
  $$
  \Delta = K \cdot \varepsilon
  $$