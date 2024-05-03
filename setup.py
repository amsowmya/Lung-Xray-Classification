from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
    name = "Xray",
    version="0.0.1",
    description="Projecto for deep learning with Pytorch",
    author="Sowmya AM",
    author_email="sowmya.anekonda@gmail.com",
    include_requires=get_requirements("requirements_dev.txt"),
    packages=find_packages(),
    # requires=
)