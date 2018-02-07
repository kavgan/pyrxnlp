from setuptools import setup, find_packages


def readme():
    readme_short = """
    PyRXNLP - NLP and Text Mining tools.



    ### Features:
     - Topics extraction
     - Text clustering
     - Opinosis opinion summarization


    """
    return readme_short


setup(
    name="pyrxnlp",
    version="0.1.1",
    packages=find_packages(),
    description='Natural language processing tools',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic'
    ],
    author='RxNLP',
    author_email='kavita.ganesan@rxnlp.com',
    license='LICENSE',
    url='https://github.com/RxNLP/pyrxnlp',
    download_url='https://github.com/RxNLP/pyrxnlp/archive/v0.1.tar.gz',
    keywords=['Sentence Clustering', 'Topics Extraction',
              'Opinosis Summarization', 'Text Similarity'],
    install_requires=[
        'requests==2.9.1'
    ],
    include_package_data=True,
    entry_points={

    }
)