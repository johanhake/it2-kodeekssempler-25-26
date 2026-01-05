## Oppgave 1

a) 

| i | m | sum |
| - | - | --- |
| 2 | 3 | 6   |
| 3 | 2 | 12  |
| 4 | 1 | 16  |

**Svar: Tallet 16 blir skrevet ut**

b) 

| i | sum |Forklaring                |
| - | --- |--------------------------|
| 2 | 0   |start, i partall          |
| 3 | 12  |i oddetall, sum får verdi |
| 4 | 12  |i partall, sum samme      | 
| 5 | 42  |i oddetall, sum får verdi |

**Svar: Tallet 42 blir skrevet ut**

c) 

If-testene gjøres i feil rekkefølge. Hvis tallet er 100, er det større enn 0, og "Tallet er mellom 1 og 10" skrives ut, som er feil. Riktig pseudokode er:

```
PRINT "Skriv inn et heltall:"
READ tall
IF tall GREATER THAN 20
    PRINT "Tallet er over 20"
ELSE IF tall GREATER THAN 10
    PRINT "Tallet er mellom 11 og 20"
IF tall GREATER THAN 0 
    PRINT "Tallet er mellom 1 og 10"
ELSE  
    PRINT "Tallet er 0 eller negativt"
ENDIF
```

Det er også mulig å teste at tallet skal ligge innenfor intervaller, som for eksempel

`IF tall GREATER THAN 0 AND tall LESSER THAN 11`

d) Programmet viser bruk av en rekursiv funksjon. En funksjon som kaller seg selv. Den beregner summen til: `5 + 4 + 3 + 2 + 1 = 15`

**Svar: Tallet 15 blir skrevet ut**
