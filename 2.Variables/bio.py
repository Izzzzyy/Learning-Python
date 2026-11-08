"""
EJERCICIOS DE VARIABLES EN PYTHON (edición bio-matemática)
===========================================================

Cómo usar este archivo:
  1. Busca las líneas con `None` o con el comentario  # TU CÓDIGO AQUÍ
  2. Reemplázalas con tu solución.
  3. Ejecuta el archivo completo:  python ejercicios_variables.py
  4. Cada ejercicio se autocorrige con ✅ o ❌. Al final verás tu puntaje.

Regla de oro: no mires las pistas hasta haberlo intentado 5 minutos.
(Sí, te vi pensando en copiar y pegar. Eso no compila neuronas.)
"""

import math

_ok = 0
_total = 0


def revisar(num, condicion, pista=""):
    """Evalúa un ejercicio sin que el programa explote si no está resuelto."""
    global _ok, _total
    _total += 1
    try:
        resultado = bool(condicion())
    except Exception:
        resultado = False
    if resultado:
        _ok += 1
        print(f" Ejercicio {num}: ¡bien!")
    else:
        print(f" Ejercicio {num}: aún no.  Pista: {pista}")


# ----------------------------------------------------------------
# EJERCICIO 1 · Asignación básica
# Guarda el nombre del gen "TP53" (texto) y su número de exones, 11 (entero).
# ----------------------------------------------------------------
nombre_gen = "TP53"
num_exones = 11

revisar(1,
        lambda: nombre_gen == "TP53" and num_exones == 11 and type(num_exones) is int,
        "El texto va entre comillas; el numero, sin comillas.")


# ----------------------------------------------------------------
# EJERCICIO 2 · Los cuatro tipos básicos
# es_codificante  -> bool, verdadero
# longitud_kb     -> float, 19.1
# organismo       -> str, "Homo sapiens"
# cromosoma       -> int, 17
# ----------------------------------------------------------------
es_codificante = True
longitud_kb = 19.1
organismo = "Homo sapiens"
cromosoma = 17

revisar(2,
        lambda: es_codificante is True
        and type(longitud_kb) is float and longitud_kb == 19.1
        and organismo == "Homo sapiens"
        and type(cromosoma) is int and cromosoma == 17,
        "True con T mayúscula, sin comillas. El float lleva punto decimal.")


# ----------------------------------------------------------------
# EJERCICIO 3 · Preguntarle a Python qué es cada cosa
# Guarda en `tipo_organismo` el TIPO de la variable `organismo`.
# (No escribas "str" a mano: usa la función que averigua tipos.)
# ----------------------------------------------------------------
tipo_organismo = type(organismo)

revisar(3,
        lambda: tipo_organismo is str,
        "La función se llama type().")


# ----------------------------------------------------------------
# EJERCICIO 4 · Aritmética con variables: contenido GC
# Ya tienes el conteo de bases de un fragmento.
# total_bases  = suma de las cuatro bases
# contenido_gc = porcentaje de (G + C) sobre el total  (0 a 100)
# ----------------------------------------------------------------
g, c, a, t = 412, 388, 350, 350
total_bases = g + a + t + c
contenido_gc = (g + c) / total_bases * 100

revisar(4,
        lambda: total_bases == 1500 and math.isclose(contenido_gc, 53.3333, rel_tol=1e-3),
        "Porcentaje = parte / total * 100. Usa paréntesis para (g + c).")


# ----------------------------------------------------------------
# EJERCICIO 5 · Intercambiar valores
# Deja codon_a con "TAA" y codon_b con "ATG" (intercámbialos).
# Pista de nivel Pythonista: se puede en UNA sola línea, sin variable temporal.
# ----------------------------------------------------------------
codon_a = "ATG"
codon_b = "TAA"
# TU CÓDIGO AQUÍ (después de esta línea)

codon_a, codon_b = codon_b, codon_a


revisar(5,
        lambda: codon_a == "TAA" and codon_b == "ATG",
        "a, b = b, a")


# ----------------------------------------------------------------
# EJERCICIO 6 · Conversión de tipos
# Un termómetro te entrega la lectura como TEXTO.
# temperatura   -> float
# temp_entera   -> int (parte entera de la temperatura)
# temp_texto    -> str de temp_entera
# Ojo: int("37.5") revienta. Piensa en el orden de las conversiones.
# ----------------------------------------------------------------
lectura = "37.5"
temperatura = float(lectura)
temp_entera = int(temperatura)
temp_texto = str(temp_entera)

revisar(6,
        lambda: temperatura == 37.5 and type(temperatura) is float
        and temp_entera == 37 and type(temp_entera) is int
        and temp_texto == "37" and type(temp_texto) is str,
        "float(...) primero, luego int(...) sobre el float, luego str(...).")


# ----------------------------------------------------------------
# EJERCICIO 7 · f-strings
# Con las variables del ejercicio 1, construye EXACTAMENTE este texto:
#   "El gen TP53 tiene 11 exones"
# Sin escribir TP53 ni 11 a mano: usa las variables.
# ----------------------------------------------------------------
mensaje = f"El gen {nombre_gen} tiene {num_exones} exones"

revisar(7,
        lambda: mensaje == "El gen TP53 tiene 11 exones",
        'f"... {variable} ..."  (no olvides la f antes de las comillas).')


# ----------------------------------------------------------------
# EJERCICIO 8 · Variables de texto y sus métodos
# Dada la secuencia, calcula:
# longitud        -> cuántas bases tiene
# n_adenina       -> cuántas "A" hay
# secuencia_minus -> la secuencia en minúsculas
# ----------------------------------------------------------------
secuencia = "ATGCGTACGTTAGC"
longitud = len(secuencia)
n_adenina = secuencia.count("A")
secuencia_minus = secuencia.lower()

revisar(8,
        lambda: longitud == 14 and n_adenina == 3 and secuencia_minus == "atgcgtacgttagc",
        "len(), .count() y .lower()")


# ----------------------------------------------------------------
# EJERCICIO 9 · Asignación múltiple
# En UNA sola línea, inicializa en 0 los contadores:
# contador_a, contador_c, contador_g, contador_t
# ----------------------------------------------------------------
contador_a, contador_c, contador_g, contador_t = 0, 0, 0, 0

revisar(9,
        lambda: (contador_a, contador_c, contador_g, contador_t) == (0, 0, 0, 0),
        "w, x, y, z = 0, 0, 0, 0")


# ----------------------------------------------------------------
# EJERCICIO 10 · Crecimiento bacteriano
# Fórmula:  N = N0 * 2 ** (t / td)
# Con N0 = 100 bacterias, td = 20 min (tiempo de duplicación), t = 120 min,
# calcula `poblacion`.
# ----------------------------------------------------------------
N0 = 100
td = 20
t_min = 120
poblacion = N0 * 2 ** (t_min / td)

revisar(10,
        lambda: math.isclose(poblacion, 6400),
        "** es la potencia. Cuidado con la precedencia: 2 ** (t_min / td).")


# ----------------------------------------------------------------
# EJERCICIO 11 · Nombres de variables válidos
# Estos nombres están PROHIBIDOS en Python (por eso van comentados):
#     1gen = "TP53"
#     mi-variable = 5
#     class = "mamifero"
#     tasa mutacion = 0.01
# Escribe versiones VÁLIDAS (y con estilo snake_case):
#     gen_1 = "TP53"
#     mi_variable = 5
#     clase = "mamifero"
#     tasa_mutacion = 0.01
# ----------------------------------------------------------------
gen_1 = "TP53"
mi_variable = 5
clase = "mamifero"
tasa_mutacion = 0.01

revisar(11,
        lambda: gen_1 == "TP53" and mi_variable == 5
        and clase == "mamifero" and tasa_mutacion == 0.01,
        "No empiezan con número, no llevan guiones ni espacios, ni son palabras reservadas.")


# ----------------------------------------------------------------
# EJERCICIO 12 · Constantes (por convención)
# Python no tiene constantes de verdad, pero se escriben en MAYÚSCULAS.
# Crea NUM_AVOGADRO = 6.022e23 y calcula las moléculas en 2 moles.
# ----------------------------------------------------------------
moles = 2
NUM_AVOGADRO = 6.022e23
moleculas = moles * NUM_AVOGADRO

revisar(12,
        lambda: NUM_AVOGADRO == 6.022e23 and math.isclose(moleculas, 1.2044e24),
        "La notación científica se escribe 6.022e23.")


# ----------------------------------------------------------------
# EJERCICIO 13 · Hardy-Weinberg
# Si la frecuencia del alelo A es p = 0.7, calcula:
# q       = frecuencia del alelo a           (q = 1 - p)
# freq_AA = p ** 2
# freq_Aa = 2 * p * q
# freq_aa = q ** 2
# ----------------------------------------------------------------
p = 0.7
q = 1 - p
freq_AA = p ** 2
freq_Aa = 2 * p * q
freq_aa = q ** 2

revisar(13,
        lambda: math.isclose(q, 0.3) and math.isclose(freq_AA, 0.49)
        and math.isclose(freq_Aa, 0.42) and math.isclose(freq_aa, 0.09)
        and math.isclose(freq_AA + freq_Aa + freq_aa, 1.0),
        "Las tres frecuencias genotípicas deben sumar 1. Si no, hay un error.")


# ----------------------------------------------------------------
# EJERCICIO 14 · La trampa del punto flotante
# suma           = 0.1 + 0.2
# es_igual       = ¿suma == 0.3 ?   (spoiler: te sorprenderá)
# son_casi_iguales = comparación correcta usando math.isclose
# Python sí sabe sumar; el problema es cómo guarda los decimales en binario.
# Como futuro ingeniero MAC, esto te va a perseguir en métodos numéricos.
# ----------------------------------------------------------------
suma = 0.1 + 0.2
es_igual = suma == 0.3
son_casi_iguales = math.isclose(suma, 0.3)

revisar(14,
        lambda: suma == 0.1 + 0.2 and es_igual is False and son_casi_iguales is True,
        "math.isclose(suma, 0.3) devuelve True.")


# ----------------------------------------------------------------
# EJERCICIO 15 (BONUS CRÍTICO) · Variables son etiquetas, no cajas
# NO ejecutes primero. Predice y luego verifica.
# ¿Cuántos elementos tendrá lista_a después de las líneas de abajo?
# Guarda tu predicción en `prediccion`.
# ----------------------------------------------------------------
prediccion = 4

lista_a = [1, 2, 3]
lista_b = lista_a
lista_b.append(4)

revisar(15,
        lambda: prediccion == len(lista_a),
        "lista_b = lista_a NO copia la lista: ambas etiquetas apuntan al mismo objeto.")


# ----------------------------------------------------------------
# RESULTADO FINAL
# ----------------------------------------------------------------
print("\n" + "=" * 40)
print(f"Puntaje: {_ok}/{_total}")
if _ok == _total:
    print(" Perfecto. Ahora intenta romperlo a proposito: eso tambien enseña.")
elif _ok >= _total * 0.7:
    print(" Bien, pero revisa los X antes de celebrar.")
else:
    print(" Todavía en fase experimental. Normal: así empiezan todos los científicos.")