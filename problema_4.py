print("introduceti numarul natural n", end=" ")
n = int(input())


def m_cm(a):
    print(a, "metrii in centimetrii ", a * 100, sep=" = ", end="\n")


def k_mg(a):
    print(a, "kilograme in miligrame ", a * 1000000, sep=" = ", end="\n")


def an_zile(a):
    luni = a * 12
    saptamani = a * 53
    zile = a * 365
    print("numarul de luni", luni, "numarul de zile", zile, " numarul de luni", luni, sep=" = ", end="\n")


print \
        (
        m_cm(n),
        k_mg(n),
        an_zile(n)
    )
