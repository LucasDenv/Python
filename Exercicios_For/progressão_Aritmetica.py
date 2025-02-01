first_term = int(input('Digite o primeiro termo da P.A:  '))
ratio = int(input('Digite a razão da P.A: '))
p_a = 0
for aux in range(0,10):
    if first_term > p_a:
        print(first_term, end = ' ')
        p_a = first_term
    else:
        p_a += ratio
        print(p_a, end = ' ')

