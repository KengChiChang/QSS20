from subprocess import CalledProcessError, run
import sys
from tempfile import TemporaryDirectory

hws_to_check = [
    (1, "hw1.zip", ["hw1/task4.sh"]),
    (2, "hw2.zip", ["hw2/task2.sh"]),
    (3, "hw3.zip", ["hw3/task2.sh", "hw3/task3.sh"]),
    (4, "homework4.sh", ["homework4.sh"]),
    (5, "homework5.sh", ["homework5.sh"]),
    (6, "hw6.zip", ["hw6/task1.sh", "hw6/task2.sh", "hw6/task3.sh"]),
    (8, "hw8.tar.gz", ["hw8/task1.sh"]),
]

quarter = "Spring 2024"
search_string = f"# CSE 391 - {quarter}"


def generate_submission_file(srcfile, tmp):
    if srcfile.endswith(".tar.gz"):
        run(["tar", "-xzf", srcfile, "-C", tmp], check=True)
    if srcfile.endswith(".zip"):
        run(["unzip", srcfile, "-d", tmp], check=True)


failures = []
with TemporaryDirectory() as tmpdir:
    print(tmpdir)
    for hw, hw_src, submission_files in hws_to_check:
        hw_src_tmp = tmpdir + "/" + hw_src
        run(["cp", f"src/homework/hw{hw}/{hw_src}", hw_src_tmp], check=True)
        generate_submission_file(hw_src_tmp, tmpdir)
        for submission_file in submission_files:
            submission_file_tmp = tmpdir + "/" + submission_file
            try:
                run(["grep", search_string, submission_file_tmp], check=True)
            except CalledProcessError:
                failures.append(
                    f'Could not find "{search_string}" in hw{hw}/{submission_file}'
                )

if len(failures) > 0:
    for failure in failures:
        print(failure, file=sys.stderr)
    sys.exit(1)
