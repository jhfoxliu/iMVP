Installation
============

Environment
-----------

Most of the functions in ``iMVP-utils`` can be run on Linux, Windows, and MacOS. 

Our interactive interface is not available on Windows because some application (e.g., ``Weblogo``) are not supported. For such a situtation, we suggest you to use ``WSL`` (https://docs.microsoft.com/en-us/windows/wsl/).

Dependencies
------------

The workflow is supported by ``Python 3``.

Tested/recommanded versions are indicated. In each notebook, we also highlight the required packages.

Basic Requirements
^^^^^^^^^^^^^^^^^^

* umap-learn (>=0.5.2)
* hdbscan (>=0.8.27)
* pandas (>=1.3.4)
* numpy (>=1.20.0)
* scipy (>=1.5.1)
* scikit-learn (>=0.23.1)
* biopython (>=1.77)

Notebooks
^^^^^^^^^

* jupyter-notebook

Approximate clustering
^^^^^^^^^^^^^^^^^^^^^^

* cv2 (>=4.5.5)

Figures generation
^^^^^^^^^^^^^^^^^^

* matplotlib (>=3.2.2)
* seaborn (>=0.10.1)
* weblogo (>=3.7.0)

Interactive interface
^^^^^^^^^^^^^^^^^^^^^
* dash (>=2.0.0)
* dash-bio (>=0.9.0)
* imageio (>=2.13.5)

GPU accerleration
^^^^^^^^^^^^^^^^^

* cuML

See :doc:`GPU_accerleration` for details.

Install from Pypi
-----------------

To install the package with ``pip``:

.. code-block:: sh

    pip install iMVP_utils

Install in a virtual environment
--------------------------------

We recommend to use ``pipenv`` to avoid interrupting your environment variables. If ``pipenv`` is not istalled, run:

.. code-block:: sh

    pip instasll pipenv

To install the package in a virtual environment (Python3 only):

.. code-block:: sh

    # make a directory for iMVP
    mkdir iMVP
    cd iMVP
    pipenv install -r requirements.txt
    pipenv install iMVP_utils
    
Then run

.. code-block:: sh

    pipenv shell
    # run iMVP-utils in an interactive mode
    iMVP_utils

To exit the environment:

.. code-block:: sh

    exit

Successful installation
^^^^^^^^^^^^^^^^^^^^^^^

To check if ``iMVP-utils`` and the interative interface are installed correctly. You can type 

.. code-block:: sh

    iMVP_viewer.py --help

in your shell, then you will see the help message:

.. code-block:: sh

    usage: iMVP_viewer [-h] [--output OUTPUT_PATH] [--host HOST] [--port PORT]

    optional arguments:
    -h, --help            show this help message and exit
    --output OUTPUT_PATH, -o OUTPUT_PATH
                            The output directory. If not exist, will make the folder. Default="./output/"
    --host HOST           The IP address of the app, default=127.0.0.1 (localhost)
    --port PORT           The port number that you want to dispaly the app.

You can also enter the Python shell to load the package:

.. code-block:: python

    import iMVP_utils
    