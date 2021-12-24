from pybliometrics.scopus import AuthorRetrieval
import sqlite3
import pandas as pd
import multiprocessing

# Define function for multiprocessing
def get_author_data(auid):
    au = AuthorRetrieval(auid)
    citaion_count = au.citation_count or 0
    cited_by_count = au.cited_by_count or 0
    h_index = au.h_index or 0
    personal_research_period = au.publication_range[1] - au.publication_range[0] + 1

    return [auid, citaion_count, cited_by_count, h_index, personal_research_period]


conn = sqlite3.connect('rsc/training_data/X_abstract_retrieval.db')
query = 'SELECT * FROM ABSTRACT_RETRIEVAL_API where language == "eng"'
X_data = pd.read_sql(query, conn)
conn.close()

# 저자 관련 데이터 수집 (Author ciations, Author publications, Author H-index) -> 총 3개
auids = list(set([auid.strip() for auid in "; ".join(X_data['author_ids']).split("; ") if auid]))
print('수집할 저자 관련 데이터 수: {:,}개'.format(len(auids)))


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=2)
    result = pool.map(get_author_data, auids)
    pool.close()
    pool.join()
    
    columns = ['auid', 'citaion_count', 'cited_by_count', 'h_index', 'personal_research_period']
    author = pd.DataFrame(result, columns=columns)

    conn = sqlite3.connect("rsc/training_data/X_abstract_retrieval.db")
    author.to_sql('AUTHOR_RETRIEVAL_API', conn, if_exists='append', index=False)
    conn.close()