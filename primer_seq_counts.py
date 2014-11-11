import pprint
import re
import os
pp = pprint.PrettyPrinter(indent=4)

#------------------------------------------------------------------
#Defining the function
#------------------------------------------------------------------

def best_pos( sequence, primer):


    nr_comp = 0

    primer.upper()
    sequence.upper()


    best_score = 0
    position = []

    for i in range(0, len(sequence) - len(primer)): # -1 here to avoid going over length of i
        local_score = 0
        for j in range(0, len(primer)):

            nr_comp += 1
            if sequence[i + j] == primer[j]: #Anchors I and then loops J over I
                local_score += 1 # Append local score

        #print best_score
        if (local_score > best_score):
            position = []
            position.append( str(i) )
            best_score = local_score
        elif ( local_score == best_score): #Appends best local score to global best score.
            pass
            position.append(str(i))

    print "Comparisons : " + str(nr_comp)
    print "score:" + str(best_score) + ",".join(position)
    return (best_score, position)

# ----------- MAIN LOOP --------------


def best_pos_bounds( sequence, primer):


    nr_comp = 0

    primer.upper()
    sequence.upper()


    best_score = 0
    position = []

    for i in range(0, len(sequence) - len(primer)): # -1 here to avoid going over length of i
        local_score = 0
        for j in range(0, len(primer)):
            
            if ( best_score > len(primer) - j + local_score):
                continue

#            print "%d > %d - %d + %d" % (best_score, len(primer), j,  local_score)

            nr_comp += 1
            if sequence[i + j] == primer[j]: #Anchors I and then loops J over I
                local_score += 1 # Append local score

        #print best_score
        if (local_score > best_score):
            position = []
            position.append( str(i) )
            best_score = local_score
        elif ( local_score == best_score): #Appends best local score to global best score.
            pass
            position.append(str(i))

    print "Comparisons : " + str(nr_comp)
    print "Score: " + str(best_score) + ", - ".join(position)
    return (best_score, position)


def best_pos_by_index_seq(sequence, primer, seed_length):

    nr_comp = 0

    primer.upper()
    sequence.upper()

    best_score = 0
    position = []

    seeds = dict()

    # build the index
    for i in range(0, len(sequence) - seed_length):
        seed = sequence[ i: i + seed_length]
        if ( seed not in seeds):
            seeds[ seed ] = []

        seeds[seed].append( i )

    primer_seed = primer[0:seed_length]

    pp.pprint(seeds[ primer_seed])

    for pos in (seeds[ primer_seed]):
        local_score = 0
        for j in range(0, len(primer)):
            
#            if ( best_score > len(primer) - j + local_score):
#                continue


            nr_comp += 1
            if sequence[pos + j] == primer[j]: #Anchors I and then loops J over I
                local_score += 1 # Append local score

        #print best_score
        if (local_score > best_score):
            position = []
            position.append( str(i) )
            best_score = local_score
        elif ( local_score == best_score): #Appends best local score to global best score.
            pass
            position.append(str(i))


    print "Comparisons : " + str(nr_comp)
    return 

# ----------- MAIN LOOP --------------


best_pos("AGACCAGATCTGAGCTTGGGAGCTCTTGGCATAACTAGGGAACCACAGTTTGAAACGT", "CTTGGCATAA")
best_pos_bounds("AGACCAGATCTGAGCTTGGGAGCTCTTGGCATAACTAGGGAACCACAGTTTGAAACGT", "CTTGGCATAA")

best_pos_bounds("AGACCAGACTTGGCATAATCTGAGCTTGGGAGCTCTAGGGAACCACAGTTTGAAACGT", "CTTGGCATAA")
best_pos_by_index_seq("AGACCAGACTTGGCATAATCTGAGCTTGGGAGCTCTAGGGAACCACAGTTTGAAACGT", "CTTGGCATAA", 3)
best_pos_by_index_seq("AGACCAGACTTGGCATAATCTGAGCTTGGGAGCTCTAGGGAACCACAGTTTGAAACGT", "CTTGGCATAA", 5)
