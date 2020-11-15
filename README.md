# Zoom-Automation-Python

![GitHub repo size](https://img.shields.io/github/repo-size/Anish-Malla/article-summarizer)
![GitHub repo stars](https://img.shields.io/github/stars/Anish-Malla/Zoom-Automation-Python?style=social)
![GitHub repo forks](https://img.shields.io/github/forks/Anish-Malla/Zoom-Automation-Python?style=social)

This python script signs into your zoom meetings / classes on time **automatically** for you.

![Showcase of project gif](/automatic_signin.gif)

## A Video Tutorial
https://www.youtube.com/watch?v=V3IOfvGmqxs

## Setup instructions

**Requirements:** python-3.8.6

* Clone the GitHub repo
```
git clone https://github.com/Anish-Malla/Zoom-Automation-Python
```
* cd into the directory
* Install required libraries
```
pip3 install pandas
```
* Follow the instructions specific to your OS for downloading pyautogui
```
https://pyautogui.readthedocs.io/en/latest/install.html
```
* Update the timings.csv with the time of the meeting, meeting id and password, do not add any unnecessary spaces. (Do not open the csv using excel as it changes the formatting)

**Note: windows users**

The code to open zoom is different for windows, this is shown in the main.py file make the changes accordingly.
