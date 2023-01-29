#!/usr/bin/env python
# coding: utf-8

import networkx as nx
import pandas as pd
import networkx.algorithms.community as nx_comm

def init(path_trust_data_csv: str):
    df = pd.read_csv(path_trust_data_csv)

    Graphtype = nx.Graph()
    G = nx.from_pandas_edgelist(df,source='userID',target="contactID", edge_attr='Trust', create_using=Graphtype)
    write_graph_pickle(G,path_trust_data_csv+".gml")

    list_commu = nx_comm.louvain_communities(G, seed=123)

    return df, list_commu

def write_graph_pickle(Graph, path_gml):
    #nx.write_gpickle(Graph,path_gml)
    pass

def read_graph_pickle(path_gml):
    #return nx.read_gpickle(path_gml)
    pass

def find_user_community(user:int, list_commu: list):
    ind=0
    for i in range(len(list_commu)):
        if user in list_commu[i] :
            ind = i
    return ind

#find if users in list_followers are in commu
def find_followees_in_community(user:int,commu:int, list_followers:list, list_commu:list):
    list_followers_in_commu = [f for f in list_followers if f in list_commu[commu]]
    return list_followers_in_commu

def top_k(community : int, list_commu : list, k : int, df):
    top_k = []
    for i in range(k): #init list
        top_k.append((None,0))

    for user in list_commu[community]:
        nb_contacts = len(df.loc[df["userID"] == user, "contactID"])
        if nb_contacts > top_k[0][1]:
            top_k[0] = (user,nb_contacts)
            top_k = sorted(top_k, key=lambda x: x[1])
    return top_k

# take second element for sort
def takeSecond(elem):
    return elem[1]

def top_k_followees(user:int,list_followers, list_commu : list, k : int, df):
    top_k = []
    commu = find_user_community(user, list_commu)
    list_followers_in_commu = find_followees_in_community(user, commu,list_followers,list_commu)

    for follower in list_followers_in_commu:
        nb_contacts = len(df.loc[df["userID"] == follower, "contactID"])
        top_k.append((follower,nb_contacts))
    
    top_k.sort(key=takeSecond,reverse=True)
    if len(top_k)<k:
        return top_k
    else:
        return top_k[0:k]

def find_top_k_followees(user:int, list_followers:list, list_commu,k:int, df):
    commu = find_user_community(user, list_commu)
    top_k = top_k_followees(user, list_followers, list_commu, k, df)
    return top_k
