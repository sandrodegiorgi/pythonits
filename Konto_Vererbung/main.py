from Konto import Konto
from GiroKonto import GiroKonto

import inspect

print(Konto.__doc__)
print(GiroKonto.__doc__)


# Konten anlegen
a = GiroKonto("Emil Braun")
b = GiroKonto("Helga Schmitt", 42)
c = GiroKonto()

d = GiroKonto.fromname("Maexle Maximalius")
e = GiroKonto.fromnamemitersteinzahlung(ersteinzahlung=235, name="Lieschen Mueller")

g = GiroKonto.fromnamemitersteinzahlung(ersteinzahlung=1235, name="Girokonto Man")

# Kontodaten audgeben
print(a)
print(b)
print(c)

# Operationen
a.einzahlen(560.6)
b.einzahlen(1340.0)
c.einzahlen(300.0)

# Kontodaten audgeben
print(a)
print(b)
print(c)

print(d)
d.__inhaber = "Cassius Clay not working?!"  # will work on "protected" though!
print(d)
d.inhaber = "Cassius Clay working"
print(d)

print(e)

print(g)
g.gk_method()


print(inspect.getmro(GiroKonto))

print("Nächste kontoNummer: ", Konto.getNaechsteNummer() )
