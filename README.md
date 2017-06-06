# Night Owls Detector

## Description
The script shows pupils of education project [DEVMAN.org](https://devman.org) who send commits with solutions after midnight acoording pupil's local time. 


## How to use
Run the script ```python3 seek_dev_nighters.py```.
By default the script determine night owls whose commits have been sent between 12am and 6am. 
You could define other time for night shift use optional key `-n`

### Example
```python3 seek_dev_nighters.py -n 5```

```
Midnighter: rancvova. Amount attempts after midnight: 5
Midnighter: mikhail.ushanov. Amount attempts after midnight: 5
Midnighter: alexander.i.kamenev. Amount attempts after midnight: 3
```

### Requirements
Install the dependencies from requirements.txt using pip:

```pip install -r requirements.txt```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
