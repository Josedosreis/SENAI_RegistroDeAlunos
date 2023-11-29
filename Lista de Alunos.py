# Gerenciamento de dados dos alunos


# Apresentação

print("\n\t\t\t -- Registered students -- \n")

# Entrada

student = str(input('Digit the name do student: '))
note = float(input("Digit a note do student: "))
course = str(input('Digit the course do student: '))
matricula = input('active or desactive: ')


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

