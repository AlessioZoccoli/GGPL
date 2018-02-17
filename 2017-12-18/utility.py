from larlib import *

def SPECULAR (D):
    """
    SPECULAR(D)(pol) is just a variation of MIRROR(D)(pol) without returning the original object,
    plus the specular polyhedron is placed so that its origin equals pol origin
    :param D: direction, integer
    :param pol: polyhedron
    """
    def SPECULAR0 (pol):
        return  STRUCT([T(D)(SIZE(D)(pol))(S(D)(-1)(pol))])
    return SPECULAR0

def backFacade():
    backWallsWidth = 95.9 - 58.9
    windowSizes = [0.019999999552965164, 1.6299999952316284, 1.0299999713897705]
        
    lrSpaceX = 15.525 #it will be automatically rounded to this value (no need to to use 15.5249...)
    x = windowSizes[1]
    xRithmLeft = [lrSpaceX/3.-0.175, -x, lrSpaceX/3.+0.4, -x, 1.6900000095000003]
    
    y =  windowSizes[2]   
    yRithmLeft = [0.4, -y*3., y*3, -y, 0.39000020027000026]
    
    xVoidLeft = [-xv for xv in xRithmLeft]
    yVoidLeft = [-yv for yv in yRithmLeft]
    
    leftWall = STRUCT([
        PROD([QUOTE(xRithmLeft),QUOTE(yRithmLeft)]),
        PROD([QUOTE(xVoidLeft),QUOTE(yRithmLeft)]),
        PROD([QUOTE(xRithmLeft),QUOTE(yVoidLeft)])
        ])
    
    rightWall = SPECULAR(1)(leftWall)
    
    # Central part is more rticulate ad less symmetrical
    # I will make some more "divide et impera", dividing the central part again in three parts
    centralPartSpace = 10.35
    
    # central part : ASSE ORIZZONTALE
    # 1.6299999952316284*3 = 4.889999985694885
    # centralPartSpace - 4.889999985694885 = 5.460000014305114
    # 5.460000014305114/4 = 1.3650000035762786 (somma della superficie occupabile da muratura)
    # .3650000035762786*2
    # array delle porzioni "piene" = [1.,1.7300000071525572,1.7300000071525572,1.]
    
    #central part n1
    xRithmCentral_1 = [1.91000000834465, -x, 2.]
    yRithmCentral_1 = [0.4, -y*12./5, y*18./5, -y, 0.39000020027000026]
    xVoidCentral_1 = [-xv for xv in xRithmCentral_1]
    yVoidCentral_1 = [-xv for xv in yRithmCentral_1]
    centralPt1 = STRUCT([
        PROD([QUOTE(xRithmCentral_1),QUOTE(yRithmCentral_1)]),
        PROD([QUOTE(xVoidCentral_1),QUOTE(yRithmCentral_1)]),
        PROD([QUOTE(xRithmCentral_1),QUOTE(yVoidCentral_1)])
        ])  
    
    #central part n2
    xRithmCentral_2 = [x]
    yRithmCentral_2 = [-y*3, 4.9100000858306885]
    xVoidCentral_2 = [-xv for xv in xRithmCentral_2]
    yVoidCentral_2 = [-xv for xv in yRithmCentral_2]
    centralPt2 = STRUCT([
        PROD([QUOTE(xRithmCentral_2),QUOTE(yRithmCentral_2)]),
        PROD([QUOTE(xVoidCentral_2),QUOTE(yRithmCentral_2)]),
        PROD([QUOTE(xRithmCentral_2),QUOTE(yVoidCentral_2)])
        ])
    
    #central part n3
    xRithmCentral_3 = xRithmCentral_1[::-1]
    yRithmCentral_3 = yRithmCentral_1
    xVoidCentral_3 = [-xv for xv in xRithmCentral_3]
    yVoidCentral_3 = [-xv for xv in yRithmCentral_3]
    centralPt3 = STRUCT([
        PROD([QUOTE(xRithmCentral_3),QUOTE(yRithmCentral_3)]),
        PROD([QUOTE(xVoidCentral_3),QUOTE(yRithmCentral_3)]),
        PROD([QUOTE(xRithmCentral_3),QUOTE(yVoidCentral_3)])
    ])

    centralPart = STRUCT([centralPt1, centralPt2, centralPt3])
    return centralPart
