import requests
import re

def get_star_link():
    # Star TV canlı yayın sayfası
    url = "https://www.startv.com.tr/canli-yayin"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        # Senin gönderdiğin 'dogus.daioncdn.net' ile başlayan o uzun linki yakalar
        match = re.search(r'(https?://dogus\.daioncdn\.net/[^"\']+\.m3u8[^"\']*)', response.text)
        
        if match:
            # Linkin içindeki varsa ters bölüleri temizle
            clean_link = match.group(1).replace("\\/", "/")
            with open("star.m3u8", "w") as f:
                f.write("#EXTM3U\n")
                f.write("#EXTINF:-1,Star TV\n")
                f.write(clean_link)
            print("Star TV linki başarıyla güncellendi.")
        else:
            print("Link sayfada bulunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    get_star_link()
