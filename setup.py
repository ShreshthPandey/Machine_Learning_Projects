from setuptools import find_packages, setup
from typing import List

HYPENED_REQUIREMENT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPENED_REQUIREMENT in requirements:
            requirements.remove(HYPENED_REQUIREMENT)
    return requirements





setup(
    name="Malicious_URL_Detection",
    version='0.0.1',
    author='Shreshth <shreshthpandey2103@g',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
)
