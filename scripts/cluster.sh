#!/bin/bash

# Prompt the user for input with a custom prompt
#read -p "Max id: " max_id
read -p "Enter fasta data: " fasta_data
read -p "output file: " output_data

output_data="../data/clusters/${output_data}"


# Modify your mmseqs command with the floating-point value
mmseqs easy-cluster "$fasta_data" "$output_data" tmp --min-seq-id 0.7 -c 0.8 --cov-mode 0



#./diamond cluster -d $fasta_data -o $output_data --approx-id $((100 - max_id)) --member-cover $((110 - max_id))
