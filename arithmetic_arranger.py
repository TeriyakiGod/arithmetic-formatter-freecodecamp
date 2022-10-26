def arithmetic_arranger(problems, displayAnswers = False):
                        
  solution = ""
  problemsCount = 0
  terms1 = []
  terms2 = []
  operators = []
  lengths = []
  answers = []

  for problem in problems:
    problemsCount +=1
    
    if problemsCount > 5:
      return "Error: Too many problems."
      
    splitProblem = problem.split()
    term1 = splitProblem[0]
    operator = splitProblem[1]

    if (operator != '+' and operator != '-'):
      return "Error: Operator must be '+' or '-'."
    
    term2 = splitProblem[2]

    if not(term1.isdigit()) or not(term2.isdigit()):
      return "Error: Numbers must only contain digits."

    if len(term1) > 4 or len(term2) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    length = len(term1)+2 if len(term1) > len(term2) else len(term2)+2
    terms1.append(term1)
    operators.append(operator)
    terms2.append(term2)
    lengths.append(length)

    if displayAnswers:
      if operator == '+':
        answers.append(str(int(term1) + int(term2)))
      else:
        answers.append(str(int(term1) - int(term2)))

  for i in range(problemsCount):
    solution += terms1[i].rjust(lengths[i])
    if i != problemsCount-1:
      solution += "    "
  solution += "\n"
  for i in range(problemsCount):
    solution += operators[i] + terms2[i].rjust(lengths[i] - 1)
    if i != problemsCount-1:
      solution += "    "
  solution += "\n"
  for i in range(problemsCount):
    for l in range(lengths[i]):
      solution += "-"
    if i != problemsCount-1:
      solution += "    "
  if displayAnswers:
    solution += "\n"
    for i in range(problemsCount):
      solution += answers[i].rjust(lengths[i])
      if i != problemsCount-1:
        solution += "    "

  return solution