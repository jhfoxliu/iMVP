# Welcome!

Are you curious about what's the picture for?

<img src=https://user-images.githubusercontent.com/20188476/150387619-6ca84c54-40e3-4048-a392-c2857e3b1669.png width=100% />

This is amazing picture is from the UMAP projection of the 21-nt sequences of **999,240** human A-to-I RNA editing sites (non-Alu repeats) in REDIportal! Each pixel here represents a set of similar sequences, and brighter pixel means higher density of sites. With this picture, we can intuitively learn what kinds of k-mers (21-mers here) are included and enriched in such huge amount of RNA editing events. This is never been done before.

## Introduction

**interactive Motif analysis by Visualization accelerated Perception (iMVP)** is a strategy inspired by the commonly used single cell analysis strategy of dimensional reduction followed by clustering. Different from the digital counts in single cell analysis, we here use the RNA sequence (and/or structure) as an input. Here, we firstly transform RNA sequences into a one-hot format; then these transformed sequences were projected to a 2D plane with UMAP, which can not only gather the similar sequences together, but also maintain the relationships between each other (compared with t-SNE); the dimensional reduced data were further clustered by density, with the super-efficient algorithm HDBSCAN, to highlight the enriched sequences.

Compared with canonical analysis, such as using MEME to scan for motifs in specific lengths of windows, this strategy works much faster, especially with large dataset (>10000 sites). Meanwhile, visulization itself can enable you to notice the distribution of noise, and perceive abnormal clusters even they are in low amount.

A detailed document can be found in link readthedocs.io

## Contents 
- Requirement
- Basic usage
- Examples
- GPU accerlation
- The interactive version
- Contact
- Citation

## Requirement

We use `Python 3` in iMVP. We list the packages required in each notebook. In summary, we require `pandas`, `numpy`, `umap-learn`, `hdbscan`, `scipy`, `matplotlib`, and `seaborn` for most of the usages. For some cases, `scikit-learn` should be isntalled for benchmarking. We recommend you to install `Weblogo` and `MEME` for further analysis of the clusters.

For Linux, all of the packages and softwares are available on Pypi (with `Pip`) or on the official websites.

For Windows, `Weblogo` and `MEME` might not be avilable. `hdbscan` from Pypi is not compatible but can be install via unofficial wheels (https://www.lfd.uci.edu/~gohlke/pythonlibs/). Meanwhile, while computing large dataset, a time out error will happen if `core_n_jobs` in `hdbscan` is larger than 1.

## Basic usage and examples

I don't think packing all the functions into a class is a good idea for this project. Everything can done with native objects of python and pandas. To make it clear, I provide a set of helper functions in the folder `Utils`, and I define all of the used functions in each notebook.

**Background knowledge** HDBSCAN

## GPU accerlation

To achieve analysis in huge dataset, we use NVIDIA `RAPIDS` library (majorly `cuML`) to accelerate `UMAP` and `HDBSCAN`. Please visit the office pages for more information.

Please note that, we can speed up `UMAP` with `RRAPIDS` in more than 10-folds. But it's hard for `HDBSCAN`, because we will have various computational complexity with different data and different parameters. I offen get out of GPU memory if too many small clusters are wating for analyzing. Hence, the current best practices for large dataset (e.g., 40 million non-repeative editing sites) is to use `UMAP` to compute the corrdinates on the 2D plane, then process the projections to CPU version `HDBSCAN` for further clustering. We also notice that, soft-clustering strategy will be buggy when the condensed tree is too large.

## The interactive version

We also develop an interactive version of iMVP. This interactive one is built with `Plotly`. This version is suitable for quick and flexible analysis with low to middle (up to 100K) sites. The detail of the interactive version please see our document.

### Credits

- The idea, major codes, and notebooks are contributed by `Jianheng Liu` (https://orcid.org/0000-0003-0216-1951) at Rui Zhang's Lab (Jan, 2022).
- The interactive version developed on Plotly is contributed `Jing Yao` at Rui Zhang's lab (Jan, 2022).

### Contact

For any bugs, please post them in `Issues`. You can also contact `Jiangheng Liu` (jhfoxliu@gmail.com) directly.

### Citation

NaN
