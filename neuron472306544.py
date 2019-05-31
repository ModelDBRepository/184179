'''
Defines a class, Neuron472306544, of neurons from Allen Brain Institute's model 472306544

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472306544:
    def __init__(self, name="Neuron472306544", x=0, y=0, z=0):
        '''Instantiate Neuron472306544.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472306544_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Nr5a1-Cre_Ai14_IVSCC_-177834.02.01.01_471678482_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472306544_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 69.59
            sec.e_pas = -92.3040847778
        for sec in self.apic:
            sec.cm = 3.32
            sec.g_pas = 5.53024413679e-05
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000543836758861
        for sec in self.dend:
            sec.cm = 3.32
            sec.g_pas = 7.21843220556e-05
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.00191334
            sec.gbar_Ih = 2.44044e-09
            sec.gbar_NaTs = 0.421007
            sec.gbar_Nap = 0.000356633
            sec.gbar_K_P = 0.000650387
            sec.gbar_K_T = 0.000211966
            sec.gbar_SK = 0.000185708
            sec.gbar_Kv3_1 = 0.09298
            sec.gbar_Ca_HVA = 0.000579632
            sec.gbar_Ca_LVA = 0.00536169
            sec.gamma_CaDynamics = 0.00324249
            sec.decay_CaDynamics = 344.751
            sec.g_pas = 0.000127994
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

