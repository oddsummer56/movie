from mov.api.call import gen_url, req, get_key, req2list, list2df, save2df, echo, apply_type2df
import pandas as pd

def test_apply_type2df():
    df = apply_type2df()
    assert isinstance(df, pd.DataFrame)
    assert str(df['rnum'].dtype) in ['int64']
    assert str(df['rank'].dtype) in ['int64']
    assert str(df['audiInten'].dtype) in ['int64']

    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']
    
    for c in num_cols:
        assert df[c].dtype in ['int64', 'float64']

def test_echo():
    r = echo("hello")
    assert r == "hello"

def test_save2df():
    df = save2df()
    assert isinstance(df, pd.DataFrame)
    assert 'load_dt' in df.columns
    #assert len(df) == 10

def test_list2df():
    df = list2df()
    print(df)
    assert isinstance(df, pd.DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'movieNm' in df.columns
    assert 'audiAcc' in df.columns

def test_req2list():
    l = req2list()
    assert len(l) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'

def test_비밀키숨기기():
    key = get_key()
    assert key


def test_유알엘테스트():
    url = gen_url()
    #assert "http" in url
    #assert "kobis" in url
    
    d = {"multiMovieYn": "N"}
    url = gen_url(req_val = d)
    assert "multiMovieYn" in url

def test_req():
    print("******************")
    code, data = req('20240728')
    #assert code == 200
    
    print(f"{code}")
    #assert code == 200
    
