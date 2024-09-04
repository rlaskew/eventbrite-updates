"""Module providing a function printing python version."""

import os
import json
import requests

def build_xls_data_row(event_row):
    """
    Multiplies two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of a and b.
    """

    """
    data_array = [event_row["id"], 
              event_row["series_id"],   
              event_row["venue_id"], 
              str(event_row["is_series"]), 
              str(event_row["is_series_parent"]), 
              event_row["start"]["timezone"], 
              event_row["start"]["local"], 
              event_row["end"]["timezone"], 
              event_row["end"]["local"], 
              event_row["url"]
        ]
        data_delimiter = ","
        data_result = data_delimiter.join(data_array)
        print(data_result)
    """
    
    event_data_id = event_row["id"] if "id" in event_row else "" 
    series_id = event_row["series_id"] if "series_id" in event_row else "" 
    venue_id = event_row["venue_id"] if "venue_id" in event_row else "" 
    is_series = str(event_row["is_series"]) if "is_series" in event_row else "" 
    is_series_parent = str(event_row["is_series_parent"]) if "is_series_parent" in event_row else ""
    start_timezone = event_row["start"]["timezone"] if "start" in event_row else ""
    start_local = event_row["start"]["local"] if "start" in event_row else ""
    end_timezone = event_row["end"]["timezone"] if "end" in event_row else ""
    end_local = event_row["end"]["local"] if "end" in event_row else ""
    url = event_row["url"] if "url" in event_row else ""
            
    return [event_data_id,
            series_id,
            venue_id,
            is_series,
            is_series_parent,
            start_timezone,
            start_local,
            end_timezone,
            end_local,
            url
            ]

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
    #if has_more_items:
    #    print(data["pagination"])

    for event_data_row in data["events"]:
        event_data_array = build_xls_data_row(event_data_row)
        data_delimiter = ","
        data_result = data_delimiter.join(event_data_array)
        print(data_result)

    if has_more_items: 
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

column_title_array = ["Event ID",
        "Series ID",
        "Venue ID",
        "Is Series",
        "Is Series Parent",
        "Start Timezone",
        "Start Local",
        "Start Timezone",
        "End Local",
        "URL"
]
column_title_delimiter = ","
result = column_title_delimiter.join(column_title_array)
print(result)

url_get_events_by_org_id_request(os_org_id,
                                os_api_key,
                                os_page_size,
                                "",
                                os_max_pages)
