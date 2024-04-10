from math import log,exp, cos


def bisseccao(f, a, b, tol, max_iter=100):

    if f(a) * f(b) > 0:
        raise ValueError("A função deve ter sinais opostos em a e b.")

    iter_count = 0
    while abs(b - a) / 2 > tol and iter_count < max_iter:
        x = (a + b) / 2
        if f(x) == 0:
            return x,iter_count
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
        iter_count += 1
        print(f(x))

    return (a + b) / 2, iter_count


def funcao_exemplo(x):
    return  x*log(x,10)-1           """ funcao da formula """
a = float(input("Digite o intervalo inferior:"))
b = float(input("Digite o intervalo superior:"))
tol = float(input("Digite o valor da tolerância:\n"))
raiz, iteracoes = bisseccao(funcao_exemplo, a, b,tol)
print("A raiz da função é aproximadamente:", raiz)
print("Número de iterações:", iteracoes)
