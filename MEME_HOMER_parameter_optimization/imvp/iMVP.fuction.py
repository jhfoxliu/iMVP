import sys, os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
import scipy.stats
import tracemalloc
import umap
import hdbscan
from Bio import SeqIO
import time

def UMAP(onehot_input, df, min_dist=0.01, n_neighbors=20, verbose=False, densmap=False, metric='euclidean'):
    df = df.copy()
    # this should takes ~20 sec  
    tracemalloc.start() 
    print("UMAP")
    current, _ = tracemalloc.get_traced_memory()
    time0 = time.time()
    
    model = umap.UMAP(init="random", random_state=42, n_components=2, min_dist=min_dist, n_neighbors=n_neighbors, verbose=verbose, densmap=densmap, metric=metric)
    umap_output = model.fit_transform(onehot_input)
    
    time1 = time.time() - time0
    _, peak = tracemalloc.get_traced_memory()
    
    mem = (peak - current)/1024./1024.
    
    print("UMAP time: {} sec".format(time1))
    print("UMAP RAM: {} MB".format(mem))
    print("==================================================")
    print()
    df["X"] = umap_output[:, 0]
    df["Y"] = umap_output[:, 1]
    
    del model
    return time1, mem, df


def cluster_HDBSCAN(df, min_cluster_size=100, min_samples=10, cluster_selection_epsilon=0.0, cluster_selection_method='eom', draw_condensed_tree=True, soft_clustering=True, optimize=True):
    # use multi-code here
    tracemalloc.start()
    df = df.copy()
    X = np.stack([df["X"], df["Y"]], axis=1)
    current, _ = tracemalloc.get_traced_memory()
    time0 = time.time()
    model = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size, min_samples=min_samples, cluster_selection_epsilon=cluster_selection_epsilon, cluster_selection_method=cluster_selection_method, core_dist_n_jobs=4, prediction_data=True)
    if optimize == True:
        validity_scorer = make_scorer(hdbscan.validity.validity_index,greater_is_better=True)
        param_dist = {'min_samples': [10, 50,100, 200], # 1,
                      'min_cluster_size':[100,200, 300, 500, 1000],  
                      'cluster_selection_method' : ['eom'],
                     }
        n_iter_search = 20
        '''
        random_search = RandomizedSearchCV(model
                                           ,param_distributions=param_dist
                                           ,n_iter=n_iter_search
                                           ,scoring=validity_scorer 
                                           ,random_state=42)
        '''
        grid_search = GridSearchCV(model,param_dist,scoring=validity_scorer)
        # random_search.fit(X)
        grid_search.fit(X)
        # print(random_search.best_params_)
        model = grid_search.best_estimator_
        print(grid_search.best_estimator_)
        # model = random_search.best_estimator_
    yhat = model.fit(X)
    
    if soft_clustering == True:
        soft_clusters = hdbscan.all_points_membership_vectors(yhat)
        labels = [np.argmax(x) for x in soft_clusters] 
    else:
        labels = yhat.labels_
    
    time1 = time.time() - time0
    _, peak = tracemalloc.get_traced_memory()
    mem = (peak - current)/1024./1024.
    
    df["Cluster"] = [i+1 if i > -1 else -1 for i in labels ]  # re-number lables to make it human-readable
    
    print("HDBSCAN soft clustering time: {} sec".format(time1))
    print("HDBSCAN soft clustering RAM: {} Mb".format(mem))
    print("HDBSCAN cluster number: {}".format(df["Cluster"].max()))
    print("==================================================")
    # check cluster number
    print(df.groupby("Cluster")["Cluster"].count())
    
    
    if draw_condensed_tree == True:
        fig, ax = plt.subplots()
        model.condensed_tree_.plot(select_clusters=True, selection_palette=sns.color_palette())
    return time1, mem, df, model


if __name__ == "__main__":
    enc = OneHotEncoder(dtype=np.int8)
    enc.fit([[i] for i in "ATCGN"])
    def onehot_enc(fa):
        seq = [[i] for i in fa.upper().replace("U","T")]

        return enc.transform(seq).toarray().reshape(-1)
    
    
    onehot_input_mix = []
    dic_mix = {}
    with open(sys.argv[1]) as handle:
        i = 0
        for record in SeqIO.parse(handle, "fasta"):
            onehot_input_mix.append(onehot_enc(record.seq))
            dic_mix[i] = {}
            dic_mix[i]["info"] = record.id
            dic_mix[i]["F10"] = str(record.seq)
            i += 1
    onehot_input_mix = np.array(onehot_input_mix)
    df_mix = pd.DataFrame.from_dict(dic_mix).T
    
    _, _, df_mix = UMAP(onehot_input_mix, df_mix, min_dist=0.01, n_neighbors=20, verbose=False, densmap=False, metric='euclidean') # _, _, df_UMAP = UMAP(onehot_input, df, min_dist=0.01, n_neighbors=20, verbose=False, densmap=False, metric='euclidean')
    df_mix.to_csv("Sim_UMAP.csv")
    # _, _, df_HDBSCAN, _ = cluster_HDBSCAN(df_UMAP, min_cluster_size=100, min_samples=10, soft_clustering=False, optimize=True)
    # cluster_HDBSCAN(df_UMAP, min_cluster_size=100, min_samples=100, soft_clustering=False, optimize=False)
    _, _, df_mix, _ = cluster_HDBSCAN(df_mix, min_cluster_size=100, min_samples=100, soft_clustering=False, optimize=False)

    df_mix.to_csv(sys.argv[2], sep = "\t", index = False)