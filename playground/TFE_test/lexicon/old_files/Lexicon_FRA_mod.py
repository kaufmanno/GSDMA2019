"""
Definition de quelques valeurs par défault pour les descriptions de cuttings.
:copyright: 2015 Agile Geoscience
:license: Apache 2.0
:Traduction: N.Y.H 
"""

# =========== LEGENDES ===========

# Canstrat
Canstrat_LEGEND = """colour,width,component lithology
#d60000,None,igné ,
#d60000,None,Ignoie acide ,
#d60000,None,métamorphique ,
#d60000,None,volcanique ,
#f4db94,None,sidérite ,
#c8965a,None,glacial jusqu'à ,
#ff9000,None,conglomérat ,
#ffc500,None,Breccia ,
#94c5c5,None,chert ,
#ffff00,None,grès ,
#ff863e,None,pierre ,
#c5ffff,None,argile ,
#909090,None,schiste argileux ,
#c5c5ff,None,bentonite ,
#020202,None,charbon ,
#c5c5c5,None,Marlstone ,
#7d96ff,None,calcaire ,
#ff46ff,None,dolomie ,
#aa6435,None,anhydrite ,
#008200,None,sel ,
#906e90,None,gypse ,
#c5ffc5,None,phosphate ,
"""

# NAGMDM__6_1
NAGMDM__6_1_LEGEND = """colour,width,component lithology
#ffffe9,None,inconsolable ,
#ffffd5,None,alluvion ,
#ffffb7,None,inondation ,
#ffff89,None,digue ,
#fdf43f,None,delta ,
#fffae9,None,cône alluvial ,
#faee7a,None,terrasse alluviale ,
#f4efe4,None,Dépôt de lac ou de marine ,
#eee7d6,None,playa ,
#eae1cc,None,plat de boue ,
#e4d8be,None,plage de sable ,
#fff6d9,None,terrasse ,
#e0b000,None,['éolien', 'éolienne'],
#e0d2b4,None,dune sable ,
#dbcca9,None,feuille de sable ,
#f5e1bd,None,lœss ,
#d6c59e,None,cendre volcanique ,
#cfbb8f,None,gaspillage de masse ,
#e1e3c3,None,colluvions ,
#dcd5b4,None,flux de boue ,
#d3ca9f,None,lahar ,
#c9be89,None,coulée de debris ,
#bcaf6c,None,glissement de terrain ,
#9d8935,None,astragale ,
#bfa743,None,glacial ,
#d2c27c,None,jusqu'à ,
#ffeebf,None,moraine ,
#ffe59d,None,sédiment glacial stratifié ,
#ffe985,None,franchement ,
#fee670,None,Sédiment sous-glacial et supra ,
#fee258,None,glaciolacustrine ,
#fedb2e,None,glacial-marine ,
#f7f3a1,None,sédiments biogéniques ,
#ffcc99,None,tourbe ,
#ffeaa7,None,corail ,
#ffe389,None,résidu ,
#ffdb67,None,argile ou boue ,
#ffd345,None,limon ,
#ffcb23,None,sable ,
#ecb400,None,gravier ,
#cfefdf,None,Roche sédimentaire ,
#d9fdd3,None,clique ,
#ace4c8,None,mudstone ,
#d5e6cc,None,argile ,
#92dcb7,None,bentonite ,
#c0d0c0,None,schiste argileux ,
#dbfebc,None,schiste noir ,
#bbffdd,None,schiste de pétrole ,
#95ffca,None,argilite ,
#d6fe9a,None,pierre ,
#e1f0d8,None,grainé fine mélangé ,
#cdffd9,None,grès ,
#cbefce,None,arénite ,
#a6fcaa,None,orthoquartzite ,
#7dffe3,None,calcarénite ,
#b8eac3,None,arkose ,
#bddbf1,None,wacke ,
#69cf9c,None,graine ,
#90a565,None,grainé moyennement grainé ,
#b7d9cc,None,conglomérat ,
#a7ba86,None,Breccia sédimentaire ,
#bcc0c5,None,grain grain grossier ,
#8dbecd,None,olistostrome ,
#a5aaad,None,mélange ,
#019ccd,None,carbonate ,
#149ef8,None,calcaire ,
#0094f8,None,Dolstone (dolomite) ,
#45c5c2,None,Clastique / carbonate mélangé ,
#38b0a2,None,Clastic / Volcanique mélangé ,
#bfe3dc,None,phosphorite ,
#cddeff,None,chimique ,
#9acefe,None,évaporite ,
#aac2c8,None,chert ,
#c0aeb6,None,novaculite ,
#b99598,None,formation de fer ,
#98004c,None,exhalite ,
#6e4900,None,charbon ,
#d9c2a3,None,Clastique / charbon mélangé ,
#ffeff3,None,ROCK PLUTONIC (PHANERTIC) ,
#ffc8bf,None,aplite ,
#ffe1e8,None,porphyre ,
#fdcfcf,None,lamprophyre ,
#ffd1dc,None,pegmatite ,
#fc6e7c,None,granitoïde ,
#fc5262,None,Granit alkali (Alaskite) ,
#fb2338,None,granit ,
#f43c6c,None,granit péralumineux ,
#f41a87,None,granit métallineux ,
#dd2972,None,granit subalumineux ,
#e45891,None,granit peralkaline ,
#e979a6,None,granodiorite ,
#ff6f6b,None,tonalite ,
#ffb3c5,None,trondhjemite ,
#f8beae,None,alcali syenite ,
#f9b5bb,None,quartz syenite ,
#ffa7bc,None,syenite ,
#ff6388,None,quartz monzonite ,
#ff275a,None,monzonite ,
#ffccc5,None,quartz monzodiorite ,
#ffa99d,None,monzodiorite ,
#ff6f5b,None,diorite de quartz ,
#ff3317,None,diorite ,
#e81c00,None,diabase ,
#ff95ae,None,gabbroïde ,
#ff819f,None,quartz monzogabro ,
#ffd6d1,None,Monzogabbro ,
#eda7ca,None,quartz gabbro ,
#e993be,None,gabbro ,
#e377ad,None,norité ,
#ffbfce,None,troctolite ,
#ffa3b9,None,anorthosite ,
#ff6f91,None,Rock intrusif alcalique ,
#ff1b51,None,Népheline Syenite ,
#e80037,None,roche intrusive ultramafique ,
#ce0031,None,péridotite ,
#b0002a,None,dunuel ,
#940023,None,kimberlite ,
#c1010a,None,pyroxénite ,
#a30109,None,hornblendite ,
#750107,None,carbonatite intrusive ,
#f9d3d3,None,Rock volcanique (aphancitique) ,
#ffe5f3,None,roche volcanique vitreuse ,
#ffd1ea,None,obsidienne ,
#ffc3f8,None,vitrophyre ,
#ffc3e4,None,pierre ponce ,
#ffedbf,None,pyroclastique ,
#ffefd9,None,tuf ,
#ffb7de,None,tuf soudé ,
#ffc8c3,None,tuf flux de cendres ,
#ffe5c3,None,ignimbrite ,
#ffd59d,None,Breccia volcanique (agglomérat) ,
#ffc10b,None,coulée de lave ,
#ffa227,None,suite bimodale ,
#f48b00,None,roche volcanique felsique ,
#fedc7e,None,alcali rhyolite ,
#fed768,None,rhyolite ,
#fec62a,None,rhédacite ,
#fecdac,None,dacite ,
#feb786,None,alcalin trachyte ,
#fea060,None,trachyte ,
#fe8736,None,quartz latite ,
#fe7518,None,latit ,
#eb6001,None,roche volcanique intermédiaire ,
#c95201,None,trachyandesite ,
#b14801,None,andésite ,
#933c01,None,rock mafic volcanique ,
#ecd5c6,None,trachybasalt ,
#ddb397,None,basalte ,
#d39d79,None,tholite ,
#c68050,None,hawaiite ,
#a96537,None,basalte alcaline ,
#854f2b,None,rock alcalique volcanique ,
#5f391f,None,phonolite ,
#c24100,None,Téphrite (Basinite) ,
#a03500,None,Ultramafitise (komatite) ,
#6e2500,None,carbonatite volcanique ,
#e6cdff,None,Roche métamorphique ,
#eaafff,None,hornfels ,
#e9ffe9,None,rocher métasédimentaire ,
#c9ffc9,None,méta-argilite ,
#a7a7ff,None,ardoise ,
#9fff9f,None,quartzite ,
#7dff7d,None,méta-conglomérat ,
#0000ff,None,marbre ,
#ffa7ff,None,rock métavolcanique ,
#ff8dff,None,roche métavolcanique felsique ,
#ff57ff,None,méta-rhyolite ,
#fe6700,None,kératophyre ,
#c9557e,None,Rock métavolcanique intermédiaire ,
#b93b68,None,rock métavolcanique mafic ,
#872b4c,None,méta-basalte ,
#ff0000,None,spilite ,
#008000,None,pierre verte ,
#ededf3,None,phyllite ,
#dbdbe7,None,schiste ,
#cacadc,None,greenschist ,
#c0c0c0,None,blueschist ,
#b1b1b1,None,Schist de mica ,
#969696,None,schiste pélitique ,
#a2a2c0,None,Schiste de quartz-feldspar ,
#b4cfe4,None,Schiste de silicate de calcul ,
#b6b6ce,None,schiste d'amphibole ,
#abffff,None,granofels ,
#79ffff,None,gneiss ,
#0fffff,None,Gneiss felsique ,
#00dbd6,None,Gneiss granitiques ,
#00a4a0,None,gneiss biotite ,
#007673,None,Gneiss mafic ,
#33cccc,None,orthogneiss ,
#2db6b3,None,paragne ,
#ac0000,None,migmatite ,
#ac7f50,None,amphibolite ,
#84613e,None,granulite ,
#ff4fff,None,eclogite ,
#ec00ec,None,greisen ,
#6600cc,None,Skarn (tactite) ,
#46008c,None,Calc-silicate rocher ,
#005c00,None,serpentinite ,
#c600c6,None,rocher tectonique ,
#9c009c,None,tectonite ,
#6a006a,None,tectonique mélange ,
#2a002a,None,tectonique breccia ,
#f4ffd5,None,cataclasite ,
#339966,None,phyllonite ,
#d0cbb0,None,mylonite ,
#b0a778,None,flase gneiss ,
#887f50,None,Augen Gneiss ,
"""

# NAGMDM__6_2
NAGMDM__6_2_LEGEND = """colour,width,component lithology
#fdf43f,None,matériau non consolidé ,
#ffff89,None,alluvion ,
#ffffd5,None,inondation ,
#fffae9,None,digue ,
#fffac8,None,delta ,
#ffffb7,None,cône alluvial ,
#faee7a,None,terrasse alluviale ,
#f4efe4,None,sédiment du lac ou de la marine ,
#f1e5df,None,playa ,
#e4d0be,None,plat de boue ,
#e4d8be,None,plage de sable ,
#fff6d9,None,terrasse ,
#e0c59e,None,matériau Eolien ,
#e0d2b4,None,dune sable ,
#dbcca9,None,feuille de sable ,
#f5e1bd,None,lœss ,
#e0b09e,None,cendre volcanique ,
#cfbb8f,None,Matériau de gaspillage de masse ,
#e1e3c3,None,colluvions ,
#e5dbb3,None,flux de boue ,
#dcd5b4,None,lahar ,
#d3ca9f,None,coulée de debris ,
#c9be89,None,glissement de terrain ,
#bcaf6c,None,astragale ,
#bfa743,None,glacial ,
#d2c27c,None,jusqu'à ,
#ffeebf,None,moraine ,
#ffe59d,None,sédiment glacial stratifié ,
#ffdf85,None,Sédiment de la sortie glaciaire ,
#fee670,None,Sédiments sub / supra-glaciaires ,
#fee258,None,sédiment glacolacustrine ,
#fedb2e,None,sédiment glacial-marine ,
#f7f3a1,None,rock biogénique ,
#ffcf81,None,tourbe ,
#ffcc99,None,corail ,
#ffe389,None,résidu ,
#ffdb67,None,argile ou boue ,
#ffd345,None,limon ,
#ffcb23,None,sable ,
#ecb400,None,gravier ,
#92dcb7,None,Roche sédimentaire ,
#d9fdd3,None,rock classique ,
#cfefdf,None,mudstone ,
#d5e6cc,None,argile ,
#c0d0c0,None,bentonite ,
#ace4c8,None,schiste argileux ,
#dbfebc,None,schiste noir ,
#bbffdd,None,schiste de pétrole ,
#e1f0d8,None,argilite ,
#d6fe9a,None,pierre ,
#95ffca,None,roche clique mixte à grain fin ,
#cdffd9,None,grès ,
#a6fcaa,None,arénite ,
#cbefce,None,orthoquartzite ,
#9acefe,None,calcarénite ,
#69cf9c,None,arkose ,
#bddbf1,None,wacke ,
#b8eac3,None,graine ,
#90a565,None,roche clique mixte à grains moyennement grains ,
#b7d9cc,None,conglomérat ,
#a7ba86,None,Breccia sédimentaire ,
#a5aaad,None,rock classique grainé grainé ,
#8dbecd,None,olistostrome ,
#bbc0c5,None,mélange ,
#56e0fc,None,rock carbonate ,
#43aff9,None,calcaire ,
#6bc3ff,None,dolosone ,
#38b4b1,None,Carbonate mixte / roche clique ,
#60ccbf,None,Rock mixte volcanique / clique ,
#bfe3dc,None,phosphorite ,
#cddeff,None,roche sédimentaire chimique ,
#019ccd,None,évaporite ,
#9abfc0,None,chert ,
#c0aeb6,None,novaculite ,
#b99598,None,formation de fer ,
#d9c2a3,None,exhalite ,
#820041,None,charbon ,
#6e4909,None,charbon mixte et roche clastique ,
#fc6e7c,None,rock plutonique ,
#ffc1b7,None,aplite ,
#ffe1e8,None,porphyre ,
#e45891,None,lampophyre ,
#ffeff3,None,pegmatite ,
#dd2972,None,granitoïde ,
#ffd1dc,None,alcali-feldspar granite ,
#f9b5bb,None,granit ,
#f8beae,None,granit péralumineux ,
#ffb3c5,None,granit métallineux ,
#ff6f6b,None,granit subalumineux ,
#fc5262,None,granit peralkaline ,
#e979a6,None,granodiorite ,
#fcb6b6,None,tonalite ,
#ffa7bc,None,trondhjemite ,
#f43c6c,None,alcali-feldspar syenite ,
#fb2338,None,quartz syenite ,
#f41a87,None,syenite ,
#ff6388,None,quartz monzonite ,
#ff275a,None,monzonite ,
#ff819f,None,quartz monzodiorite ,
#ffa99d,None,monzodiorite ,
#e81c00,None,diorite de quartz ,
#ff3317,None,diorite ,
#d60000,None,diabase ,
#ac0000,None,gabbroïde ,
#ff6f5b,None,quartz monzogabro ,
#e377ad,None,Monzogabbro ,
#eda7ca,None,quartz gabbro ,
#e993be,None,gabbro ,
#ffd6d1,None,norité ,
#ffbfce,None,troctolite ,
#ff95ae,None,anorthosite ,
#ff6f91,None,Rock intrusif alcalique ,
#ff1b51,None,Népheline Syenite ,
#e80037,None,roche intrusive ultramafique ,
#ce0031,None,péridotite ,
#b0002a,None,dunuel ,
#c1010a,None,kimberlite ,
#940023,None,pyroxénite ,
#a30109,None,hornblendite ,
#750107,None,carbonatite intrusive ,
#ffb7de,None,Roche volcanique ,
#ffc3e4,None,roche volcanique vitreuse ,
#ffd1ea,None,obsidienne ,
#ffc3f8,None,vitrophyre ,
#ffe5f3,None,pierre ponce ,
#ffe0de,None,pyroclastique ,
#f9d3d3,None,tuf ,
#fff3c9,None,tuf soudé ,
#ffefd9,None,tuf flux de cendres ,
#ffe5c3,None,ignimbrite ,
#ffd59d,None,Breccia volcanique ,
#ffa227,None,coulée de lave ,
#ffc16f,None,suite bimodale ,
#f48b00,None,roche volcanique felsique ,
#fedc7e,None,alcali-feldsprs rhyolite ,
#fecc68,None,rhyolite ,
#fec62a,None,rhédacite ,
#fecdac,None,dacite ,
#feb786,None,Alkali-feldspath Trachyte ,
#fea060,None,trachyte ,
#fe8736,None,quartz latite ,
#fe7518,None,latit ,
#eb6001,None,roche volcanique intermédiaire ,
#c95201,None,trachyandesite ,
#b14801,None,andésite ,
#933c01,None,rock mafic volcanique ,
#ecd5c6,None,trachybasalt ,
#ddb397,None,basalte ,
#d39d79,None,tholite ,
#c68050,None,hawaiite ,
#a96537,None,basalte alcaline ,
#c24100,None,rock alcalique volcanique ,
#5f391f,None,phonolite ,
#854f2b,None,téphrite ,
#a03500,None,ultramafitate ,
#6e2500,None,carbonatite volcanique ,
#a7a7ff,None,Roche métamorphique ,
#eaafff,None,hornfels ,
#7dff7d,None,rocher métasédimentaire ,
#c9ffc9,None,méta-argilite ,
#e6cdff,None,ardoise ,
#9fff9f,None,quartzite ,
#e9ffe9,None,métaconglomérer ,
#0000ff,None,marbre ,
#ff57ff,None,rock métavolcanique ,
#ff8dff,None,roche métavolcanique felsique ,
#ffa7ff,None,métarhyolite ,
#fe6700,None,kératophyre ,
#ff0000,None,Rock métavolcanique intermédiaire ,
#b93b68,None,rock métavolcanique mafic ,
#872b4c,None,métabasalt ,
#c9557e,None,spilite ,
#008000,None,pierre verte ,
#b4cfe4,None,phyllite ,
#dbdbe7,None,schiste ,
#ededf3,None,greenschist ,
#c0c0c0,None,blueschist ,
#b1b1b1,None,Schist de mica ,
#cacadc,None,schiste pélitique ,
#a2a2c0,None,Schiste de quartz-feldspar ,
#b6b6ce,None,Schiste de silicate de calcul ,
#969696,None,schiste d'amphibole ,
#a337fd,None,granofels ,
#ecd6fe,None,gneiss ,
#e0bcfe,None,Gneiss felsique ,
#d5a4fe,None,Gneiss granitiques ,
#c886fe,None,gneiss biotite ,
#ccb7ff,None,Gneiss mafic ,
#b395ff,None,orthogneiss ,
#9063ff,None,paragne ,
#9f00ca,None,migmatite ,
#7b009c,None,amphibolite ,
#6a006a,None,granulite ,
#ce9dff,None,eclogite ,
#a449ff,None,greisen ,
#8103ff,None,skarn ,
#46008c,None,Calc-silicate rocher ,
#005c00,None,serpentinite ,
#84613e,None,tectonite ,
#d0cbb0,None,tectonique mélange ,
#b0a778,None,tectonique breccia ,
#887f50,None,cataclasite ,
#ac7f50,None,phyllonite ,
#6d5033,None,mylonite ,
#64020b,None,flase gneiss ,
#887f50,None,Augen Gneiss ,
"""

# NSDOE
NSDOE_LEGEND = """colour,width,component lithology
#f7e9a6,None,grès ,
#ff99cc,None,anhydrite ,
#dbd6bc,None,hétérolithique ,
#ff4c4a,None,volcanique ,
#86f0b6,None,conglomérat ,
#ff96f6,None,halite ,
#f2ff42,None,grès ,
#dbc9bc,None,hétérolithique ,
#a68374,None,pierre ,
#a657fa,None,dolomie ,
#ffd073,None,grès ,
#a6d1ff,None,calcaire ,
#ffdbba,None,grès ,
#ffe040,None,grès ,
#a1655a,None,pierre ,
#363434,None,charbon ,
#664a4a,None,mudstone ,
#666666,None,mudstone ,
"""

# SGMC
SGMC_LEGEND = """colour,width,component lithology
#fdf43f,None,inconsolable ,
#ffff89,None,coarse_detrital ,
#ffda63,None,rochers ,
#ffce1d,None,gravier ,
#eec102,None,sable ,
#ffcc99,None,corail ,
#eeefb3,None,fine_detrital ,
#e5e081,None,argile ,
#f9f5d3,None,limon ,
#fef2b8,None,marne ,
#ffe389,None,tourbe ,
#bddbf1,None,l'eau ,
#92dcb7,None,sédimentaire ,
#56e0fc,None,carbonate ,
#6bc3ff,None,dolosone ,
#43aff9,None,calcaire ,
#deeffe,None,craie ,
#8ce5fe,None,coquina ,
#bae5fe,None,Marlstone ,
#cddeff,None,chimique ,
#d5d11f,None,Banded_iron_formation ,
#c9b655,None,barite ,
#8cb7b8,None,chert ,
#c7c299,None,diatomie ,
#dee5c4,None,évaporite ,
#e7f6f1,None,anhydrite ,
#e1e9ec,None,gypse ,
#c5d5e9,None,sel ,
#a3adcb,None,novaculite ,
#bfe3dc,None,phosphorite ,
#d9fdd3,None,clique ,
#b7d9cc,None,conglomérat ,
#65cfcc,None,claquement mixte ,
#98c8ae,None,conglomérat_sandstone ,
#95ffca,None,Sandstone_mudstone ,
#3dbfb0,None,siltstone_mudstone ,
#cfefdf,None,mudstone ,
#d5e6cc,None,argile ,
#c0d0c0,None,bentonite ,
#ace4c8,None,schiste argileux ,
#dbfebc,None,Black_shale ,
#bbffdd,None,huile_shale ,
#9ed7c2,None,phosphatic_shale ,
#cdffd9,None,grès ,
#a6fcaa,None,arénite ,
#9acefe,None,calcarénite ,
#69cf9c,None,arkose ,
#a7e5b4,None,graine ,
#a7ba86,None,sédimentaire_breccia ,
#d6fe9a,None,pierre ,
#8c8cf0,None,charbon ,
#6363eb,None,anthracite ,
#2727e3,None,['bitumineux', 'bitumineuse'],
#1616a8,None,lignite ,
#001086,None,sub_bitumous ,
#c61585,None,plutonique ,
#ffe3e0,None,anorthosite ,
#eed5d3,None,charnockite ,
#dfc8c8,None,diioritique ,
#d7a7ad,None,diorite ,
#eea0aa,None,monzodiorite ,
#ffadb8,None,quartz_diorite ,
#ffb8c1,None,quartz monzodiorite ,
#e88ca0,None,foidal_dioritique ,
#ce929f,None,foidal_gabbroïque ,
#ff9ebe,None,foidal_syénitique ,
#ff80aa,None,cancrinite_synite ,
#ed789d,None,foid_synite ,
#cd6a8b,None,Népheline_synite ,
#cf208f,None,sodalite_synite ,
#fd1d68,None,foidolite ,
#ff5b5b,None,gabroque ,
#e993be,None,gabbro ,
#ff85fb,None,gabbronorite ,
#ee7ce8,None,norité ,
#cd6aca,None,troctolite ,
#ffbdff,None,Monzogabbro ,
#eeafee,None,quartz_gabbro ,
#cd98cd,None,quartz_monzogabro ,
#ee68a6,None,granitique ,
#ff70b5,None,alcali_feldspar_granite ,
#ff3895,None,alcali_granite ,
#ff33b4,None,granit ,
#ff00ff,None,monzogranite ,
#fc9efe,None,syenogranite ,
#ee2fa8,None,granodiorite ,
#d7339a,None,leucocratique_granitic ,
#d503b4,None,alaskite ,
#b300b3,None,aplite ,
#ca61ff,None,pegmatite ,
#ff5bb9,None,quartz_rich_granitoid ,
#a82475,None,tonalite ,
#f80094,None,trondhjemite ,
#f00000,None,intrusion_carbonatite ,
#ff3838,None,mélilitiique ,
#cd3278,None,syentique ,
#ff1492,None,alcali_feldspar_synite ,
#ee1187,None,monzonite ,
#cc0f74,None,quartz_alkali_feldspar_synite ,
#ff9faa,None,quartz monzonite ,
#ff61a8,None,quartz syenite ,
#b80f5b,None,syenite ,
#cc0000,None,ultra-cadre ,
#8a475c,None,hornblendite ,
#8a668a,None,péridotite ,
#8c6969,None,dunuel ,
#7d1c66,None,kimberlite ,
#6b0000,None,pyroxénite ,
#e4dbec,None,la glace ,
#f84d4d,None,['igné', 'ignée'],
#cdb79d,None,hypocyssal ,
#deb887,None,felsic_hypabyses ,
#ffefdb,None,Dacite hypocyssal ,
#faead6,None,Hypabyssal_felsic_alkaline ,
#eee1ce,None,Hypabyssal latite ,
#ffe0c2,None,Hypabyssal_quartz_Latite ,
#ffd399,None,Hypabyssal_quartz_trachyte ,
#eec591,None,Hypabyssal_rhyolite ,
#cdab7e,None,Hypabyssal_trachyte ,
#cc8500,None,lamprophyre ,
#ee7620,None,mafic_hypabyses ,
#ffb70f,None,Hypabyssal_andesite ,
#ecad0e,None,hypabysesal_basalt ,
#ffa600,None,hypabysesal_basaltic_andesite ,
#f09c00,None,Hypabyssal_mafic_alkaline ,
#ee694f,None,volcanique ,
#ffa352,None,alcalic_volcanique ,
#ff8052,None,basanique ,
#ff7357,None,foidite ,
#d57562,None,phonolite ,
#cd7637,None,felsic_volcanique ,
#fcbe92,None,dacite ,
#ff9d47,None,latit ,
#ff8259,None,quartz_latite ,
#ee5e44,None,quartz_trachyte ,
#c2755b,None,rhyolite ,
#cd4e37,None,trachyte ,
#ea9090,None,mafic_volcanique ,
#ee2b2b,None,andésite ,
#e46c6c,None,basalte ,
#db3939,None,basaltique_andesite ,
#b33000,None,komatite ,
#8a2500,None,picrite ,
#a7a7ff,None,métamorphique ,
#7b009c,None,amphibolite ,
#8c298a,None,argilite ,
#6a006a,None,eclogite ,
#9f00ca,None,gneiss ,
#a337fd,None,granofels ,
#9b02b0,None,granulite ,
#698263,None,pierre verte ,
#eaafff,None,hornfels ,
#6900ff,None,marbre ,
#a184a2,None,métasédimentaire ,
#de5785,None,métavolcanique ,
#9f8aca,None,migmatite ,
#dbdbe7,None,phyllite ,
#b4cfe4,None,quartzite ,
#bbc0c5,None,schiste ,
#638a57,None,serpentinite ,
#ab70ff,None,skarn ,
#8103ff,None,ardoise ,
#84613e,None,tectonite ,
#887f50,None,cataclasite ,
#ac7f50,None,mélange ,
#6d5033,None,mylonite ,
#64020b,None,phyllonite ,
"""


# =========== ECHELLES DES TEMPS ===========

# DNAG
DNAG_TIMESCALE = """colour,width,component age
#aaff00,None,aalénien ,
#4cb319,None,Albian ,
#66cc99,None,anisien ,
#80ff4c,None,aptitude ,
#de7038,None,aquitaïanien ,
#e1e1e1,None,['archéen', 'archéenne'],
#ad4cb3,None,arénigien ,
#00a9e6,None,Artininskian ,
#e6b3d1,None,ashgillien ,
#9efa00,None,bajocien ,
#8fdb00,None,barrémie ,
#dea640,None,bartonien ,
#9bb2ff,None,bashkirien ,
#a3ff73,None,bathonien ,
#009c21,None,béros ,
#e6780d,None,burdigalien ,
#ffedc7,None,calabrian ,
#e9ffbe,None,callovien ,
#ff8099,None,Cambrien ,
#66cc33,None,['campanien', 'campanienne'],
#cc99b8,None,caradocian ,
#8fa8ff,None,carbonifère ,
#99cc99,None,carnien ,
#99e666,None,cénomanien ,
#faffa3,None,cénozoïque ,
#e6b34c,None,['chat', 'chatte'],
#99e666,None,coniacien ,
#b3ff80,None,['crétacé', 'crétacée'],
#b36600,None,Danian ,
#8099ff,None,['dévonien', 'dévonienne'],
#ebb3b3,None,Dresbachian ,
#828282,None,début archéen ,
#ffcccc,None,Cambrian tôt ,
#99b3e6,None,carbonifère précoce ,
#7de34a,None,Crétacé précoce ,
#9999ff,None,Devonien tôt ,
#d6b34c,None,Eocène précoce ,
#4cff80,None,tôt jurassique ,
#e6780d,None,Miocène précoce ,
#cc9933,None,oligocène précoce ,
#cc6bd1,None,premiers ordonnés ,
#b36600,None,paléocène précoce ,
#87e8ff,None,permien tôt ,
#d98c00,None,pliocène précoce ,
#e6cccc,None,Protérozoïque précoce ,
#ccb3ff,None,Silurien tôt ,
#66ebb3,None,triasique précoce ,
#8080cc,None,Eifelian ,
#8080e6,None,Emsian ,
#ebcc80,None,éocène ,
#b3b3e6,None,famné ,
#ebb3b3,None,franconien ,
#9999cc,None,frasnien ,
#4c4cb3,None,gedinnien ,
#9999e6,None,gevitian ,
#9ebbd7,None,gzélien kasimovien ,
#c4e300,None,hautérivien ,
#008519,None,hettangien ,
#ffff29,None,holocène ,
#00e07a,None,jurassique ,
#bee8ff,None,Kazanien ,
#ccffd4,None,kimmeridgien ,
#00c5ff,None,kungurien ,
#80e6b3,None,Ladinian ,
#d97a00,None,langhien ,
#cccccc,None,tachete ,
#ff99b3,None,Cambrien tardif ,
#80ccff,None,carbonifère tardive ,
#99ff66,None,Crétacé tardif ,
#ccccff,None,Dévonien tardif ,
#ffcc99,None,Eocène tardive ,
#ccffcc,None,tardif du jurassique ,
#ffb35e,None,Miocène tardif ,
#e6b34c,None,oligocène tardif ,
#ffcceb,None,Ordovicien tardif ,
#f2a640,None,paléocène fin ,
#bdedff,None,permien tardif ,
#f2a60d,None,Pliocène tardif ,
#b39999,None,Protérozoïque tardif ,
#ebccff,None,silurien tardif ,
#ccffeb,None,triasique tardif ,
#c791d9,None,lllandeilan ,
#9980cc,None,llandverien ,
#a16bb3,None,llanvirnian ,
#b899cc,None,ludlovien ,
#c48c26,None,luttian ,
#80cc4c,None,maastrichtier ,
#cfffb5,None,mésozoïque ,
#f29e52,None,Messinien ,
#b2b2b2,None,hérien du milieu ,
#eb8099,None,Cambrien du milieu ,
#b3b3ff,None,au milieu dévonien ,
#ebb34c,None,eocène moyen ,
#80ff99,None,jurystique moyen ,
#fc9e00,None,Miocène moyen ,
#e3adf5,None,Ordovicien du milieu ,
#998080,None,Protérozoïque moyen ,
#99ffcc,None,médiocre ,
#ffc780,None,miocène ,
#91b3e6,None,Mississippian ,
#bed2ff,None,moscovien ,
#66cc33,None,néocomique ,
#ffd96e,None,neogène ,
#b3e6b3,None,Norian ,
#ffcc66,None,oligocène ,
#ff80e6,None,['ordovicien', 'ordovicienne'],
#d3ffbe,None,['Oxfordien', 'Oxfordienne'],
#ffb34c,None,paléocène ,
#ffedc7,None,paléogène ,
#e3e3ff,None,paléozoïque ,
#80ccff,None,pennsylvanien ,
#c4ffff,None,['permien', 'permienne'],
#f2a60d,None,piacenzien ,
#fffaa8,None,pléistocène ,
#19cc4c,None,pliensbachien ,
#ffb300,None,pliocène ,
#999966,None,précocbrien ,
#ffcc99,None,priabian ,
#d1b3e6,None,pridolien ,
#ccb3b3,None,prothézoïque ,
#ffff8c,None,quaternaire ,
#cc9933,None,rubelien ,
#009cb3,None,asselian sakmarian ,
#66e633,None,santonien ,
#33b880,None,Scythe ,
#f2a640,None,selandien ,
#80b3e6,None,serpukhovien ,
#f29400,None,Serravallien ,
#6666cc,None,siegenian ,
#b380ff,None,['silurien', 'silurienne'],
#4ce600,None,sinémurien ,
#d4f7ff,None,tatarien ,
#ffd900,None,tertiaire ,
#ffa673,None,Thanétien ,
#00fca3,None,ithonien ,
#33e666,None,toarcian ,
#e89c14,None,tortonien ,
#cce6eb,None,tournaisie ,
#cc66b3,None,tremadocien ,
#ebb3b3,None,trempealeau ,
#66ffcc,None,triassique ,
#80e64c,None,turonique ,
#4ce6e6,None,ufimien ,
#85b000,None,valanginien ,
#b3cceb,None,['visuel', 'visuelle'],
#b399e6,None,wenlockien ,
#d6b34c,None,Ypresian ,
#d98c00,None,Zanclean ,
"""

# ISC
ISC_TIMESCALE = """colour,width,component age
#6fdaed,None,phanerozoïque ,
#f6ec39,None,cénozoïque ,
#fef691,None,quaternaire ,
#f2f902,None,tertiaire ,
#fedd2d,None,neogène ,
#fef1e0,None,holocène ,
#feefb8,None,pléistocène ,
#fef1d6,None,Pléistocène supérieur ,
#fef1d6,None,taantian ,
#fef0cc,None,pléistocène du milieu ,
#fef0cc,None,['ionien', 'ionienne'],
#feefc1,None,calabrian ,
#feeead,None,gélasien ,
#fef8a6,None,pliocène ,
#fefac8,None,piacenzien ,
#fef9bd,None,Zanclean ,
#feef00,None,miocène ,
#fef587,None,Messinien ,
#fef47d,None,tortonien ,
#fef472,None,Serravallien ,
#fef366,None,langhien ,
#fef259,None,burdigalien ,
#fef14d,None,aquitaïanien ,
#fea163,None,paléogène ,
#fea163,None,palæogène ,
#fea163,None,paléogène ,
#fec386,None,oligocène ,
#fee4b2,None,['chat', 'chatte'],
#fed9a2,None,rubelien ,
#feb979,None,éocène ,
#fecfa7,None,priabian ,
#fec498,None,bartonien ,
#feb98a,None,luttian ,
#feae7d,None,Ypresian ,
#fead6e,None,paléocène ,
#fead6e,None,palæocène ,
#fead6e,None,paléocène ,
#fec37d,None,Thanétien ,
#fec274,None,selandien ,
#feb872,None,Danian ,
#07caea,None,mésozoïque ,
#6fc86b,None,['crétacé', 'crétacée'],
#a6d468,None,Crétacé tardif ,
#a6d468,None,Crétacé supérieur ,
#f3f29c,None,maastrichtier ,
#eaed93,None,['campanien', 'campanienne'],
#dee78a,None,santonien ,
#d1e382,None,coniacien ,
#c3df79,None,turonique ,
#b5da71,None,cénomanien ,
#7ecd74,None,Crétacé précoce ,
#7ecd74,None,Crétacé inférieur ,
#cde5a8,None,Albian ,
#bfe19f,None,aptitude ,
#afdd97,None,barrémie ,
#9ed78e,None,hautérivien ,
#8dd285,None,valanginien ,
#7cce7c,None,béros ,
#00bbe7,None,jurassique ,
#97e3fa,None,tardif du jurassique ,
#97e3fa,None,Haut Jurassique ,
#cff0fc,None,ithonien ,
#bdebfb,None,kimmeridgien ,
#abe7fb,None,['Oxfordien', 'Oxfordienne'],
#34d1eb,None,milieu jurassique ,
#34d1eb,None,jurystique moyen ,
#aee6f0,None,callovien ,
#9ce2ef,None,bathonien ,
#87deee,None,bajocien ,
#6fdaed,None,aalénien ,
#00b7ea,None,tôt jurassique ,
#00b7ea,None,jurystique inférieur ,
#74d1f0,None,toarcian ,
#3cc9ef,None,pliensbachien ,
#07c1ed,None,sinémurien ,
#00bbeb,None,hettangien ,
#994e96,None,triassique ,
#c698c2,None,triasique tardif ,
#c698c2,None,triassique supérieur ,
#e8c2d8,None,rhédie ,
#ddb4d1,None,Norian ,
#d1a6c9,None,carnien ,
#bf7cb1,None,Mid Triassique ,
#bf7cb1,None,médiocre ,
#d492bd,None,Ladinian ,
#c986b6,None,anisien ,
#ad579a,None,triasique inférieur ,
#ad579a,None,triasique précoce ,
#c26aa5,None,olènekien ,
#b861a0,None,Indien ,
#92c3a0,None,paléozoïque ,
#92c3a0,None,paléozoïque ,
#92c3a0,None,paléozoïque ,
#f7583c,None,['permien', 'permienne'],
#feaf97,None,permien tardif ,
#feaf97,None,permien supérieur ,
#feaf97,None,lopingien ,
#fec6b3,None,Changhsingien ,
#febba5,None,Wuchiapingien ,
#fe8367,None,permien du milieu ,
#fe8367,None,midi ,
#fe8367,None,Guadalupian ,
#fea38a,None,capitalien ,
#fe987e,None,Wordien ,
#fe8e72,None,radian ,
#f76e54,None,permien tôt ,
#f76e54,None,permien inférieur ,
#f76e54,None,cisalien ,
#ef947f,None,kungurien ,
#ef8a74,None,Artininskian ,
#ef806a,None,sakmarian ,
#f0775f,None,asselian ,
#3faead,None,carbonifère ,
#8ac6c3,None,carbonifère supérieur ,
#8ac6c3,None,pennsylvanien ,
#bdd0c4,None,Upper Pennsylvanian ,
#cbd5cd,None,gzhélian ,
#bbd1cd,None,kasimovien ,
#9dcac4,None,Cennsylvanien moyen ,
#9dcac4,None,milieu pennsylvanien ,
#aecdc4,None,moscovien ,
#77c2c3,None,Pennsylvanien inférieur ,
#8ac6c3,None,bashkirien ,
#619d7e,None,carbonifère inférieur ,
#619d7e,None,Mississippian ,
#bbc082,None,Haute Mississippian ,
#c8c281,None,serpukhovien ,
#9bb983,None,milieu mississippien ,
#abbc82,None,['visuel', 'visuelle'],
#7ab284,None,Mississippien inférieur ,
#8ab584,None,tournaisie ,
#dd9651,None,['dévonien', 'dévonienne'],
#f4e0a9,None,Haute-Dévonien ,
#f4e0a9,None,Dévonien tardif ,
#f3ebcc,None,frasnien ,
#f4eab9,None,faménien ,
#f6c87a,None,au milieu dévonien ,
#f6c87a,None,milieu Devonian ,
#f5de94,None,givétien ,
#f5d386,None,Eifelian ,
#efb063,None,bas dévonien ,
#efb063,None,Devonien tôt ,
#eccf87,None,Emsian ,
#eec57b,None,pragien ,
#eec57b,None,praghien ,
#eeba6e,None,lochkovien ,
#a6dfc5,None,['silurien', 'silurienne'],
#e4f2e6,None,Dernière silurienne ,
#e4f2e6,None,pridoli ,
#b4e5db,None,silurien tardif ,
#b4e5db,None,Silurien supérieur ,
#b4e5db,None,ludlow ,
#d4eee6,None,ludfordien ,
#c3eae6,None,gorsstian ,
#a4e0d0,None,silurien moyen ,
#a4e0d0,None,milieu sileurien ,
#a4e0d0,None,wenlock ,
#c5e9db,None,homérian ,
#b6e4d0,None,sheinwoodien ,
#7ed7c6,None,silurien inférieur ,
#7ed7c6,None,Silurien tôt ,
#7ed7c6,None,llandvery ,
#b4e5db,None,Telychian ,
#a4e0d0,None,aéronien ,
#93dbc6,None,rhuddanien ,
#00a98a,None,['ordovicien', 'ordovicienne'],
#5ecca9,None,Ordovicien supérieur ,
#5ecca9,None,Ordovicien tardif ,
#95dabc,None,hirnantian ,
#81d6bc,None,katian ,
#72d0a9,None,sandbien ,
#00bd97,None,Ordovicien du milieu ,
#00bd97,None,médiocre ,
#35c9b2,None,darriwilian ,
#12c5a9,None,dapingien ,
#00af89,None,Ordovicien inférieur ,
#00af89,None,premiers ordonnés ,
#00af89,None,tremadoc ,
#00af89,None,ashgill ,
#00baa0,None,floian ,
#00b698,None,tremadocien ,
#81aa72,None,Cambrien ,
#addda8,None,furongien ,
#addda8,None,Cambrian Series 4 ,
#addda8,None,Série 4 ,
#e5f1d1,None,Stage Cambrien 10 ,
#e5f1d1,None,étape 10 ,
#d8ecc6,None,joligshanian ,
#d8ecc6,None,Cambrian Stage 9 ,
#d8ecc6,None,étape 9 ,
#cae7bc,None,pabian ,
#a1cf9b,None,Cambrian Series 3 ,
#a1cf9b,None,Série 3 ,
#a1cf9b,None,Cambrien du milieu ,
#a1cf9b,None,mi-cambrien ,
#ccddb8,None,Guzhangian ,
#bfd8ad,None,drumian ,
#b2d4a3,None,Cambrien Stage 5 ,
#b2d4a3,None,Étape 5 ,
#95c28f,None,Cambrian Série 2 ,
#95c28f,None,Cambrien inférieur ,
#95c28f,None,Série 2 ,
#b4cba0,None,Cambrien Stage 4 ,
#b4cba0,None,étape 4 ,
#a5c697,None,Étape 3 Cambrien 3 ,
#a5c697,None,Étape 3 ,
#8ab584,None,terréavien ,
#8ab584,None,Cambrian Series 1 ,
#8ab584,None,Série 1 ,
#a8bd93,None,Étape 2 Cambrien ,
#a8bd93,None,étape 2 ,
#9aba8b,None,fortunien ,
#9aba8b,None,Cambrien Stage 1 ,
#9aba8b,None,étape 1 ,
#9fb885,None,Cambrian tôt ,
#fe5b71,None,précocbrien ,
#fe4c68,None,prothézoïque ,
#feb757,None,néoprotérozoïque ,
#fed67b,None,édiacaran ,
#fecc6f,None,cryogénien ,
#fec262,None,tonien ,
#feb872,None,mésoprotérozoïque ,
#fed9a2,None,sténien ,
#fece94,None,ectasien ,
#fec386,None,calymatique ,
#fe5b71,None,paléoprotérozoïque ,
#fe5b71,None,paléoprotérozoïque ,
#fe5b71,None,paléoprotérozoïque ,
#fe86a1,None,Stadaten ,
#fe7b94,None,orosirien ,
#fe7087,None,Rhyacien ,
#fe657b,None,Sideler ,
#fe007c,None,['archéen', 'archéenne'],
#fea6ba,None,néoarchéien ,
#fe7ca3,None,mésoarchéien ,
#fe5b97,None,paléoarchéien ,
#fe5b97,None,palæoarchéan ,
#fe5b97,None,paléoarchéien ,
#ee007d,None,eoarchien ,
#cb0381,None,hadian ,
"""

# USGS_ISC
USGS_ISC_TIMESCALE = """colour,width,component age
#99adac,None,['archéen', 'archéenne'],
#fa815f,None,Cambrien ,
#98bbd9,None,carbonifère ,
#ffff00,None,cénozoïque ,
#80cfc9,None,cisalien ,
#7fc21b,None,['crétacé', 'crétacée'],
#dbaaa9,None,cryogénien ,
#9999c9,None,['dévonien', 'dévonienne'],
#7f8f8f,None,eoarchaen ,
#ebae44,None,éocène ,
#9ad9d9,None,Guadalupian ,
#ffffb3,None,holocène ,
#4eb580,None,jurassique ,
#9858a8,None,llandvery ,
#b2e2ed,None,lopingien ,
#e87c72,None,Cambrien inférieur ,
#b1de7e,None,Crétacé inférieur ,
#807dba,None,bas dévonien ,
#65bf91,None,jurystique inférieur ,
#de7ca3,None,Ordovicien inférieur ,
#68b39f,None,triasique inférieur ,
#caa7d1,None,ludlow ,
#b2b5b0,None,mésoarchaen ,
#dec38a,None,mésoprotérozoïque ,
#7fad51,None,mésozoïque ,
#e8ae97,None,Cambrien du milieu ,
#9a84bf,None,au milieu dévonien ,
#7fc993,None,jurystique moyen ,
#fa9bb1,None,Ordovicien du milieu ,
#98d6bd,None,médiocre ,
#ffdd00,None,miocène ,
#7191ad,None,Mississippian ,
#caccc8,None,néoarchaen ,
#fccb8b,None,neogène ,
#c9a595,None,néoprotérozoïque ,
#ebd9bc,None,néoprotérozoiciiii ,
#ebc773,None,oligocène ,
#fa82a6,None,['ordovicien', 'ordovicienne'],
#997391,None,paléoarchaen ,
#eb9100,None,paléocène ,
#ffb300,None,paléogène ,
#b3b15f,None,paléoprotérozoïque ,
#81b5d6,None,paléozoïque ,
#679fc9,None,pennsylvanien ,
#68c6de,None,['permien', 'permienne'],
#b3e3d1,None,phanerozoïque ,
#ffea61,None,pléistocène ,
#ffecad,None,pliocène ,
#b38654,None,précocbrien ,
#e8c5e1,None,pridoli ,
#cdd991,None,prothézoïque ,
#ffff4d,None,quaternaire ,
#b172b5,None,['silurien', 'silurienne'],
#cca46c,None,tonien ,
#67c2b6,None,triassique ,
#fccdb8,None,Cambrien supérieur ,
#dff299,None,Crétacé supérieur ,
#cabddb,None,Haute-Dévonien ,
#ccebc5,None,Haut Jurassique ,
#fab4bd,None,Ordovicien supérieur ,
#ccede2,None,triassique supérieur ,
#b089b3,None,wenlock ,
"""


# =========== LEXIQUE ===========
LEXICON = {'lithology': ['mort-terrain', 'remblai', 'Quartzite', 'Tourbe', 'Alios', 'Trachyte', 'Granite', 'Ponce', 'Greisen', 'Monazite', 'Granodiorite', 'Anatexite', 'Houille', 'Ardoise', 'Anthracite', 'Poudingue', 'Cendres', 'Dolérite', 'Lapillis', 'Tuf volcanique', 'Silex', 'Aplite', 'éclogite', 'Glauconite', 'Bentonite', 'Andésite', 'Cendre', 'Grès', 'Amphibolite', 'Calcaire', 'Molasse', 'brèche', 'Marbre', 'Rhyolite', 'Radiolarite', 'Gabbro', 'Glauconie', 'Kersantite', 'Phonolite', 'tillite', 'Schiste', 'Syénite', 'Ignimbrite', 'Molasse ', 'Combarbalite', 'Gravier', 'Gypse', 'Conglomérat', 'Craie', 'Cargneule', 'Marne', 'Pierre coquillière', 'Dolomie', 'anhydrite', 'poudingue', 'Cinérite', 'Ophite', 'Pierre coquillère', 'Tuffeau', 'Argile', 'Halite', 'Bauxite', 'Micaschiste', 'Phtanite', 'Péridotite', 'Pyroxénite', 'Carbonatite', 'Kimberlite', 'Monzonite', 'Diatomite', 'Obsidienne', 'Jaspe', 'Arkose', 'Diorite', 'Dacite', 'Cipolin', 'Basalte', 'Sable', 'Pegmatite', 'Gneiss', 'Lignite', "Granite d'anatexie", 'Tuf', 'Silcrète', 'Porphyre', 'Brèche', 'Leptynite', 'Limon', 'Charbon', 'Gr(?:è|e|é)s', ],
           'state':['altéré(?:e|es)?', 'sain(?:s|e|es)?', 'hétérogène(?:s)?', 'homogène(?:s)?'],
           'shape':['lentille(?:s)?', 'biseau(x)?', 'strie(?:s)?', 'veine(?:s)?', 'filet(?:s)?', 'filon(?:s)?', 'intercalé(?:s|e|es)?', 'intercalation(?:s)?', 'interstratifié(?:s|e|es)?', 'tacheté(?:s|e|es)?', 'bande(?:s)?', 'bariolé(?:e|es)?' ],
           'material':['laitier', 'béton', 'scorie(?:s)?', 'ballast(?:s)?', 'g[e|é]otextile(?:s)?'],
           'modifier': ['silteu(?:x|se)', 'sableu(?:x|se)', 'argileu(?:x|se)', 'shisteu(?:x|se)', 'boueu(?:x|se)', 'caillouteu(?:x|se)', 'graveleu(?:x|se)', 'bitumineu(?:x|se)', 'pierreu(?:x|se)', 'saturé(?:e|es)?'],
           'colour': ['rouge(?:âtre)?', 'gris(?:e|âtre)?', 'noir(?:e|âtre)?', 'blanc(?:he|hâtre)?', 'bleu(?:e|âtre)?', 'ros(?:e|âtre)?', 'jaun(?:e|âtre)?', 'ver(?:t|dâtre)?', 'marron', 'clair(e)?', 'foncé(e)?','sombre'],
           'grainsize': ['(?:pluri(?:-)?)?(?:d[e|é]ci|centi|milli)?m[e|é]trique(?:s)?','vf(?:-)?', 'f(?:-)?', '\d+ m(?:-)?', 'c(?:-)?', 'vc', 'très fin(?:e à)?', 'fin(?:e|s|es à)?', 'moyen(?:ne à)?', 'grossi(?:er|ers|ère|ères à)?', 'très grossi(?:er|ère)', 't fin(?:e|s|es à)?', 'moy(?: à)?', 'moy.(?: à)?', 't grossier(?:s)?', 'granules?', 'cailloux?', 'galets?', 'blocs rocheux?'],
           'quantity': ['beaucoup', 'peu', 'moins', 'plusieurs', 'fragment(?:s)?', 'impurité(?:es)', 'abondant(?:e|es)', 'mineur', 'quelques', 'rare', 'flocon(?:s)?', 'trace(?:s)', '[-.\\d]+%', '[-.\\d]+pc', '[-.\\d]+pourcent'],
           'Pollutant':['naphtalène', 'HAP', 'huile(?:s)?'],
           'synonyms': {'mort-terrain': ['terre'], 'Anhydrite': ['Gypse'], 'Sel': ['Halite', 'Sylvite']},
           'splitters': [' avec ', ' de ', ' cont(?:ient|enant) ', '\\. '],
           'parts_of_speech': {'noun': ['lithology'], 'adjective': ['colour', 'grainsize', 'modifier'], 'subordinate': ['quantity']}
           }

# =========== COULEURS ===========
COLORS = {'k': '#000000', 'w': '#FFFFFF', 'r': '#FF0000', 'g': '#00FF00', 'b': '#0000FF', 'c': '#00FFFF', 'm': '#FF00FF', 'y': '#FFFF00', 'aliceblue': '#F0F8FF', 'antiquewhite': '#FAEBD7', 'aqua': '#00FFFF', 'aquamarine': '#7FFFD4', 'azure': '#F0FFFF', 'beige': '#F5F5DC', 'bisque': '#FFE4C4', 'black': '#000000', 'blanchedalmond': '#FFEBCD', 'blue': '#0000FF', 'blueviolet': '#8A2BE2', 'brown': '#A52A2A', 'burlywood': '#DEB887', 'cadetblue': '#5F9EA0', 'chartreuse': '#7FFF00', 'chocolate': '#D2691E', 'coral': '#FF7F50', 'cornflowerblue': '#6495ED', 'cornsilk': '#FFF8DC', 'crimson': '#DC143C', 'cyan': '#00FFFF', 'darkblue': '#00008B', 'darkcyan': '#008B8B', 'darkgoldenrod': '#B8860B', 'darkgray': '#A9A9A9', 'darkgreen': '#006400', 'darkkhaki': '#BDB76B', 'darkmagenta': '#8B008B', 'darkolivegreen': '#556B2F', 'darkorange': '#FF8C00', 'darkorchid': '#9932CC', 'darkred': '#8B0000', 'darksage': '#598556', 'darksalmon': '#E9967A', 'darkseagreen': '#8FBC8F', 'darkslateblue': '#483D8B', 'darkslategray': '#2F4F4F', 'darkturquoise': '#00CED1', 'darkviolet': '#9400D3', 'deeppink': '#FF1493', 'deepskyblue': '#00BFFF', 'dimgray': '#696969', 'dodgerblue': '#1E90FF', 'firebrick': '#B22222', 'floralwhite': '#FFFAF0', 'forestgreen': '#228B22', 'fuchsia': '#FF00FF', 'gainsboro': '#DCDCDC', 'ghostwhite': '#F8F8FF', 'gold': '#FFD700', 'goldenrod': '#DAA520', 'gray': '#808080', 'green': '#008000', 'greenyellow': '#ADFF2F', 'honeydew': '#F0FFF0', 'hotpink': '#FF69B4', 'indianred': '#CD5C5C', 'indigo': '#4B0082', 'ivory': '#FFFFF0', 'khaki': '#F0E68C', 'lavender': '#E6E6FA', 'lavenderblush': '#FFF0F5', 'lawngreen': '#7CFC00', 'lemonchiffon': '#FFFACD', 'lightblue': '#ADD8E6', 'lightcoral': '#F08080', 'lightcyan': '#E0FFFF', 'lightgoldenrodyellow': '#FAFAD2', 'lightgreen': '#90EE90', 'lightgray': '#D3D3D3', 'lightpink': '#FFB6C1', 'lightsage': '#BCECAC', 'lightsalmon': '#FFA07A', 'lightseagreen': '#20B2AA', 'lightskyblue': '#87CEFA', 'lightslategray': '#778899', 'lightsteelblue': '#B0C4DE', 'lightyellow': '#FFFFE0', 'lime': '#00FF00', 'limegreen': '#32CD32', 'linen': '#FAF0E6', 'magenta': '#FF00FF', 'maroon': '#800000', 'mediumaquamarine': '#66CDAA', 'mediumblue': '#0000CD', 'mediumorchid': '#BA55D3', 'mediumpurple': '#9370DB', 'mediumseagreen': '#3CB371', 'mediumslateblue': '#7B68EE', 'mediumspringgreen': '#00FA9A', 'mediumturquoise': '#48D1CC', 'mediumvioletred': '#C71585', 'midnightblue': '#191970', 'mintcream': '#F5FFFA', 'mistyrose': '#FFE4E1', 'moccasin': '#FFE4B5', 'navajowhite': '#FFDEAD', 'navy': '#000080', 'oldlace': '#FDF5E6', 'olive': '#808000', 'olivedrab': '#6B8E23', 'orange': '#FFA500', 'orangered': '#FF4500', 'orchid': '#DA70D6', 'palegoldenrod': '#EEE8AA', 'palegreen': '#98FB98', 'paleturquoise': '#AFEEEE', 'palevioletred': '#DB7093', 'papayawhip': '#FFEFD5', 'peachpuff': '#FFDAB9', 'peru': '#CD853F', 'pink': '#FFC0CB', 'plum': '#DDA0DD', 'powderblue': '#B0E0E6', 'purple': '#800080', 'red': '#FF0000', 'rosybrown': '#BC8F8F', 'royalblue': '#4169E1', 'saddlebrown': '#8B4513', 'salmon': '#FA8072', 'sage': '#87AE73', 'sandybrown': '#FAA460', 'seagreen': '#2E8B57', 'seashell': '#FFF5EE', 'sienna': '#A0522D', 'silver': '#C0C0C0', 'skyblue': '#87CEEB', 'slateblue': '#6A5ACD', 'slategray': '#708090', 'snow': '#FFFAFA', 'springgreen': '#00FF7F', 'steelblue': '#4682B4', 'tan': '#D2B48C', 'teal': '#008080', 'thistle': '#D8BFD8', 'tomato': '#FF6347', 'turquoise': '#40E0D0', 'violet': '#EE82EE', 'wheat': '#F5DEB3', 'white': '#FFFFFF', 'whitesmoke': '#F5F5F5', 'yellow': '#FFFF00', 'yellowgreen': '#9ACD32'}