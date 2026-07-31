---
created: 2025-04-17T10:38
updated: 2026-06-13T14:36
---
# Inhoudsopgave

```toc
```

## Datatypes

**BOOL** - 1 bit
**BYTE** - 8 bit (0 … 255)
**WORD** - 16 bit (0 … 65 535)
**DWORD** - 32 bit (0 … 4 294 967 295)
**LWORD** - 64 bit (0 … 18 446 744 073 709 551 615) (exclusief op S 7-1500)

**SINT / USINT** - 8 bit signed / unsigned 
**INT / UINT** - 16 bit signed / unsigned 
**DINT / UDINT** - 32 bit signed / unsigned 
**LINT / ULINT** - 64 bit signed / unsigned (exclusief op S 7-1500) 
**REAL** - 32 bit floating point 
**LREAL** - 64 bit floating point (exclusief op S 7-1500)

Tijd- en datumtypes
&nbsp; &nbsp; &nbsp;&nbsp; Bijvoorbeeld: **TIME en DATE** 
Tekst- en karaktertypes 
&nbsp; &nbsp; &nbsp;&nbsp; Bijvoorbeeld: **CHAR en STRING** 
Samengestelde datatypes 
&nbsp; &nbsp; &nbsp;&nbsp; Bijvoorbeeld: **ARRAY en STRUCT** 
Systeem- en speciale types 
&nbsp; &nbsp; &nbsp;&nbsp; Bijvoorbeeld: **POINTER en COUNTER**


## Addressering

De PLC heeft drie registers

Ingangsregister (I)
- I 2.1
- IB 37

Deze neemt 8 bits of 1 byte in beslag

Uitgangsregister (Q)
- Q 3.7
- QW 18

Deze neemt 16 bits of 2 byte in beslag

Merker (M)
- M 0.0
- MD 64

Deze neemt 32 bits of 4 byte in beslag

## Programmeerblokken

OB: Organization Block 
**FC: Function** 
**FB: Function Block** 
**DB: Data Block SFC:** 
System Function 
SFB: System Function Block 
SDB: System Data Block 

### Organization Block (OB)
Organization blocks worden aangeroepen door bepaalde gebeurtenissen en koppelen het besturingssysteem van de plc met het gebruikersprogramma.

### Function (FC)

Functies:
- Hebben een return waarde
- Kunnen parameters meekrijgen
- Hebben geen eigen data blok

### Function Block (FB)

Function Blocks:
- Hebben geen return waarde, wel een out of in-out
- Kunnen gegevens behouden over aanroepen heen
	- Statische variabelen
- Zijn  gekoppeld aan een Data Block
	- Wordt een instance Data Block genoemd
	- Wordt gebruikt bij parameter-overdracht
	- Bij aanroep van GB dus DB opgeven

### Data Block (DB)
Een Data Block wordt gebruikt voor data opslag

DB's kunnen ook complexe datatypen aan:
- Array's
- Structures
- Date_and_time

Twee verschillende type DB's:
- Shared DB
	- Gemeenschappelijl gebruik, alle programma-bouwstenen kunnen gier data lezen en schrijven
- Instance DB
	- Gekoppeld aan één FB

### System Functions (SFC, SFB en SDB) 
Deze bouwstenen maken systeemfuncties en -data toegankelijk voor het gebruikersprogramma, je kunt ze aanroepen/lezen maar niet aanpassen. 
SFC: System Function 
&nbsp; &nbsp; &nbsp;&nbsp; Bijvoorbeeld: SFC 1 – *read PLC clock* 
SFB: System Function Block 
&nbsp; &nbsp; &nbsp;&nbsp; Bijvoorbeeld: SFB 2 – *IEC up/down counter*
SDB: System Data Block 
&nbsp; &nbsp; &nbsp;&nbsp; Bijvoorbeeld: SDB 0 – *Hardware configuration*

### System Functions

Systeemfuncties zijn voorgeprogrammeerde functies je kan ze aanroepen/lezen maar niet aanpassen

![[Pasted image 20260613143627.png]]

