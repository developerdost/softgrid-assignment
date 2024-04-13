import sys
import pandas


if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except IndexError:
        print('No file selected')
        sys.exit(0)

    try:
        # Read csv file
        df = pandas.read_csv(file_name)
    except FileNotFoundError:
        print('File Not Found !')
        sys.exit(0)

    # Get the 2nd column name
    second_index = df.keys()[1]

    # Sort the dataframe in decending order based on 2nd column
    sorted_df = df.sort_values(by=[second_index], ascending=False)

    # Generate new csv file
    sorted_df.to_csv('output.csv')

    print('File generated successfully.')