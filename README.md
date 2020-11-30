# Response Rate Visualizer
Visualize respone rates from text data (blogs, twitter, etc.)

![Schedules of reinforcement](https://github.com/youssefabdelm/responseratevisualizer/blob/master/Schedules%20of%20Reinforcement.png)

# Usage
1. ```pip install -r requirements.txt```
2. For datasets with sentences or paragraphs per cell, use `schedulesngrams.py`. For datasets where it's just one word per cell, use `schedulesfavorites.py`
3. Make sure your CSV file's column name starts with 'tweet' if using `schedulesngrams.py` (or 'user' if using `schedulesfavorites.py`) and that there's a column called 'date' with the date formatted as follows: `2012-03-24`
4. Make sure the columns are sorted by descending order (latest dates first).

# Example
Originally, I made this for twitter data, but of course it also works for blogs. For example, here's my analysis of the amazing systems scientist George Mobus' blog.

![https://questioneverything.typepad.com/](https://github.com/youssefabdelm/responseratevisualizer/blob/master/Top%2017%201%20terms%20for%20questioneverything%20latest%20occurence%20date%202020-03-19.png)

# How to read it

Extremely roughly, you could say 'the steeper the lines, the higher the "interest" ' 

Plateuing lines means "interest" is decaying.

But heads up: this is oversimplifying it.
