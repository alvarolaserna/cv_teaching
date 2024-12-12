# Automation MasterClass

## Installation

create environment:

<pre>
    python -m venv venv
</pre>

activate environment unix/linux/mac:

<pre>
    . venv/bin/activate
</pre>

activate environment windows:

<pre>
    venv\Scripts\activate
</pre>

Install requirements:

<pre>
    pip install -r requirements.txt
</pre>

## Run cases

<pre>
    python -m pytest tests -s -p no:warnings
</pre>


# Automation Latency Meassure

## Installation

Create environment:

```sh
    python -m venv venv
```

Activate environment unix/linux/mac:

```sh
    . venv/bin/activate
```

Activate environment windows:

```sh
    venv\Scripts\activate
```

Install requirements:

```sh
    pip install -r requirements.txt
```

## Run script with different options


```sh
python track_latency.py PATH_WITH_MP4_VIDEOS APPLICATION SCENARIO
```

- PATH_WITH_MP4_VIDEOS: Root path where files mp4 are stored. It go over for all folders looking them.
- APPLICATION: 
-- Youtube
- SCENARIO: Different scenarios we defined, choose between:
-- ColdAppStartup

## Run script to reencoding the video to 30 fps and then meassure the latency with an example

```sh
./calculate_latency.sh resources YouTube iPhone-7 ColdAppStartup
```