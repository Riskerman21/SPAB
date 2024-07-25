const dict = {"Nonthaburi": ['Sai Noi District', 'Bang Bua Thong District', 'Bang Yai District', 'Pak Kret District', 'Bang Kruai District', 'Mueang Nonthaburi District'], 'Phra Nakhon Si Ayudhya': ['Phra Nakhon Si Ayutthaya District', 'Bang Ban District', 'Bang Pahan District', 'Phak Hai District', 'Lat Bua Luang District', 'Sena District', 'Bang Sai District', 'Maha Rat District', 'Ban Phraek District', 'Tha Ruea District', 'Nakhon Luang District', 'Bang Pa-in District', 'Phachi District', 'Wang Noi District', 'Uthai District'], 'Ang Thong': ['Mueang Ang Thong District', 'Chaiyo District', 'Pa Mok District', 'Pho Thong District', 'Wiset Chai Chan District', 'Sawaeng Ha District', 'Samko District'], 'Lopburi': ['Mueang Lop Buri District', 'Tha Wung District', 'Ban Mi District', 'Phatthana Nikom District', 'Khon Samrong District', 'Chai Badan District', 'Sa Bot District', 'Khok Charoen District', 'Nong Muang Khai District', 'Lam Sonthi District', 'Tha Luang District'], 'Singburi': ['Mueang Sing Buri District', 'Khai Bang Rachan District', 'Tha Chang District', 'In Buri District', 'Bang Rachan District', 'Phrom Buri District'], 'Saraburi': ['Don Phut District', 'Nong Don District', 'Nong Khae District', 'Wihan Daeng District', 'Mueang Saraburi District', 'Kaeng Khoi District', 'Nong Saeng District', 'Ban Mo District', 'Phra Phutthabat District', 'Sao Hai District', 'Chaloem Phra Kiat District', 'Wang Muang District'], 'Nakhon Sawan': ['Mueang Nakhon Sawan District', 'Krok Phra District', 'Chum Saeng District', 'Kao Liao District', 'Tha Tako District', 'Nong Bua District', 'Banphot Phisai District', 'Phaisali District', 'Lat Yao District', 'Mae Wong District', 'Chum Ta Bong District', 'Takhli District', 'Phayuha Khiri District', 'Tak Fa District'], 'Uthai Thani': ['Mueang Uthai Thani District', 'Sawang Arom District', 'Thap Than District', 'Nong Chang District', 'Nong Khayang District', 'Ban Rai District', 'Lan Sak District', 'Huai Khot District'], 'Suphan Buri': ['Mueang Suphan Buri District', 'Bang Pla Ma District', 'Song Phi Nong District', 'U Thong District', 'Si Prachan District', 'Nong Ya Sai District', 'Doem Bang Nang Buat District', 'Don Chedi District', 'Sam Chuk District', 'Dan Chang District'], 'Nakhon Prathom': ['Kamphaeng Saen District', 'Nakhon Chai Si District', 'Don Tum District', 'Bang Len District', 'Phutthamonthon District', 'Mueang Nakhon Pathom District', 'Sam Phran District'], 'Prachuap Khilikhan': ['Mueang Prachuap Khiri Khan District', 'Kui Buri District', 'Thap Sakae District', 'Bang Saphan District', 'Bang Saphan Noi District', 'Pran Buri District', 'Sam Roi Yot District', 'Hua Hin District'], 'Nakhon Si Thammarat': ['Mueang Nakhon Si Thammarat District', 'Phrom Khiri District', 'Lan Saka District', 'Chawang District', 'Chian Yai District', 'Cha-uat District', 'Tha Sala District', 'Thung Song District', 'Na Bon District', 'Thung Yai District', 'Pak Phanang District', 'Ron Phibun District', 'Sichon District', 'Khanom District', 'Hua Sai District', 'Bang Khan District', 'Tham Phannara District', 'Chulabhorn District', 'Phra Phrom District', 'Chaloem Phra Kiat District', 'Nopphitam District', 'Chang Klang District', 'Phipun District'], 'Surat Thani': ['Mueang Surat Thani District', 'Kanchanadit District', 'Don Sak District', 'Chaiya District', 'Tha Chana District', 'Tha Chang District', 'Ban Na San District', 'Ban Na Doem District', 'Khian Sa District', 'Wiang Sa District', 'Phrasaeng District', 'Phunphin District', 'Khiri Rat Nikhom District', 'Ban Ta Khun District', 'Phanom District', 'Ko Samui District', 'Chai Buri District'], 'Chumphon': ['Mueang Chumphon District', 'Tha Sae District', 'Pathio District', 'Lang Suan District', 'Lamae District', 'Sawi District', 'Thung Tako District'], 'Songkhla': ['Mueang Songkhla District', 'Sathing Phra District', 'Chanae District', 'Na Thawi District', 'Thepha District', 'Saba Yoi District', 'Ranot District', 'Krasae Sin District', 'Rattaphum District', 'Sadao District', 'Hat Yai District', 'Khuan Niang District', 'Bang Klam District', 'Singhanakhon District', 'Khlong Hoi Khong District', 'Na Mom District'], 'Trang': ['Mueang Trang District', 'Kantang District', 'Huai Yot District', 'Wang Wiset District', 'Ratsada District', 'Yan Ta Khao District', 'Palian District', 'Sikao District', 'Na Yong District'], 'Phatthalung': ['Mueang Phatthalung District', 'Khao Chaison District', 'Khuan Khanun District', 'Pak Phayun District', 'Pa Bon District', 'Bang Kaeo District', 'Kong Ra District', 'Tamot District', 'Si Banphot District', 'Srinagarindra District', 'Pa Phayom District'], 'Pattani': ['Mueang Pattani District', 'Khok Pho District', 'Nong Chik District', 'Panare District', 'Mayo District', 'Thung Yang Daeng District', 'Sai Buri District', 'Mae Kaen District', 'Yaring District', 'Yarang District', 'Kapho District', 'Mae Lan District'], 'Yala': ['Mueang Yala District', 'Yaha District', 'Raman District', 'Krong Pinang District', 'Bannang Sata District'], 'Narathiwat': ['Mueang Narathiwat District', 'Tak Bai District', 'Bacho District', 'Yi-ngo District', 'Ra-ngae District', 'Rueso District', 'Si Sakhon District', 'Waeng District', 'Su-ngai Kolok District', 'Su-ngai Padi District', 'Chanae District', 'Cho-airong District', 'Sukhirin District'], 'Samut Prakarn': ['Mueang Samut Prakan District', 'Bang Bo District', 'Bang Phli District', 'Bang Sao Thong District', 'Phra Pradaeng District', 'Phra Samut Chedi District'], 'Pathum Thani': ['Nong Suea District', 'Lat Lum Kaeo District', 'Mueang Pathum Thani District', 'Khlong Luang District', 'Thanyaburi District', 'Lam Luk Ka District', 'Sam Khok District'], 'Chonburi': ['Phan Thong District', 'Phanat Nikhom District', 'Mueang Chonburi District', 'Ban Bueng District', 'Bang Lamung District', 'Bo Thong District', 'Ko Chan District', 'Si Racha District'], 'Chachoengsao': ['Mueang Chachoengsao District', 'Bang Khla District', 'Bang Pakong District', 'Ban Pho District', 'Phanom Sarakham District', 'Ratchasan District', 'Plaeng Yao District', 'Khlong Khuean District', 'Bang Nam Priao District', 'Sanam Chai Khet District', 'Tha Takiap District'], 'Prachinburi': ['Mueang Prachin Buri District', 'Ban Sang District', 'Si Mahosot District', 'Kabin Buri District', 'Si Maha Phot District', 'Na Di District', 'Prachantakham District'], 'Nakhon Nayok': ['Mueang Nakhon Nayok District', 'Ban Na District', 'Ongkharak District', 'Pak Phli District'], 'Phang Nga': ['Takua Pa District', 'Mueang Phang-nga District', 'Khura Buri District', 'Thai Mueang District'], 'Chiang Mai': ['Chom Thong District', 'Mae Chaem District', 'San Pa Tong District', 'Hot District', 'Doi Tao District', 'Omkoi District', 'Mae Wang District', 'Doi Lo District', 'Mueang Chiang Mai District', 'Doi Saket District', 'Mae Taeng District', 'Mae Rim District', 'Phrao District', 'San Kamphaeng District', 'San Sai District', 'Hang Dong District', 'Saraphi District', 'Mae On District', 'Chiang Dao District', 'Fang District', 'Mae Ai District', 'Wiang Haeng District', 'Chai Prakan District'], 'Lamphun': ['Ban Hong District', 'Li District', 'Pa Sang District', 'Wiang Nong Long District', 'Mueang Lamphun District', 'Ban Thi District', 'Mae Tha District', 'Thung Hua Chang District'], 'Lampang': ['Mae Phrik District', 'Mueang Lampang District', 'Ko Kha District', 'Soem Ngam District', 'Thoeng District', 'Mae Tha District', 'Sop Prap District', 'Hang Chat District', 'Chae Hom District', 'Mueang Pan District', 'Mae Mo District', 'Ngao District', 'Wang Nuea District'], 'Mae Hong Son': ['Khun Yuam District', 'Mae Sariang District', 'Mae La Noi District', 'Sop Moei District', 'Pai District'], 'Tak': ['Mueang Tak District', 'Ban Tak District', 'Sam Ngao District', 'Mae Ramat District', 'Tha Song Yang District', 'Mae Sot District', 'Wang Chao District', 'Phop Phra District'], 'Krabi': ['Khao Phanom District', 'Ao Luek District', 'Plai Phraya District', 'Nuea Khlong District'], 'Satun': ['La-ngu District', 'Mueang Satun District', 'Khuan Don District', 'Khuan Kalong District', 'Tha Phae District', 'Manang District', 'Thung Wa District'], 'Srakaeo': ['Mueang Sa Kaeo District', 'Watthana Nakhon District', 'Aranyaprathet District', 'Khao Chakan District', 'Kok Sung District', 'Khlong Hat District', 'Ta Phraya District', 'Wang Nam Yen District', 'Wang Sombun District'], 'Nakhon Ratchasima': ['Mueang Nakhon Ratchasima District', 'Khon Buri District', 'Soeng Sang District', 'Khong District', 'Ban Lueam District', 'Chakkarat District', 'Chok Chai District', 'Dan Khun Thot District', 'Non Thai District', 'Non Sung District', 'Kham Sakaesaeng District', 'Pak Thong Chai District', 'Phimai District', 'Huai Thalaeng District', 'Chum Phuang District', 'Sung Noen District', 'Kham Thale So District', 'Sikhio District', 'Nong Bunmak District', 'Non Daeng District', 'Wang Nam Khiao District', 'Thepharak District', 'Phra Thong Kham District', 'Chaloem Phra Kiat District', 'Bua Yai District', 'Kaeng Sanam Nang District', 'Sida District', 'Prathai District', 'Mueang Yang District', 'Lam Thamenchai District', 'Bua Lai District', 'Pak Chong District'], 'Burirum': ['Mueang Buri Ram District', 'Krasang District', 'Nang Rong District', 'Nong Ki District', 'Prakhon Chai District', 'Lam Plai Mat District', 'Satuek District', 'Pakham District', 'Na Pho District', 'Nong Hong District', 'Phlapphla Chai District', 'Huai Rat District', 'Non Suwan District', 'Chamni District', 'Ban Dan District', 'Khaen Dong District', 'Chaloem Phra Kiat District', 'Khu Mueang District', 'Lahan Sai District', 'Non Din Daeng District', 'Phutthaisong District', 'Ban Mai Chaiyaphot District', 'Ban Kruat District'], 'Surin': ['Mueang Surin District', 'Chumphon Buri District', 'Prasat District', 'Tha Tum District', 'Chom Phra District', 'Rattanaburi District', 'Sanom District', 'Sikhoraphum District', 'Sangkha District', 'Lamduan District', 'Samrong Thap District', 'Buachet District', 'Si Narong District', 'Khwao Sinrin District', 'Non Narai District', 'Kap Choeng District', 'Phanom Dong Rak District'], 'Sisaket': ['Kantharalak District', 'Khukhan District', 'Phrai Bueng District', 'Khun Han District', 'Si Rattana District', 'Nam Kliang District', 'Phu Sing District', 'Benchalak District', 'Phayu District', 'Mueang Si Sa Ket District', 'Yang Chum Noi District', 'Kanthararom District', 'Prang Ku District', 'Rasi Salai District', 'Uthumphon Phisai District', 'Huai Thap Than District', 'Non Khun District', 'Wang Hin District', 'Sila Lat District', 'Bueng Bun District', 'Pho Si Suwan District', 'Mueang Chan District'], 'Ubon Ratchathani': ['Nam Khun District', 'Mueang Ubon Ratchathani District', 'Khueang Nai District', 'Muang Sam Sip District', 'Warin Chamrap District', 'Samrong District', 'Khemarat District', 'Det Udom District', 'Na Chaluai District', 'Nam Yuen District', 'Trakan Phuet Phon District', 'Kut Khaopun District', 'Phibun Mangsahan District', 'Tan Sum District', 'Don Mot Daeng District', 'Thung Si Udom District', 'Na Yia District', 'Na Tan District', 'Lao Suea Kok District', 'Sawang Wirawong District', 'Khong Chiam District', 'Sirindhorn District', 'Si Mueang Mai District', 'Buntharik District'], 'Chaiyaphum': ['Mueang Chaiyaphum District', 'Ban Khwao District', 'Kaset Sombun District', 'Nong Bua Daeng District', 'Chatturat District', 'Bamnet Narong District', 'Nong Bua Rawe District', 'Thep Sathit District', 'Phu Khiao District', 'Ban Thaen District', 'Kaeng Khro District', 'Khon San District', 'Noen Sa-nga District', 'Sap Yai District', 'Khon Sawan District', 'Phakdi Chumphon District'], 'Nong Bua Lamphu': ['Non Sang District', 'Si Bun Rueang District', 'Suwannakhuha District', 'Na Klang District', 'Na Wang District', 'Mueang Nong Bua Lam Phu District'], 'Khon Kaen': ['Nong Ruea District', 'Chum Phae District', 'Phon District', 'Nong Song Hong District', 'Phu Pha Man District', 'Nong Na Kham District', 'Mueang Khon Kaen District', 'Phra Yuen District', 'Si Chomphu District', 'Nam Phong District', 'Ubolratana District', 'Kranuan District', 'Ban Phai District', 'Pueai Noi District', 'Waeng Yai District', 'Waeng Noi District', 'Phu Wiang District', 'Mancha Khiri District', 'Chonnabot District', 'Khao Suan Kwang District', 'Sam Sung District', 'Khok Pho Chai District', 'Ban Haet District', 'Non Sila District', 'Wiang Kao District', 'Ban Fang District'], 'Udon Thani': ['Ban Phue District', 'Mueang Udon Thani District', 'Kumphawapi District', 'Nong Han District', 'Thung Fon District', 'Chai Wan District', 'Si That District', 'Ban Dung District', 'Phen District', 'Sang Khom District', 'Phibun Rak District', 'Ku Kaeo District', 'Prachak Sinlapakhom District', 'Kut Chap District', 'Nong Wua So District', 'Nam Som District', 'Wang Sam Mo District'], 'Loei': ['Mueang Loei District', 'Chiang Khan District', 'Wang Saphung District', 'Dan Sai District', 'Tha Li District', 'Na Duang District', 'Phu Kradueng District', 'Phu Luang District', 'Erawan District', 'Nong Hin District'], 'Nong Khai': ['Tha Bo District', 'Si Chiang Mai District', 'Mueang Nong Khai District', 'Phon Phisai District', 'Sangkhom District', 'Fao Rai District', 'Rattanawapi District', 'Pho Tak District', 'Sakhrai District'], 'Mahasarakham': ['Phayakkhaphum Phisai District', 'Wapi Pathum District', 'Na Dun District', 'Yang Si Surat District', 'Mueang Maha Sarakham District', 'Kosum Phisai District', 'Kantharawichai District', 'Chiang Yuen District', 'Borabue District', 'Na Chueak District', 'Kut Rang District', 'Chuen Chom District', 'Kae Dam District'], 'Roi Et': ['Pathum Rat District', 'Mueang Roi Et District', 'Kaset Wisai District', 'Chaturapak Phiman District', 'Thawat Buri District', 'Suwannaphum District', 'Mueang Suang District', 'Phanom Phrai District', 'Phon Thong District', 'Pho Chai District', 'Nong Phok District', 'Selaphum District', 'Phon Sai District', 'At Samat District', 'Moei Wadi District', 'Changhan District', 'Chiang Khwan District', 'Nong Hi District', 'Thung Khao Luang District', 'Si Somdet District'], 'Auttaradit': ['Mueang Uttaradit District', 'Tron District', 'Tha Pla District', 'Phichai District', 'Laplae District', 'Thong Saen Khan District', 'Nam Pat District', 'Fak Tha District', 'Ban Khok District'], 'Phrae': ['Mueang Phrae District', 'Rong Kwang District', 'Sung Men District', 'Den Chai District', 'Song District', 'Nong Muang Khai District', 'Long District', 'Wang Chin District'], 'Phayao': ['Mueang Phayao District', 'Chun District', 'Chiang Kham District', 'Dok Khamtai District', 'Mae Chai District', 'Phu Kamyao District', 'Phu Sang District', 'Chiang Muan District', 'Pong District'], 'Chiangrai': ['Mueang Chiang Rai District', 'Wiang Chai District', 'Thoeng District', 'Phan District', 'Pa Daet District', 'Phaya Mengrai District', 'Chiang Khong District', 'Mae Chan District', 'Chiang Saen District', 'Mae Sai District', 'Wiang Pa Pao District', 'Khun Tan District', 'Wiang Chiang Rung District', 'Mae Suai District', 'Mae Lao District', 'Doi Luang District', 'Wiang Kaen District'], 'Kampaeng Phet': ['Mueang Kamphaeng Phet District', 'Sai Ngam District', 'Khlong Lan District', 'Khanu Woralaksaburi District', 'Khlong Khlung District', 'Phran Kratai District', 'Lan Krabue District', 'Sai Thong Watthana District', 'Pang Sila Thong District', 'Bueng Samakkhi District', 'Kosamphi Nakhon District'], 'Sukhothai': ['Mueang Sukhothai District', 'Ban Dan Lan Hoi District', 'Khiri Mat District', 'Kong Krailat District', 'Si Satchanalai District', 'Si Samrong District', 'Sawankhalok District', 'Si Nakhon District', 'Thung Saliam District'], 'Phitsanu Lok': ['Mueang Phitsanulok District', 'Bang Rakam District', 'Bang Krathum District', 'Phrom Phiram District', 'Wat Bot District', 'Wang Thong District', 'Noen Maprang District', 'Nakhon Thai District', 'Chat Trakan District'], 'Phichit': ['Mueang Phichit District', 'Wang Sai Phun District', 'Pho Prathap Chang District', 'Taphan Hin District', 'Bang Mun Nak District', 'Pho Thale District', 'Sam Ngam District', 'Thap Khlo District', 'Sak Lek District', 'Bueng Na Rang District', 'Dong Charoen District', 'Wachirabarami District'], 'Phetchabun': ['Mueang Phetchabun District', 'Chon Daen District', 'Lom Sak District', 'Lom Kao District', 'Wichian Buri District', 'Si Thep District', 'Nong Phai District', 'Bueng Sam Phan District', 'Wang Pong District', 'Khao Kho District'], 'Kanchanaburi': ['Phanom Thuan District', 'Huai Krachao District', 'Tha Maka District', 'Tha Muang District', 'Mueang Kanchanaburi District', 'Bo Phloi District', 'Lao Khwan District', 'Dan Makham Tia District'], 'Bangkok': ['Nong Chok District', 'Bang Khen District', 'Min Buri District', 'Lat Krabang District', 'Bang Khun Thian District', 'Prawet District', 'Don Mueang District', 'Sai Mai District', 'Khan Na Yao District', 'Khlong Sam Wa District', 'Thawi Watthana District', 'Bang Kapi District', 'Nong Khaem District', 'Bueng Kum District', 'Lat Phrao District', 'Lak Si District', 'Saphan Sung District', 'Phra Nakhon District', 'Dusit District', 'Pathum Wan District', 'Phaya Thai District', 'Huai Khwang District', 'Khlong San District', 'Taling Chan District', 'Bangkok Noi District', 'Bang Phlat District', 'Din Daeng District', 'Bang Sue District', 'Chatuchak District', 'Khlong Toei District', 'Suan Luang District', 'Chom Thong District', 'Ratchathewi District', 'Bang Khae District', 'Wang Thonglang District', 'Bang Na District', 'Bang Rak District', 'Pom Prap Sattru Phai District', 'Phra Khanong District', 'Yan Nawa District', 'Samphanthawong District', 'Thon Buri District', 'Bangkok Yai District', 'Phasi Charoen District', 'Rat Burana District', 'Sathon District', 'Bang Kho Laem District', 'Vadhana District', 'Thung Khru District', 'Bang Bon District'], 'Chainat': ['Mueang Chai Nat District', 'Manorom District', 'Wat Sing District', 'Sapphaya District', 'Sankhaburi District', 'Hankha District', 'Nong Mamong District', 'Noen Kham District'], 'Yasothon': ['Maha Chana Chai District', 'Kho Wang District', 'Mueang Yasothon District', 'Sai Mun District', 'Kut Chum District', 'Kham Khuean Kaeo District', 'Pa Tio District', 'Loeng Nok Tha District', 'Thai Charoen District'], 'Amnaj Charoen': ['Hua Taphan District', 'Mueang Amnat Charoen District', 'Chanuman District', 'Pathum Ratchawongsa District', 'Phana District', 'Senangkhanikhom District', 'Lue Amnat District'], 'Nan': ['Mueang Nan District', 'Pua District', 'Tha Wang Pha District', 'Wiang Sa District', 'Chiang Klang District', 'Phu Phiang District', 'Ban Luang District', 'Na Noi District', 'Thung Chang District', 'Na Muen District', 'Santi Suk District', 'Mae Charim District'], 'Ratchaburi': ['Mueang Ratchaburi District', 'Damnoen Saduak District', 'Ban Pong District', 'Bang Phae District', 'Photharam District', 'Chom Bueng District', 'Pak Tho District', 'Wat Phleng District'], 'Samut Sakhon': ['Mueang Samut Sakhon District', 'Krathum Baen District', 'Ban Phaeo District'], 'Samut Songkham': ['Mueang Samut Songkhram District', 'Amphawa District'], 'Phetchaburi': ['Mueang Phetchaburi District', 'Khao Yoi District', 'Ban Laem District', 'Tha Yang District', 'Ban Lat District', 'Kaeng Krachan District', 'Cha-am District'], 'Rayong': ['Klaeng District', 'Mueang Rayong District', 'Ban Khai District', 'Pluak Daeng District', 'Nikhom Phatthana District'], 'Chanthaburi': ['Mueang Chanthaburi District', 'Khlung District', 'Tha Mai District', 'Makham District', 'Laem Sing District', 'Na Yai Am District', 'Khao Khitchakut District'], 'Trat': ['Mueang Trat District', 'Khao Saming District', 'Bo Rai District'], 'Bung Kan': ['Mueang Bueng Kan District', 'Phon Charoen District', 'So Phisai District', 'Bueng Khong Long District', 'Bung Khla District', 'Pak Khat District', 'Si Wilai District'], 'Bung kan': ['Seka District'], 'Kalasin': ['Mueang Kalasin District', 'Na Mon District', 'Kamalasai District', 'Rong Kham District', 'Kuchinarai District', 'Khao Wong District', 'Yang Talat District', 'Huai Mek District', 'Sahatsakhan District', 'Kham Muang District', 'Tha Khantho District', 'Nong Kung Si District', 'Somdet District', 'Huai Phueng District', 'Sam Chai District', 'Na Khu District', 'Don Chan District', 'Khong Chai District'], 'Sakon Nakhon': ['Mueang Sakon Nakhon District', 'Kusuman District', 'Kut Bak District', 'Phanna Nikhom District', 'Phang Khon District', 'Waritchaphum District', 'Nikhom Nam Un District', 'Wanon Niwat District', 'Kham Ta Kla District', 'Ban Muang District', 'Akat Amnuai District', 'Sawang Daen Din District', 'Song Dao District', 'Tao Ngoi District', 'Khok Si Suphan District', 'Charoen Sin District', 'Phon Na Kaeo District', 'Phu Phan District'], 'Nakhon Phanom': ['Mueang Nakhon Phanom District', 'Pla Pak District', 'Tha Uthen District', 'Ban Phaeng District', 'That Phanom District', 'Renu Nakhon District', 'Na Kae District', 'Si Songkhram District', 'Na Wa District', 'Phon Sawan District', 'Na Thom District', 'Wang Yang District'], 'Mukdahan': ['Mueang Mukdahan District', 'Nikhom Kham Soi District', 'Don Tan District', 'Dong Luang District', 'Khamcha-i District', 'Wan Yai District', 'Nong Sung District']}

// maps.js
document.addEventListener('DOMContentLoaded', function() {
    var provinceData = dict;

    var provinces = Object.keys(provinceData);
    $('#province').empty();
    $('#province').append('<option value="">Select a province</option>');
    $('#amphoe').append('<option value="">Please select a province first</option>'); // Default message
    provinces.forEach(function(province) {
        $('#province').append('<option value="' + province + '">' + province + '</option>');
    });

    // Populate amphoes based on selected province
    $('#province').on('change', function() {
        var selectedProvince = $(this).val();
        var amphoes = provinceData[selectedProvince] || [];

        $('#amphoe').empty();
        $('#amphoe').append('<option value="">Please select a amphoe</option>'); // Default message

        amphoes.forEach(function(amphoe) {
            $('#amphoe').append('<option value="' + amphoe + '">' + amphoe + '</option>');
        });
    });

    document.getElementById('signup-form').addEventListener('submit', function(event) {
        event.preventDefault(); 

        var email = document.getElementById('email').value;
    
        // Send the email to the server using AJAX
        fetch('http://127.0.0.1:5000/send_email', {  // Ensure this URL is correct
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: email })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
    
            // Switch to signup.html
            window.location.href = 'signup.html';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
 
    document.getElementById('predict-button').addEventListener('click', function(event) {
        event.preventDefault();
    
        var amphoe = document.getElementById('amphoe').value;
        var province = document.getElementById('province').value;
        var month = document.getElementById('month').value;
    
        const response = fetch('http://127.0.0.1:5000/long_predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                month: month,
                amphoe: amphoe,
                province: province
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.predictions);
            const riskContainer = document.getElementById('current-risk');

            // Update width based on risk level
            switch (data.predictions) {
                case 'Low Risk':
                    widthPercentage = 18; // Set the desired width for low risk
                    break;
                case 'Medium Risk':
                    widthPercentage = 50; // Set the desired width for medium risk
                    break;
                case 'High Risk':
                    widthPercentage = 83; // Set the desired width for high risk
                    break;
                default:
                    widthPercentage = 0; // Default width if risk level is unknown
                    break;
            }
            
            riskContainer.style.width = `${widthPercentage}%`;
        })
        .catch((error) => {
            console.error('Error:', error);
        });

        console.log();
    });  
});

async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatContent = document.getElementById('chat-content');

    // Add user's message to the chat
    const userMessageDiv = document.createElement('div');
    userMessageDiv.textContent = userInput;
    chatContent.appendChild(userMessageDiv);

    // Style "You: " part separately
    const youSpan = document.createElement('span');
    youSpan.textContent = 'You: ';
    youSpan.style.fontWeight = 'bold';  // Apply bold font weight
    userMessageDiv.insertBefore(youSpan, userMessageDiv.firstChild);  // Insert "You: " at the beginning of userMessageDiv

    // Send user's message to the server
    const response = await fetch('http://127.0.0.1:5000/send_to_bot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    });

    const responseData = await response.json();

    // Add bot's response to the chat
    const botMessageDiv = document.createElement('div');
    const botResponse = responseData.answer;

    // Creating elements and applying styles
    const steveSpan = document.createElement('span');
    steveSpan.textContent = 'Steve: ';
    steveSpan.style.fontWeight = 'bold';  // Make "Steve" bold

    const responseSpan = document.createElement('span');
    responseSpan.textContent = botResponse;

    // Add both spans to the div
    botMessageDiv.appendChild(steveSpan);
    botMessageDiv.appendChild(responseSpan);

    // Add botMessageDiv to chatContent (assuming chatContent is your chat area)
    chatContent.appendChild(botMessageDiv);

    // Scroll to the bottom of the chat content
    chatContent.scrollTop = chatContent.scrollHeight;

    // Clear the input field
    document.getElementById('user-input').value = '';
}

function toggleChatbot() {
    var chatbot = document.getElementById('chatbot-overlay');
    if (chatbot.style.display === 'none' || chatbot.style.display === '') {
        chatbot.style.display = 'block';
    } else {
        chatbot.style.display = 'none';
    }
}  

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}