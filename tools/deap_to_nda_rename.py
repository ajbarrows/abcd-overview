import pandas as pd
import argparse


def apply_nda_names(df: pd.DataFrame, abcd_dict: pd.DataFrame) -> pd.DataFrame:
    '''Replace new names with old.'''

    def parse_data_dictionary(abcd_dict: pd.DataFrame) -> dict:
        '''Create dictionary with new names as keys and old names as values.'''

        tmp = abcd_dict.set_index('var_name')['var_name_nda']
        tmp = tmp.dropna()

        return tmp.to_dict()
    
    rename_dict = parse_data_dictionary(abcd_dict)

    return df.rename(columns=rename_dict)


if __name__ == "__main__":

    abcd_dictpath = './abcd_5-1_dictionary.csv'

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--infile", type=str)
    parser.add_argument("-o", "--outfile", type=str)
    parser.add_argument("-d", "--dictpath", type=str, default=abcd_dictpath)

    args = parser.parse_args()

    if args.outfile:
        out_fname = args.outfile
    else:
        idx = args.infile.index(".csv")
        out_fname = args.infile[:idx] + '_renamed' + args.infile[idx:]

 
    abcd_dict = pd.read_csv(args.dictpath)
    df = pd.read_csv(args.infile)

    df = apply_nda_names(df, abcd_dict)
    df.to_csv(out_fname, index=False)



