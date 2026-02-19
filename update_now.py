import requests
import re

def get_now_tv_link():
    url = "https://www.nowtv.com.tr/canli-yayin"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': 'https://www.nowtv.com.tr/'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # m3u8 uzantılı yayın linkini yakalar
        match = re.search(r'(https://[^"]+?\.m3u8[^"]*)', response.text)
        
        if match:
            return match.group(0).replace('\\/', '/')
        return None
    except:
        return None

def main():
    link = get_now_tv_link()
    if link:
        with open("now.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write('#EXTINF:-1 tvg-id="NowTV" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/47/NOW_logo_%28Turkey%29.png" group-title="CANLI",NOW TV\n')
            f.write(f"{link}\n")
        print("now.m3u başarıyla güncellendi.")
    else:
        print("NOW TV linki bulunamadı.")

if __name__ == "__main__":
    main()
