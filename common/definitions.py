from collections import OrderedDict

AMINO_ACIDS = OrderedDict([
        ('A', 'Ala'),
        ('C', 'Cys'),
        ('D', 'Asp'),
        ('E', 'Glu'),
        ('F', 'Phe'),
        ('G', 'Gly'),
        ('H', 'His'),
        ('I', 'Ile'),
        ('K', 'Lys'),
        ('L', 'Leu'),
        ('M', 'Met'),
        ('N', 'Asn'),
        ('P', 'Pro'),
        ('Q', 'Gln'),
        ('R', 'Arg'),
        ('S', 'Ser'),
        ('T', 'Thr'),
        ('V', 'Val'),
        ('W', 'Trp'),
        ('Y', 'Tyr'),
        ('B', 'Asx'),
        ('Z', 'Glx'),
        ('J', 'Xle'),
        ('X', 'Xaa'),
    ])

AMINO_ACID_GROUPS = OrderedDict([
        ('hp',     ('A', 'C', 'F', 'I', 'L', 'M', 'P', 'V', 'W', 'Y')),
        ('alhp',   ('A', 'C', 'I', 'L', 'M', 'P', 'V')),
        ('arhp',   ('F', 'W', 'Y')),
        ('ar',     ('F', 'H', 'W', 'Y')),
        ('pol',    ('D', 'E', 'H', 'K', 'N', 'Q', 'R', 'S', 'T')),
        ('hb',     ('D', 'E', 'H', 'K', 'N', 'Q', 'R', 'S', 'T', 'W', 'Y')),
        ('hbd',    ('H', 'K', 'N', 'Q', 'R', 'S', 'T', 'W', 'Y')),
        ('hba',    ('D', 'E', 'H', 'N', 'Q', 'S', 'T', 'Y')),
        ('charge', ('D', 'E', 'H', 'K', 'R')),
        ('neg',    ('D', 'E')),
        ('pos',    ('H', 'K', 'R')),
        ('lar',    ('E', 'F', 'H', 'K', 'Q', 'R', 'W', 'Y')),
        ('sma',    ('A', 'C', 'D', 'G', 'N', 'P', 'S', 'T', 'V')),
        ('any',    ()),
        ('custom', ()),
    ])

AMINO_ACID_GROUP_NAMES = OrderedDict([
        ('hp',     'Hydrophobic - All'),
        ('alhp',   'Hydrophobic - Aliphatic'),
        ('arhp',   'Hydrophobic - Aromatic'),
        ('ar',     'Aromatic'),
        ('pol',    'Polar'),
        ('hb',     'H-Bonding'),
        ('hbd',    'H-Bond Donor'),
        ('hba',    'H-Bond Acceptor'),
        ('charge', 'Charge'),
        ('neg',    'Negative charge'),
        ('pos',    'Positive charge'),
        ('lar',    'Large'),
        ('sma',    'Small'),
        ('any',    'Any feature'),
        ('custom', 'Custom'),
    ])

DESIGN_SUBSTITUTION_MATRIX = OrderedDict([
        ('hydrophobic', {
            #'A':[[['L','V','I']],['Increase size to "block" binding']],
            'C':[['A'],['Remove vdW interactions (and polar)']],
            'F':[['A'],['Remove vdW interaction possibility']],
            'I':[['A'],['Remove vdW interaction possibilities']],
            'L':[['A'],['Remove vdW interaction possibilities']],
            'M':[['A'],['Remove vdW interaction possibilities']],
            #'P':[['A'],['Remove vdW interactions / change the shape of the site Normaly Prolines have a structural role and are dangerous to tamper with']],
            'V':[['A'],['Remove vdW interaction possibility']],
            'R':[['A'],['Remove vdW interaction possibility']],
            'N':[['A'],['Remove vdW interaction possibility']],
            'D':[['A'],['Remove vdW interaction possibility']],
            'Q':[['A'],['Remove vdW interaction possibility']],
            'E':[['A'],['Remove vdW interaction possibility']],
            'H':[['A'],['Remove vdW interaction possibility']],
            'K':[['A'],['Remove vdW interaction possibility']],
            'T':[['A'],['Remove vdW interaction possibility']],
            'W':[['A'],['Remove vdW interaction possibility']],
            'Y':[['A'],['Remove vdW interaction possibility']],
            }
        ),
        ('aromatic', { #same for all types of aromatic interactions #fixme check aro_ion 
            'Y':[[['L','M'],'A'],['Remove aromatic and polar interaction possibilities while retaining vdW interaction possibilities','Remove polar, aromatic and vdW interaction possibilities']],
            'W':[[['L','M'],'A','H'],['Remove aromatic and polar interaction possibilities while retaining vdW interaction possibilities','Remove polar, aromatic and vdW interaction possibilities','Weaken aromatic interaction possibilities while retaining polar interaction possibilities']],
            'F':[[['L','M'],'A','Y'],['Remove aromatic interaction possibilities while retaining vdW interaction possibilities','Remove aromatic and vdW interaction possibilities','Prevent Phe-edge to ligand-face aromatic interaction (Should only be attempted when based on a detailed binding mode hypothesis showing the aromatic interaction in question.)']],
            'H':[['A','N',['L','M']],['Remove polar, aromatic and vdW interaction possibilities','Remove aromatic interaction possibilities while retaining polar interaction possibilities','Remove aromatic and polar interaction possibilities while retaining vdW interaction possibilities']],
            }
        ),
        ('polar', { #same for all types of polar interactions
            'D':[['L','A'],['Remove polar interaction possibility, while retaining vdW interaction possibilities','Remove polar interaction possibility']],
            'E':[[['L','M'],'A'],['Remove polar interaction possibility, while retaining vdW interaction possibilities','Remove polar and vdW interaction possibility']],
            'H':[[['L','M'],'A','F'],['Remove aromatic and polar interaction possibilities while retaining vdW interaction possibilities','Remove polar, aromatic and vdW interaction possibilities','Remove polar interaction possibility, while retaining aromatic interaction possibilities']],
            'K':[['M','A'],['Remove polar interaction possibility, while retaining vdW interaction possibilities','Remove polar and vdW interaction possibility']],
            'N':[['L','A'],['Remove polar interaction possibility, while retaining vdW interaction possibilities','Remove polar and vdW interaction possibility']],
            'Q':[[['L','M'],'A'],['Remove polar interaction possibility, while retaining vdW interaction possibilities','A - remove the side chain and all interactions']],
            'R':[[['L','M'],'A'],['Remove polar interaction possibility, while retaining vdW interaction possibilities','Remove polar and vdW interaction possibility']],
            'S':[['A'],['Remove polar interaction possibility']],
            'T':[['A','V'],['Remove polar and vdW interaction possibility','Remove polar interaction possibility, while retaining vdW interaction possibilities']],
            'W':[['F','A',['L','M']],['Remove polar interaction possibility, while retaining aromatic interaction possibilities','Remove polar, aromatic and vdW interaction possibilities','Remove aromatic and polar interaction possibilities while retaining vdW interaction possibilities']],
            'Y':[['F','A',['L','M']],['Remove polar interaction possibility, while retaining aromatic interaction possibilities (Aromatic interaction cannot be investigated independently from h-bond as none of the polar residues can confromationally match the Tyr OH)','Remove polar, aromatic and vdW interaction possibilities','Remove aromatic and polar interaction possibilities while retaining vdW interaction possibilities']],
            }
        ),
        ('unknown', { #empty
            }
        ),
        ('steric', {
            'A':[[['L','V']],['Increase size to block the binding site']],
            'C':[[['L','I']],['Increase size to block the binding site']],
            'G':[[['A','V','M']],['Add side chain to block the binding site (Glycines are often structurally important and should be mutated with causion - unless closely related receptors show different residues in equivalent position.)']],
            'S':[['L','M'],['Increase size to block the binding site']],
            'T':[['L','M'],['Increase size to block the binding site']], 
            'P':[['L','M'],['Increase size to block the binding site (Prolines are often structurally important and should be mutated with causion - unless closely related receptors show different residues in equivalent position.)']],     
        })
    ])

AMINO_ACID_GROUP_NAMES = OrderedDict([
        ('hp',     'Hydrophobic - All'),
        ('alhp',   'Hydrophobic - Aliphatic'),
        ('arhp',   'Hydrophobic - Aromatic'),
        ('ar',     'Aromatic'),
        ('pol',    'Polar'),
        ('hb',     'H-Bonding'),
        ('hbd',    'H-Bond Donor'),
        ('hba',    'H-Bond Acceptor'),
        ('charge', 'Charge'),
        ('neg',    'Negative charge'),
        ('pos',    'Positive charge'),
        ('lar',    'Large'),
        ('sma',    'Small'),
        ('any',    'Any feature'),
        ('custom', 'Custom'),
    ])

G_PROTEIN_SEGMENTS = OrderedDict([
        ('Full', ['HN','hns1','S1','s1h1','H1','h1ha','HA','hahb','HB','hbhc','HC','hchd','HD','hdhe','HE','hehf','HF','hfs2','S2','s2s3','S3','s3h2','H2','h2s4','S4','s4h3','H3','h3s5','S5','s5hg','HG','hgh4','H4','h4s6','S6','s6h5','H5']),
        ('Structured', ['HN','S1','H1','HA','HB','HC','HD','HE','HF','S2','S3','H2','S4','H3','S5','HG','H4','S6','H5']),
    ])