# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:32:00 2021
@author: Susung Kim

"""

import multiprocessing
from pybliometrics.scopus import ScopusSearch
import pandas as pd
import pickle

def get_doc_count_by_ISSN(ISSN):
    ss = ScopusSearch("ISSN(" + ISSN + ")", download=True, verbose=True)
    return ss

# df_ai = pd.read_excel(r"D:\myproject\research_work\citation_prediction\rsc\conf\journal_info\AI-SJR.xlsx", skiprows=1)
df_ae = pd.read_excel(r"D:\myproject\research_work\citation_prediction\rsc\conf\journal_info\AE-SJR.xlsx", skiprows=1)

# Retrieval the scopus data using scopus api
# df_ai = df_ai[df_ai['ISSN'] != "-"]
# ISSN = df_ai['ISSN'].values
df_ae = df_ae[df_ae['ISSN'] != "-"]
ISSN = df_ae['ISSN'].values

# ISSN_docData_dict = {}
# for issn in ISSN:
#     ss = get_doc_count_by_ISSN(issn)
#     ISSN_docData_dict[issn] = ss

# with open("ISSN_docData_dict_ai.pickle", "wb") as f:
#     pickle.dump(ISSN_docData_dict, f)

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    result = pool.map(get_doc_count_by_ISSN, ISSN)
    pool.close()
    pool.join()
    

    ISSN_docData_dict = {}
    for issn, rst in zip(ISSN, result):
        ISSN_docData_dict[issn] = rst
    
    with open(r"D:\myproject\research_work\citation_prediction\rsc\rst\ISSN_docData_dict_ae.pickle", "wb") as f:
        pickle.dump(ISSN_docData_dict, f)

# if __name__ == '__main__':
#     pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
#     result = pool.map(get_doc_count_by_ISSN, ISSN)
#     pool.close()
#     pool.join()

#     ISSN_docData_dict = {}
#     for issn, rst in zip(ISSN, result):
#         ISSN_docData_dict[issn] = rst

#     with open("ISSN_docData_dict_ai.pickle", 'wb') as f:
#         pickle.dump(ISSN_docData_dict, f)
#     # with open("ISSN_docData_dict_ae.pickle", 'wb') as f:
#     #     pickle.dump(ISSN_docData_dict, f)

    