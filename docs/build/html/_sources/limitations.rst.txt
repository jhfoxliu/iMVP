Limitations
===========

Like other EDA (exploratory data analysis) methods, ``iMVP`` also had its limitations:

* First, iMVP is not suitable for dataset with too few sites without clear patterns. 

* Second, as mentioned in m6A method comparison and m5C motif sub-typing in human oocyte data, iMVP had its possibility of false discovery if two types of sites were similar to each other. 

* Third, just as a double-edged sword, iMVP is a position-sensitive strategy and gets stunned when the number of phases is too big. To solve this problem and extend iMVP for other usages (e.g., motif searching in iCLIP), further refinement like using ``parametric UMAP`` is needed.

* Last, in some cases, iMVP is too flexible in cluster determination. In the HDBSCAN step, the cluster output is determined by multiple parameters, especially the method used in cluster extraction from the condensed density tree. When encounters complicated partitioning issue, it requires an experienced user to find an optimized solution.

It is sure that, iMVP is a workflow that simplifies the motif discovery issue, but not a replacement of traditional motif finders. We strongly recommend you to integrate them with iMVP in practices.