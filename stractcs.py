def Read_FastA_Names_And_Sequences(filepath):
    # =====================================================================
    # Return a tuple composed of two lists: �sequence_names� and �sequences�
    # that contain the sequence_names and sequences read from the downloaded
    # fastA file.  The sequence_names list must contain string elements
    # corresponding to each name, and the sequences list must contain string
    # elements corresponding to each sequence.  The string elements may not
    # contain spaces, newline or �>� characters. #=====================================================================

    # *********************************************************************
    text = open("/Users/hannobrandt/PycharmProjects/project_324/" + filepath + ".txt", "r")
    text_lines = text.readlines()
    sequence_names = []
    sequences = []
    string = str()
    tuple = (sequence_names, sequences)
    empty_line = 0
    for line in text_lines:
       # print(tuple)

        if line.startswith(">" or ""):


            if string != "":
                #print(string)
                sequences.append(string)
                #print(sequences)
                string = str()


            line = line[1:-1]
            line = line.strip()
            #print(line)
            sequence_names.append(line)
            #print(sequence_names)

        else:
            #print(line)


            line = line.strip()
            string += line
            #print(string)



    print(tuple)




    # *********************************************************************

    return ((sequence_names, sequences))


filepath = str("demo_fasta_file_2018.fsa")
# number_of_sequences = Number_Of_Sequences(filepath)
# print("Number of sequences =",number_of_sequences)
sequence_names, sequences = Read_FastA_Names_And_Sequences(filepath)
# AT_Percentage = AT_Percentage(sequences)
for i in range(0, 4):
    print(sequence_names[i], '\n', sequences[i], '\n')
print('done...')

