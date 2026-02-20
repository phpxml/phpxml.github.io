import requests
import re

def get_star():
    url = "https://www.startv.com.tr/canli-yayin"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Referer": "https://www.startv.com.tr/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }
    
    try:
        session = requests.Session()
        r = session.get(url, headers=headers)
        # Linki bulmak için daha geniş bir arama yapıyoruz
        match = re.search(r'https?://[^\s"\']+\.m3u8[^\s"\']*', r.text)
        
        if match:
            link = match.group(0).replace("\\/", "/")
            with open("star.m3u8", "w") as f:
                f.write("#EXTM3U\n#EXTINF:-1,Star TV\n" + link)
            print("Sonunda oldu!")
        else:
            print("Link hala bulunamıyor, Star korumayı artırmış.")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    get_star()
