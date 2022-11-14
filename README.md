

<img src="resources/overview.gif" alt="Overview of Methods in Course" width="100%"/>

*(Left to Right): Avalanche activity cascades in a sandpile automaton; a vortex street formed by flow past a cylinder; and Turing patterns in a reaction-diffusion model. All simulations from the course homeworks; a higher-resolution video may be viewed [here](https://player.vimeo.com/video/739921904?title=0&byline=0&portrait=0)*
<!-- <iframe src="https://player.vimeo.com/video/739921904?title=0&byline=0&portrait=0" width="100%" height="400" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
 -->
<!-- https://user-images.githubusercontent.com/8154246/184846814-5b5c80e1-34f9-4063-9b26-36b2a0369827.mov -->
<!-- <img src="https://user-images.githubusercontent.com/8154246/184846814-5b5c80e1-34f9-4063-9b26-36b2a0369827.mov" alt="Overview of Methods in Course" width="100%"/> -->


# Computational Physics

## Summary

Materials for UT Austin's graduate computational physics course, taught by [William Gilpin](http://www.wgilpin.com/?utm_source=en_us_bhg226180pc).

This course aims to provide a very broad survey of computational methods that are particularly relevant to modern physics research. We will aim to cover efficient algorithm design and performance analysis, traditional numerical recipes such as integration and matrix manipulation, and emerging methods in data analysis and machine learning. Our goal by the end of the class will be to feel comfortable approaching diverse, open-ended computational problems that arise during research, and to be ready to design and share new algorithms with the broader research community.

The class website is located [here](https://www.wgilpin.com/cphy/?utm_source=en_us_bh224180tg). If you are enrolled in the course at UT, the syllabus and calendar are [here](https://docs.google.com/document/d/1URJmdpTVG8E2bLLu5xAHctICb6krbZ0fC0hO2i2xEXY/edit?usp=sharing)

## Contents


#### Homework Assignments
+ [HW1: The sandpile cellular automaton and directed percolation](https://github.com/williamgilpin/cphy/blob/main/hw/cellular_automata_complexity.ipynb). *Covers recursion, runtime scaling, vectorization*
+ [HW2: Linear dynamical systems and decomposing a chaotic flow](https://github.com/williamgilpin/cphy/blob/main/hw/matrices_unsupervised_learning.ipynb). *Covers numerical linear algebra, optimization, and unsupervised learning*
+ [HW3: Turing patterns and phase separation](https://github.com/williamgilpin/cphy/blob/main/hw/pde_turing.ipynb). *Covers numerical integration; finite-difference and spectral methods*
+ [HW4: Predicting turbulence with operator methods](https://github.com/williamgilpin/cphy/blob/main/hw/forecasting_regression_supervised.ipynb). *Covers Supervised learning, time series forecasting, ridge, kernel, and logistic regression*
+ [Homework solutions](https://github.com/williamgilpin/cphy/blob/main/hw/solutions/)

#### Lecture Slides and Notes
+ [Lecture 1: Python for Scientific Computing, Vectorization, and the Mandelbrot set](https://github.com/williamgilpin/cphy/blob/main/talks/python_intro.ipynb)
+ [Lecture 2: Inheritance, Object-Oriented Programming, and the Game of Life](https://github.com/williamgilpin/cphy/blob/main/talks/inheritance_game_of_life.ipynb)
+ [Lecture 3: Time & Space complexity, recursion, and solving a labyrinth](https://github.com/williamgilpin/cphy/blob/main/talks/time_and_space_complexity_recursion.ipynb)
+ [Lecture 4: Recursion and the Fast Fourier Transform](https://github.com/williamgilpin/cphy/blob/main/talks/fast_fourier.ipynb)
+ [Lecture 5: Numerical Linear Algebra, Condition Number, Preconditioning](https://github.com/williamgilpin/cphy/blob/main/talks/numerical_linear_algebra_preconditioning.ipynb)
+ [Lecture 6 : Matrix inversion and LU factorization](https://github.com/williamgilpin/cphy/blob/main/talks/lu_decomposition.ipynb)
+ [Lecture 7: The QR algorithm for eigenvalues](https://github.com/williamgilpin/cphy/blob/main/talks/qr_eigenvalues.ipynb)
+ [Lecture 8: Singular Value Decomposition](https://github.com/williamgilpin/cphy/blob/main/talks/svd_decomp.ipynb)
+ [Lecture 9: Krylov subspace methods & Conjugate gradient methods](https://github.com/williamgilpin/cphy/blob/main/talks/krylov_methods.ipynb)
+ [Lecture 10: Optimization in low dimensions](https://github.com/williamgilpin/cphy/blob/main/talks/convex_optimization_univariate.ipynb)
+ [Lecture 11: Multivariate Optimization and Potential Flows](https://github.com/williamgilpin/cphy/blob/main/talks/optimization_multivariate.ipynb)
+ [Lecture 12: Numerical Integration and predicting chaos](https://github.com/williamgilpin/cphy/blob/main/talks/lorenz_odeint.ipynb)
+ [Lecture 13: Variable step integration, symplectic and stochastic systems](https://github.com/williamgilpin/cphy/blob/main/talks/integrator_chaos_variable_step.ipynb)
+ [Lecture 14: A pragmatist's guide to numerical integration](https://github.com/williamgilpin/cphy/blob/main/talks/pragmatic_integration.ipynb)
+ [Lecture 15: Boundary value problems and electrodynamics](https://github.com/williamgilpin/cphy/blob/main/talks/laplace_equation.ipynb)
+ [Lecture 16: Shocks, solitons, and hyperbolic partial differential equations](https://github.com/williamgilpin/cphy/blob/main/talks/hyperbolic_pde.ipynb)
+ [Lecture 17: Spectral methods using the Dedalus Python Package](https://github.com/williamgilpin/cphy/blob/main/talks/dedalus.ipynb)
+ [Lecture 18: Supervised Learning & The Ising Model](https://github.com/williamgilpin/cphy/blob/main/talks/supervised_learning_ising.ipynb)
+ [Lecture 19: Classification, Logistic Regression, and phases of matter](https://github.com/williamgilpin/cphy/blob/main/talks/logistic_regression_phases.ipynb)
+ [Lecture 20: Overfitting, bias-variance tradeoff, and double-descent](https://github.com/williamgilpin/cphy/blob/main/talks/overfitting_bias_variance_free_lunch.ipynb)
+ [Lecture 21: Unsupervised learning, embedding, clustering](https://github.com/williamgilpin/cphy/blob/main/talks/unsupervised_clustering_embedding.ipynb)
+ [Lecture 22: Time series representation, featurizing chaos, kernel methods](https://github.com/williamgilpin/cphy/blob/main/talks/time_series_chaos_clustering.ipynb)
+ [Lecture 23: Gaussian mixtures, expectation-maximization, and superresolution microscopy](https://github.com/williamgilpin/cphy/blob/main/talks/gmm_mle_em.ipynb)
+ [Lecture 24: Introduction to deep learning, predicting the Reynolds number of turbulence](https://github.com/williamgilpin/cphy/blob/main/talks/neural_networks_overview.ipynb)
+ [Lecture 25: Types of neural networks; symmetries in physical systems:](https://github.com/williamgilpin/cphy/blob/main/talks/neural_network_types.ipynb)
+ [Lecture 26: Training neural networks with backpropagation:](https://github.com/williamgilpin/cphy/blob/main/talks/neural_networks_training.ipynb)
+ [Lecture 27: Using convolutional neural networks to predict the phases of the Ising Model](https://github.com/williamgilpin/cphy/blob/main/talks/convolutional_neural_networks_pytorch.ipynb)


#### Laboratory Exercises
+ [Lab 1: Getting started with Python](labs/getting_started_with_python.md)
+ [Lab 2: git, GitHub, and GitHub Pages](labs/git_and_github.md)
+ [Lab 3: Documentation and Formatting](labs/documentation_and_formatting.md)
+ [Lab 4: Automatically creating online documentation with Sphinx](http://www.wgilpin.com/howto/howto_sphinx.html)
+ [Lab 5: Unit Testing](http://www.wgilpin.com/howto/python_unit_testing.html)
+ [Lab 6: Structuring an Open-Source Repository](http://www.wgilpin.com/howto/python_project.html)


#### Additional Notes
+ [Notes on using TACC](https://github.com/williamgilpin/howto/blob/master/using_tacc.md)

<!-- + [`lab1`](https://github.com/williamgilpin/cphy/blob/main//lab2/lab1.ipynb)x -->


## Fixes, typos, and improvements

If you find any errors or typos, please open an issue or submit a correction as a pull request on [GitHub](https://github.com/williamgilpin/cphy/).

Please let us know if you find these materials helpful, so that we can keep track of the course's impact, which could potentially help us expand this course's offering in future years.

Course-related questions are best posted on GitHub as [Discussions](https://github.com/williamgilpin/cphy/discussions) or Issues on [the course repository](https://github.com/williamgilpin/cphy/); for other issues, I be reached via [email](mailto:wgilpin@[saxetu%20spelled%20backwards].edu)


## Attributions

Portions of the material in this course are adapted or inspired by other open-source classes, including: [Pankaj Mehta's Machine Learning for Physics Course](https://github.com/drckf/mlreview_notebooks), [Chris Rycroft's Numerical Recipe's Course](https://people.math.wisc.edu/~chr/am205/fall19/), [Volodymyr Kuleshov's Applied Machine Learning course](https://github.com/kuleshov/cornell-cs5785-2022-applied-ml), [Fei-Fei Li's Deep Learning for Computer Vision course](http://cs231n.stanford.edu/), [Lorena Barba's CFD course](https://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/) and [Jim Crutchfield's Nonlinear Dynamics course](http://csc.ucdavis.edu/~chaos/courses/nlp/)


## Requirements

We will primarily use Python 3 with the following packages

+ numpy
+ matplotlib
+ scipy
+ scikit-learn
+ jupyter

For projects and other parts of the class, you might also need

+ ipykernel
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



