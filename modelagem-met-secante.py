from math import log, exp, cos


def falsa_posicao(f, a, b, tol, max_iter=100):

    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos em a e b.")
    iter_count = 0
    u=1
    while u> tol and iter_count < max_iter:
        x = (a*f(b)-b*f(a))/(f(b)-f(a))
        u=abs(f(x))
        if f(x) == 0:
            return x
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
        iter_count += 1

    return x, iter_count


# Exemplo de uso
def funcao_exemplo(x):
    return x*log(x,10)-1

a = float(input("Digite o intervalo inferior:"))
b = float(input("Digite o intervalo superior:"))
tol = float(input("Digite o valor da tolerância:\n"))
raiz, iteracoes = falsa_posicao(funcao_exemplo, a, b,tol)
print("A raiz da função é aproximadamente:", raiz)
print("Número de iterações:", iteracoes)
