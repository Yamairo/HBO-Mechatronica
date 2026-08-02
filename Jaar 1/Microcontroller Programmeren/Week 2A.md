---
created: 2025-09-09T10:31
updated: 2025-09-09T11:58
---

> [!example] LEDS CHANGE
> ![[Pasted image 20250909114414.png]]



# Inhoudsopgave

```toc
```

---

## if

### Commentaar

```c
// Beginwaarden van de variabelen
int invoer = 20;
int uitkomst = 0;
/*
Berekening van de resultaten vindt plaats aan het begin
*/
resultaat1 = 2 * invoer + marge;
resultaat2 = invoer + uitkomst;
```

```c
int main(void) {
	int waarde;
	scanf("%d", waarde)'
	
	// Print als de waarde > 0 is.
	
	return 0'
}
```

### Beslissen in NSD


| Waar | Niet Waar |
| ---- | --------- |
|      |           |
|      |           |
|      |           |
|      |           |

### Beslissen in C: if-statement

```c
if (conditie) {
	//Voer code uit voor uitkomst "Waar"
}
```

### Toepassing if-statement

```c
int main(void) {
	int snelheid;
	scanf("%d", &snelheid);
	
	if(snelheid > 50) {
		printf("U rijdt te hard \n");
	}
	
	return 0;
}

```

---

## AVR-Programmeren (Knipperend LED) 

### Knipperend ledje in NSD : deel 1

| Configureer LEDs |
| ---------------- |
| LED aan          |
| wacht 0,5 s      |
| LED uit          |
| wacht 0,5 s      | 

### Herhalen in NSD

| **Altijd**      |
| ----------- |
| <div></div> |
|             |
|             |

### Herhalen met while lus

```c
while (1) {
	//code die telkens wordt herhaald
}
```

### Knipperend ledje in NSD : deel 2

| **Altijd**           |
| ---------------- |
| Configureer LEDs |
| LED aan          |
| wacht 0,5 s      |
| LED uit          |
| wacht 0,5 s      |

### Knipperend LED in c
```c
#include <avr/io.h>

int main(void) {
	while(1) {
		// Wacht 0,5s
		_delay_ms(500);
		// Led aan
		DDRB = 0b00000000;
		// Wacht 0,5s
		_delay_ms(500);
		// Led uitn
		DDRB = 0b10000000;
	}
}
```


## In- en Output 

### Nummers en namen van pinnen

- Op de [[Arduino]] zijn alle pins genummerd
- De pinnen zijn verbonden met pinnen van de [[AVR]]

- Pinnetjes zijn gegroepeerd in banks van elk maximaal acht pinnen
- Lezen en schrijven vanuit software gaat via [[registers]] PA, PB, PC, PD etc.

### Configureer pin

- *Met welke pin is het ledje verbonden?*
	- <span style="color:rgb(146, 208, 80)">Antwoord in elektrisch schema en pinout</span>
- *Met welke waarde van de pin gaat de led aan?*
	- <span style="color:rgb(146, 208, 80)">Antwoord in elektrisch schema</span>
- *Hoe configureren we de pin als output pin?*
	- <span style="color:rgb(146, 208, 80)">Antwoord in de datasheet</span>

```c
#include <avr/io.h>
DDRB = 0b10000000;
PORTB = 0b10000000;
```

