
#Importations des librairies
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio import SeqIO

# Variables à définir
fasta_file = "scaffolds.fasta"  # Fichier FASTA contenant les contigs
gene_fasta = "gene-Repl.fasta"   # Fichier FASTA contenant la séquence du gène d'intérêt
output_file = "contig_with_gene.fasta"  # Fichier de sortie contenant le contig

# Exécuter BLAST pour trouver le contig contenant le gène
blast_output = "blast_result.xml"
blastn_cline = NcbiblastnCommandline(query=gene_fasta, subject=fasta_file, outfmt=5, out=blast_output)
stdout, stderr = blastn_cline()

# Parser les résultats BLAST pour récupérer le contig d'intérêt
from Bio.Blast import NCBIXML

with open(blast_output) as result_handle:
    blast_records = NCBIXML.parse(result_handle)
    for blast_record in blast_records:
        if blast_record.alignments:
            contig_id = blast_record.alignments[0].hit_id
            break

# Extractio du contig contenant le gène repL du fichier FASTA
contig_found = False
with open(fasta_file, "r") as input_handle:
    for record in SeqIO.parse(input_handle, "fasta"):
        if record.id == contig_id:
            with open(output_file, "w") as output_handle:
                SeqIO.write(record, output_handle, "fasta")
                contig_found = True
            break

if contig_found:
    print(f"Le contig contenant le gène repL a été écrit dans {output_file}")
else:
    print("Aucun contig correspondant n'a été trouvé.")
