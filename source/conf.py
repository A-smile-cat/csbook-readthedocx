# Configuration file for the Sphinx documentation builder.
import os
import sys

project = 'Web 安全学习笔记'
copyright = '2026, ebook'
author = 'ebook'
release = 'latest'

extensions = [
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# —— Read the Docs 经典主题 ——
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# 与原站一致：显示 "Edit on GitHub"（换成你自己的仓库地址即可启用）
html_context = {
    'display_github': True,
    'github_user': 'A-smile-cat',
    'github_repo': 'csbook-readthedocx',
    'github_version': 'main',
    'conf_py_path': '/source/',
}

# 中英混排时的字体与宽度优化
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
}

# PDF 构建用 xelatex（中文必需）
latex_engine = 'xelatex'
latex_elements = {
    'preamble': r'''
\usepackage{ctex}
''',
}

def setup(app):
    pass
