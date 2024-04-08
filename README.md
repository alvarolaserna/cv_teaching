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