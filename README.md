# Visulization Accerlated Motif Analysis (VAMA)

<img src=https://user-images.githubusercontent.com/20188476/150387619-6ca84c54-40e3-4048-a392-c2857e3b1669.png width=80% />

Welcome to use VAMA! Are you curious about what's the picture for?

This is amazing picture is from the UMAP projection of the 21-nt sequences of **999,240** human A-to-I RNA editing sites (in non-Alu repeats) in REDIportal! For this picture, we can intuitively learn what kinds of k-mers (21-mers here) are included and enriched in such huge amount of RNA editing events. This is never been done before.

## Introduction

VAMA is a strategy inspired by the commonly used single cell analysis strategy of dimensional reduction followed by clustering. Different from the digital counts in single cell analysis, we here use the RNA sequence (and/or structure) as an input. Here, we firstly transform RNA sequences into a one-hot format; then these transformed sequences were projected to a 2D plane with UMAP, which can not only gather the similar sequences together, but also maintain the relationships between each other (compared with t-SNE); the dimensional reduced data were further clustered by density, with the super-efficient algorithm HDBSCAN, to highlight the enriched sequences.

Compared with canonical analysis, such as using MEME to scan for motifs in specific lengths of windows, this strategy works much faster, especially with large dataset (>10000 sites). Meanwhile, visulization itself can enable you to notice the distribution of noise, and perceive abnormal clusters even they are in low amount.


