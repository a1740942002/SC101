"""
File: coin_flip_runs.py
Name:
-----------------------
This program simulates a sequence of coin flips until
the number of runs specified by the user is reached.

A run is defined as consecutive occurrences of the same
result, either 'H' or 'T'. For example, the sequence
'HHHHHTHTT' is considered a 2-run result.

The program stops immediately once the total number of
runs reaches the user-defined value.
"""

import random as r


def main():
	print("Let's flip a coin!")
	num_run = int(input("Number of runs: "))

	result = ""        # 累積整個擲硬幣過程
	last_coin = ""     # 上一次擲出的面
	streak = 0         # 目前這一段「連續同一面」的次數
	runs = 0           # 已經出現過幾段（長度 >= 2 的連續）

	while runs < num_run:
		# 擲硬幣：1 當作 H，2 當作 T
		coin = "H" if r.randint(1, 2) == 1 else "T"

		if coin == last_coin:
			streak += 1
			if streak == 2:    # 連續剛好湊到 2，代表新誕生一段 run
				runs += 1
		else:
			streak = 1         # 跟上次不一樣，連續中斷，重新從 1 算起

		result += coin
		last_coin = coin

	print(result)



# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
