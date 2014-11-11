#!/usr/bin/python



def seq_reverse(sequence):

	rev_sequence = []

	dna_dict = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}

	for base in sequence:
		if base in dna_dict.keys():
			rev_sequence.append(dna_dict[base])
		else:
			rev_sequence.append(base)

	"".join(rev_sequence)

	trev_sequence = rev_sequence[::-1]		

	
	return "".join(trev_sequence)


print "hello world"
print seq_reverse("AATTNCCGG")

