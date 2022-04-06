Limitations
===========

Like other EDA (exploratory data analysis) methods, ``iMVP`` also had its limitations:

* First, iMVP is not suitable for a dataset with too few sites or sites without sequence preferences. 

* Second, iMVP is a position-sensitive strategy and even with a phase-matching strategy, the current version may have poor performance when dealing with datasets with high numbers of phases. Future improvement such as the use of "parametric UMAP" in the dimension reduction may improve its performance on such datasets and broaden the usage of iMVP.

* Third, in the clustering step, the cluster output may be varied with different parameters, especially when extracting clusters from the condensed density tree. Thus, prior knowledge may be required for the selection of the proper parameters.
