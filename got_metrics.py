import sys
import psutil

def main():

    try:

        type = sys.argv[1]
    except Exception:
        print('Please use argument. (mem | cpu)')
        sys.exit(1)

    if str.lower(type) == 'cpu':
        print('\nCPU: \n')    
        cpu = psutil.cpu_times(percpu = False)
        print('system.cpu.idle', cpu.idle) 
        print('system.cpu.user', cpu.user)
        print('system.cpu.guest', cpu.guest)
        print('systemc.cpu.iowait', cpu.iowait)
        print('systemc.cpu.stolen', cpu.steal)
        print('system.cpu.system', cpu.system)




    elif str.lower(type) == 'mem':
        print('\nMEM: \n')
        mem = psutil.virtual_memory()
        swp = psutil.swap_memory()
        print('virtual total', mem.total)
        print('virtual used', mem.used)
        print('virtual free', mem.free)
        print('virtual shared', mem.shared)
        print('swap total', swp.total)
        print('swap used', swp.used)
        print('swap free', swp.free)





    else:
        print('Only (mem | cpu) arguments are allowed')

main()
