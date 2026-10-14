# ---------- 1) FERRAMENTA ----------
# Traz do SciPy a função linprog, que resolve problemas de programação linear
from scipy.optimize import linprog

# ---------- 2) FUNÇÃO OBJETIVO ----------
# Lucros por unidade, na ordem [x1 = camiseta, x2 = calça]
# Estão NEGATIVOS porque o linprog só MINIMIZA.
# Maximizar 3x1 + 5x2  é o mesmo que  minimizar -3x1 - 5x2.
c = [-3, -5]

# ---------- 3) RESTRIÇÕES ----------
# Cada linha de A é uma restrição, na ordem [x1, x2]:
#   2x1 + 1x2 <= 8   (horas)
#   1x1 + 2x2 <= 8   (tecido)
A = [[2, 1],
     [1, 2]]

# Lado direito de cada restrição (o que está disponível)
b = [8, 8]

# ---------- 4) RESOLUÇÃO ----------
# A_ub e b_ub significam "upper bound": restrições do tipo <=
# bounds define os limites de cada variável: (0, None) é x >= 0, sem limite superior
# method="highs" é o algoritmo de resolução
resultado = linprog(c, A_ub=A, b_ub=b,
                    bounds=[(0, None), (0, None)],
                    method="highs")

# ---------- 5) RESULTADO ----------
# resultado.x   = lista com os valores ótimos [x1, x2]
# resultado.fun = valor da função objetivo (negativo, por causa da troca de sinal)
x1, x2 = resultado.x
lucro = -resultado.fun    # desfaz a troca de sinal

print("Camisetas (x1):", round(x1, 2))
print("Calças (x2):", round(x2, 2))
print("Lucro total:", round(lucro, 2))

# ---------- 6) PREÇO SOMBRA ----------
# marginals guarda a variação da função objetivo por unidade extra de cada recurso.
# Como trocamos o sinal do lucro, trocamos de novo aqui.
sombra = -resultado.ineqlin.marginals
print("Preço sombra (horas):", round(sombra[0], 2))
print("Preço sombra (tecido):", round(sombra[1], 2))

# ---------- 7) FOLGA ----------
# resultado.slack = quanto sobrou de cada recurso (b - A·x)
print("Folga (horas, tecido):", [round(s, 2) for s in resultado.slack])