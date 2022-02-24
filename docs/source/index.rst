.. iMVP-utils documentation master file, created by
   sphinx-quickstart on Tue Feb 22 14:46:48 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The iMVP-utils
==============
**interactive epitranscriptomic Motif Visualization and Sub-type Partitioning (iMVP)** is a strategy inspired by the commonly used single cell analysis strategy of dimensional reduction followed by clustering. Different from the digital counts in single cell analysis, we here use the RNA sequence (and/or structure) as an input. Here, we firstly transform RNA sequences into a one-hot format; then these transformed sequences were projected to a 2D plane with UMAP, which can not only gather the similar sequences together, but also maintain the relationships between each other (compared with t-SNE); the dimensional reduced data were further clustered by density, with the super-efficient algorithm HDBSCAN, to highlight the enriched sequences.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Background
==========

.. toctree::

   background

Installation
============

.. toctree::

   install

For beginners
=============

.. toctree::

   beginners

For advanced users
==================

.. toctree::

   advanced_users


Algorithm and parameter selections
==================================

Dimension Reduction Algorithms
------------------------------

.. toctree::

   UMAP

Unsupervised clustering algorithms
----------------------------------

.. toctree::

   HDBSCAN

Towards huge dataset
====================

.. toctree::

   GPU_accerleration


Limitations
===========

.. toctree::

   limitations

Notebooks
=========

.. toctree::

   notebooks


Gallery
====================

.. toctree::

   gallery


API Reference
=============

.. toctree::

   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
