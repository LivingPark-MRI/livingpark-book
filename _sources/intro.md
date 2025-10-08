# LivingPark

## Context

Advances in early diagnosis, understanding, and treatment of Parkinson's disease (PD) critically rely on the establishment of biomarkers to identify disease subtypes and to track disease progression. Neuroimaging, in particular T1-weighted structural Magnetic Resonance Imaging (sMRI), is a promising source of biomarkers given its ability to capture rich and descriptive information about brain structure non-invasively. However, it has yet to become a part of standard clinical and research routines because the reliability of MRI-based measurements is susceptible to several different sources of variability, including those introduced by different analysis methods, imaging acquisition parameters, and approaches to population sampling.

The variability induced by software selection and data acquisition significantly threatens the reliability of MRI-derived biomarkers. Until now, no systematic attempt has been made to quantify the effect of such variations on the associations with clinical outcomes. Identifying the most important sources of variability is a first step towards developing "best practice" guidelines for MRI analysis. Quantifying the variability will allow for accounting for measurement error when estimating sample sizes for clinical trials that include MRI-derived predictive variables.

This same variability could also be informative because distinct methods could be differentially sensitive to unique aspects of the disease. Multivariate statistics or Machine Learning (ML) techniques could be applied to the full range of possible data analyses to extract and then aggregate the most predictive features from distinct methods, resulting in improved biomarker quality.

## Goals

The goal of this project is to quantify the effect of software and data induced variability on the performance of potential sMRI-derived biomarkers of PD, and to investigate the use of this variability to improve biomarker quality. Our specific objectives are to:

1. Evaluate the impact of MRI analysis software toolboxes on the reliability of potential PD biomarkers.
1. Evaluate the generalizability of potential PD MRI-derived biomarkers across different datasets.
1. Improve potential biomarkers by using multivariate statistics and ML to aggregate measurements obtained from different analytical specifications or datasets.

# Methods

## Task 0: Replication of selected MRI-derived PD biomarkers

There are currently no established MRI biomarker of disease stage or progression. Therefore, in our study on the source of measurement variability, we replicate eleven sMRI-derived measures of neurodegeneration listed in {cite}`Mitchell2021`.

The goal is not to debunk previous findings, nor to merely replicate them, but rather, to use the analytic methods behind these published results as a starting point for comparing different analysis choices and measuring their impact.

We replicated the eleven selected measures on the [PPMI](https://www.ppmi-info.org/) dataset to allow for the variability evaluations planned in Tasks 1-4. This Jupyter Book contains the Jupyter Notebooks fully describing the analyses, providing a reference resource for the community to further investigate these measures. Note that two of the eleven measures were identified in [PPMI](https://www.ppmi-info.org/) and were reproduced in identical analytical conditions, to enable their investigation in Tasks 1-4. [PPMI](https://www.ppmi-info.org/) includes sMRIs and motor as well as neuropsychological evaluations either identical or comparable to the ones used in the initial measures.

The [PPMI](https://www.ppmi-info.org/) dataset contains 198 healthy controls and 432 PD (35% female, mean age 61 years) — all with baseline MRI acquisitions. All subjects underwent standardized MRI imaging at baseline to identify significant non-PD pathology, including a 3D magnetization prepared rapid gradient echo (MPRAGE) sequence for anatomical imaging, and a cardiac-gated 2D single-shot echo-planar DTI sequence on 3 Tesla Siemens Trio. Motor impairment was assessed with the MDS-UPDRS (Movement Disorders Society-Unified Parkinson Disease Rating Scale). Global cognition was assessed with the MoCA. Other assessments included memory (Hopkins Verbal Learning Test-Revised), visuospatial function (Benton Judgment of Line Orientation), speed-attention (Symbol-Digit Modalities Test), and executive abilities-working memory (Letter-Number Sequencing and semantic fluency). The [PPMI](https://www.ppmi-info.org/) dataset also includes a prodromal cohort with 27 subjects with iRBD and at least one T1 image from which measures identified in the prodromal or preclinical stage will be replicated.

## Task 1: Between-toolbox variability

We evaluated the impact of the choice of image processing toolbox on the accuracy of the selected measures using the same metrics as in the original assessments. For each tested measure, we varied the software toolbox among SPM, FSL, Freesufer or ANTs. All these toolboxes are widely used, well documented, and freely accessible. For each type of analysis (VBM, DBM and CT), we accurately described and differentiated toolboxes to provide insights on possible causes for the observed discrepancies. For measures involving statistical testing (non-ML studies), we only varied the imaging toolboxes, whether they include the statistical analyses or not (i.e. when these are provided by a third party toolbox such as R). For ML studies, we only varied the image analysis toolbox while keeping the ML toolbox and parametrization fixed. The rationale behind this design is to simulate typical SPM, FSL, or Freesurfer users while keeping other software choices consistent.

## Task 2: Within-toolbox variability

We tested the impact of the image-processing toolbox version, MATLAB interpreter version (SPM only), operating system version, and pipeline parametrization. As a general rule, we tested the different versions and parametrizations among the values found across all the selected measures. We ported analyses to multiple FSL, Freesurfer, ANTs or SPM versions. To vary operating system versions, we will use the numerical framework described in {cite}`Salari2021` as it allows to simulate between-operating-system differences without having to install the toolboxes in different environments. We will review the differences between software versions and explain potential causes of the observed discrepancies, providing detailed insights on the stability of image analysis software.

## Task 3: Between-dataset evaluations

We replicated the measures obtained on the PPMI dataset within the C-BIG (Clinical Biospecimen Imaging and Genetic) dataset {cite}`Das2021`, a dataset collected by the Quebec Parkinson's Network (QPN). C-BIG’s demographics and assessments were chosen to match the PPMI cohort, which makes the replication of most studies feasible. C-BIG includes 364 PD participants (145 female) among which 130 have at least 1 sMRI available. C-BIG also includes (1) motor evaluations (Unified Parkinson’s Disease Rating Scale), a Quantitative Clinical Motor Testing (QCMT), TUG, Purdue Pegboard, and alternate finger tapping, and (2) computerized cognitive battery as per the recommendations of the Movement Disorder Society Task Force for cognitive assessment in PD. Cognitive domains assessments include: attention and working memory (Trail Making Test, Stroop, Rey Complex Figure copy and recall), executive function (Tower of London, Verbal Fluency Test, Boston Naming Test, Brixton Spatial Anticipation Test), and memory (Hopkins Verbal Learning Test, Rey Auditory Verbal Learning Test, Digit span).

We replicated the non-prodromal PPMI measures in C-BIG by aligning the imaging and clinical measures in both datasets according to (1) imaging sequences, (2) imaging features, in particular regional volumes, (3) demographic distributions and outcome variables. We then extracted C-BIG cohorts either close or distant from the original PPMI study to quantify the generalizability of PPMI associations or ML predictions to C-BIG. This evaluation provides insights on the potential clinical applicability of MRI biomarkers beyond the specific dataset with which they were developed.

## Task 4: Measurements aggregation

We aggregated measures obtained from multiple software toolboxes, from different parameterizations of the same software toolbox, or from different datasets, and evaluate the resulting improvement of the tested measures. Two main approaches were investigated: (1) a multivariate statistical framework modeling the effect of software toolbox, parameterizations, and data acquisition, and (2) machine-learning techniques such as bootstrap aggregation {cite}`Breiman1996`, data augmentation, or stacked generalization {cite}`Chen2018`. Similar to our previous work in {cite}`Kiar2020`, we tested different aggregation techniques and evaluated the increased generalizability on the C-BIG dataset. Leveraging analytical variability in such a way is novel. It is enabled by the wide availability of high-performance computing and by the complexity, and therefore methodological flexibility, of neuroimaging analyses.

Sample sizes will be identical to the ones used in the existing assessments of the selected measures.

The project aims to advance the design, understanding, and clinical applicability of PD biomarkers by providing (1) an overview of biomarker replicability, (2) a review of the impact of study design decisions on biomarker performance, and (3) frameworks to aggregate measurements obtained in different conditions in a single, more reliable prediction. Further, this project provides a much needed comprehensive set of best practices for reproducible PD MRI analysis, impacting future studies at large. To further increase impact, all the software code and derived data produced by the project is publicly available in this Jupyter Book.

```{bibliography}
```
