from typing import List
import os

from problems import CheckedProblem, ProblemTestCase


def build_problem_archives(problems: List[CheckedProblem]):
    # Delete folder ./build/problems if exists
    if os.path.exists("./build/problems"):
        os.system("rm -rf ./build/problems")

    # Delete folder ./build/problem_zips if exists
    if os.path.exists("./build/problem_zips"):
        os.system("rm -rf ./build/problem_zips")

    os.makedirs("./build/problems", exist_ok=True)
    os.makedirs("./build/problem_zips", exist_ok=True)

    for problem in problems:
        folder = f"./build/problems/{problem.foldername}"
        os.makedirs(folder, exist_ok=True)

        # Write domjudge-problem.ini
        with open(f"{folder}/domjudge-problem.ini", "w") as f:
            f.write(
                f"""
name = {problem.data.name}
timelimit = {problem.data.timelimit}
"""
            )

        def write_test_cases(path: str, cases: List[ProblemTestCase]):
            # Make path directory
            os.makedirs(path, exist_ok=True)

            # Write test cases
            for i, case in enumerate(cases):
                with open(f"{path}/{i}.in", "w") as f:
                    f.write(case.input)
                with open(f"{path}/{i}.ans", "w") as f:
                    f.write(case.output)

        # Write samples
        write_test_cases(f"{folder}/data/samples", problem.samples)

        # Write secrets
        write_test_cases(f"{folder}/data/secrets", problem.secrets)

        # Zip the contents of the folder and move it to ./build/problem_zips
        os.system(
            f"cd ./build/problems/{problem.foldername} && find . -type f | zip -@ ../../problem_zips/{problem.foldername}.zip > /dev/null"
        )


def build_docs(problems: List[CheckedProblem]):
    # Delete folder ./build/docs if exists
    if os.path.exists("./build/docs"):
        os.system("rm -rf ./build/docs")

    os.makedirs("./build/docs", exist_ok=True)

    # Copy all files from ./docs into ./build/docs
    os.system("cp -r ./docs/* ./build/docs")

    # Build sidebar
    sidebar = """
- Main

  - [Welcome!](README.md)

- Problems

"""

    for problem in problems:
        problem_name = f"{problem.foldername}.md"
        problem_scaffolds = f"{problem.foldername}-scaffolds.md"

        sidebar += f"  - {problem.data.name}\n"
        sidebar += f"    - [Problem]({problem_name})\n"
        sidebar += f"    - [Scaffolds]({problem_scaffolds})\n"

        # Write problem markdown
        with open(f"./build/docs/{problem_name}", "w") as f:
            desc = problem.markdown_description
            desc += "\n\n"

            desc += "## Samples\n\n"
            desc += "Here are some samples of input and output:\n\n"

            for sample in problem.samples:
                desc += f"### {sample.name}\n\n"
                desc += "#### Input\n\n"
                desc += f"```\n{sample.input}\n```\n\n"
                desc += "#### Output\n\n"
                desc += f"```\n{sample.output}\n```\n\n"

            f.write(desc)

        # Write scaffolds markdown
        with open(f"./build/docs/{problem_scaffolds}", "w") as f:
            scaffolds = ""

            for solution in problem.language_solutions:
                if solution.scaffold_path is not None:
                    lang_name = get_language_name(solution.kind)
                    scaffolds += f"### {lang_name}\n\n"
                    # Read the solution file
                    with open(solution.scaffold_path, "r") as f2:
                        scaffolds += f"```{solution.kind}\n{f2.read()}\n```\n\n"

            f.write(scaffolds)

    with open("./build/docs/_sidebar.md", "w") as f:
        f.write(sidebar)


def get_language_name(kind: str):
    match kind:
        case "py":
            return "Python"
        case "cpp":
            return "C++"
        case "java":
            return "Java"
        case "c":
            return "C"
