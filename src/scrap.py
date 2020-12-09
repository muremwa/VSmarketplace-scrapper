from typing import Dict, Any
from urllib import request
from urllib.error import HTTPError
import json
import re


def m_address(extension_id: str) -> str:
    """get the marketplace URL loaded with the extension ID"""
    if not re.search(r'.*?\..*?', extension_id):
        raise ValueError('Incorrect extension ID')

    ad_f_p = re.split(r'\\\w+\.\w+', __file__)[0]
    ad_file = f"{ad_f_p}\\val/address.json"

    with open(ad_file, 'r') as ad_f:
        ads: dict = json.load(ad_f)
        ad = ads.get('url', '')

    return f'{ad}{extension_id}'


def extract_details(text: str) -> Dict[str, Any]:
    """Get text and extract the title, publisher, image, installs"""
    title, ps_name, img, installs = None, None, None, None

    # extract title
    _title = re.findall(r'<span\s+class="ux-item-name">(.*?)</span>', text, re.M)
    if _title:
        title = _title[0]

    # extract publisher name
    _ps_name = re.findall(r'<a.*?\sclass="ux-item-publisher-link.*?".*?>(.*?)</a>', text, re.M)
    if _ps_name:
        ps_name = _ps_name[0]

    # extract image
    _img = re.findall(r'<td.*?id="vss_2"><img.*?class="image-display".*?src="(.*?)".*?/></td>', text, re.M)
    if _img:
        img = _img[0]

    # extract installs
    _installs = re.findall(r'<span\s+class="installs-text".*?>\s*(.*?)\s{1}installs</span>', text, re.M)
    if _installs:
        _in: str = _installs[0]
        installs = int(_in.replace(',', ''))

    return {
        'title': title,
        'publisher_name': ps_name,
        'default_image': img,
        'installs': installs
    }


def retrieve_extension_page(url: str) -> str:
    """
    gets the url of an extension in the marketplace and returns string of its HTML code.
    URL is typically the result of m_address function
    """
    try:
        page = request.urlopen(url)
        data = page.read().decode('utf8') if page.code == 200 else None
    except HTTPError:
        data = None

    return data
