#5. 1.	Пользователь вводит данные о количестве предприятий, 
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) 
# и вывести наименования предприятий, чья прибыль выше среднего 
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

entity_profit_by_q = collections.defaultdict(tuple)
entity_qty = int(input('Введите количество предприятий: '))
total_profit = float()
entities_above_avrg = ''
entities_below_avrg = ''

for i in range(entity_qty):
	entity_name = input('Введите наименование предприятия: ')
	profit_by_q = input('Введите прибыль за 1, 2, 3, 4 кварталы через пробел: ')

	entity_profit_by_q[entity_name] = tuple(map(float, (profit_by_q.split())))
	total_profit += sum(entity_profit_by_q[entity_name])


for j in entity_profit_by_q:
	# предприятия чья прибыль выше среднего
	if sum(entity_profit_by_q[j]) > (total_profit / entity_qty):
		entities_above_avrg += f'{j}\n'
	# предприятия чья прибыль ниже среднего
	elif sum(entity_profit_by_q[j]) < (total_profit / entity_qty):
		entities_below_avrg += f'{j}\n'

print(f'Предприятия с годовой прибылью выше среднего:\n{entities_above_avrg}\nПредприятия с прибылью ниже среднего:\n{entities_below_avrg}')