# A note on Reproducibility vs. Replicability

Both reproducibility and replicability aims to verify an experiment outcome by recreating the original experiment environment and methods identically or with some level or variability.

To limit ambiguity, throughout this book we use the following definitions:

**Reproduction**

> Recreating an original experiment using the same methods, data, and computation methods to the best of our capabilities.

**Replication**

> Recreating an original experiment using the same methods, but varying the data and/or computation methods.

# Challenges & Suggestions

Reproducing or replicating a study is often a tedious task with several challenges to be addressed. In the following subsections, we discuss some of the main challenges faced during the LivingPark project and proposed solution for enabling reproducibility in future studies.

## Data cleaning

Initiatives such as PPMI offer availability to large amount of data to perform studies. However, it is inevitable for such an effort to have some data entry error or missing data, due to manual data entry.

To avoid excluding valuable data and reduce cohort size, researchers may attempt to impute the erroneous data. In this process, numerous decision will be made to correct or predict data entries.
While describing the methods for correcting the data can help with reproducibility, some gap might remains and require assumptions to be made.

To address this issue, we created publicly available notebook which perform the data correction from the initial data and produce a derivate dataset. It describes the rational for different correction, assumptions made, and allow re-execution for any user to correct the same dataset.

## Cohort selection

Unfortunately for reproducibility, publishing data along side an article is not always possible due to ethical or security reasons. While authors often describe their cohort using group statistics, individual level information is lost. Therefore, it is challenging to recreate a cohort, even on the same dataset, due to numerous assumptions required to reproduce a cohort {cite}`Arafe2023`.

To address this issue, each reproduction study in this project has code available to handle downloading subjects and applying inclusion/exclusion criteria for creating a cohort.
Due to the evolving nature of datasets such as PPMI, the exact subjects composing our cohorts might change. However, the cohorts characteristic remain the same.

## Code availability

The sheer amount of neuroimaging pipelines available for pre-processing combined with the amount of parameters within a pipelines provides a large decision matrix for preparing a cohort for statistical analysis.
The impact on results from using different pipelines or varying a pipeline parameters highlights the importance of having code availability.

<!-- TODO: Cite paper on impact of pipeline and hyperparameter -->

Therefore, it is challenging to reproduce a paper without code available or using close source software.

Similarly, statistical test and parameters can impact the outcomes of analysis. Therefore, being able to rerun or modify the analysis to verify the results enhance reproducibility.

To address this issue, we make publicly available the code for pre-processing the cohort and performing statistical analysis. The reproduction notebooks call the containerized pipeline directly to improve reproducibility.

## Quality control

It is crucial to ensure the output from processing pipelines is valid. Without proper quality control (QC), analysis outcomes could result from noise or invalid data, which affect replicability while using other datasets or pipelines.
Unfortunately, performing quality control often require manual expert intervention. While authors generally describe their QC steps, it is not always throughout and may leave space assumptions. Therefore, having automated QC with minimal expert intervention would be beneficial for reproducibility.

<!-- TODO explain what was done in LivingPark for QC -->
