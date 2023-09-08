from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
import re


def main():
    # ask for the id numbers
    id = list(input("List the ID numbers: "))
    # assign a key and value into the new variables
    key, value = get_seq(id)
    # using the function and key and values create a dictionary 
    # make_dictionary(key, value)
    print(key, "\n", value)
# get the sequence from the database
key = []
value = []
def get_seq(id_list): #function for get the id-s sequences 
    Entrez.email = "sviatoslavkharuk@gmail.com" 
    with Entrez.efetch(db = "protein", 
                    id = id_list,
                    rettype = "gb",
                    retmode = "text") as protein:
        for aa_record in SeqIO.parse(protein, "genbank"): # reading the sequence 
            print(f"Seq record id is: {aa_record.id}")
            print(aa_record.seq)
            seq_aa = str(aa_record.seq)
            key.append(aa_record)
            value.append(seq_aa)
            # print(len(seq_aa))
         ## maybe I should return name Id as key and sequence as value?
            return key, value

## loop for parsing and saving the sequences in dictionary
# def make_dictionary(key, value):
    





#     # save the sequence in the file for further work
#     with open("pro_seq.txt", "w+") as pro_seq: ## зберегти як словник? айді як ключ, а послідовність як значення 
#         pro_seq.write(seq_aa)

# ## maybe I do not need to have this and just have a one dictionary 
# # open file and read  
# with open("pro_seq.txt", "r") as protein:
#     reader = protein.read()
#     print(reader)


# ## rebuild on work with dictionary
# # re.expressions
# pattern = r"N[^P][ST]"

# ## loop for matches in the values

# matches = re.finditer(pattern, reader)

# for match in matches:
#     position = match.start()
#     print(position + 1, end=" ")

if __name__ == "__main__":
    main()
    

