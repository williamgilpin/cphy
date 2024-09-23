

<img src="resources/overview.gif" alt="Overview of Methods in Course" width="100%"/>

*(Left to Right): Avalanche activity cascades in a sandpile automaton; a vortex street formed by flow past a cylinder; and Turing patterns in a reaction-diffusion model. All simulations from the course homeworks; a higher-resolution video may be viewed [here](https://player.vimeo.com/video/739921904?title=0&byline=0&portrait=0)*
<!-- <iframe src="https://player.vimeo.com/video/739921904?title=0&byline=0&portrait=0" width="100%" height="400" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
 -->
<!-- https://user-images.githubusercontent.com/8154246/184846814-5b5c80e1-34f9-4063-9b26-36b2a0369827.mov -->
<!-- <img src="https://user-images.githubusercontent.com/8154246/184846814-5b5c80e1-34f9-4063-9b26-36b2a0369827.mov" alt="Overview of Methods in Course" width="100%"/> -->


# Computational Physics

## Summary

Materials for computational physics course, taught by [William Gilpin](http://www.wgilpin.com/?utm_source=en_us_bhg226180pc).

This course aims to provide a very broad survey of computational methods that are particularly relevant to modern physics research. We will aim to cover efficient algorithm design and performance analysis, traditional numerical recipes such as integration and matrix manipulation, and emerging methods in data analysis and machine learning. Our goal by the end of the class will be to feel comfortable approaching diverse, open-ended computational problems that arise during research, and to be ready to design and share new algorithms with the broader research community.

The class website is located [here](https://www.wgilpin.com/cphy/?utm_source=en_us_bh224180tg). 
+ If you are enrolled in 329 at UT, the syllabus and calendar are [here](https://docs.google.com/document/d/1c3_XWOZAYTVmQGKoqcifzEXX7VwzWmhIRT4zVcy9lFU/edit?usp=sharing). 
+ If you are enrolled in 381C at UT, the syllabus and calendar are [here](https://docs.google.com/document/d/1URJmdpTVG8E2bLLu5xAHctICb6krbZ0fC0hO2i2xEXY/edit?usp=sharing). 
+ For both UT courses, the Discussions page may be found [here](https://edstem.org/us/courses/59769).

## Contents

Many links below direct to Google Colab, and can be run-in-browser without installation as long as you are signed into a Google account. To download the raw source files, please refer to [the GitHub repository](https://github.com/williamgilpin/cphy/tree/main). Some lecture videos are linked below, and the remaining lecture videos are linked in the Syllabus (above).

#### Homework Assignments {#hw}
+ [HW1: The sandpile cellular automaton and directed percolation](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/hw/cellular_automata_complexity.ipynb). [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/hw/cellular_automata_complexity.ipynb) *Covers recursion, runtime scaling, vectorization*
+ [HW2: Linear dynamical systems and decomposing a chaotic flow](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/hw/matrices_unsupervised_learning.ipynb). [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/hw/matrices_unsupervised_learning.ipynb) *Covers numerical linear algebra, optimization, and unsupervised learning*
+ [HW3: Turing patterns and phase separation](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/hw/pde_turing.ipynb). [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/hw/pde_turing.ipynb) *Covers numerical integration; finite-differences and spectral methods*
+ [HW4: Predicting turbulence with operator methods](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/hw/forecasting_regression_supervised.ipynb). [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/hw/forecasting_regression_supervised.ipynb) *Covers Supervised learning, time series forecasting, ridge, kernel, and logistic regression*
<!-- + [Homework solutions](https://github.com/williamgilpin/cphy/blob/main/hw/solutions/) -->

#### Lecture Slides {#lectures}
+ [Lecture 1: Python syntax for Scientific Computing](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/python_intro.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/python_intro.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/python_intro.ipynb)

+ [Lecture 2: Object-oriented programming to find first-passage times of Brownian motion](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/first_passage_and_inheritance.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/first_passage_and_inheritance.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/first_passage_and_inheritance.ipynb)
<!-- [[vid1]](https://youtu.be/N8PJH9WxvUk)
[[vid2]](https://youtu.be/R1fDglciddo) -->

+ [Lecture 3: Vectorization, arrays, and the Mandelbrot set](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/vectorization_mandelbrot.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/vectorization_mandelbrot.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/vectorization_mandelbrot.ipynb)
<!-- [[video]](https://youtu.be/PqntSbG4IuM) -->

+ [Lecture 4: Runtime complexity, convolutions, and the continuous Game of Life](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/inheritance_game_of_life.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/inheritance_game_of_life.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/inheritance_game_of_life.ipynb)
<!-- [[video]](https://youtu.be/Pgycaa_D8h4?t=434) -->

+ [Lecture 5: Finding the Feigenbaum constant with recursion and dynamic programming](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/time_and_space_complexity_recursion.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/time_and_space_complexity_recursion.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/time_and_space_complexity_recursion.ipynb)

+ [Lecture 6: Detecting the onset of turbulence with the Fast Fourier Transform](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/fast_fourier.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/fast_fourier.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/fast_fourier.ipynb)
<!-- [[video]](https://www.youtube.com/watch?v=AUMu5xL2rjY) -->

+ [Lecture 7: Condition Number and the irreversibility of chaos](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/numerical_linear_algebra_preconditioning.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/numerical_linear_algebra_preconditioning.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/numerical_linear_algebra_preconditioning.ipynb)
<!-- [[video]](https://youtu.be/9ZqXsIzBlCg) -->

+ [Lecture 8: Random walks on complex graphs](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/intro_graph_adjacency.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/intro_graph_adjacency.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/intro_graph_adjacency.ipynb)

+ [Lecture 9: Probing social networks with PageRank](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/lu_decomposition.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/lu_decomposition.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/lu_decomposition.ipynb)

+ [Lecture 10: Spectral graph theory and the QR eigenvalue algorithm](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/qr_eigenvalues.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/qr_eigenvalues.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/qr_eigenvalues.ipynb)
 <!-- [[vid]](https://youtu.be/jiS4D5pvwy0) -->

+ [Lecture 11: Singular Value Decomposition](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/svd_decomp.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/svd_decomp.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/svd_decomp.ipynb)
<!-- [[video]](https://youtu.be/6w-_26aogH4?t=366) -->

+ [Lecture 12: Krylov subspace methods & Conjugate gradient methods](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/krylov_methods.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/krylov_methods.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/krylov_methods.ipynb)

+ [Lecture 13: Optimization in low dimensions](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/convex_optimization_univariate.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/convex_optimization_univariate.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/convex_optimization_univariate.ipynb)

+ [Lecture 14: Lagrangian Duality](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/lagrangian_duality.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/lagrangian_duality.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/lagrangian_duality.ipynb)

+ [Lecture 15: Multivariate Optimization and Potential Flows](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/optimization_multivariate.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/optimization_multivariate.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/optimization_multivariate.ipynb)
 <!-- [[video]](https://youtu.be/ADkCO1sED0w) -->

+ [Lecture 16: Evolving Cellular Automata with Genetic Algorithms](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/evolving_cellular_automata.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/evolving_cellular_automata.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/evolving_cellular_automata.ipynb)

+ [Lecture 17: Monte Carlo methods and Hard Sphere Packing](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/monte_carlo_metropolis.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/monte_carlo_metropolis.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/monte_carlo_metropolis.ipynb)

+ [Lecture 18: Numerical Integration and predicting chaos](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/lorenz_odeint.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/lorenz_odeint.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/lorenz_odeint.ipynb)
<!-- [[Raw Notebook]](https://github.com/williamgilpin/cphy/blob/main/talks/lorenz_odeint.ipynb) -->

+ [Lecture 19: Variable step integration, symplectic and stochastic systems](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/integrator_chaos_variable_step.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/integrator_chaos_variable_step.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/integrator_chaos_variable_step.ipynb)
 <!-- [[video]](https://youtu.be/q754u2a7uCA) -->

+ [Lecture 20: A pragmatist's guide to numerical integration](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/pragmatic_integration.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/pragmatic_integration.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/pragmatic_integration.ipynb)
<!-- [[video]](https://www.youtube.com/watch?v=hUgcgO1ZJMQ) -->

+ [Lecture 21: Diffusion, relaxation, and instability](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/laplace_equation.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/laplace_equation.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/laplace_equation.ipynb)

+ [Lecture 22: Shocks, solitons, and hyperbolic partial differential equations](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/hyperbolic_pde.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/hyperbolic_pde.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/hyperbolic_pde.ipynb)
<!-- [[video]](https://youtu.be/lqyKeuCsHDU) -->

+ [Lecture 23: Spectral solving using the Dedalus Python Package](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/dedalus.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/dedalus.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/dedalus.ipynb)
<!-- [[vid]](https://www.youtube.com/watch?v=9Biw4oVs-sA) -->

+ [Lecture 24: Supervised Learning & The Ising Model](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/supervised_learning_ising.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/supervised_learning_ising.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/supervised_learning_ising.ipynb)
<!-- [[vid]](https://www.youtube.com/watch?v=DEAaoJpl6-Y) -->

+ [Lecture 25: Classification, Logistic Regression, and phases of matter](https://github.com/williamgilpin/cphy/blob/main/talks/logistic_regression_phases.ipynb)

+ [Lecture 26: Overfitting, bias-variance tradeoff, and double-descent](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/overfitting_bias_variance_free_lunch.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/overfitting_bias_variance_free_lunch.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/overfitting_bias_variance_free_lunch.ipynb)

+ [Lecture 27: Unsupervised learning, embedding, clustering](https://github.com/williamgilpin/cphy/blob/main/talks/unsupervised_clustering_embedding.ipynb)

+ [Lecture 28: Time series representation, featurizing chaos, kernel methods](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/time_series_chaos_clustering.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/time_series_chaos_clustering.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/time_series_chaos_clustering.ipynb)

+ [Lecture 29: Gaussian mixtures, expectation-maximization, and superresolution microscopy](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/gmm_mle_em.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/gmm_mle_em.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/gmm_mle_em.ipynb)

+ [Lecture 30: Predicting the Reynolds number of turbulence with deep learning](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/neural_networks_overview.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/neural_networks_overview.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/neural_networks_overview.ipynb)
 <!-- [[video]](https://youtu.be/wvxnVAuVB0E) -->

+ [Lecture 31: Types of neural networks; symmetries in physical systems](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/neural_networks_types.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/neural_networks_types.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/neural_networks_types.ipynb)

+ [Lecture 32: Training neural networks with backpropagation](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/neural_networks_training.ipynb)
<br>[[html]](https://www.wgilpin.com/cphy/talks/html_static/neural_networks_training.html) [[ipynb]](https://github.com/williamgilpin/cphy/blob/main/talks/neural_networks_training.ipynb)

#### Notes

+ [How to use the high-performance computing cluster](https://github.com/williamgilpin/howto/blob/master/using_tacc.md)
+ [Matrix Derivatives notes](https://github.com/williamgilpin/cphy/blob/main/talks/matrix_derivative.ipynb)
+ [Hopfield Networks and Spin Glasses](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/vignettes/hopfield_model.ipynb)
[[ipynb]](https://github.com/williamgilpin/cphy/blob/main/vignettes/hopfield_model.ipynb)
+ [Variational Autoencoders](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/vignettes/basic_vae.ipynb)
[[ipynb]](https://github.com/williamgilpin/cphy/blob/main/vignettes/basic_vae.ipynb)
+ [Vector-Quantized Variational Autoencoders (VQ-VAE)](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/vignettes/vq_vae.ipynb)
[[ipynb]](https://github.com/williamgilpin/cphy/blob/main/vignettes/vq_vae.ipynb)


#### Laboratory Exercises
+ [Lab 1: Getting started with Python](labs/getting_started_with_python.md)
+ [Lab 2: git, GitHub, and GitHub Pages](http://www.wgilpin.com/howto/howto_github.html)
+ [Lab 3: Documentation and Formatting](labs/documentation_and_formatting.md)
+ [Lab 4: Automatically creating online documentation with Sphinx](http://www.wgilpin.com/howto/howto_sphinx.html)
+ [Lab 5: Unit Testing](http://www.wgilpin.com/howto/python_unit_testing.html)
+ [Lab 6: Structuring an Open-Source Repository](http://www.wgilpin.com/howto/python_project.html)

## Example Final Projects

+ [Quantum Reinforcement Learning with the Grover method](https://github.com/jiangzz-lab/GroverQLearning)
+ [Modelling the contractile dynamics of muscle](https://github.com/jakemcgrath1999/muscle_model)
+ [Tight binding and Anderson localization on complex graphs](https://github.com/ravikoka/qgraph)
+ [Neural System Identification by Training Recurrent Neural Networks](https://github.com/liuyuezhang/nsi)
+ [Assimilating a realistic neuron model onto a reduced-order model](https://github.com/sepstein22/computational_brain)
+ [Testing particle phenomenology beyond the Standard Model with Bayesian classification](https://github.com/ramreddy-physics/Madgraph_Search)
+ [Monte Carlo sampling for many-body systems](https://github.com/Potatoasad/Computational-Physics-Final-Project)


## Usage and improvements

If you are teaching a similar course, please feel free to use any or all of these materials. If you have any suggestions for improvements or find any errors, I would very much appreciate any feedback. Consider submitting corrections as issues or pull requests on [GitHub](https://github.com/williamgilpin/cphy/).

For students, logistics and project questions are best posted on the classroom forum (Ed Discussions); errors in the materials should be issues on [the course repository](https://github.com/williamgilpin/cphy/); for other issues, I can be reached via [email](mailto:wgilpin@[saxetu%20spelled%20backwards].edu)


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

## Attributions

Portions of the material in this course are adapted or inspired by other open-source classes, including: [Pankaj Mehta's Machine Learning for Physics Course](https://github.com/drckf/mlreview_notebooks), [Chris Rycroft's Numerical Recipe's Course](https://people.math.wisc.edu/~chr/am205/fall19/), [Volodymyr Kuleshov's Applied Machine Learning course](https://github.com/kuleshov/cornell-cs5785-2022-applied-ml), [Fei-Fei Li's Deep Learning for Computer Vision course](http://cs231n.stanford.edu/), [Lorena Barba's CFD course](https://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/) and [Jim Crutchfield's Nonlinear Dynamics course](http://csc.ucdavis.edu/~chaos/courses/nlp/)

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-37RSFCXBQY"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-37RSFCXBQY');
</script>



