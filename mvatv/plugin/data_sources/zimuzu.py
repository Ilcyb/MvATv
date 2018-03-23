# 人人影视数据源 
# http://www.zimuzu.tv/

import requests
import re
from bs4 import BeautifulSoup

# from ..plugin import Plugin
from mvatv.plugin.plugin import Plugin
from mvatv.exception.exceptions import NoResourceError
from mvatv.utils.utils import Quality


class ZIMUZU(Plugin):
    
    def __init__(self):
        pass

    def _search(self, keyword, season=1, episode=1, quality=Quality.Medium, need_subscript=True):
        headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8','Referer':'http://www.zimuzu.tv/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        data = {'keyword':keyword,'type':'resource'}

        try:
            response = requests.get('http://www.zimuzu.tv/search', params=data, headers=headers)
            response.raise_for_status()
            doc = BeautifulSoup(response.text, 'html.parser')
            urls = [i.find('a')['href'] for i in doc.find_all(class_='t f14') if '《'+keyword+'》' in i.find('strong').string]
            if len(urls) == 0:
                raise NoResourceError()
            url = urls[0]
            resource_id = url.split('/')[-1]
            resource_url = r'http://m.zimuzu.tv/resource/item'
            resource_data = {'rid':resource_id, 'season':season, 'episode':episode}
            resource_response = requests.get(resource_url, params=resource_data, headers=headers)
            resource_response.raise_for_status()
            resource_doc = BeautifulSoup(resource_response.text, 'html.parser')
            lis = resource_doc.find_all(class_='mui-table-view-cell mui-collapse')
            zimu_type_and_capacity_list_list = \
            [[i.find(class_='mui-badge').string, i.find(class_='mui-pull-right').string] for i in lis]
            resource_index = self._choose_resource_by_quality(zimu_type_and_capacity_list_list, quality, need_subscript)
            return self._get_magnet_link(lis[resource_index])
        except NoResourceError:
            raise
        except requests.exceptions.HTTPError:
            print('Can\'t connect to the data source, please check the data source is normal.')
        except Exception as e:
            print('Unhandled exception occurred:', '\n', e)
            raise


    def _choose_resource_by_quality(self, subscript_quality_list, quality, need_subscript):
        require_resource_list = list()
        for i in range(len(subscript_quality_list)):
            if need_subscript:
                if '中文字幕版' in subscript_quality_list[i][0]:
                    require_resource_list.append(i)
            else:
                require_resource_list.append(i)
            cap = subscript_quality_list[i][1]
            if 'GB' in cap:
                subscript_quality_list[i][1] = float(cap.split('GB')[0]) * 1000
            elif 'MB' in cap:
                subscript_quality_list[i][1] = float(cap.split('MB')[0])
        for i in require_resource_list:
            if subscript_quality_list[i][1] > quality.value:
                return i
        if len(require_resource_list) == 0:
            raise NoResourceError
        else:
            return require_resource_list[0]


    def _get_magnet_link(self, bs_doc):
        data_url = re.findall(r'magnet:?[^\"]+', str(bs_doc))
        return data_url
