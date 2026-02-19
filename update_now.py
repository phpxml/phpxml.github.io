import requests
import re

def get_now_bozz_direct():
    # NOW TV (Fox) sayfası
    url = "https://www.elahmad.com/tv/live-now-tv.php"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': 'https://www.elahmad.com/'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        content = response.text
        
        # 1. Yöntem: Direkt linki yakala (Senin verdiğin formatta)
        match = re.search(r'(https://tgn\.bozztv\.com/[^"\' ]+turkfoxtv[^"\' ]+)', content)
        
        if not match:
            # 2. Yöntem: Eğer link parçalıysa, m3u8 ve wmsAuthSign kısmını birleştir
            token_match = re.search(r'wmsAuthSign=([^"\' &]+)', content)
            if token_match:
                token = token_match.group(1)
                return f"https://tgn.bozztv.com/gin-trn09/gin-turkfoxtv/index.m3u8?wmsAuthSign={token}"
        
        if match:
            return match.group(0).replace('\\/', '/')
            
        return None
    except:
        return None

def main():
    link = get_now_bozz_direct()
    if link:
        with open("now.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write('#EXTINF:-1 tvg-id="NowTV" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/47/NOW_logo_%28Turkey%29.png" group-title="CANLI",NOW TV\n')
            f.write(f"{link}\n")
        print(f"Başarılı! Link: {link}")
    else:
        print("BozzTV/Elahmad üzerinde link bulunamadı. Site yapısı değişmiş olabilir.")

if __name__ == "__main__":
    main()
