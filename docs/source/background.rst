Background
==========
    
If you were assigned to identify the enriched motifs from a set of sequences, what is your first idea?

* Statistical based methods? For example, compute the entropies of sequence preferences from the sliding windows?

* Graph-based methods? By computing the connections between the sequences?

* Deep-learning based methods? Just hands off and wait for the best fitting?

And what will you do if you were assigned to analyze **1 million sequences**, instead of hundreds? There should be a solution for such a scenario.

Just jump out of the box. Let's repeat the essence of our question: how can we isolate **a set of similar things** from a crowd of sequences. Wait... do you find something is similar? For example, the popular **single cell analysis**, that we project the thousands to millions of cells in a (N, M) matrix onto a 2D plane, where N is the number of cells and M is the number of gene expression values, for further analysis.

Such a method can also be applied on motif discovery! Here we can firstly use one-hot encoding to transform the sequences into vectors (ATCG to [1,0,0,0,...]). Then we can use a dimension reduction algorithm to seprate the sequences as much as possible on the 2D plane. And finally, we can use a Unsupervised clustering method to identify the similar sequences into clusters.

This is the idea for **interactive epitranscriptomic Motif Visualization and Sub-type Partitioning (iMVP)**. Here, we chose two powerful tools, UMAP and HDBSCAN, for the embedding and clustering steps. Such a combination is highly reliable in both speed, sensibility, fliexibility, and most importanly scalability. We now extend our ability in motif analysis from thousands to millions, when GPU accerleration is available.

In this documenet, we provide various examples for users at any levels and for any purposes:

* For beginners, we provide an interactive interface of iMVP, with which one can analyze the motifs - what you see is what you get.

* For advanced users, we prepared Notebooks for analysis for different propuses.

Wish you enjoy this document and get what you want from your data :)

.. image:: ../Images/iMVP_workflow.png
    :align: center

|
|
