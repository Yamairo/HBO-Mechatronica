---
created: 2026-09-07T22:53
updated: 2026-09-07T23:00
---
```dataview
TABLE WITHOUT ID L.date as "Datum", L.start as "Start Tijd", L.end as "Eind Tijd", L.activity as "Taak" FROM "Logboek" FLATTEN file.lists as L WHERE L.activity SORT L.date DESC, L.start DESC
```