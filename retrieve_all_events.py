"""Module providing a function printing python version."""

import os
import json
import requests

def url_get_events_by_org_id_request(org_id,api_key,page_size,continuation,max_pages):
    """
    Multiplies two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of a and b.
    """
    base_url = "https://www.eventbriteapi.com/v3/organizations/"
    url_to_get = base_url + org_id + "/events/?token=" + api_key + "&page_size=" + str(page_size)
    if continuation:
        url_to_get = url_to_get + "&continuation=" + continuation

    response = requests.get(url_to_get, timeout=10)
    data = json.loads(response.text)
    has_more_items = data["pagination"]["has_more_items"]
    if has_more_items:
        print(data["pagination"])
    current_page_number = int(data["pagination"]["page_number"])
    current_continuation_string = data["pagination"]["continuation"]
    if current_page_number < max_pages:
        url_get_events_by_org_id_request(org_id,
                                        api_key,
                                        page_size,
                                        current_continuation_string,
                                        max_pages)

os_api_key = os.environ.get("API_KEY")
os_org_id = os.environ.get("ORG_ID")
os_page_size = int(os.environ.get("PAGE_SIZE"))
os_max_pages = int(os.environ.get("MAX_PAGES"))

url_get_events_by_org_id_request(os_org_id,
                                os_api_key,
                                os_page_size,
                                "",
                                os_max_pages)
