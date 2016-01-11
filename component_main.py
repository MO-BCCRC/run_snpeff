'''
Created on Apr 8, 2014

@author: jrosner
'''

import os
from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    Run snpEff, load dependencies and requirements
    '''

    def __init__(self, component_name='run_snpeff', component_parent_dir=None, seed_dir=None):
        self.version = ""

         ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)


    def make_cmd(self, chunk=None):
        '''
        generate the snpEff command
        '''

        java_mem = '-Xmx3072M'
        java_jar_option = '-jar'
        snpeff_jar = os.path.join(self.seed_dir, 'snpEff_3_6', 'snpEff.jar')
        snpeff_config_option = '-c'

        if not os.path.isfile(self.args.config):
            snpeff_config = os.path.join(self.seed_dir, self.args.config)
        else:
            snpeff_config = self.args.config

        snpeff_outfile =  '> ' + self.args.out

        cmd = self.requirements['java']
        cmd_args = [
            java_mem,
            java_jar_option,
            snpeff_jar,
            snpeff_config_option,
            snpeff_config,
            self.args.genome_version,
            self.args.variants_file,
            snpeff_outfile
        ]

        return cmd, cmd_args


# to run as stand alone
def _main():
    '''main function'''
    snpeff = Component()
    snpeff.args = component_ui.args
    snpeff.run()


if __name__ == '__main__':
    import component_ui

    _main()
