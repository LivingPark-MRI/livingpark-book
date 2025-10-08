(livingpark-utils)=
# LivingPark_Utils

A unified API to facilitate the writing of LivingPark replication notebooks.

## Motivation

As part of the LivingPark project, eleven papers are replicated by various researchers. While developing a package to streamline the replication process takes significant time, it brings several benefits.

First, standardizing the code across the replication notebook accelerate the review process. Second, fixing bugs in the package feature directly benefit all notebooks. Last, it accelerate the process for users trying to replicate or extend our replication studies.

## Features

The following are currently supported

- Interface the usage of different dataset downloader with a CLI.
- Implements common filters and metric computations for datasets.
- Offer routines for correcting missing data.
- Implements and containerize pre-processing pipelines.
- Allow exclusion of patients from a cohort without leaking their metadata.

<!-- ### Example -->
<!-- TODO -->

## Limitations

This tools is developed on a use case basis. If you are using this tool and require a new feature, please [open a issue on GitHub](https://github.com/LivingPark-MRI/livingpark-utils/issues).
