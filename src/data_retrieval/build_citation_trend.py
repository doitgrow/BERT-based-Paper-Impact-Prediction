from scopus.scopus import Citation
import time
import multiprocessing
import datetime
import sqlite3
import pickle
import pandas as pd

# DB에 없는 EID 만 선택
def load_eids_from_pickle(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    
    return set(data.eid)


def load_eids_from_sql(file):
    conn = sqlite3.connect(file)
    sql_df = pd.read_sql("SELECT * FROM PAPER_CITATION_TREND", conn)
    conn.close

    return set(sql_df['EID'])
    

# SQL에 크롤링한 데이터 저장
def save_data_to_sql(dict_data, db_path):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    columns = ':EID, :2006, :2007, :2008, :2009, :2010, :2011, :2012, :2013, :2014, :2015, :2016, :2017, :2018, :2019, :2020, :2021, :DATE'
    cur.execute(f'INSERT INTO PAPER_CITATION_TREND VALUES({columns})', dict_data)
    con.commit()
    con.close()


# 인용 수 데이터 얻기
def get_citation(EID):
    try:
        ct = Citation()
        ct.get_citation_page_about_EID(EID)
        time.sleep(5)
        rst = ct.get_citation_values_by_year()
        rst['EID'] = EID
        rst['DATE'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ct.driver.close()
        save_data_to_sql(rst, r"D:\BERT-based-Paper-Impact-Prediction\rsc\training_data\Citation_data.db")
        # print(rst)
    except Exception as e:
        ct.driver.close()

def run(data:list, n_processes=4):
    exist_eids = load_eids_from_sql(r"D:\BERT-based-Paper-Impact-Prediction\rsc\training_data\Citation_data.db")
    new_eids = set(data)
    target_eids = list(new_eids - exist_eids)
    print(f"데이터 수집 개수 : {len(target_eids)}")

    try:
        pool = multiprocessing.Pool(processes=n_processes) # multiprocessing.cpu_count()
        pool.map(get_citation, target_eids) 
        pool.close()
        pool.join()
    except:
        try:
            pool = multiprocessing.Pool(processes=n_processes) # multiprocessing.cpu_count()
            pool.map(get_citation, target_eids) 
            pool.close()
            pool.join()
        except:
            try:
                pool = multiprocessing.Pool(processes=n_processes) # multiprocessing.cpu_count()
                pool.map(get_citation, target_eids) 
                pool.close()
                pool.join()
            except:
                pass

if __name__ == "__main__":

    with open(r"D:\BERT-based-Paper-Impact-Prediction\rsc\preparation_data\train_eids.txt", 'r', encoding='UTF-8') as f:
        eids = f.readlines()
        
    eids = [eid.strip() for eid in eids]

    run(eids, 4)

