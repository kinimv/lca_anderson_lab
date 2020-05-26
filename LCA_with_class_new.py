class tax_list:
    # This comprises of two lists of all tax ids (along with parent) and tax id names
    # These are the linked lists
    tax_ids = []
    parent_tax_ids = []

    tax_ids_names = []
    names_list = []

    def __init__(self, tax_id_file, tax_names_file):
        # Initializing and reading files
        f = open(tax_id_file, 'r')
        lines = f.readlines()
        for x in lines:
            self.tax_ids.append(int(x.split('\t|')[0]))
            self.parent_tax_ids.append(int(x.split('\t|\t')[1]))
        f.close()

        f = open(tax_names_file, 'r')
        lines = f.readlines()
        for x in lines:
            self.tax_ids_names.append(int(x.split('\t|')[0]))
            self.names_list.append(x.split('\t|\t')[1])
        f.close()

    def get_tax_id(self, name):
        # Returns a tax id for a given name. It uses linked lists of all tax ids and names
        if name not in self.names_list:
            return "error"
        else:
            i = self.names_list.index(name)
            return int(self.tax_ids_names[i])

    def get_tax_name(self, id):
        # Returns a tax name for a given tax id. It uses linked lists of all tax ids and names
        if id not in self.tax_ids_names:
            return "error"
        else:
            return self.names_list[self.tax_ids_names.index(id)]

    def get_anc_tree(self, name):
        # This builds and returns a tree (list) of all ancestors upto root
        if name not in self.names_list:
            return "error"
        else:
            anc = []
            i = self.names_list.index(name)
            id = int(self.tax_ids_names[i])
            anc.append(id)

            p = id
            while p != 1:
                i = self.tax_ids.index(p)
                p = self.parent_tax_ids[i]
                anc.append(p)
        return anc


print("This program shows you the least common ancestor of two organisms")
# Build the taxnomy database in memory as an object - taxdb
print("Loading databases...")
taxdb = tax_list('nodes.dmp', 'names.dmp')

cont = True
while cont:
    # Input of organism 1
    while True:
        # Eg. H1N1 swine influenza virus
        org1 = str(input("Enter name of the first organism, Enter 'exit' to exit the program: "))
        if org1 == "exit":
            exit()
        # Search input in the taxlist
        if taxdb.get_tax_id(org1) == "error":
            print('Organism name: ', org1, ' not found in NIH database. Please try again')
        else:
            break
        pass

    # Input of organism 2
    while True:
        # Eg. Middle East respiratory syndrome-related coronavirus
        org2 = str(input("Enter name of the second organism, Enter 'exit' to exit the program: "))
        if org2 == "exit":
            exit()
        # Search input in the taxlist
        if taxdb.get_tax_id(org2) == "error":
            print('Organism name: ', org2, ' not found in NIH database. Please try again')
        else:
            break
        pass

    # Building the ancestor trees for the two organisms
    anc1_tree = taxdb.get_anc_tree(org1)
    anc2_tree = taxdb.get_anc_tree(org2)

    # Create a list the shows the path down the tree by reversing the chains
    org1_tree, org2_tree = anc1_tree[::-1], anc2_tree[::-1]

    # Finds the common element (ancestor) by intersecting two ancestor lists
    anc = list(set(org1_tree).intersection(set(org2_tree)))
    lca_ind = len(anc) - 1
    lca = org1_tree[len(anc) - 1]

    print("Least Common Ancestor is: ", taxdb.get_tax_name(org1_tree[lca_ind]))

    # Prints the links to the common ancestor with nicely formatted columns
    print()
    print("Ancestor Tree:")
    print("%30s %s" % (org1_tree[lca_ind], taxdb.get_tax_name(org1_tree[lca_ind])))
    for i in range(lca_ind+1, min(len(org1_tree), len(org2_tree))):
        print("%-50s %s" % ((str(org1_tree[i]) + " " + taxdb.get_tax_name(org1_tree[i])),
                            (str(org2_tree[i]) + " " + taxdb.get_tax_name(org2_tree[i]))))
    if len(org1_tree) > len(org2_tree):
        for i in range(len(org2_tree), len(org1_tree)):
            print((str(org1_tree[i]) + " " + taxdb.get_tax_name(org1_tree[i])))
    if len(org2_tree) > len(org1_tree):
        for i in range(len(org1_tree), len(org2_tree)):
            print("%-50s %s" % (" ", (str(org2_tree[i]) + " " + taxdb.get_tax_name(org2_tree[i]))))

    # Prompts whether to repeat the operation
    repeat = input("Do you want to continue? Enter 'Yes' or 'No': ").lower()
    if repeat == 'yes':
        pass
    elif repeat == 'no':
        cont = False
