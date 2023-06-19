import os
from typing import List, NamedTuple, Optional
import yaml
from joblib import Parallel, delayed

from run_solutions import (
    LanguageSolution,
    ProblemTestCase,
    run_all_solutions,
    run_languages_solution,
)


class ProblemData(NamedTuple):
    name: str
    timelimit: float


class Problem(NamedTuple):
    foldername: str
    data: ProblemData
    description_path: str
    language_solutions: List[LanguageSolution]
    sample_paths: List[str]
    secret_paths: List[str]


class CheckedProblem(NamedTuple):
    foldername: str
    data: ProblemData
    markdown_description: str
    language_solutions: List[LanguageSolution]
    samples: List[ProblemTestCase]
    secrets: List[ProblemTestCase]


def load_problem_metadata_file(file_path: str) -> ProblemData:
    if not os.path.isfile(file_path):
        raise Exception(f"File {file_path} does not exist")
    with open(file_path, "r") as f:
        problem_yaml = yaml.safe_load(f)

    return ProblemData(name=problem_yaml["name"], timelimit=problem_yaml["timelimit"])


def read_problem(folder_path: str) -> Problem:
    problem_yaml_path = os.path.join(folder_path, "problem.yml")
    if not os.path.isfile(problem_yaml_path):
        raise Exception(f"Problem {folder_path} does not have a problem.yml file")

    problem_data = load_problem_metadata_file(problem_yaml_path)

    description_path = os.path.join(folder_path, "description.md")

    language_solutions = []
    for filename in os.listdir(folder_path):
        if filename.startswith("solution."):
            kind = filename.split(".")[-1]
            solution_path = os.path.join(folder_path, filename)
            scaffold_path = (
                os.path.join(folder_path, f"scaffold.{kind}")
                if os.path.isfile(os.path.join(folder_path, f"scaffold.{kind}"))
                else None
            )
            language_solutions.append(
                LanguageSolution(
                    kind=kind, solution_path=solution_path, scaffold_path=scaffold_path
                )
            )
    language_solutions = sort_solutions(language_solutions)

    sample_paths = [
        os.path.join(folder_path, "samples", filename)
        for filename in sorted(os.listdir(os.path.join(folder_path, "samples")))
    ]
    secret_paths = [
        os.path.join(folder_path, "secrets", filename)
        for filename in sorted(os.listdir(os.path.join(folder_path, "secrets")))
    ]

    foldername = os.path.basename(folder_path)

    return Problem(
        foldername=foldername,
        data=problem_data,
        description_path=description_path,
        language_solutions=language_solutions,
        sample_paths=sample_paths,
        secret_paths=secret_paths,
    )


def sort_solutions(solutions: List[LanguageSolution]) -> List[LanguageSolution]:
    # The order is: `py`, `java`, `cpp`, then the rest
    main_languages = ["py", "java", "cpp"]

    main_solutions = [
        solution for solution in solutions if solution.kind in main_languages
    ]
    main_solutions.sort(key=lambda solution: main_languages.index(solution.kind))

    other_solutions = [
        solution for solution in solutions if solution.kind not in main_languages
    ]
    other_solutions.sort(key=lambda solution: solution.kind)

    return main_solutions + other_solutions


def read_problems(problems_folder: str) -> List[Problem]:
    problems = []
    folders = sorted(os.listdir(problems_folder))
    for folder_name in folders:
        if folder_name.startswith("_"):
            continue
        problem_path = os.path.join(problems_folder, folder_name)
        if not os.path.isdir(problem_path):
            continue
        problem = read_problem(problem_path)
        problems.append(problem)
    return problems


def process_problem(problem: Problem) -> CheckedProblem:
    samples_length = len(problem.sample_paths)

    paths_joined = problem.sample_paths + problem.secret_paths

    cases = run_all_solutions(problem.language_solutions, paths_joined)

    samples = cases[:samples_length]
    secrets = cases[samples_length:]

    return CheckedProblem(
        foldername=problem.foldername,
        data=problem.data,
        markdown_description=open(problem.description_path).read(),
        language_solutions=problem.language_solutions,
        samples=samples,
        secrets=secrets,
    )


def read_and_process_problems(problems_folder: str) -> List[CheckedProblem]:
    problems = read_problems(problems_folder)
    return Parallel(n_jobs=10)(
        delayed(process_problem)(problem) for problem in problems
    )
