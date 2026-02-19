import requests
import re

def get_show_tv_live_link():
    url = "https://www.showtv.com.tr/canli-yayin"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # Sayfa kaynağındaki .m3u8 uzantılı ve içinde token barındıran asıl linki bulur
        match = re.search(r'(https://[^"]+?\.m3u8[^"]*)', response.text)
        
        if match:
            # Link içindeki kaçış karakterlerini (Eğik çizgi vb.) temizler
            raw_link = match.group(0).replace('\\/', '/')
            return raw_link
        return None
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None

def main():
    live_link = get_show_tv_live_link()
    
    if live_link:
        # Sadece bu kanalın olduğu m3u dosyasını oluşturur
        m3u_content = f"#EXTM3U\n#EXTINF:-1,SHOW TV\n{live_link}"
        with open("show.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("show.m3u başarıyla güncellendi.")
    else:
        print("Geçerli bir link bulunamadı.")

if __name__ == "__main__":
    main()
