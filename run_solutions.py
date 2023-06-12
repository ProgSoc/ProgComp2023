from typing import List, NamedTuple, Optional
import subprocess
import sys
import os
from tempfile import NamedTemporaryFile, TemporaryDirectory


class LanguageSolution(NamedTuple):
    kind: str
    solution_path: str
    scaffold_path: Optional[str]


class ProblemTestCase(NamedTuple):
    path: str
    name: str
    input: str
    output: str


def run_all_solutions(
    solutions: List[LanguageSolution], input_paths: List[str]
) -> List[ProblemTestCase]:
    # List of solution outputs, child list is each problem for that solution
    outputs: List[List[ProblemTestCase]] = []
    for solution in solutions:
        input_names = [os.path.basename(path) for path in input_paths]
        inputs = [open(path).read() for path in input_paths]

        results = run_languages_solution(solution, inputs)
        results = [
            ProblemTestCase(path=path, name=name, input=input, output=output)
            for path, name, input, output in zip(
                input_paths, input_names, inputs, results
            )
        ]

        outputs.append(results)

    final_outputs: List[ProblemTestCase] = []

    # Iterate over each problem's outputs
    for problem_outputs in zip(*outputs):
        output_strings = [case.output for case in problem_outputs]

        # Check all outputs are the same
        if len(set(output_strings)) != 1:
            # Format the solution path and the solution output for a nice print
            test_case_outputs = [
                f"{case.path}:\n```\n{case.output}\n```" for case in problem_outputs
            ]

            print("\n".join(test_case_outputs))

            raise Exception(f"Outputs are not the same for {solutions}")

        final_outputs.append(problem_outputs[0])

    return final_outputs


def run_languages_solution(solution: LanguageSolution, inputs: List[str]) -> List[str]:
    match solution.kind:
        case "py":
            return run_python_solution(solution.solution_path, inputs)
        case "java":
            return run_java_solution(solution.solution_path, inputs)
        case "cpp":
            return run_cpp_solution(solution.solution_path, inputs)
        case _:
            raise Exception(f"Unknown language {solution.kind}")


def run_python_solution(solution_path: str, inputs: List[str]) -> List[str]:
    with NamedTemporaryFile("w", suffix=".py") as f:
        f.write(open(solution_path).read())
        f.flush()

        def run_single(input: str) -> str:
            return subprocess.check_output(
                [sys.executable, f.name], input=input, encoding="utf-8"
            )

        return [run_single(input) for input in inputs]


def run_java_solution(solution_path: str, inputs: List[str]) -> List[str]:
    with TemporaryDirectory() as temp_dir:
        java_file_path = f"{temp_dir}/solution.java"
        with open(solution_path) as f:
            java_code = f.read()
        with open(java_file_path, "w") as f:
            f.write(java_code)
        subprocess.check_call(["javac", java_file_path])
        class_name = "solution"

        def run_single(input: str) -> str:
            return subprocess.check_output(
                ["java", class_name], input=input, encoding="utf-8", cwd=temp_dir
            )

        return [run_single(input) for input in inputs]


def run_cpp_solution(solution_path: str, inputs: List[str]) -> List[str]:
    with TemporaryDirectory() as temp_dir:
        cpp_file_path = f"{temp_dir}/solution.cpp"
        with open(solution_path) as f:
            cpp_code = f.read()
        with open(cpp_file_path, "w") as f:
            f.write(cpp_code)
        subprocess.check_call(["g++", "-o", f"{temp_dir}/solution", cpp_file_path])

        def run_single(input: str) -> str:
            return subprocess.check_output(
                [f"{temp_dir}/solution"], input=input, encoding="utf-8"
            )

        return [run_single(input) for input in inputs]
