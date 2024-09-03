


## Gets USER info including ID for token
curl https://www.eventbriteapi.com/v3/users/me/?token=${TOKEN}

## https://www.eventbrite.com/platform/api#/reference/organization/list-organizations-by-user/list-organizations-by-user
## Gets Org IDs for Token
curl -sS  https://www.eventbriteapi.com/v3/users/me/organizations/?token=${TOKEN}

## needs description
curl -sS https://www.eventbriteapi.com/v3/series/${EVENT_ID}/?token=${TOKEN}

## needs description
curl -sS https://www.eventbriteapi.com/v3/events/${EVENT_ID}/?token=${TOKEN}

## TODO  -- curl -X POST  ???
curl -sS https://www.eventbriteapi.com/v3/events/${EVENT_ID}/schedules/

{
  "schedule": {
    "occurrence_duration": 3600,
     "recurrence_rule": "DTSTART:20250214T183000Z\nRRULE:FREQ=MONTHLY;COUNT=1"
  }
}

## 
