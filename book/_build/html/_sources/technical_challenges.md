
# Data Usage Agreement
The [PPMI](https://www.ppmi-info.org/) Data Usage Agreement prohibit sharing individual patient data and metadata (including IDs).
We developed the [ppmi_downloader](https://github.com/LivingPark-MRI/ppmi-scraper) Python package to download subject data and metadata within the notebooks.
To display the cohort data without leaking individual patient data, the notebook report on group statistics instead.

# Computation methods
The replication notebooks in this project use different computation methods: local, pre-computation, and HPC cluster. In the following subsections, we explain these methods, their benefits, and drawbacks.

## Local
With this method, the computation are performed on a local machine (PC, laptop, etc.).

While local computation is strategy to implement, it quickly becomes impractical with large cohort size or computationally expensive preprocessing.
Therefore, we limit the use of local computation for small cohorts with low computation cost for preprocessing.
However, statistical analysis is often performed locally due to it's low computational demand.

## Pre-Computation
With this method, the entire dataset is downloaded and preprocessed using various pipelines. The results are stored and accessible on a institutional server.

One the one hand, pre-computed data can be accessed by multiple notebook, thus saving computation resources. On the other hand, the notebooks need to used the same pipeline parameters for this method be to beneficial.
Since the data is stored on a institutional server, detailed description of the pre-processing steps should be described.
Otherwise, reproducing the pre-processing might be challenging.

## HPC Cluster
With this method, the data is downloaded and processed on an HPC cluster.
While this offer more computing resources, it also offer its own challenges.

To download the data with [ppmi_downloader](https://github.com/LivingPark-MRI/ppmi-scraper), Chrome drivers need to be installed. We developed a script to build and run a containerized chrome driver instance (see {ref}`ppmi-downloader:hpc`)<!-- TODO: Put actual link -->

For computation we used *Narval* cluster managed by Digital Research Alliance of Canada. Computing jobs are scheduled directly from the notebooks.
