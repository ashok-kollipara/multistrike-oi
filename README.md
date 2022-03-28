# NSE Options Multi Strike Open Interest Analysis using Python
Monitor and analyse support and resistances for positions to take in range bound markets while waiting for breakouts

**Why do this ?**

1. Showcase python and Database skills learnt in real world usage
2. Didnot want to pay :) for this service
3. Work with slowest internet connection
4. Provides ability to use and make data as per my usage
5. Last but not least no login required


## Getting Started

**Step 1: Clone** 

Clone the project/repository into desired folder

```
git clone git@github.com:ashok-kollipara/multistrike-oi.git
```

**Step 2. Get Python**

> Python 3.10.x (Tested) 

```
https://www.python.org/downloads/

https://docs.python.org/3/library/tkinter.html

```

Setup help for windows ( environment variables and MAX PATH limitations, with tkinter installation)

```
https://docs.python.org/3/using/windows.html
```
Most Linux distributions have python installed by default

**Step 3. Install required Python packages**
 
```
pip install -r requirements.txt
```

## Usage

**Step A : Launch program**

In case python is added to environment variables it can be directly used in command line at any folder level. 

Navigate into the folder in which the repo is cloned

```
python main.py
```

![Step A](/images/UI.PNG)

**Step B : Plot Window**

If everything is done perfectly so far there will be a window that appears as below

![Step B](/images/PLOT.PNG)

Wait and see the data populate.

## Note :

- Default auto refresh rate is 5 mins.
- Data will be stored from start of plot
- Database will be reset on start and close of window


## Whats Next ?

1. WIP single window operation
