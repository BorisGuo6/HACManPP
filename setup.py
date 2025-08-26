from setuptools import setup, find_packages

# Core dependencies
required_packages = [
    'patchelf==0.12',
    'numba==0.57.0',
    'class-resolver==0.3.10',
    'numpy==1.23.0',
    'imageio==2.29.0',
    'matplotlib==3.7.1',
    'hydra-core==1.3.2',
    'open3d',
    'pandas==2.0.1',
    'plotly==5.14.1',
    'scipy==1.10.1',
    'tensorboard==2.13.0',
    'tqdm==4.65.0',
    'transforms3d==0.4.1',
    'wandb==0.15.3',
    'cython==0.29.26',
    'h5py==3.7.0',
    'lxml==4.9.1',
    'opencv-python==4.6.0.66',
    'gym==0.21.0',
    'mani-skill2==0.4.2',
    'mujoco-py',
    'pydrive',
    'numpy-quaternion',
    'torch>=1.11.0',
    'torchvision>=0.12.0',
    'torchaudio>=0.11.0',
    'torch-scatter>=2.0.9',
    'torch-sparse>=0.6.15',
    'torch-geometric>=2.0.4',
    'torch-cluster>=1.6.0'
]

dependency_links = []

setup(
    name='HACMan',
    version='0.1dev',
    packages=find_packages(),
    install_requires=required_packages + ['packaging>=21.0'],
    dependency_links=dependency_links,
    license='MIT License',
    long_description='Learning Hybrid Actor-Critic Maps for 6D Non-Prehensile Manipulation',
)