import pandas as pd

def run_cli():
    while True:
        user_input = input("rtk-cli: ")    
        print(user_input)

def check_character():
    df = pd.read_csv("./resources/rtk2.csv") # may need objective file path 
    print(df['kanji'].size)


if __name__ == "__main__":
    check_character()
