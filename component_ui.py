# -*- coding: utf-8 -*-
'''
Created on 08 April 2014 (Tuesday)

@author: jrosner
'''

import sys
import argparse

__version__ = 'SnpEff 3.6b (build 2014-05-01)'

# Usage: snpEff [eff] genome_version [variants_file]

#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(prog='snpeff',
                                 description='''Genetic variant annotation and effect
                                 prediction toolbox. It annotates and predicts the
                                 effects of variants on genes (such as amino acid changes)''',
                                 epilog='''Input file: Default is STDIN''')

# required arguments
required_arguments = parser.add_argument_group("Required arguments")

required_arguments.add_argument("--out",
                               default=None,
                               required=True,
                               help='''specify the path/to/out.vcf to save output to a file''')

# mandatory / positional arguments
required_arguments.add_argument("genome_version",
                               choices=['GRCh37.66'],
                               help='''genomic build version''')

required_arguments.add_argument("variants_file",
                               help='''file containing variants''')


# optional options
optional_options = parser.add_argument_group("Options")

optional_options.add_argument("-a", "--around",
                              default=False, action="store_true",
                              help='''Show N codons and amino acids around change
                              (only in coding regions). Default is 0 codons.''')

optional_options.add_argument("-i", "--input-format",
                              default='vcf',
                              choices=['vcf', 'txt', 'pileup', 'bed'],
                              help='''Input format''')

optional_options.add_argument("-o", "--output_format",
                              default='vcf',
                              choices=['txt', 'vcf', 'bed', 'bedAnn'],
                              help='''Output format''')

optional_options.add_argument("--chr",
                              help='''Prepend 'string' to chromosome name (e.g. 'chr1'
                              instead of '1'). Only on TXT output.''')

optional_options.add_argument("-s", "--stats",
                              default='snpEff_summary.html',
                              help='''Name of stats file (summary)''')

optional_options.add_argument("--noStats",
                             default=True, action="store_true",
                             help='''Do not create stats (summary) file''')

optional_options.add_argument("--download",
                             default=False, action="store_true",
                             help='''Download reference genome if not available. Default: False''')

optional_options.add_argument("--fileList",
                             default=False, action="store_true",
                             help='''Input actually contains a list of files to process''')

optional_options.add_argument("--csvStats",
                             default=False, action="store_true",
                             help='''Create CSV summary file instead of HTML''')


# Sequence change filter options
seq_change_filter_options = parser.add_argument_group("Sequence change filter options")

seq_change_filter_options.add_argument("--snp",
                                       default=False, action="store_true",
                                       help='''Only SNPs (single nucleotide polymorphisms''')

seq_change_filter_options.add_argument("--nmp",
                                       default=False, action="store_true",
                                       help='''Only MNPs (multiple nucleotide polymorphisms)''')

seq_change_filter_options.add_argument("--het",
                                       default=False, action="store_true",
                                       help='''Analyze heterozygous variants only''')

seq_change_filter_options.add_argument("--hom",
                                       default=False, action="store_true",
                                       help='''Analyze homozygous variants only''')

seq_change_filter_options.add_argument("--del",
                                       default=False, action="store_true",
                                       help='''Analyze deletions only''')

seq_change_filter_options.add_argument("--ins",
                                       default=False, action="store_true",
                                       help='''Analyze insertions only''')

seq_change_filter_options.add_argument("--minQ",
                                       metavar='X',
                                       help='''Filter out variants with quality lower than X''')

seq_change_filter_options.add_argument("--maxQ",
                                       metavar='X',
                                       help='''Filter out variants with quality higher than X''')

seq_change_filter_options.add_argument("--minC",
                                       metavar='X',
                                       help='''Filter out variants with coverage lower than X''')

seq_change_filter_options.add_argument("--maxC",
                                       metavar='X',
                                       help='''Filter out variants with coverage higher than X''')


# Results filter options
results_filter_options = parser.add_argument_group("Results filter options")

results_filter_options.add_argument("--no_downstream",
                                    default=False, action="store_true",
                                    help='''Do no show DOWNSTREAM changes''')

results_filter_options.add_argument("--no_intergenic",
                                    default=False, action="store_true",
                                    help='''Do no show INTERGENIC changes''')

results_filter_options.add_argument("--no_intron",
                                    default=False, action="store_true",
                                    help='''Do no show INTRON changes''')

results_filter_options.add_argument("--no_upstream",
                                    default=False, action="store_true",
                                    help='''Do no show UPSTREAM changes''')

results_filter_options.add_argument("--no_utr",
                                    default=False, action="store_true",
                                    help='''Do no show 5_PRIME_UTR or 3_PRIME_UTR changes''')

results_filter_options.add_argument("--filterInterval",
                                  metavar='<file>', action="append",
                                  help='''Only analyze changes that intersect with the intervals
                                  specified in this file (you may use this option many times)''')

results_filter_options.add_argument("--no",
                                  metavar='<EffectType>', action="append",
                                  help='''Do not show 'EffectType'. This option
                                  can be used several times''')


# Annotations options
annotations_options = parser.add_argument_group("Annotations options")
annotations_options.add_argument("--cancer",
                                  default=False, action="store_true",
                                  help='''Perform 'cancer' comparisons (Somatic vs Germline)''')

annotations_options.add_argument("--cancerSamples",
                                  metavar='<file>',
                                  help='''Two column TXT file defining
                                  'oringinal \t derived' samples''')

annotations_options.add_argument("--geneId",
                                  action="store_true",
                                  help='''Use gene ID instead of gene name (VCF output)''')

annotations_options.add_argument("--hgvs",
                                  action="store_true",
                                  help='''Use HGVS annotations for amino acid sub-field''')

annotations_options.add_argument("--lof",
                                  action="store_true",
                                  help='''Add loss of function (LOF) and Nonsense
                                  mediated decay (NMD) tags''')

annotations_options.add_argument("--oicr",
                                  action="store_true",
                                  help='''Add OICR tag in VCF file''')

annotations_options.add_argument("--sequenceOntology",
                                  action="store_true",
                                  help='''Use Sequence Ontology terms''')

# Database options
database_options = parser.add_argument_group("Database options")
database_options.add_argument("--canon",
                                  default=False, action="store_true",
                                  help='''Only use canonical transcripts''')

database_options.add_argument("--upDownStreamLen",
                                  metavar='<int>',
                                  help='''Set upstream downstream interval length (in bases)''')

database_options.add_argument("--onlyReg",
                                  default=False, action="store_true",
                                  help='''Only use regulation tracks''')

database_options.add_argument("--reg",
                                  metavar='<name>', action="append",
                                  help='''Regulation track to use''')

database_options.add_argument("--interval", action='append',
                              help='''Use a custom interval file
                              (you may use this option many times)''')

database_options.add_argument("--motif",
                                  action="store_true",
                                  help='''Annotate using motifs (requires Motif database)''')

database_options.add_argument("--nextProt",
                                  action="store_true",
                                  help='''Annotate using NextProt (requires NextProt database)''')

database_options.add_argument("--onlyTr",
                                  metavar="<file.txt>",
                                  help='''Only use the transcripts in this file.
                                  Format: One transcript ID per line''')

database_options.add_argument("--spliceSiteSize",
                                  metavar='<int>',
                                  help='''Set size for splice sites (donor and acceptor) in bases.
                                  Default: 2''')

# Generic options
generic_options = parser.add_argument_group("Generic options")

generic_options.add_argument("--inOffset",
                             default=False, action="store_true",
                             help='''Offset input by a number of bases.
                             E.g. '-inOffset 1' for one-based input files''')

generic_options.add_argument("--outOffset",
                             default=False, action="store_true",
                             help='''Offset output by a number of bases.
                             E.g. '-outOffset 1' for one-based output files''')

generic_options.add_argument("--noLog",
                             default=False, action="store_true",
                             help='''Do not report usage statistics to server''')

generic_options.add_argument("-t", "--threads",
                              default='off',
                              help='''Use multiple threads (implies '-noStats').''')

generic_options.add_argument("-q", "--quiet",
                             default=False, action="store_true",
                             help='''Quiet mode (do not show any messages or errors)''')

generic_options.add_argument("--verbose",
                             default=False, action="store_true",
                             help='''verbose''')

generic_options.add_argument("-c", "--config",
                               default='./snpEff_3_6/snpEff.config',
                               help='''specify the path/to/snpEff.config file''')

generic_options.add_argument("--debug",
                             action="store_true",
                             help='''debug mode, very verbose''')

generic_options.add_argument("--dataDir",
                             metavar='<path>',
                             help='''debug mode, very verbose''')



args, unknown = parser.parse_known_args()

# ensure stats logging is deactivated for multiple threads
if args.threads:
    args.noStats = False

# prepending 'chr' only allowed on TXT output
if args.chr and (args.output_format == 'txt'):
    parser.print_help()
    print '''Only prepend 'chr' string with TXT output.'''
    sys.exit()
