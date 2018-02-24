//Maya ASCII 2016ff07 scene
//Name: soccerBall.ma
//Last modified: Mon, Apr 04, 2016 01:12:34 AM
//Codeset: 932
requires maya "2016ff07";
requires -dataType "byteArray" "Mayatomr" "2016.0 - 3.13.1.10 ";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2016";
fileInfo "version" "2016";
fileInfo "cutIdentifier" "201511301000-979500-1";
fileInfo "osv" "Microsoft Windows 7 Home Premium Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -n "soccerBall_geo";
	rename -uid "881BE4A4-4E06-9EBC-60E6-B79CB01C95C9";
	setAttr ".gh" yes;
	setAttr ".gc" 4;
	setAttr ".gre" 23;
createNode mesh -n "soccerBall_geoShape" -p "soccerBall_geo";
	rename -uid "233B6CF5-4815-C435-367D-50948D3EAFCD";
	setAttr -k off ".v";
	setAttr ".gh" yes;
	setAttr ".gc" 1;
	setAttr ".gpr" 100;
	setAttr ".gps" 100;
	setAttr ".gss" 4;
	setAttr ".gf" -type "Int32Array" 7 1 6 11 12 13 18
		 23 ;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 120 ".uvst[0].uvsp[0:119]" -type "float2" 0.032258064 0.29928011
		 0.096774191 0.29928011 0.12903225 0.35515273 0.096774191 0.41102532 0.032258064 0.41102532
		 0 0.35515273 0.22580644 0.29928011 0.29032257 0.29928011 0.32258064 0.35515273 0.29032257
		 0.41102532 0.22580644 0.41102532 0.19354838 0.35515273 0.41935483 0.29928011 0.48387095
		 0.29928011 0.51612902 0.35515273 0.48387095 0.41102532 0.41935483 0.41102532 0.38709676
		 0.35515273 0.61290324 0.29928011 0.6774193 0.29928011 0.7096774 0.35515273 0.6774193
		 0.41102532 0.61290324 0.41102532 0.58064514 0.35515273 0.80645156 0.29928011 0.87096775
		 0.29928011 0.90322578 0.35515273 0.87096775 0.41102532 0.80645156 0.41102532 0.77419353
		 0.35515273 0.90322578 0.46689793 0.87096775 0.52277052 0.80645156 0.52277052 0.77419353
		 0.46689793 0.7096774 0.46689793 0.6774193 0.52277052 0.61290324 0.52277052 0.58064514
		 0.46689793 0.51612902 0.46689793 0.48387095 0.52277052 0.41935483 0.52277052 0.38709676
		 0.46689793 0.32258064 0.46689793 0.29032257 0.52277052 0.22580644 0.52277052 0.19354838
		 0.46689793 0.12903225 0.46689793 0.096774191 0.52277052 0.032258064 0.52277052 0
		 0.46689793 0.19354838 0.57864314 0.12903225 0.57864314 0.38709676 0.57864314 0.32258064
		 0.57864314 0.58064514 0.57864314 0.51612902 0.57864314 0.77419353 0.57864314 0.7096774
		 0.57864314 0.96774191 0.46689793 1 0.52277052 0.96774191 0.57864314 0.90322578 0.57864314
		 1 0.63451576 0.96774191 0.69038838 0.90322578 0.69038838 0.87096775 0.63451576 0.80645156
		 0.63451576 0.77419353 0.69038838 0.7096774 0.69038838 0.6774193 0.63451576 0.61290324
		 0.63451576 0.58064514 0.69038838 0.51612902 0.69038838 0.48387095 0.63451576 0.41935483
		 0.63451576 0.38709676 0.69038838 0.32258064 0.69038838 0.29032257 0.63451576 0.22580644
		 0.63451576 0.19354838 0.69038838 0.12903225 0.69038838 0.096774191 0.63451576 0.11671077
		 0.58412904 0.064516127 0.62205064 0.012321487 0.58412904 0.31025913 0.58412904 0.25806451
		 0.62205064 0.20586987 0.58412904 0.50380754 0.58412904 0.45161289 0.62205064 0.39941823
		 0.58412904 0.69735593 0.58412904 0.64516127 0.62205064 0.59296662 0.58412904 0.89090431
		 0.58412904 0.83870965 0.62205064 0.786515 0.58412904 0.21348496 0.75174683 0.16129032
		 0.7896685 0.10909567 0.75174683 0.10909567 0.40553945 0.16129032 0.36761782 0.21348496
		 0.40553945 0.30264407 0.40553945 0.3548387 0.36761782 0.40703335 0.40553945 0.49619243
		 0.40553945 0.54838705 0.36761782 0.60058177 0.40553945 0.68974078 0.40553945 0.74193549
		 0.36761782 0.79413015 0.40553945 0.88328916 0.40553945 0.93548381 0.36761782 0.98767853
		 0.40553945 0.20586987 0.23792163 0.25806451 0.2 0.31025913 0.23792163 0.22580644
		 0.29928011 0.29032257 0.29928011;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 60 ".vt[0:59]"  0 1 2.220446e-016 0.39524779 0.91857398 2.039644e-016
		 -0.2227855 0.91857398 -0.32647699 -0.14409696 0.91857398 0.36804506 0.5677101 0.75572282 -0.32647699
		 0.495428 0.7868247 0.36804506 -0.58966798 0.75572282 -0.2849099 -0.050323799 0.75572282 -0.65295494
		 0.162095 0.7868247 0.59550929 -0.51097941 0.75572282 0.40961313 0.84035259 0.46112242 -0.2849099
		 0.34492457 0.67429775 -0.65295494 0.76807052 0.49222428 0.40961313 -0.64395201 0.49222428 -0.5856964
		 -0.73376495 0.67429775 0.083135463 -0.310619 0.49222428 -0.81316066 0.10140353 0.49222428 0.86454165
		 -0.57166994 0.46112242 0.67864448 0.78606856 0.19762389 -0.5856964 0.9405328 0.32937315 0.083135463
		 0.47987756 0.32937315 -0.81316066 0.70737904 0.19762389 0.67864448 -0.84233201 0.14730069 -0.51843882
		 -0.93214494 0.32937315 0.15039372 -0.175666 0.14730069 -0.97336727 0.37404603 0.19762389 0.90610969
		 -0.26547894 0.32937315 0.90610969 -0.83196473 0.19762389 0.51843882 0.83196473 -0.19762389 -0.51843882
		 0.98642504 -0.065874629 0.15039372 0.21958178 0.065874629 -0.97336727 0.84233201 -0.14730069 0.51843882
		 -0.70737904 -0.19762389 -0.67864448 -0.98642504 0.065874629 -0.15039372 -0.37404603 -0.19762389 -0.90610969
		 0.175666 -0.14730069 0.97336727 -0.21958178 -0.065874629 0.97336727 -0.78606856 -0.19762389 0.5856964
		 0.57166994 -0.46112242 -0.67864448 0.93214494 -0.32937315 -0.15039372 0.26547894 -0.32937315 -0.90610969
		 0.64395201 -0.49222428 0.5856964 -0.76807052 -0.49222428 -0.40961313 -0.9405328 -0.32937315 -0.083135463
		 -0.10140353 -0.49222428 -0.86454165 0.310619 -0.49222428 0.81316066 -0.47987756 -0.32937315 0.81316066
		 -0.84035259 -0.46112242 0.2849099 0.51097941 -0.75572282 -0.40961313 0.73376495 -0.67429775 -0.083135463
		 0.58966798 -0.75572282 0.2849099 -0.495428 -0.7868247 -0.36804506 -0.162095 -0.7868247 -0.59550929
		 0.050323799 -0.75572282 0.65295494 -0.34492457 -0.67429775 0.65295494 -0.5677101 -0.75572282 0.32647699
		 0.14409696 -0.91857398 -0.36804506 0.2227855 -0.91857398 0.32647699 -0.39524779 -0.91857398 -2.039644e-016
		 0 -1 -2.220446e-016;
	setAttr -s 90 ".ed[0:89]"  0 1 1 1 4 1 4 11 1 11 7 1 7 2 1 2 0 1 2 6 1
		 6 14 1 14 9 1 9 3 1 3 0 1 3 8 1 8 5 1 5 1 1 5 12 1 12 19 1 19 10 1 10 4 1 7 15 1
		 15 13 1 13 6 1 9 17 1 17 26 1 26 16 1 16 8 1 10 18 1 18 20 1 20 11 1 16 25 1 25 21 1
		 21 12 1 13 22 1 22 33 1 33 23 1 23 14 1 20 30 1 30 24 1 24 15 1 23 27 1 27 17 1 19 29 1
		 29 39 1 39 28 1 28 18 1 21 31 1 31 29 1 24 34 1 34 32 1 32 22 1 26 36 1 36 35 1 35 25 1
		 27 37 1 37 46 1 46 36 1 28 38 1 38 40 1 40 30 1 35 45 1 45 41 1 41 31 1 32 42 1 42 43 1
		 43 33 1 43 47 1 47 37 1 40 44 1 44 34 1 39 49 1 49 48 1 48 38 1 41 50 1 50 49 1 44 52 1
		 52 51 1 51 42 1 46 54 1 54 53 1 53 45 1 47 55 1 55 54 1 48 56 1 56 52 1 53 57 1 57 50 1
		 51 58 1 58 55 1 57 59 1 59 56 1 59 58 1;
	setAttr -s 32 -ch 180 ".fc[0:31]" -type "polyFaces" 
		f 6 0 1 2 3 4 5
		mu 0 6 16 17 12 13 14 15
		f 6 -6 6 7 8 9 10
		mu 0 6 16 15 38 39 40 41
		f 5 11 12 13 -1 -11
		mu 0 5 41 42 103 104 105
		f 6 14 15 16 17 -2 -14
		mu 0 6 9 10 11 6 7 8
		f 5 18 19 20 -7 -5
		mu 0 5 107 108 37 38 106
		f 6 21 22 23 24 -12 -10
		mu 0 6 40 52 53 43 42 41
		f 5 -18 25 26 27 -3
		mu 0 5 118 115 116 117 119
		f 6 -13 -25 28 29 30 -15
		mu 0 6 9 42 43 44 45 10
		f 6 -21 31 32 33 34 -8
		mu 0 6 38 37 36 54 55 39
		f 6 -4 -28 35 36 37 -19
		mu 0 6 23 18 19 20 21 22
		f 5 -9 -35 38 39 -22
		mu 0 5 40 39 88 89 90
		f 6 40 41 42 43 -26 -17
		mu 0 6 2 3 4 5 0 1
		f 5 44 45 -41 -16 -31
		mu 0 5 45 46 100 101 102
		f 6 -20 -38 46 47 48 -32
		mu 0 6 37 22 21 34 35 36
		f 5 49 50 51 -29 -24
		mu 0 5 85 86 87 44 43
		f 6 52 53 54 -50 -23 -40
		mu 0 6 74 75 76 77 53 52
		f 6 55 56 57 -36 -27 -44
		mu 0 6 26 27 28 29 24 25
		f 6 -30 -52 58 59 60 -45
		mu 0 6 45 44 50 51 47 46
		f 5 -49 61 62 63 -33
		mu 0 5 36 35 91 92 93
		f 6 -64 64 65 -53 -39 -34
		mu 0 6 54 70 71 72 73 55
		f 5 -37 -58 66 67 -47
		mu 0 5 109 110 111 33 34
		f 5 68 69 70 -56 -43
		mu 0 5 114 58 30 112 113
		f 6 -46 -61 71 72 -69 -42
		mu 0 6 3 46 47 48 49 4
		f 6 -48 -68 73 74 75 -62
		mu 0 6 35 34 33 32 56 57
		f 6 -51 -55 76 77 78 -59
		mu 0 6 50 78 79 80 81 51
		f 5 79 80 -77 -54 -66
		mu 0 5 98 99 80 79 97
		f 6 81 82 -74 -67 -57 -71
		mu 0 6 30 31 32 33 28 27
		f 5 -60 -79 83 84 -72
		mu 0 5 47 82 83 84 48
		f 6 85 86 -80 -65 -63 -76
		mu 0 6 56 66 67 68 69 57
		f 6 -70 -73 -85 87 88 -82
		mu 0 6 30 58 59 60 61 31
		f 5 -75 -83 -89 89 -86
		mu 0 5 96 32 31 94 95
		f 6 -78 -81 -87 -90 -88 -84
		mu 0 6 62 63 64 65 61 60;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode animCurveTL -n "pSolid1_translateX";
	rename -uid "4DD42C23-42E4-1D5D-DB1F-0DA68D93A325";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -4.6013240627438758 11 -0.38684097403730572
		 12 -5.1089055648088747e-008 13 0.35028289112808536 23 4.9703752496771072;
	setAttr -s 5 ".kyts[0:4]" yes yes no yes yes;
	setAttr -s 5 ".kit[1:4]"  18 9 18 9;
	setAttr -s 5 ".kot[1:4]"  18 9 18 9;
createNode animCurveTL -n "pSolid1_translateY";
	rename -uid "F40163C0-4FD0-419E-D468-068DB7D5441F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 4.3683538210363544 11 1.2568482575379532
		 12 0.58904189193331513 13 1.4497427748113823 23 3.1084444239554481;
	setAttr -s 5 ".kyts[0:4]" yes yes no yes yes;
	setAttr -s 5 ".kit[2:4]"  1 18 18;
	setAttr -s 5 ".kot[2:4]"  1 18 18;
	setAttr -s 5 ".kix[2:4]"  0.086043022572994232 0.17898376286029816 
		1;
	setAttr -s 5 ".kiy[2:4]"  -0.99629145860671997 0.98385202884674072 
		0;
	setAttr -s 5 ".kox[2:4]"  0.083454087376594543 0.17898374795913696 
		1;
	setAttr -s 5 ".koy[2:4]"  0.99651163816452026 0.98385196924209595 
		0;
createNode animCurveTL -n "pSolid1_translateZ";
	rename -uid "D1D989EE-443B-44F7-1991-A8A0BBA2CC46";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 11 0 12 0 13 0 23 0;
	setAttr -s 5 ".kyts[0:4]" yes yes yes yes yes;
createNode animCurveTA -n "pSolid1_rotateX";
	rename -uid "7C5AA487-473D-ADD4-DFE8-AF8186A8E93C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 6 0 11 0 12 0 13 0 18 0 23 0;
	setAttr -s 7 ".kyts[0:6]" yes no yes yes yes no yes;
createNode animCurveTA -n "pSolid1_rotateY";
	rename -uid "A964EAB6-47CF-3F00-15FF-0988DEF7DE45";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 6 0 11 0 12 0 13 0 18 0 23 0;
	setAttr -s 7 ".kyts[0:6]" yes no yes yes yes no yes;
createNode animCurveTA -n "pSolid1_rotateZ";
	rename -uid "920D72EF-4025-1313-8416-95B44446B341";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 6 -146.01920814843123 11 -327.27274064432061
		 12 -360.00000731511568 13 -378.76803418480927 18 -584.55434092335497 23 -720;
	setAttr -s 7 ".kyts[0:6]" yes no yes yes yes no yes;
	setAttr -s 7 ".kit[0:6]"  9 18 18 18 18 18 9;
	setAttr -s 7 ".kot[0:6]"  9 18 18 18 18 18 9;
createNode animCurveTU -n "pSolid1_scaleX";
	rename -uid "E7318BCC-4878-F2FA-BBA1-3299FBE20F7F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 11 0.80962393390160092 12 1 13 0.81207701499885931
		 23 1;
createNode animCurveTU -n "pSolid1_scaleY";
	rename -uid "695CDC9F-4751-CAF5-23E6-238D27C1A189";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 11 1.3788793708288474 12 0.62461527267700456
		 13 1.4695062338468505 23 1;
	setAttr -s 5 ".kyts[1:4]" yes no yes no;
createNode animCurveTU -n "pSolid1_scaleZ";
	rename -uid "50F000F8-4C76-3ED0-1399-3CB7AA4F5524";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 11 0.80962393390160092 12 1 13 0.81207701499885931
		 23 1;
createNode animCurveTU -n "pSolidShape1_sofx";
	rename -uid "D88D268A-4E9E-2CCF-C363-A1A148ECE942";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  11 0 13 0;
createNode animCurveTU -n "pSolidShape1_sofy";
	rename -uid "E637E865-4E5B-B7BA-580E-169D6694C12C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  11 0 13 0;
createNode animCurveTU -n "pSolidShape1_sofz";
	rename -uid "A4379291-4076-D56A-6FEF-DE86A9C4B15F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  11 0 13 0;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 1;
	setAttr -av ".unw" 1;
	setAttr -k on ".etw";
	setAttr -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -k on ".mico";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -k on ".micr";
	setAttr -k on ".micg";
	setAttr -k on ".micb";
	setAttr -cb on ".mica";
	setAttr -av -cb on ".micw";
	setAttr -cb on ".mirw";
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -k on ".mico";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -k on ".micr";
	setAttr -k on ".micg";
	setAttr -k on ".micb";
	setAttr -cb on ".mica";
	setAttr -av -cb on ".micw";
	setAttr -cb on ".mirw";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar";
	setAttr -av -k on ".ldar";
	setAttr -cb on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -cb on ".isu";
	setAttr -cb on ".pdu";
select -ne :defaultColorMgtGlobals;
	setAttr ".cme" no;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr -av ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "pSolid1_translateX.o" "soccerBall_geo.tx";
connectAttr "pSolid1_translateY.o" "soccerBall_geo.ty";
connectAttr "pSolid1_translateZ.o" "soccerBall_geo.tz";
connectAttr "pSolid1_rotateX.o" "soccerBall_geo.rx";
connectAttr "pSolid1_rotateY.o" "soccerBall_geo.ry";
connectAttr "pSolid1_rotateZ.o" "soccerBall_geo.rz";
connectAttr "pSolid1_scaleX.o" "soccerBall_geo.sx";
connectAttr "pSolid1_scaleY.o" "soccerBall_geo.sy";
connectAttr "pSolid1_scaleZ.o" "soccerBall_geo.sz";
connectAttr "pSolidShape1_sofx.o" "soccerBall_geoShape.sx";
connectAttr "pSolidShape1_sofy.o" "soccerBall_geoShape.sy";
connectAttr "pSolidShape1_sofz.o" "soccerBall_geoShape.sz";
connectAttr "soccerBall_geoShape.iog" ":initialShadingGroup.dsm" -na;
// End of soccerBall.ma
