import pandas as pd

def load_report(filepath) -> pd.core.frame.DataFrame | int | int:
    
    data = []
    
    with open(filepath, 'r') as report_file:
        for line in report_file:
            line = line.strip('\n')
            fields = line.split(':')
            
            if 'MODEL PARAMETERS:' in line:
                pass
            
            elif 'Number of Days: ' in line:
                Number_of_days = fields[1]
            
            elif 'Number of Lower Probability Letters: ' in line:
                Number_of_prob_letters = fields[1]
            
            elif 'Num' in line:
                pass
            
            else:
                fields = line.split(',')
                data.append({'Test Number' : fields[0],
                            'Number of Attempts' : int(fields[1]),
                            'Num of Lower Prob Letters' : fields[2]})
            
    report_file.close()
    
    report_df = pd.DataFrame(data)
    
    report_df.set_index('Test Number', inplace = True)
        
    return report_df, Number_of_days, Number_of_prob_letters

def report_info(report_data, num_days, num_letters):
    print("Displaying Report Data...")
    
    print("This report is on the model with the following parameters:\n")
    
    print(f"Number of Previous Days Solutions: {num_days}\nNumber of Lower Probability Letters: {num_letters}\n")

    print("Below is the information...")
    
    print(report_data.info())  
    
def report_guess_avg(report_data):
    return report_data['Number of Attempts'].mean()

def show_report_parameters():
    pass

def show_report_target_word():
    pass

def show_report_total_attempts():
    pass