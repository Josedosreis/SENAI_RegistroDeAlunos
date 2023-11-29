# Gerenciamento de dados dos alunos


# Apresentação

print("\n\t\t\t -- Registered students -- \n")

# Entrada

student = str(input('Digite o nome do student: '))
note = float(input("Digit a nota do student: "))
course = str(input('Digit o curso do student: '))
matricula = bool(input('active or desactive: '))


# Processamento

register = {'Nome': 'nome', 'Nota': 'nota', 'Curso': 'curso', 'Matrícula': ''}

register['Nome'] = student
register['Nota'] = note
register['Curso'] = course

register['Matrícula'] = matricula

# saída

if matricula == 'active':
    print('true')
else:
    print('false')


print(f'{register}')

