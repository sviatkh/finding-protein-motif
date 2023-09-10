from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
import re


def main():
    # ask for the id numbers
    id_list = input("Enter a Id number: ").strip().split()
    # assign a key and value into the new variables
    key_list, value_list = get_seq(id_list)
    # using the function and key and values create a dictionary 
    make_dictionary(key_list, value_list)

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
id_dictionary = {}
def make_dictionary(key_list, value_list):
     for key in key_list:
          for value in value_list:
               id_dictionary[key] = value

# ## rebuild to work with dictionary
# # re.expressions for searching the protein motif
# pattern = r"N[^P][ST]"

# ## loop for matches in the values

# matches = re.finditer(pattern, reader)

# for match in matches:
#     position = match.start()
#     print(position + 1, end=" ")

if __name__ == "__main__":
    main()
    

