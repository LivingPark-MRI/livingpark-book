(ppmi-downloader)=

# PPMI_Downloader

A 3rd-party crawler to download PPMI metadata and imaging data from LONI.

## Motivation

The Parkinson's Progression Markers Initiative (PPMI) dataset provides a large cohort of subjects to perform studies. The Laboratory of Neuro Imaging (LONI) provides a web portal to search and download subject metadata and imaging data. Unfortunately, manually creating and downloading cohort is prone to human errors. Moreover, the process does not encourage reproducibility.

With the development of the [`ppmi_downloader`](https://github.com/LivingPark-MRI/ppmi-scraper) Python package, we aim to provide a replicable method to download a cohort from the PPMI dataset.

## Features

The following features are currently supported

- Participant study metadata
- 3D MRI image metadata
- fMRI image metadata
- Imaging data

<!-- ### Example -->
<!-- TODO -->

(ppmi-downloader:hpc)=
### Use on HPC

Our tool use Selenium, which interacts with a Chrome driver. As most HPCs don't have Chrome available, we integrated a script to build and run a Selenium grid container. This spawns a containerized Chrome driver instance for Selenium to interact with.

## Limitations

As this tool is a unofficial downloader, we are not directly developing the [official LONI portal](https://ida.loni.usc.edu). Therefore, major or minor changes to the official portal can break functionality of our API.

Additionally, this tools is developed on a use case basis. If you are using this tool and require a new feature, please [open a issue on GitHub](https://github.com/LivingPark-MRI/ppmi-scraper/issues).
