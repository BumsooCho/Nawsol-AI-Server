from dotenv import load_dotenv
load_dotenv()

import os
import requests


class FundAPI:

    @staticmethod
    def fetch_fund_list():
        service_key = os.getenv("FUND_SERVICE_KEY")
        url = "https://apis.data.go.kr/1160100/service/GetFundProductInfoService/getStandardCodeInfo"

        params = {
            "serviceKey": service_key,
            "pageNo": 1,  # 첫 페이지
            "numOfRows": 1000,  # 1000개 가져오기
            "resultType": "json"
        }

        res = requests.get(url, params=params)
        print(res)

        data = res.json()

        print("\n===== API RAW RESPONSE START =====")
        print(res.text[:1000])  # 앞 1,000자만 출력
        print("===== API RAW RESPONSE END =====\n")

        items = data["response"]["body"]["items"].get("item", [])

        return items


        # page_no = 1
        # num_rows = 1000
        #
        # all_items = []
        #
        # while True:
        #     params = {
        #         "serviceKey": service_key,
        #         "pageNo": page_no,
        #         "numOfRows": num_rows,
        #         "resultType": "json"
        #     }
        #
        #     res = requests.get(url, params=params)
        #     print(res)
        #     data = res.json()
        #
        #     print("\n===== API RAW RESPONSE START =====")
        #     print(res.text[:1000])  # 앞 1,000자만 출력
        #     print("===== API RAW RESPONSE END =====\n")
        #
        #     items = data["response"]["body"]["items"].get("item", [])
        #     total_count = data["response"]["body"]["totalCount"]
        #
        #     if not items:
        #         break
        #
        #     all_items.extend(items)
        #
        #     # 마지막 페이지 도달하면 중단
        #     if page_no * num_rows >= total_count:
        #         break
        #
        #     page_no += 1
        #
        # return all_items
