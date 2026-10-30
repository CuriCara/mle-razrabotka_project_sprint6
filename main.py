from src.reporter import *
import pandas as pd

def main():
    df = pd.read_csv("data/payments.csv")
    reporter = DataFrameReporter()

    reporter.show_report(df)

if __name__ == '__main__':
    main()
