import pandas as pd
import csv
import tkinter as tk

dict_arr = []

def load_csv(fp: str, col_one: int, col_two: int):
  with open (fp, mode='r', encoding="utf8") as inp:
    reader = csv.reader(inp)
    dict_arr.append({rows[col_one]:rows[col_two] for rows in reader})

def update():
    dict_arr[1].update(dict_arr[0])
    data = dict_arr[1].items()
    pd.DataFrame(data = data).to_csv("test.csv", index=False, header=None)


if __name__ == '__main__':
  load_csv('sales.csv', 26, 30)
  load_csv('export.csv', 2, 14)
  update()

  387838-ddc91a7e-5647-464b-b45a-4e650524764c
https://www.figma.com/file/1uZAudYytH0IxrwxsW6V7z/Untitled?node-id=0%3A1