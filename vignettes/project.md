# Computational Physics Course Projects

Find a problem that you are excited to spend time implementing and releasing, and which is suitably general that others in the open source community could find your GitHub code or method useful. 

There are a few heuristics that you might use to identify a good problem:
+ Start with a problem we saw in the course (e.g. an implementation of a single algorithm like a spectral PDE solver) and then branch out into related extensions (e.g. generalize the solver to different coordinate systems or geometries).
+ Look for creative but underappreciated older methods papers in your field, especially where the author’s code is unavailable, where the implementation is in a very different language like FORTRAN or Perl, or where the provided code is poorly documented. A clean, easy-to-use implementation of an uncommon method often proves very valuable.
+ Find a very common task or method in your field (e.g., stacking microscopy images, or synchronizing experimental recordings), and use tricks from vectorization, dynamic programming or linear algebra to speed up the task.


#### A few common pitfalls to avoid

+ Don't pick a problem that is so hard or open-ended that it delays getting started writing code. Your goal should be to get started writing code as soon as possible, since it's the emphasis of the project.
+ Please don't copy or very lightly modify code that is primarily taken from a blog post, a GitHub repo you found, or an LLM. Remember that the project will be public on GitHub and thus searchable on Google.
+ Don't use ML unless you are either experienced with it, or are willing to read ahead and make sure you are on top of the best statistical practices. If you want to use a deep learning model, is it really appropriate for your dataset scale? Can you fairly separate test and training data? 


#### Project Learning Goals

Beyond providing a setting to try out some of the ideas we are learning in this class, I am hoping that this project will have residual value to you after the course is over. Having prior experience with open-source development and visible existing code examples may prove useful to you in your graduate research, and potentially on the academic and industry job market. By posting the code publicly on GitHub, your code will help others in the future who are trying to solve similar problems.

#### Parameters
+ I would prefer groups of 4 people, for a total of 8 projects per course
+ You’re allowed (and encouraged) to work on something relevant to your research group's work, but please make the GitHub repo self-contained. You should plan to write substantial new code to be written for this project (although re-factoring a “rough” implementation is okay), so please use your best judgment to ensure that you get the most value out of this project.
+ If there is a method you’d like to add to a large, existing package that is widely used in your field (e.g. Biopython, Astropy, scikit-learn, sktime) check with me about submitting a well-structured PR to the main repo instead of implementing a standalone package. Please check with the repo maintainers that your feature would be welcome, and about the format and testing in order to get accepted. Generally, the larger the repo’s userbase, the smaller the addition should be, and the more testing it will need to pass—however, the potential impact could be huge. 


#### Grading Rubric
+ Problem scope: 20% 
+ + Contains an interesting and challenging problem, and makes a good-faith effort to approach it.
+ + Creativity: An unexpected application or novel algorithm or interpretation of an algorithm is exciting and appreciated.
+ + Thoroughness: Makes a thorough attempt to solve the problem, even if ultimately unsuccessful
Code quality: 40%
+ + Logical structure, minimal redundancy
+ + Variables and objects have appropriate scope
+ + Use of appropriate abstractions
+ + Code legibility
+ + Unit tests
Documentation: 20%
+ + README contains Installation instructions
+ + README contains example usage and minimum working example
+ + I’m not requiring a written report this term, and so if you have benchmarks or results, please put them in a section of your repo’s README.md file. Please use best practices for publication-quality writing and figure-making.
+ + Major functions and classes have clear docstrings
+ + Documentation exists for major functions and API
Talk: 20%
+ + Only one group member needs to present, though you are welcome to structure this however you’d like.
+ + These will be ~10 minutes + 2 min questions during the last few sessions of the course (5 talks per class).
+ + Please be ready to present the class session before you are scheduled, just in case someone can’t come on their scheduled presentation day.
+ + You can organize these however you want, but if you would prefer a template: 5-8 minutes background, 3 minutes on problem formulation, 5 minutes on your solution and any pitfalls or dead ends, and remaining time on future directions, applications, connections to interesting other ideas.

#### Project Ideas
You can pick anything that interests you and which involves writing new code, here are just some ideas
+ Implement the [orthogonality-constrained optimizer of Edelman et al.](https://arxiv.org/abs/physics/9806030)
+ Implement a finite-element solver for PDEs in 2D, and compare and contrast with the finite-difference method
+ Recreate the key results of Kauffman’s [random Boolean circuits paper](https://www.sciencedirect.com/science/article/abs/pii/0022519369900150)
+ Recreate the key results of [Lenski et al.'s digital organisms paper](https://www.nature.com/articles/23245)

## Project resources
+ [Pineau Lab machine learning reproducibility checklist](https://github.com/paperswithcode/releasing-research-code)
+ It’s not necessary to include everything in this guide, but it’s a great guide to what the research community thinks good, reusable code should look like.

#### Example code repositories
+ [Quantum Reinforcement Learning with the Grover method](https://github.com/jiangzz-lab/GroverQLearning)
+ [Modelling the contractile dynamics of muscle](https://github.com/jakemcgrath1999/muscle_model)
+ [Tight binding and Anderson localization on complex graphs](https://github.com/ravikoka/qgraph)
+ [Neural System Identification by Training Recurrent Neural Networks](https://github.com/liuyuezhang/nsi)
+ [Assimilating a realistic neuron model onto a reduced-order model](https://github.com/sepstein22/computational_brain)
+ [Testing particle phenomenology beyond the Standard Model with Bayesian classification](https://github.com/ramreddy-physics/Madgraph_Search)
+ [Monte Carlo sampling for many-body systems](https://github.com/Potatoasad/Computational-Physics-Final-Project)
+ [William’s dynamical systems repo from NeurIPS 2021](https://github.com/williamgilpin/dysts)
+ [tsfresh time series featurization library](https://github.com/blue-yonder/tsfresh)
+ [darts forecasting library](https://github.com/unit8co/darts)
+ [JAX](https://github.com/google/jax)
+ An [example pull request](https://github.com/scikit-learn/scikit-learn/issues/2688) to the widely-used sklearn machine learning package, which implements varimax PCA: 


Example class projects from other courses:
+ [Final Projects for Stanford CS229: Machine Learning](https://cs229.stanford.edu/proj2021spr/)
+ [Final Projects for Stanford CS231n: Convolutional Neural Networks](http://cs231n.stanford.edu/2017/reports.html)
+ [Final Projects for UC Davis's Nonlinear Physics course](http://csc.ucdavis.edu/~chaos/courses/nlp/Projects2009/Projects2009.html)
