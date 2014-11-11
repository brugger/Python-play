print "hello world!"

#------------------------------------------------------------------
#Defining the function
#------------------------------------------------------------------

def best_pos( sequence, primer):

    primer.upper()
    sequence.upper()


    best_score = 0
    position = []

    for i in range(0, len(sequence) - len(primer)): # -1 here to avoid going over length of i
        local_score = 0
        for j in range(0, len(primer)):
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

#    print "score:" + str(best_score) + ",".join(str(position))
    return (best_score, position)

#------------------------------------------------------------------
#Looping through inputs
#------------------------------------------------------------------
import sys
import re
import pprint




def readin_fasta(file):

    infile = open(file, 'rU')

    res = []

    seq_name = ""
    seq      = ""

    for line in infile:

        line = line.strip("\n")


        if (  re.match(r'\>', line)):
            line = re.sub(r'\>', "", line)
            if ( seq_name ):
                res.append( [seq_name, seq] )
                #res[ seq_name ] = seq

            seq = ""
            seq_name = line
        else:
            seq += line

    if ( seq_name ):
        res.append( [seq_name, seq] )

    pprint.pprint( res )

    return res

# ----------- MAIN LOOP --------------


references = readin_fasta(sys.argv[ 1 ])
primers    = readin_fasta(sys.argv[ 2 ])

for reference in references:
    [ref_name, ref_seq] = reference
    for primer in primers:
        [primer_name, primer_seq] = primer

        (score, pos) = best_pos(ref_seq, primer_seq)
        print "%s vs %s (score: %d) (pos :%s)" % (ref_name, primer_name, score, "-".join(pos))
