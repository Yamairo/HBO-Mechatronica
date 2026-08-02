---
created: 2025-09-02T11:14
updated: 2025-09-02T12:03
---

# Inhoudsopgave
```toc
```

## Hello World

Een bassis programma dat `Hellow World` in de console weergeeft
`main.c`
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	printf("Hello World \n");
	return 0;
}
```

Een bassis programma dat `Het is nu 2025` in de console weergeeft, hierbij is `2025` een variabele die met vanalles vervangen kan worden door het gebruik van `%d`. In dit geval moet dit een decimaal getal zijn.
`main.c`
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	printf("Het is nu %d \n", 2025);
	return 0;
}
```

Een toepassing hiervan is het gebruiken van een variabele die in de string wordt geformat en uitgeprint.
`main.c`
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int jaar = 2025;
	printf("Het is nu %d \n", jaar);
	return 0;
}
```

### Commentaar

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int jaar = 2025;
	// Jaartal is nodig voor schermafdrukken
	printf("Het is nu %d \n", jaar);
	// printf("Demoversie\n")
	return 0; // wordt niet gebruikt
}
```

### Commentaaarblok
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	/*
	Dit programma doet niet zo veel.
	Het toont een jaartal,
	dat niet eens altijd klopt...
	*/
	int jaar = 2025;
	printf("Het is nu %d \n", jaar);
	return 0;
}
```

## Variabelenamen
**Deel 1**
- Gebruik geen keywords als variabele namen
- C is case sensitive
- Cijfers, letters en underscores mogen gebruikt worden
	- Begin niet met een cijfer
- Variabele namen moeten uniek zijn, je kan geen dubbele namen gebruiken

*Kunnen deze namen?*
- [-] 7-up
- [-] Seven-Up
- [v] A4
- [-] Return

**Deel 2**
- De naam moet beschrijvend zijn
- Overeenkomen met eigen standaard
- Is vaak een zelfstandig naamwoord

*Kunnen deze namen?*
- [-] result
- [-] herhalingen
- [v] aantal_herhalingen
- [v] aantalBultenVanKameel

### Invoer van een variabele

`main.c`
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int jaar;
	printf("Welk jaar is het nu?\n");
	scanf("%d", &jaar);
	printf("Het is nu%d.\n", jaar);
	return 0;
}
```

`main.c`
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int jaar;
	printf("Welk jaar is het nu?\n");
	scanf("%d", &jaar);
	jaar = jaar + 1;
	printf("Het is volgend jaar%d.\n", jaar);
	return 0;
}
```