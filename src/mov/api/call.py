def req(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "46a57e9bf36f985bb6de9191d20e71f9"
    url = f"{base_url}?key={key}&targetDt={dt}"
    print(url)

req()
req(dt="<지정할 날짜>")
req("8" * 3)
