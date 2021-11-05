# A  function to return the format of each value in a DataFrame
def color_corr(val):
    if abs(val) < 0.5 or val==1:
        color = 'grey'
        opacity = '50'
    else:
        color = 'green'
        opacity = '100'
    
    col_op = 'color:'+color+';opacity:'+opacity+'%'
    
    return col_op

# A simple function to extract the first value of a list in a DataFrame row
def extract_initial_list_value(row):
    return row[0]