from math import pow, log, ceil
from sys import argv

def calc_x(i, n):
    pw = pow(i + 1, n)
    x = (i * pw) / (pw - 1)
    return x

def calc_a(interest, periods, principal):
    return ceil(principal * calc_x(interest, periods))
    
def calc_d(interest, periods, principal):
    d = []
    for m in range(0, int(periods)):
        d_m = principal / periods + interest * (principal - (principal * (m)) / periods)
        d.append(d_m)
        
    return d
    
def calc_p(interest, periods, payment):
    return payment / calc_x(interest, periods)
    
def calc_n(interest, payment, principal):
    return ceil(log(payment / (payment - interest * principal), interest + 1))

args = argv[1:]
params = {}
error_msg = "Incorrect parameters"

for arg in args:
    arg = arg.strip('-')
    arg_parts = arg.split('=')
    key = arg_parts[0]
    params[key] = arg_parts[1] if key == 'type' else float(arg_parts[1])
    

if 'type' not in params or len(params) != 4 or 'interest' not in params:
    print(error_msg)
else:
    params['interest'] = params['interest'] / (100 * 12)
    calc_params = {k: v for k, v in params.items() if k != 'type'}
    if params['type'] == 'annuity':
        if 'principal' not in params:
            params['principal'] = calc_p(**calc_params)
            print(f"Your loan principal = {params['principal']}!")        
        elif 'payment' not in params:
            params['payment'] = calc_a(**calc_params)
            print(f"Your monthly payment = {params['payment']}!")
        elif 'periods' not in params:
            params['periods'] = calc_n(**calc_params)
            n = params['periods']
            print(f"It will take {n // 12} years and {f'{n % 12} months' if n % 12 else ''} to repay this loan!")
            
        print(f"Overpayment {params['payment'] * params['periods'] - params['principal']}")
                
    elif params['type'] == 'diff':
        d = calc_d(**calc_params)
        sum = 0
        for m, d_m in enumerate(d):
            print(f"Month {m + 1}: payment is {ceil(d_m)}")
            sum += ceil(d_m)
        
        print(f"Overpayment {sum - params['principal']}")
    else:
        print(error_msg)
