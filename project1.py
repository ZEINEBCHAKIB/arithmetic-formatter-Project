def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    firsts = []
    seconds = []
    operators = []
    results = []
    
    for problem in problems:
        parts = problem.split()
        first = parts[0]
        operator = parts[1]
        second = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        firsts.append(first)
        seconds.append(second)
        operators.append(operator)
        
        if operator == '+':
            results.append(str(int(first) + int(second)))
        else:
            results.append(str(int(first) - int(second)))
    
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    
    for i in range(len(problems)):
        length = max(len(firsts[i]), len(seconds[i])) + 2
        space1 = length - len(firsts[i])
        right_aligned_firsts = ' ' * space1 + firsts[i]
        line1.append(right_aligned_firsts)
        
        space2 = length - len(seconds[i]) - 1
        line2.append(operators[i] + ' ' * space2 + seconds[i])
        
        line3.append('-' * length)
        
        if show_answers:
            space4 = length - len(results[i])
            line4.append(' ' * space4 + results[i])
    
    arranged_problems = '    '.join(line1) + '\n' + '    '.join(line2) + '\n' + '    '.join(line3)      
    if show_answers:
        arranged_problems += '\n' + '    '.join(line4)
    
    return arranged_problems



print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49"], True))