from requests import Request, Session
from core.settings import API_KEY, API_BASE_URL


class CoinMarket:
    def __int__(self):
        self.url = API_BASE_URL
        self.headers = {
            "X-CMC_PRO_API_KEY": API_KEY
        }
        self.session = Session()

    def get_ohcl(self) -> list:
        pass

    def get_period(self) -> list:
        pass

    def create_request(self, url_prefix: str, params: dict) -> Request:
        r = Request(method="GET", url=self.url + url_prefix, headers=self.headers, params=params)
        # return requests.get(url=self.url + url_prefix, params=params, headers=self.headers)
        return r

    def send_request(self, r: Request) -> dict:
        """resp = s.send(prepped,
                    stream=stream,
                    verify=verify,
                    proxies=proxies,
                    cert=cert,
                    timeout=timeout
                )
        """
        try:
            resp = self.session.send(request=r.prepare())
            return resp.json()
        except Exception as e:
            print(e)
