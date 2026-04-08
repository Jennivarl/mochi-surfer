from genvm_linter import GenVMLinter
linter = GenVMLinter()
results = linter.lint_file('./contracts/leaderboard.py')
for r in results:
    print(r.severity.name + ' L' + str(r.line) + ': ' + r.message)
if not results:
    print('PASS - no issues found')
