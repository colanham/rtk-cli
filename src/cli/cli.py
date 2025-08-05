import pandas as pd

def run_cli():
    while True:
        user_input = input("rtk-cli: ")    
        check_for_english(user_input)
        check_for_explanation(user_input)
        check_for_primitive(user_input)

def check_for_english(kanji):
    df = pd.read_csv("./resources/rtk2.csv") # may need objective file path 
    kanji_list = df["kanji"]
    if kanji in kanji_list.values:
        row_data = df.loc[df['kanji'] == kanji]
        row_index = row_data.index[0]
        english_value = row_data.loc[row_index, 'english']
        print("English Value: " + english_value)
    else:
        print("Error: Kanji not found")

def check_for_explanation(kanji):
    df = pd.read_csv("./resources/rtk2.csv") 
    kanji_list = df["kanji"]
    if kanji in kanji_list.values:
        row_data = df.loc[df['kanji'] == kanji]
        row_index = row_data.index[0]
        explanation_value = row_data.loc[row_index, 'explanation']
        print("Explanation Value: " + explanation_value)
    else:
        print("Error: Kanji not found")

def check_for_primitive(kanji):
    df = pd.read_csv("./resources/rtk2.csv") 
    kanji_list = df["kanji"]
    if kanji in kanji_list.values:
        row_data = df.loc[df['kanji'] == kanji]
        row_index = row_data.index[0]
        primitive_value = row_data.loc[row_index, 'primitive']
        print("Primitive Value: " + primitive_value)
    else:
        print("Error: Kanji not found")



if __name__ == "__main__":
    run_cli()
    # check_for_characters