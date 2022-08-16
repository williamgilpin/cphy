# Computational Physics

Materials for UT Austin's graduate computational physics course, taught in Fall 2022 by William Gilpin

![Overview of Methods in Course](resources/overview_video.gif)
<iframe src="https://player.vimeo.com/video/739921904?title=0&byline=0&portrait=0" width="100%" height="400" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

The class website is located [here](https://www.wgilpin.com/cphy/?utm_source=en_us_bh224180tg). If you are enrolled in the course at UT, the syllabus and calendar is [here](https://docs.google.com/document/d/1URJmdpTVG8E2bLLu5xAHctICb6krbZ0fC0hO2i2xEXY/edit?usp=sharing)


# Summary

This course aims to provide a very broad survey of computational methods that are particularly relevant to modern physics research. We will aim to cover efficient algorithm design and performance analysis, traditional numerical recipes such as integration and matrix manipulation, and emerging methods in data analysis and machine learning. Our goal by the end of the class will be to feel comfortable approaching diverse, open-ended computational problems that arise during research, and to be ready to design and share new algorithms with the broader research community.

# Contents

+ [`HW1: The sandpile cellular automaton and directed percolation`](https://github.com/williamgilpin/cphy/blob/main/hw/cellular_automata_complexity.ipynb). *Covers recursion, runtime scaling, vectorization*
+ [`HW2: Linear dynamical systems and decomposing a chaotic flow`](https://github.com/williamgilpin/cphy/blob/main/hw/matrices_unsupervised_learning.ipynb). *Covers numerical linear algebra, optimization, and unsupervised learning*
+ [`HW3: Turing patterns and phase separation.`](https://github.com/williamgilpin/cphy/blob/main/hw/pde_turing.ipynb). *Topics: Numerical integration; finite-difference and spectral methods*
+ [`HW4: Predicting turbulence and finite-time Lyapunov exponents`](https://github.com/williamgilpin/cphy/blob/main/hw/forecasting_regression_supervised.ipynb). *Topics: Supervised learning, kernel and logistic regression*

+ [Homework solutions](hw/solutions/)
+ [`Lab 1: Getting started with Python`](labs/getting_started_with_python.md)

<!-- + [`lab1`](https://github.com/williamgilpin/cphy/blob/main//lab2/lab1.ipynb)x -->


# Fixes, typos, and attribution

If you find any errors or typos, please open an issue or submit a correction as a pull request.

If you use any of these materials for your own class, please submit typos or improvements as Issues or Pull Requests, so that we can improve this version of the course. Please let us know if you find these materials helpful, so that we can keep track of the course's impact, which could  potentially help us continue to offer this course in future years.

I can be reached most easily via Discussions or Issues on this repository; otherwise, I be reached via [email](`mailto:wgilpin@[saxetu spelled backwards].edu`)


# Requirements

We will use Python 3 with the following packages

+ numpy
+ matplotlib
+ scipy
+ scikit-learn
+ jupyter

For your projects and other parts of the class, you might also need

+ scikit-image
+ umap-learn
+ statsmodels
+ pytorch
+ jax
+ numba



<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-37RSFCXBQY"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-37RSFCXBQY');
</script>



