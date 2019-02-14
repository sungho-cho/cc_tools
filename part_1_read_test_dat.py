import cc_dat_utils

#Part 1
input_dat_file = "data/pfgd_test.dat"

#Use cc_dat_utils.make_cc_data_from_dat() to load the file specified by input_dat_file
#print the resulting data



if __name__ == '__main__':
    # Reading from input dat file
    dat_file = "data/pfgd_test.dat"
    result = cc_dat_utils.make_cc_data_from_dat(dat_file)

    # Writing spring representation to outfile
    outfile = "data/pfgd_test.txt"
    f = open(outfile,"w")
    f.write(str(result))
    f.close()
