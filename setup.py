from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='ils-nlp',
    version='0.1.0',
    description='A project for extracting and processing text from offering circulars using ML and NLP.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_project_name',  # Replace with your project URL
    author='cbcote',
    author_email='',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'tika',
        'azure-storage-blob',
        'nltk',
        'spacy',
        'pandas',
        'scikit-learn',
        'PyYAML',
        'pytest'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Adjust as necessary
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'ingest-data=scripts.ingest_data:main',
            'extract-text=scripts.extract_text:main',
            'preprocess-text=scripts.preprocess_text:main',
        ],
    },
)
