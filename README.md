<h3>collapse_dup_seqs.py</h3>
Collapses duplicate haplotypes in an input fasta file.

<h3>SLiM Files</h3>
<i>neutral_model.slim</i> represents the actual neutral SLiM model of DFT1 evolution. <i>devil_protein_coding_CDS_SLiM_ref.fa.gz</i> contains all ~19k devil protein coding CDSs arranged contiguously on a single chromosome is used by the neutral SLiM model to explicitly evolve DFT1 CDSs. <i>devil_protein_coding_CDS_SLiM_ref_locus_map.tsv</i> defines gene CDS ranges within the SLiM reference fasta (e.g., all contiguous CDSs of ENSSHAG00000026811 are at locus A:1-2013 on the + strand).
