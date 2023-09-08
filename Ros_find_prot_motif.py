from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
import re


def main():
    # ask for the id numbers
    id_list = input("Enter a Id number: ").strip().split()
    # assign a key and value into the new variables
    key, value = get_seq(id_list)
    print(key, value)
    # using the function and key and values create a dictionary 

def get_seq(id_list): #function for get the id-s sequences 
    Entrez.email = "sviatoslavkharuk@gmail.com" 
    with Entrez.efetch(db = "protein", 
                    id = id_list,
                    rettype = "gb",
                    retmode = "text") as protein:
            aa_records = list(SeqIO.parse(protein, "genbank")) # convert to list for later use list comrehensions
            key = [aa_record.id for aa_record in aa_records]
            value = [str(aa_record.seq) for aa_record in aa_records]
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
    

