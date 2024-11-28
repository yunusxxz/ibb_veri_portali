import requests as req
import pandas as pd

BASE_URL = 'https://api.ibb.gov.tr/ispark/'

def json(park_id: int = -1):
    """
    İBB İSPARK API'sinden park bilgilerini döndürür.

    Args:
        park_id (int, optional): Park ID'si. Varsayılan -1, tüm park bilgilerini çeker.

    Returns:
        dict or None:
            - Eğer `park_id` belirtilmemişse tüm parkları içeren bir sözlük döner.
            - Eğer `park_id` belirtilmişse, belirtilen parkın detaylarını içeren bir sözlük döner.
            - Hata durumunda `None` döner.
    """
    if park_id < 0:
        res = req.get(BASE_URL + 'Park')
        if res.status_code == 200:
            return res.json()
    else:
        res = req.get(BASE_URL + f'ParkDetay?id={park_id}')
        if res.status_code == 200:
            return res.json()[0]

def dataframe():
    """
    İBB İSPARK API'sinden alınan park bilgilerini bir DataFrame'e dönüştürür.

    Returns:
        pandas.DataFrame:
            Tüm park bilgilerini içeren bir DataFrame döner.
            Eğer API'den veri alınamazsa hata verir.
    """
    return pd.read_json(BASE_URL + 'Park')

def series(park_id: int):
    """
    Belirtilen park ID'sine göre park bilgilerini bir pandas Series olarak döndürür.

    Args:
        park_id (int): Park ID'si.

    Returns:
        pandas.Series:
            - Belirtilen parkın detaylarını içeren bir Series döner.
            - Hata durumunda boş bir Series dönebilir.
    """
    return pd.Series(json(park_id))


if __name__ == '__main__':
    #print(json(882))
    #print(dataframe())
    print(series(882))