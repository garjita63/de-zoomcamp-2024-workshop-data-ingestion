

Command prompt
```
python -m venv ./env
source ./env/bin/activate
pip install dlt[duckdb]

Successfully installed PyYAML-6.0.1 SQLAlchemy-2.0.25 astunparse-1.6.3 certifi-2024.2.2 charset-normalizer-3.3.2 click-8.1.7 dlt-0.4.2 duckdb-0.9.2 fsspec-2024.2.0 gitdb-4.0.11 gitpython-3.1.41 giturlparse-0.12.0 greenlet-3.0.3 hexbytes-1.0.0 humanize-4.9.0 idna-3.6 jsonpath-ng-1.6.1 makefun-1.15.2 orjson-3.9.13 packaging-23.2 pathvalidate-3.2.0 pendulum-3.0.0 ply-3.11 python-dateutil-2.8.2 pytz-2024.1 requests-2.31.0 requirements-parser-0.5.0 semver-3.0.2 setuptools-69.0.3 simplejson-3.19.2 six-1.16.0 smmap-5.0.1 tenacity-8.2.3 time-machine-2.13.0 tomlkit-0.12.3 types-setuptools-69.0.0.20240125 typing-extensions-4.9.0 tzdata-2023.4 urllib3-2.2.0 wheel-0.42.0

```

Command prompt
```
python
```

Python prompt
```
data = [
    {
        "vendor_name": "VTS",
		"record_hash": "b00361a396177a9cb410ff61f20015ad",
        "time": {
            "pickup": "2009-06-14 23:23:00",
            "dropoff": "2009-06-14 23:48:00"
        },
        "Trip_Distance": 17.52,
        "coordinates": {
            "start": {
                "lon": -73.787442,
                "lat": 40.641525
            },
            "end": {
                "lon": -73.980072,
                "lat": 40.742963
            }
        },
        "Rate_Code": None,
        "store_and_forward": None,
        "Payment": {
            "type": "Credit",
            "amt": 20.5,
            "surcharge": 0,
            "mta_tax": None,
            "tip": 9,
            "tolls": 4.15,
			"status": "booked"
        },
        "Passenger_Count": 2,
        "passengers": [
            {"name": "John", "rating": 4.9},
            {"name": "Jack", "rating": 3.9}
        ],
        "Stops": [
            {"lon": -73.6, "lat": 40.6},
            {"lon": -73.5, "lat": 40.5}
        ]
    },
]
```
Pipeline taxi_data load step completed in 1.69 seconds<br>
1 load package(s) were loaded to destination duckdb and into dataset taxi_rides<br>
The duckdb destination used duckdb:////mnt/c/WINDOWS/system32/taxi_data.duckdb location to store data<br>
Load package 1707269084.1495888 is LOADED and contains no failed jobs<br>

