from setuptools import find_packages,setup
from typing import List

def get_require(file_path:str)->list[str]:
    Hypen_e_dot="-e ."
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements


setup(
    name= 'Bunny-ml-project-2',
    version='0.1.0', 
    packages=find_packages(),
    install_requires=get_require('requirements.txt')
)