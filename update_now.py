import requests
import re

def get_now_tv_bozz():
    # Elahmad'ın NOW TV sayfası (BozzTV altyapısını kullanıyor)
    url = "https://www.elahmad.com/tv/live-now-tv.php"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': 'https://www.elahmad.com/'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        # Senin bulduğun tgn.bozztv.com yapısındaki m3u8 linkini arıyoruz
        # Token (wmsAuthSign) ile birlikte tamamını yakalar
        match = re.search(r'(https://tgn\.bozztv\.com/[^"]+\.m3u8\?wmsAuthSign=[^"\' ]+)', response.text)
        
        if match:
            return match.group(0).replace('\\/', '/')
        return None
    except Exception as e:
        print(f"Hata: {e}")
        return None

def main():
    link = get_now_tv_bozz()
    if link:
        with open("now.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write('#EXTINF:-1 tvg-id="NowTV" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/47/NOW_logo_%28Turkey%29.png" group-title="CANLI",NOW TV\n')
            f.write(f"{link}\n")
        print(f"BozzTV Linki Yakalandı: {link}")
    else:
        print("BozzTV linki veya token bulunamadı.")

if __name__ == "__main__":
    main()
