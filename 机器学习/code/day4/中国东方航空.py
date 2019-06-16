import requests
url='http://www.ceair.com/otabooking/flight-search!doFlightSearch.shtml'
data={
'_': 'a10d77f03e2411e9927ee73ad307c5b8',
'searchCond':'{"adtCount":1,"chdCount":0,"infCount":0,"currency":"CNY","tripType":"OW","recommend":false,"reselect":"","page":"0","sortType":"a","sortExec":"a","segmentList":[{"deptCd":"PEK","arrCd":"SHA","deptDt":"2019-03-07","deptAirport":"","arrAirport":"","deptCdTxt":"杭州","arrCdTxt":"上海","deptCityCode":"BJS","arrCityCode":"SHA"}],"version":"A.1.0"}'}
print(requests.post(url,data=data).content.decode('utf-8'))
from scrapy.spiders import CrawlSpider

