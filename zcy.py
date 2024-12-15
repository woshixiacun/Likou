import meijulei
import inspect

m = meijulei.STATUS.MON.value
print(m)

cmd = 'init()'
res = '结果'

def add():
    lineno = inspect.stack()[0].lineno
    lineno2 = inspect.stack()[1].lineno
    print(f'[{lineno}]{cmd}'+f'---------------》{111}')
    print(f'[{lineno2}]{cmd}'+f'---------------》{res}')

# lineno = inspect.stack()[0].lineno
add()

print(f'\033[1;33m{str(123456).zfill(10)}\033[0m\n')



