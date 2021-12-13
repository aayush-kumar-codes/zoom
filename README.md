# Zoom App Integration

## Summary:

Api endpoints to create meetings via zoom app.

## Procedure of using endpoints to create and get meetings:

### To generate authorization code:

#### Request:
```bash    
    Endpoint: '{{origin}}/'
```

#### Response:
```bash
    Redirected_to: '{{origin}}/zoom/callback/?code={{generated_code}}'
```

### To get an access token:

#### Request:
```bash
    Endpoint: '{{origin}}/token'

    payload: 

        {
            "code": "{{ authorization_code }}"
        }
    

```


#### Response:
```bash
    {
        "access_token": "{{ generated_access_token }}",
        "expires_in": "{{ expiration_time }}"
    }
    
```

### To create a meeting:

#### Request:
```bash
    Endpoint: '{{ origin }}/create/'

    Headers: {
        "Authorization": "{{ access token }}"
    }

    Payload:

        {"topic": "Meeting Title",
                  "type": 2,
                  "start_time": "2019-06-14T10: 21: 57",
                  "duration": "30",
                  "timezone": "UTC",
                  "agenda": "test",
  
                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }
```

#### Response:

```bash
    {
    "uuid": "kWhVJ4xfQjmQiMUShu2i3w==",
    "id": 81346685739,
    "host_id": "{{ host_id }}",
    "host_email": "{{ host_email }}",
    "topic": "Meeting Title",
    "type": 2,
    "status": "waiting",
    "start_time": "2021-12-13T07:25:22Z",
    "duration": 30,
    "timezone": "UTC",
    "agenda": "test",
    "created_at": "{{ created_at }}",
    "start_url": "{{ start_url }}",
    "join_url": "{{ join_url }}",
    "password": "SRp5iX",
    "h323_password": "216825",
    "pstn_password": "216825",
    "encrypted_password": "UlFObCtRTzR2Y1p4cTkrUHBRYnNuUT09",
    "settings": {
        "host_video": true,
        "participant_video": true,
        "cn_meeting": false,
        "in_meeting": false,
        "join_before_host": false,
        "jbh_time": 0,
        "mute_upon_entry": false,
        "watermark": true,
        "use_pmi": false,
        "approval_type": 2,
        "audio": "voip",
        "auto_recording": "none",
        "enforce_login": false,
        "enforce_login_domains": "",
        "alternative_hosts": "",
        "close_registration": false,
        "show_share_button": false,
        "allow_multiple_devices": false,
        "registrants_confirmation_email": true,
        "waiting_room": false,
        "request_permission_to_unmute_participants": false,
        "registrants_email_notification": true,
        "meeting_authentication": false,
        "encryption_type": "enhanced_encryption",
        "approved_or_denied_countries_or_regions": {
            "enable": false
        },
        "breakout_room": {
            "enable": false
        },
        "alternative_hosts_email_notification": true,
        "device_testing": false,
        "focus_mode": false
    },
    "pre_schedule": false
}
```

### To get meeting:

#### Request:

```bash
    Endpoint: '{{ origin }}/get_meetings/'
    Headers: {
        "Authorization": "{{ access token }}"
    }
```

#### Response

```bash
    {
    "page_size": 30,
    "total_records": 3,
    "next_page_token": "",
    "meetings": [
        {
            "uuid": "8GdKhMNIR0C0amd2Wc/TTQ==",
            "id": 88410615733,
            "host_id": "{{ host id }}",
            "topic": "The title of your zoom meeting",
            "type": 2,
            "start_time": "2021-12-11T17:55:07Z",
            "duration": 45,
            "timezone": "{{ timezone }}",
            "agenda": "test",
            "created_at": "2021-12-11T17:55:07Z",
            "join_url": "{{ join_url }}"
        },
        {
            "uuid": "fik2C9EgTs29Rp36GWHqUg==",
            "id": 82132648813,
            "host_id": "{{ host id }}",
            "topic": "The title of your zoom meeting",
            "type": 2,
            "start_time": "2021-12-11T17:55:25Z",
            "duration": 45,
            "timezone": "{{ timezone }}",
            "agenda": "test",
            "created_at": "2021-12-11T17:55:24Z",
            "join_url": "{{ join_url }}"
        },
        {
            "uuid": "4xeBnfWoTD+ANutLRS2tng==",
            "id": 86952919719,
            "host_id": "{{ host id }}",
            "topic": "Meeting Title",
            "type": 2,
            "start_time": "2021-12-13T07:03:26Z",
            "duration": 30,
            "timezone": "{{ timezone }}",
            "agenda": "test",
            "created_at": "2021-12-13T07:03:25Z",
            "join_url": "{{ join_url }}"
        }
    ]
}
```
