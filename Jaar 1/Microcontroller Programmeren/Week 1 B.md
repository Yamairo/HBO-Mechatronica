---
created: 2025-09-04T10:35
updated: 2025-09-04T11:11
---
# Inhoudsopgave

```toc
```

---

## Optellen, aftrekken en vermenigvuldigen

`main.c`
```c
int x = 7;
int x = 4;

int main(void) {
	printf("%d", x + y); // 11
	printf("%d", x - y); // 3
	printf("%d", x * y); // 28
}
```
 
---

## Gehele deling

`main.c`
```c
int x = 7;
int y = 2;
int z = 2;

int main(void) {
	printf("%d", x / y); // 3
	printf("%d", y / z); // -1
	printf("%d", x / z); // -3
}
```

---

## Rest (modulus)

`main.c`
```c
int x = 7;
int y = 2;
int z = -2;

int main(void) {
	printf("%d", x % y); // 1
	printf("%d", x % z); // 1
}
```

---


