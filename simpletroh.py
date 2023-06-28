
print('''----------------------------------------------------------------------------------------
[SIMPLETRON]
- Para realizar uma simulação, será necessário entrar com uma unidade de instrução ou dado em determinada posição da memória -
- As posições(endereços) serão exibidas em ordem e seu número irá aparecer para questões de melhor organização, no formato "00/"-
- Para finalizar os inputs, digite "-00" e a simulação irá começar a ser carregada -
----------------------------------------------------------------------------------------''')

# Células na memória (00 até 49)
cells = ['0000'] * 50
storage = 0 # Variável para armazenar o conteúdo que será armazenado 
end = 0 # Variável para controlar o endereçamento
pc = rem = 0
rdm = 0
ri = 0
r0 = 0

# Instruções SIMPLETRON

# Operações aritméticas
add = 30
sub = 31 # Subtract 
div = 32 # Divide 
mul = 33 # Multiply
# Operações de entrada/saída 
read = 11 
write = 10
# Operações de carga/armazenamento
load = 20
store = 21 
# Operações de transferência de controle
branch = 40
branchNEG = 41 # Branchneg
branch0 = 42 # Branchzero
halt = 43

# Seção Para definir o conteúdo da memória 
while storage != '-00':
    storage = input(f'0{end}/ ')
    if storage != '-00':
        cells[end] = storage
    end += 1

print('''----------------------------------------------------------------------------------------
Dados carregados para a memória 
[Iniciando execução da simulação. . .]
----------------------------------------------------------------------------------------
''')

for i in range(len(cells)):
        COp = int(cells[i][:2]) # Código de operação
        rem = pc = COp
        rdm = ri = cells[i]
        Op = int(cells[i][2:]) if cells[i][2:] else 0 # Operando
        if COp == halt:
            print('[Finalizando a simulação. . .]')
            break
        elif COp == write:
            print('Digite um novo conteúdo para ser escrito na memória:')
            cells[Op] = input(f'{Op}/ ')
        elif COp == read:
            print(cells[Op])
        elif COp == store:
            cells[Op] = str(r0)
        elif COp == load:
            r0 = int(cells[Op])
        elif COp == branch:
            COp = cells[Op]
            continue
        elif COp == branchNEG:
            if r0 < 0:
                COp = cells[Op]
                continue
        elif COp == branch0:
            if r0 == 0:
                COp = cells[Op]
                continue 
        elif COp == mul:
            r0 *= int(cells[Op])
        elif COp == div:
            r0/= int(cells[Op])
        elif COp == add:
            r0 += int(cells[Op])
        elif COp == sub:
            r0 -= int(cells[Op])

print(f'''----------------------------------------------------------------------------------------
[PROCESSADOR]
REM - {rem}
RI - {ri}
R0 - {r0}
----------------------------------------------------------------------------------------''')

# Seção para exibir o contéudo da memória 
end = 0
print('[MEMÓRIA]')
for i in range(len(cells)):
    print(f'{end}/ {cells[i].zfill(4)}')
    end += 1

