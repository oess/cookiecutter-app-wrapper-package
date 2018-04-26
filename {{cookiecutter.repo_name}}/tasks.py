"""
Copyright (C) 2018 OpenEye Scientific Software, Inc.
"""
import os
import sys
import shutil
from json import loads, dump
from invoke import task, run
from setuptools import convert_path


@task
def flake8(ctx):
    run("flake8 --max-line-length 100 {{cookiecutter.module_name}}")

@task
def update_manifest(ctx):
    """
    Updates manifest.json with the correct version of {{cookiecutter.repo_name}}
    """
    spec = loads(open('manifest.json', 'r').read())
    sys.path.append(os.path.dirname(__file__))
    import {{cookiecutter.module_name}}
    spec['version'] = {{cookiecutter.module_name}}.__version__
    dump(spec, open('manifest.json', 'w'))



@task
def package(ctx):
    """
    Create package
    """

    # Get the requirements and version of the package
    requirements = loads(run("python setup.py --requires", hide='both').stdout.strip("\n\r"))

    # Create the Orion packaging files
    reqs_filename = convert_path("./orion-requirements.txt")
    def clean_orion_package_files():
        if os.path.isfile(reqs_filename):
            os.remove(reqs_filename)
    clean_orion_package_files()
    with open(reqs_filename, "w") as reqs_file:
        for req in requirements:
            reqs_file.write(req)
            reqs_file.write("\n")

    update_manifest(ctx)
    # Run standard python packaging, which will include the Orion packaging files we just created
    run("python setup.py sdist --formats=gztar")

    # Removed the Orion packaging files now that we are done with packaging
    clean_orion_package_files()


@task
def docs(ctx):
    curdir = os.getcwd()
    run('cube_doc {{cookiecutter.module_name}} docs/source')
    run('floe_doc {{cookiecutter.module_name}} floes docs/source')
    os.chdir('docs')
    if sys.platform == 'win32':
        run("make.bat html")
    else:
        run("make html")
    os.chdir(curdir)


# need to clean out .pyc files to share a directory
# with both Windows and Bash/WSL
@task
def clean_pyc(ctx):
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".pyc"):
                filename = os.path.join(root, file)
                if os.path.exists(filename):
                    os.unlink(filename)


@task
def clean_docs(ctx):
    doc_dir = "docs/build/html"
    _clean_out_dir(doc_dir)

    if os.path.isdir("docs/build/doctrees"):
        shutil.rmtree("docs/build/doctrees")


@task
def flint(ctx):
    run("floe lint floes/")


@task
def test(ctx):
    """
    run tests
    """
    clean_pyc(ctx)
    os.system("python -m pytest -s --tb=native")


@task
def serve_docs(ctx):
    docs(ctx)
    curdir = os.getcwd()
    os.chdir('docs/build/html')
    run('python -m http.server')
    os.chdir(curdir)


@task
def clean(ctx):
    """
    Clean up doc and package builds
    """
    clean_pyc(ctx)
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("build", ignore_errors=True)
    egg_path = "{}.egg-info".format("{{cookiecutter.repo_name}}".replace("-","_"))
    if os.path.isfile(egg_path):
        os.remove(egg_path)
    elif os.path.isdir(egg_path):
        shutil.rmtree(egg_path)


def _clean_out_dir(dir_path):
    if os.path.isdir(dir_path):
        for the_file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(e)



