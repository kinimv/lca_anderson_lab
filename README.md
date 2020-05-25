# Summary

This is a program that shows you the least common ancestors given names of two organisms. It also displays the path that the two organisms take to reach the common ancestor

# Installation

This programs requires Python and the pandas data analysis library. the docs to these can be found here:
https://docs.python.org/3/
https://pandas.pydata.org/docs/

If these are not present, the recommended way to use Python and pandas is through Anaconda. More information about Anaconda, its features and how to install it:
https://docs.conda.io/projects/conda/en/latest/user-guide/install/

To install Python, open either Anaconda or your terminal of choice and enter:
conda install python
or
pip install python

To install the pandas library, open either Anaconda or your terminal of choice and enter:
conda install pandas
or
pip install pandas

# Database
This repo contains files names names.txt and nodes.txt which is acquired from this link:
https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz

The National Center for Biotechnology Information (NCBI) creates and maintains this database, more information for which can be found here:
https://www.ncbi.nlm.nih.gov/taxonomy

# Description
The programs prompts you to enter the names of two organisms you want to find the common ancestor of, and then searches the NCBI database for the taxonomy id and its parent's taxonomy id

It then builds a tree of the ancestors of the given compounds up to the common ancestor

# Files
1. LCA.ipynb: a Jupyter notebook file for interpretive running of the program
2. LCA.py: a Python program that can be run locally as long as the other files are present in the same folder of your computer
3. names.dmp: file containing the names in the taxonomy database from the NCBI website
4. nodes.dmp: file containing the nodes in the taxonomy database from the NCBI website
5. README.md: this readme file
6. Sample with H1N1 and MERS.pdf: a PDF example of the program running and its output