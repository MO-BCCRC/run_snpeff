'''
Created on Apr 29, 2014

@author: jrosner
'''
input_params = {'genome_version':'GRCh37.66',
                'around':'__FLAG__',
                'interval':None,
                'chr':None,
                'threads':None,
                'input_format':'vcf',
                'output_format':'vcf',
                'snp':'__FLAG__',
                'nmp':'__FLAG__',
                'het':'__FLAG__',
                'hom':'__FLAG__',
                'ins':'__FLAG__',
                'minQ':None,
                'maxQ':None,
                'minC':None,
                'maxC':None,
                'no_downstream':'__FLAG__',
                'no_intergenic':'__FLAG__',
                'no_intron':'__FLAG__',
                'no_upstream':'__FLAG__',
                'no_utr':'__FLAG__',
                'canon':'__FLAG__',
                'onlyReg':'__FLAG__',
                'reg':None,
                'treatAllAsProteinCoding':None,
                'upDownStreamLen':None,
                'zero':'__FLAG__',
                'one':'__FLAG__',
                'inOffset':'__FLAG__',
                'outOffset':'__FLAG__',
                'noLog':'__FLAG__',
                'noStats':True,
                'quiet':'__FLAG__',
                'verbose':'__FLAG__',
                'download':'__FLAG__',
                'cvsStats':'__FLAG__',
                'del':'__FLAG__',
                'filterInterval':None,
                'no':None,
                'cancer':'__FLAG__',
                'cancerSamples':None,
                'geneId':'__FLAG__',
                'hgvs':'__FLAG__',
                'lof':'__FLAG__',
                'oicr':'__FLAG__',
                'sequenceOntology':'__FLAG__',
                'debug':'__FLAG__',
                'dataDir':None,
                'help':'__FLAG__',
                'motif':'__FLAG__'
                }

input_files  = {'config':'snpEff_3_6/snpEff.config',
                'variants_file':'__REQUIRED__'
                }
output_files = {'out':'__REQUIRED__', 'stats':'snpEff_summary.html'}
return_value = []

