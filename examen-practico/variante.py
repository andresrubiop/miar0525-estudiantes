"""Asigna la variante del examen práctico (estado de EE. UU. y semilla) a partir del código de estudiante.

    python variante.py A00123456

La asignación es determinista: el mismo código siempre da la misma variante. Solo se usan estados con al menos
10 000 personas en ACS Income, para que el análisis por grupos tenga datos suficientes.
"""
import hashlib
import sys

ESTADOS = ["AL", "AR", "AZ", "CA", "CO", "CT", "FL", "GA", "IA", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "MI", "MN",
           "MO", "MS", "NC", "NE", "NJ", "NV", "NY", "OH", "OK", "OR", "PA", "SC", "TN", "TX", "UT", "VA", "WA", "WI"]


def asignar_variante(codigo: str) -> tuple[str, int]:
    """Devuelve (estado, semilla) para un código de estudiante."""
    h = hashlib.sha256(f"MIAR0525-2026|{codigo.strip().upper()}".encode()).hexdigest()
    return ESTADOS[int(h[:8], 16) % len(ESTADOS)], 1000 + int(h[8:16], 16) % 9000


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python variante.py <tu código de estudiante>")
    estado, semilla = asignar_variante(sys.argv[1])
    print(f"Estado: {estado} · semilla: {semilla}")
