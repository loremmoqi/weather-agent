import requests
from config import AMAP_KEY

def get_weather(city:str,date:str = "today") -> dict:
    clean_city = city.replace("市","").replace("省","").strip()
    geo_url = f"https://restapi.amap.com/v3/geocode/geo?address={clean_city}&key={AMAP_KEY}"
    try:
        geo_res = requests.get(geo_url, timeout=5).json()
    except Exception as e:
        return {"error": f"网络请求失败: {str(e)}"}
    
    if geo_res.get('status') != '1' or not geo_res.get('geocodes'):
        return {"error": f"找不到城市: {clean_city}"}
        
    adcode = geo_res['geocodes'][0]['adcode']
    real_city = geo_res['geocodes'][0].get('city') or geo_res['geocodes'][0].get('province')
    
    weather_url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={adcode}&key={AMAP_KEY}"
    try:
        weather_res = requests.get(weather_url, timeout=5).json()
    except Exception as e:
        return {"error": f"获取天气失败: {str(e)}"}
        
    if weather_res.get('status') != '1' or not weather_res.get('lives'):
        return {"error": "未获取到实时天气数据"}
        
    live_weather = weather_res['lives'][0]
    return {
        "city": real_city,
        "weather": live_weather['weather'],
        "temperature": f"{live_weather['temperature']}°C",
        "winddirection": f"{live_weather['winddirection']}风",
        "windpower": f"{live_weather['windpower']}级",
    }