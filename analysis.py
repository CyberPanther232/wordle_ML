from model_analysis.model_analysis_tools import load_report, report_info, report_guess_avg
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('overall_report.txt')

df.columns = ['Model_ID', 'Days Param', 'Numb of Lower Prob Letters', 'Model Average Guess']

print(df)

plt.plot(df['Model_ID'], df['Model Average Guess'])
plt.show()

plt.scatter(df['Days Param'], df['Model Average Guess'])
plt.show()