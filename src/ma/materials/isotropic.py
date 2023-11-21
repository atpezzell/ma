from ma.materials.mat_types import IsotropicMaterial

Al6061T6_sheet = IsotropicMaterial(
    reference = """ 
    MIL-HBDK-5J
    Table 3.6.2.0(b1). Design Mechanical and Physical Properties of 6061 Aluminum Alloy Sheet
    Specification = AMS 4025, AMS 4027 and AMS-QQ-A-250/11
    Form = Sheet
    Thickness = 0.010-0.249
    """,
    E= 9.9e6,
    nu= 0.33,
    rho= 0.098,
    alpha= 13.1e-6,
    F_ty= 35000,
    F_tu= 42000,
    F_cy= 35000,
    F_su= 27000,
    F_bru_1p5= 67000,
    F_bru_2p0= 88000,
    F_bry_1p5= 50000,
    F_bry_2p0= 58000,
)