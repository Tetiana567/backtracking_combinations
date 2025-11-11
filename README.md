# Backtracking-Algorithmus in Python

Dieses kleine Übungsprojekt zeigt, wie man mit Hilfe eines rekursiven Backtracking-Algorithmus alle möglichen Zahlenkombinationen findet, deren Summe einem vorgegebenen Zielwert entspricht.

## Beschreibung

Der Algorithmus durchläuft systematisch alle möglichen Kombinationen von Zahlen aus einer gegebenen Liste und überprüft, ob deren Summe dem Zielwert (target) entspricht.  
Jede Zahl darf dabei nur einmal verwendet werden.

## Beispiel

```python
candidates = [2, 3, 4, 5, 6]
target = 7
print(find_combinations(candidates, target))
# Ausgabe: [[2, 5], [3, 4]]
