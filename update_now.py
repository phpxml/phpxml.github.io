import requests
import re

def get_now_from_elahmad():
    # Elahmad üzerindeki NOW TV'nin ID'si genellikle 'now_tv' veya benzeridir
    # Sayfa URL'si: https://www.elahmad.com/tv/live-now-tv.php (NOW TV sayfası)
    url = "https://www.elahmad.com/tv/live-now-tv.php"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': 'https://www.elahmad.com/'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        # Sitede m3u8 linkini arıyoruz
        # Genellikle "file": "http..." veya src: 'http...' şeklinde saklanır
        match = re.search(r'(https?://[^"]+?\.m3u8[^"]*)', response.text)
        
        if match:
            link = match.group(0).replace('\\/', '/')
            # Linkin sonundaki fazlalıkları temizle
            link = link.split("'")[0].split('"')[0]
            return link
        return None
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        return None

def main():
    link = get_now_from_elahmad()
    if link:
        with open("now.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write('#EXTINF:-1 tvg-id="NowTV" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/47/NOW_logo_%28Turkey%29.png" group-title="CANLI",NOW TV\n')
            f.write(f"{link}\n")
        print(f"Link Elahmad üzerinden başarıyla çekildi: {link}")
    else:
        print("Elahmad sayfasında yayın linki bulunamadı.")

if __name__ == "__main__":
    main()
