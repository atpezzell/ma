class IsotropicMaterial:
    def __init__(self,
                 reference,
                 E=None,
                 nu=None,
                 rho=None,
                 alpha=None,
                 F_ty=None,
                 F_tu=None,
                 F_su=None,
                 F_cy=None,
                 F_cu=None,
                 F_bry_1p5=None,
                 F_bru_1p5=None,
                 F_bry_2p0=None,
                 F_bru_2p0=None,
                 ):
        
        self.reference = reference
        self.E = E
        self.nu = nu
        self.rho = rho
        self.G = self.E / (2*(1 + self.nu))
        self.alpha = alpha
        self.F_ty = F_ty
        self.F_tu = F_tu
        self.F_su = F_su
        self.F_cy = F_cy
        self.F_cu = F_cu
        self.F_bry_1p5 = F_bry_1p5
        self.F_bru_1p5 = F_bru_1p5
        self.F_bry_2p0 = F_bry_2p0
        self.F_bru_2p0 = F_bru_2p0

    def __str__(self):

        x = 'Reference \n'
        x += '------------\n'
        x += '{}\n'.format(self.reference)
        x += 'Basic properties\n'
        x += '------------\n'        
        x += 'Elastic modulus : {}\n'.format(self.E)
        x += 'Poisson ratio : {}\n'.format(self.nu)
        x += 'Density : {}\n'.format(self.rho)
        x += 'Bulk modulus : {}\n'.format(round(self.G, 4))
        x += 'CTE : {}\n'.format(self.alpha)
        x += '\nStrength\n'
        x += '------------\n'
        x += 'Yield tensile strength (F_ty) : {}\n'.format(self.F_ty)
        x += 'Ultimate tensile strength (F_tu) : {}\n'.format(self.F_tu)
        x += 'Yield compressive strength (F_cy) : {}\n'.format(self.F_cy)
        x += 'Ultimate compressive strength (F_cu) : {}\n'.format(self.F_cu)        
        x += 'Bearing yield strength, e/D=1.5 (F_bry_1p5) : {}\n'.format(self.F_bry_1p5)        
        x += 'Bearing ultimate strength, e/D=1.5 (F_bru_1p5) : {}\n'.format(self.F_bru_1p5)
        x += 'Bearing yield strength, e/D=2.0 (F_bry_2p0) : {}\n'.format(self.F_bry_2p0)        
        x += 'Bearing ultimate strength, e/D=2.0 (F_bru_2p0) : {}\n'.format(self.F_bru_2p0)                 

        return x