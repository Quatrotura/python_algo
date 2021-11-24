# Подсчитать, сколько было выделено памяти под переменные в ранее 
# разработанных программах в рамках первых трех уроков. 
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# MacOS, 64bit
# SYakubov@192 ~ % python3
# Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:20) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin

# ссылка на рекурсивную функцию с офиц сайта: https://docs.python.org/3/library/sys.html

from __future__ import print_function
from sys import getsizeof, stderr
from itertools import chain
from collections import deque
try:
    from reprlib import repr
except ImportError:
    pass

def total_size(o, handlers={}, verbose=False):
    """ Returns the approximate memory footprint an object and all of its contents.

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    """
    dict_handler = lambda d: chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                   }
    all_handlers.update(handlers)     # user handlers take precedence
    seen = set()                      # track which object id's have already been seen
    default_size = getsizeof(0)       # estimate sizeof object without __sizeof__

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        if verbose:
            print(s, type(o), repr(o), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)

# Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, 
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# Андрей, возможно я слишком заморачиваюсь, но мне кажется, что 
# правильно измерить кол-во выделенной памяти на переменные след образом:
# надо учитывать, что числа от -5 до 256 зашиты в билде и так сказать константны и они будут занимать место в памяти в любом случае,
# то есть если две переменные
# ссылаются на целое число 2, то память под 2 выделяется один раз в любом случае, один раз выделяется память на ссылки для каждой переменной
# соответственно если объект один и тот же (одинаковый id) и встроен в билд для двух переменных, то правильно было бы замерить 
# только вес ссылок для каждой переменной в отдельности
# далее, есть переменная, к примеру, b, у нее начальное значение целое число 9999999999, выделено 32 бита памяти (на объект и ссылки)
# далее значение переменной b изменяется, к примеру, на целое число 1, под b = 1 требуется уже 28 бит памяти, объект
# остается в том же блоке(которые каталогизируются по объему выделенной памяти, к пример есть блок 25-32 бита), весь блок занимает 32 бита
# и в том же пуле, но разницу (4 бита) питон в данном случае не освобождает, то есть надо учитывать размерность блоков
# соответственно в данном случае было бы правильно считать, что питон под приложение выделил 32 бита, а не 28 бит

a = 300
b = 300

print(id(a))
print(id(a))

print(total_size(a))
print(getsizeof(a))

a = '1265' # в задании пользователь вводит, убрал input для простоты

even, odd = 0, 0
print('a', total_size(a))
print('even', total_size(even))
print('odd', total_size(odd))

if a.isdigit() == True and a[0] != '0':
	a = int(a)
	print('a is int', total_size(a))
	while a > 0:		
		if a % 2 == 0:
			even += 1
			print(total_size(even))
		else:
			odd += 1
			print(total_size(even))

		a = a // 10
		print(total_size(a))

	print(f'There are {even} even digits and {odd} odd digits in your number.')
else:
	print('Enter only natural numbers')

