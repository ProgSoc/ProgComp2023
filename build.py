from outputs import build_docs, build_problem_archives
from problems import read_and_process_problems, read_problems


problems = read_and_process_problems("problems")

build_problem_archives(problems)
build_docs(problems)
