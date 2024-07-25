import json

dict = {'Sakon Nakhon': ['Akat Amnuai', 'Ban Muang', 'Charoen Sin', 'Kham Ta Kla', 'Khok Si Suphan', 'Kusuman', 'Kut Bak', 'Mueang Sakon Nakhon', 'Nikhom Nam Un', 'Phang Khon', 'Phanna Nikhom', 'Phon Na Kaeo', 'Phu Phan', 'Sawang Daen Din', 'Song Dao', 'Tao Ngoi', 'Wanon Niwat', 'Waritchaphum'], 
        'Samut Songkhram': ['Amphawa', 'Bang Khonthi', 'Mueang Samut Songkhram'], 
        'Krabi': ['Ao Luek', 'Khao Phanom', 'Khlong Thom', 'Ko Lanta', 'Lam Thap', 'Mueang Krabi', 'Nuea Khlong', 'Plai Phraya'], 
        'Sa Kaeo': ['Aranyaprathet', 'Khao Chakan', 'Khlong Hat', 'Khok Sung', 'Mueang Sa Kaeo', 'Ta Phraya', 'Wang Nam Yen', 'Wang Sombun', 'Watthana Nakhon'], 
        'Roi Et': ['At Samat', 'Changhan', 'Chaturaphak Phiman', 'Chiang Khwan', 'Kaset Wisai', 'Moei Wadi', 'Mueang Roi Et', 'Mueang Suang', 'Nong Hi', 'Nong Phok', 'Pathum Rat', 'Phanom Phrai', 'Pho Chai', 'Phon Sai', 'Phon Thong', 'Selaphum', 'Si Somdet', 'Suwannaphum', 'Thawat Buri', 'Thung Khao Luang'], 
        'Narathiwat': ['Bacho', 'Chanae', 'Cho-airong', 'Mueang Narathiwat', 'Ra-ngae', 'Rueso', 'Si Sakhon', 'Su-ngai Kolok', 'Su-ngai Padi', 'Sukhirin', 'Tak Bai', 'Waeng', 'Yi-ngo'], 
        'Chaiyaphum': ['Bamnet Narong', 'Ban Khwao', 'Ban Thaen', 'Chatturat', 'Kaeng Khro', 'Kaset Sombun', 'Khon San', 'Khon Sawan', 'Mueang Chaiyaphum', 'Noen Sa-nga', 'Nong Bua Daeng', 'Nong Bua Rawe', 'Phakdi Chumphon', 'Phu Khiao', 'Sap Yai', 'Thep Sathit'], 
        'Chonburi': ['Ban Bueng', 'Bang Lamung', 'Bo Thong', 'Ko Chan', 'Ko Sichang', 'Mueang Chonburi', 'Nong Yai', 'Phan Thong', 'Phanat Nikhom', 'Sattahip', 'Si Racha'], 
        'Rayong': ['Ban Chang', 'Ban Khai', 'Khao Chamao', 'Klaeng', 'Mueang Rayong', 'Nikhom Phatthana', 'Pluak Daeng', 'Wang Chan'], 
        'Buriram': ['Ban Dan', 'Ban Kruat', 'Ban Mai Chaiyaphot', 'Chaloem Phra Kiat', 'Chamni', 'Huai Rat', 'Khaen Dong', 'Khu Mueang', 'Krasang', 'Lahan Sai', 'Lam Plai Mat', 'Mueang Buriram', 'Na Pho', 'Nang Rong', 'Non Din Daeng', 'Non Suwan', 'Nong Hong', 'Nong Ki', 'Pakham', 'Phlapphla Chai', 'Phutthaisong', 'Prakhon Chai', 'Satuek'], 
        'Sukhothai': ['Ban Dan Lan Hoi', 'Khiri Mat', 'Kong Krailat', 'Mueang Sukhothai', 'Sawankhalok', 'Si Nakhon', 'Si Samrong', 'Si Satchanalai', 'Thung Saliam'], 
        'Udon Thani': ['Ban Dung', 'Ban Phue', 'Chai Wan', 'Ku Kaeo', 'Kumphawapi', 'Kut Chap', 'Mueang Udon Thani', 'Na Yung', 'Nam Som', 'Non Sa-at', 'Nong Han', 'Nong Saeng', 'Nong Wua So', 'Phen', 'Phibun Rak', 'Prachaksinlapakhom', 'Sang Khom', 'Si That', 'Thung Fon', 'Wang Sam Mo'], 
        'Khon Kaen': ['Ban Fang', 'Ban Haet', 'Ban Phai', 'Chonnabot', 'Chum Phae', 'Khao Suan Kwang', 'Khok Pho Chai', 'Kranuan', 'Mancha Khiri', 'Mueang Khon Kaen', 'Nam Phong', 'Non Sila', 'Nong Na Kham', 'Nong Ruea', 'Nong Song Hong', 'Phon', 'Phra Yuen', 'Phu Pha Man', 'Phu Wiang', 'Pueai Noi', 'Sam Sung', 'Si Chomphu', 'Ubolratana', 'Waeng Noi', 'Waeng Yai', 'Wiang Kao'], 
        'Lamphun': ['Ban Hong', 'Ban Thi', 'Li', 'Mae Tha, Lamphun', 'Mueang Lamphun', 'Pa Sang', 'Thung Hua Chang', 'Wiang Nong Long'], 
        'Ratchaburi': ['Ban Kha', 'Ban Pong', 'Bang Phae', 'Chom Bueng', 'Damnoen Saduak', 'Mueang Ratchaburi', 'Pak Tho', 'Photharam', 'Suan Phueng', 'Wat Phleng'], 
        'Uttaradit': ['Ban Khok', 'Fak Tha', 'Laplae', 'Mueang Uttaradit', 'Nam Pat', 'Phichai', 'Tha Pla', 'Thong Saen Khan', 'Tron'], 
        'Phetchaburi': ['Ban Laem', 'Ban Lat', 'Cha-am', 'Kaeng Krachan', 'Khao Yoi', 'Mueang Phetchaburi', 'Nong Ya Plong', 'Tha Yang'], 
        'Nan': ['Ban Luang', 'Bo Kluea', 'Chaloem Phra Kiat', 'Chiang Klang', 'Mae Charim', 'Mueang Nan', 'Na Muen', 'Na Noi', 'Phu Phiang', 'Pua', 'Santi Suk', 'Song Khwae', 'Tha Wang Pha', 'Thung Chang', 'Wiang Sa'], 
        'Nakhon Ratchasima': ['Ban Lueam', 'Bua Lai', 'Bua Yai', 'Chaloem Phra Kiat', 'Chakkarat', 'Chok Chai', 'Chum Phuang', 'Dan Khun Thot', 'Huai Thalaeng', 'Kaeng Sanam Nang', 'Kham Sakaesaeng', 'Kham Thale So', 'Khon Buri', 'Khong', 'Lam Thamenchai', 'Mueang Nakhon Ratchasima', 'Mueang Yang', 'Non Daeng', 'Non Sung', 'Non Thai', 'Nong Bun Mak', 'Pak Chong', 'Pak Thong Chai', 'Phimai', 'Phra Thong Kham', 'Prathai', 'Sida', 'Sikhio', 'Soeng Sang', 'Sung Noen', 'Thepharak', 'Wang Nam Khiao'], 
        'Lopburi': ['Ban Mi', 'Chai Badan', 'Khok Charoen', 'Khok Samrong', 'Lam Sonthi', 'Mueang Lopburi', 'Nong Muang', 'Phatthana Nikhom', 'Sa Bot', 'Tha Luang', 'Tha Wung'], 
        'Saraburi': ['Ban Mo', 'Chaloem Phra Kiat', 'Don Phut', 'Kaeng Khoi', 'Muak Lek', 'Mueang Saraburi', 'Nong Don', 'Nong Khae', 'Nong Saeng', 'Phra Phutthabat', 'Sao Hai', 'Wang Muang', 'Wihan Daeng'],
        'Nakhon Nayok': ['Ban Na', 'Mueang Nakhon Nayok', 'Ongkharak', 'Pak Phli'], 
        'Surat Thani': ['Ban Na Doem', 'Ban Na San', 'Ban Ta Khun', 'Chai Buri', 'Chaiya', 'Don Sak', 'Kanchanadit', 'Khian Sa', 'Khiri Rat Nikhom', 'Ko Pha-ngan', 'Ko Samui', 'Mueang Surat Thani', 'Phanom', 'Phrasaeng', 'Phunphin', 'Tha Chana', 'Tha Chang', 'Vibhavadi', 'Wiang Sa'], 
        'Nakhon Phanom': ['Ban Phaeng', 'Mueang Nakhon Phanom', 'Na Kae', 'Na Thom', 'Na Wa', 'Phon Sawan', 'Pla Pak', 'Renu Nakhon', 'Si Songkhram', 'Tha Uthen', 'That Phanom', 'Wang Yang'], 
        'Samut Sakhon': ['Ban Phaeo', 'Krathum Baen', 'Mueang Samut Sakhon'], 
        'Chachoengsao': ['Ban Pho', 'Bang Khla', 'Bang Nam Priao', 'Bang Pakong', 'Khlong Khuean', 'Mueang Chachoengsao', 'Phanom Sarakham', 'Plaeng Yao', 'Ratchasan', 'Sanam Chai Khet', 'Tha Takiap'], 
        'Phra Nakhon Si Ayutthaya': ['Ban Phraek', 'Bang Ban', 'Bang Pa-in', 'Bang Pahan', 'Bang Sai 1404', 'Bang Sai 1413', 'Lat Bua Luang', 'Maha Rat', 'Nakhon Luang', 'Phachi', 'Phak Hai', 'Phra Nakhon Si Ayutthaya', 'Sena', 'Tha Ruea', 'Uthai', 'Wang Noi'], 
        'Uthai Thani': ['Ban Rai', 'Huai Khot', 'Lan Sak', 'Mueang Uthai Thani', 'Nong Chang', 'Nong Khayang', 'Sawang Arom', 'Thap Than'], 
        'Prachinburi': ['Ban Sang', 'Kabin Buri', 'Mueang Prachinburi', 'Na Di', 'Prachantakham', 'Si Maha Phot', 'Si Mahosot'], 
        'Tak': ['Ban Tak', 'Mae Ramat', 'Mae Sot', 'Mueang Tak', 'Phop Phra', 'Sam Ngao', 'Tha Song Yang', 'Umphang', 'Wang Chao'], 
        'Samut Prakan': ['Bang Bo', 'Bang Phli', 'Bang Sao Thong', 'Mueang Samut Prakan', 'Phra Pradaeng', 'Phra Samut Chedi'], 
        'Nonthaburi': ['Bang Bua Thong', 'Bang Kruai', 'Bang Yai', 'Mueang Nonthaburi', 'Pak Kret', 'Sai Noi'], 
        'Phatthalung': ['Bang Kaeo', 'Khao Chaison', 'Khuan Khanun', 'Kong Ra', 'Mueang Phatthalung', 'Pa Bon', 'Pa Phayom', 'Pak Phayun', 'Si Banphot', 'Srinagarindra', 'Tamot'], 'Nakhon Si Thammarat': ['Bang Khan', 'Cha-uat', 'Chaloem Phra Kiat', 'Chang Klang', 'Chawang', 'Chian Yai', 'Chulabhorn', 'Hua Sai', 'Khanom', 'Lan Saka', 'Mueang Nakhon Si Thammarat', 'Na Bon', 'Nopphitam', 'Pak Phanang', 'Phipun', 'Phra Phrom', 'Phrom Khiri', 'Ron Phibun', 'Sichon', 'Tha Sala', 'Tham Phannara', 'Thung Song', 'Thung Yai'], 'Songkhla': ['Bang Klam', 'Chana', 'Hat Yai', 'Khlong Hoi Khong', 'Khuan Niang', 'Krasae Sin', 'Mueang Songkhla', 'Na Mom', 'Na Thawi', 'Ranot', 'Rattaphum', 'Saba Yoi', 'Sadao', 'Sathing Phra', 'Singhanakhon', 'Thepha'], 
        'Phitsanulok': ['Bang Krathum', 'Bang Rakam', 'Chat Trakan', 'Mueang Phitsanulok', 'Nakhon Thai', 'Noen Maprang', 'Phrom Phiram', 'Wang Thong', 'Wat Bot'], 
        'Nakhon Pathom': ['Bang Len', 'Don Tum', 'Kamphaeng Saen', 'Mueang Nakhon Pathom', 'Nakhon Chai Si', 'Phutthamonthon', 'Sam Phran'], 
        'Phichit': ['Bang Mun Nak', 'Bueng Na Rang', 'Dong Charoen', 'Mueang Phichit', 'Pho Prathap Chang', 'Pho Thale', 'Sak Lek', 'Sam Ngam', 'Taphan Hin', 'Thap Khlo', 'Wachirabarami', 'Wang Sai Phun'], 
        'Suphan Buri': ['Bang Pla Ma', 'Dan Chang', 'Doem Bang Nang Buat', 'Don Chedi', 'Mueang Suphanburi', 'Nong Ya Sai', 'Sam Chuk', 'Si Prachan', 'Song Phi Nong', 'U Thong'], 
        'Sing Buri': ['Bang Rachan', 'In Buri', 'Khai Bang Rachan', 'Mueang Sing Buri', 'Phrom Buri', 'Tha Chang'], 
        'Prachuap Khiri Khan': ['Bang Saphan', 'Bang Saphan Noi', 'Hua Hin', 'Kui Buri', 'Mueang Prachuap Khiri Khan', 'Pran Buri', 'Sam Roi Yot', 'Thap Sakae'], 
        'Yala': ['Bannang Sata', 'Betong', 'Kabang', 'Krong Pinang', 'Mueang Yala', 'Raman', 'Than To', 'Yaha'], 
        'Nakhon Sawan': ['Banphot Phisai', 'Chum Saeng', 'Chum Ta Bong', 'Kao Liao', 'Krok Phra', 'Lat Yao', 'Mae Poen', 'Mae Wong', 'Mueang Nakhon Sawan', 'Nong Bua', 'Phaisali', 'Phayuha Khiri', 'Tak Fa', 'Takhli', 'Tha Tako'], 
        'Sisaket': ['Benchalak', 'Bueng Bun', 'Huai Thap Than', 'Kantharalak', 'Kanthararom', 'Khukhan', 'Khun Han', 'Mueang Chan', 'Mueang Sisaket', 'Nam Kliang', 'Non Khun', 'Phayu', 'Pho Si Suwan', 'Phrai Bueng', 'Phu Sing', 'Prang Ku', 'Rasi Salai', 'Si Rattana', 'Sila Lat', 'Uthumphon Phisai', 'Wang Hin', 'Yang Chum Noi'], 
        'Kanchanaburi': ['Bo Phloi', 'Dan Makham Tia', 'Huai Krachao', 'Lao Khwan', 'Mueang Kanchanaburi', 'Nong Prue', 'Phanom Thuan', 'Sai Yok', 'Sangkhla Buri', 'Si Sawat', 'Tha Maka', 'Tha Muang', 'Thong Pha Phum'], 
        'Trat': ['Bo Rai', 'Khao Saming', 'Khlong Yai', 'Ko Chang', 'Ko Kut', 'Laem Ngop', 'Mueang Trat'], 
        'Maha Sarakham': ['Borabue', 'Chiang Yuen', 'Chuen Chom', 'Kae Dam', 'Kantharawichai', 'Kosum Phisai', 'Kut Rang', 'Mueang Maha Sarakham', 'Na Chueak', 'Na Dun', 'Phayakkhaphum Phisai', 'Wapi Pathum', 'Yang Sisurat'], 
        'Surin': ['Buachet', 'Chom Phra', 'Chumphon Buri', 'Kap Choeng', 'Khwao Sinarin', 'Lamduan', 'Mueang Surin', 'Non Narai', 'Phanom Dong Rak', 'Prasat', 'Rattanaburi', 'Samrong Thap', 'Sangkha', 'Sanom', 'Si Narong', 'Sikhoraphum', 'Tha Tum'], 
        'Bueng Kan': ['Bueng Khong Long', 'Bung Khla', 'Mueang Bueng Kan', 'Pak Khat', 'Phon Charoen', 'Seka', 'Si Wilai', 'So Phisai'], 
        'Phetchabun': ['Bueng Sam Phan', 'Chon Daen', 'Khao Kho', 'Lom Kao', 'Lom Sak', 'Mueang Phetchabun', 'Nam Nao', 'Nong Phai', 'Si Thep', 'Wang Pong', 'Wichian Buri'], 
        'Kamphaeng Phet': ['Bueng Samakkhi', 'Khanu Woralaksaburi', 'Khlong Khlung', 'Khlong Lan', 'Kosamphi Nakhon', 'Lan Krabue', 'Mueang Kamphaeng Phet', 'Pang Sila Thong', 'Phran Kratai', 'Sai Ngam', 'Sai Thong Watthana'], 
        'Ubon Ratchathani': ['Buntharik', 'Det Udom', 'Don Mot Daeng', 'Khemarat', 'Khong Chiam', 'Khueang Nai', 'Kut Khaopun', 'Lao Suea Kok', 'Muang Sam Sip', 'Mueang Ubon Ratchathani', 'Na Chaluai', 'Na Tan', 'Na Yia', 'Nam Khun', 'Nam Yuen', 'Phibun Mangsahan', 'Pho Sai', 'Samrong', 'Sawang Wirawong', 'Si Mueang Mai', 'Sirindhorn', 'Tan Sum', 'Thung Si Udom', 'Trakan Phuet Phon', 'Warin Chamrap'], 
        'Lampang': ['Chae Hom', 'Hang Chat', 'Ko Kha', 'Mae Mo', 'Mae Phrik', 'Mae Tha, Lampang', 'Mueang Lampang', 'Mueang Pan', 'Ngao', 'Soem Ngam', 'Sop Prap', 'Thoen', 'Wang Nuea'], 
        'Ang Thong': ['Chaiyo', 'Mueang Ang Thong', 'Pa Mok', 'Pho Thong', 'Samko', 'Sawaeng Ha', 'Wiset Chai Chan'], 
        'Chiang Mai': ['Chai Prakan', 'Chiang Dao', 'Chom Thong', 'Doi Lo', 'Doi Saket', 'Doi Tao', 'Fang', 'Galyani Vadhana', 'Hang Dong', 'Hot', 'Mae Ai', 'Mae Chaem', 'Mae On', 'Mae Rim', 'Mae Taeng', 'Mae Wang', 'Mueang Chiang Mai', 'Omkoi', 'Phrao', 'Samoeng', 'San Kamphaeng', 'San Pa Tong', 'San Sai', 'Saraphi', 'Wiang Haeng'], 
        'Amnat Charoen': ['Chanuman', 'Hua Taphan', 'Lue Amnat', 'Mueang Amnat Charoen', 'Pathum Ratchawongsa', 'Phana', 'Senangkhanikhom'], 
        'Phayao': ['Chiang Kham', 'Chiang Muan', 'Chun', 'Dok Khamtai', 'Mae Chai', 'Mueang Phayao', 'Phu Kamyao', 'Phu Sang', 'Pong'], 
        'Loei': ['Chiang Khan', 'Dan Sai', 'Erawan', 'Mueang Loei', 'Na Duang', 'Na Haeo', 'Nong Hin', 'Pak Chom', 'Pha Khao', 'Phu Kradueng', 'Phu Luang', 'Phu Ruea', 'Tha Li', 'Wang Saphung'], 
        'Chiang Rai': ['Chiang Khong', 'Chiang Saen', 'Doi Luang', 'Khun Tan', 'Mae Chan', 'Mae Fa Luang', 'Mae Lao', 'Mae Sai', 'Mae Suai', 'Mueang Chiang Rai', 'Pa Daet', 'Phan', 'Phaya Mengrai', 'Thoeng', 'Wiang Chai', 'Wiang Chiang Rung', 'Wiang Kaen', 'Wiang Pa Pao'], 
        'Phrae': ['Den Chai', 'Long', 'Mueang Phrae', 'Nong Muang Khai', 'Rong Kwang', 'Song', 'Sung Men', 'Wang Chin'], 
        'Kalasin': ['Don Chan', 'Huai Mek', 'Huai Phueng', 'Kamalasai', 'Kham Muang', 'Khao Wong', 'Khong Chai', 'Kuchinarai', 'Mueang Kalasin', 'Na Khu', 'Na Mon', 'Nong Kung Si', 'Rong Kham', 'Sahatsakhan', 'Sam Chai', 'Somdet', 'Tha Khantho', 'Yang Talat'], 
        'Mukdahan': ['Don Tan', 'Dong Luang', 'Khamcha-i', 'Mueang Mukdahan', 'Nikhom Kham Soi', 'Nong Sung', 'Wan Yai'], 
        'Nong Khai': ['Fao Rai', 'Mueang Nong Khai', 'Pho Tak', 'Phon Phisai', 'Rattanawapi', 'Sakhrai', 'Sangkhom', 'Si Chiang Mai', 'Tha Bo'], 
        'Chai Nat': ['Hankha', 'Manorom', 'Mueang Chai Nat', 'Noen Kham', 'Nong Mamong', 'Sankhaburi', 'Sapphaya', 'Wat Sing'], 
        'Trang': ['Hat Samran', 'Huai Yot', 'Kantang', 'Mueang Trang', 'Na Yong', 'Palian', 'Ratsada', 'Sikao', 'Wang Wiset', 'Yan Ta Khao'], 
        'Chanthaburi': ['Kaeng Hang Maeo', 'Khao Khitchakut', 'Khlung', 'Laem Sing', 'Makham', 'Mueang Chanthaburi', 'Na Yai Am', 'Pong Nam Ron', 'Soi Dao', 'Tha Mai'], 
        'Pattani': ['Kapho', 'Khok Pho', 'Mae Lan', 'Mai Kaen', 'Mayo', 'Mueang Pattani', 'Nong Chik', 'Panare', 'Sai Buri', 'Thung Yang Daeng', 'Yarang', 'Yaring'], 
        'Ranong': ['Kapoe', 'Kra Buri', 'La-un', 'Mueang Ranong', 'Suk Samran'], 
        'Phang Nga': ['Kapong', 'Khura Buri', 'Ko Yao', 'Mueang Phang Nga', 'Takua Pa', 'Takua Thung', 'Thai Mueang', 'Thap Put'], 
        'Phuket': ['Kathu', 'Mueang Phuket', 'Thalang'], 'Yasothon': ['Kham Khuean Kaeo', 'Kho Wang', 'Kut Chum', 'Loeng Nok Tha', 'Maha Chana Chai', 'Mueang Yasothon', 'Pa Tio', 'Sai Mun', 'Thai Charoen'], 
        'Pathum Thani': ['Khlong Luang', 'Lam Luk Ka', 'Lat Lum Kaeo', 'Mueang Pathum Thani', 'Nong Suea', 'Sam Khok', 'Thanyaburi'], 
        'Satun': ['Khuan Don', 'Khuan Kalong', 'La-ngu', 'Manang', 'Mueang Satun', 'Tha Phae', 'Thung Wa'], 
        'Mae Hong Son': ['Khun Yuam', 'Mae La Noi', 'Mae Sariang', 'Mueang Mae Hong Son', 'Pai', 'Pang Mapha', 'Sop Moei'], 
        'Chumphon': ['Lamae', 'Lang Suan', 'Mueang Chumphon', 'Pathio', 'Phato', 'Sawi', 'Tha Sae', 'Thung Tako'], 
        'Nong Bua Lamphu': ['Mueang Nongbua Lamphu', 'Na Klang', 'Na Wang', 'Non Sang', 'Si Bun Rueang', 'Suwannakhuha']
    }

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('monthly_flood_risk_area.csv')
provinces_amphoes = df[['PROV_E', 'AMPHOE_E']]
unique_rows = provinces_amphoes.drop_duplicates()

unique_rows_tuples = [tuple(x) for x in unique_rows.to_numpy()]

new_dict = {}

for tuple in unique_rows_tuples:
    item1 = tuple[0]
    item2 = tuple[1]

    if item1 in new_dict:
        new_dict[item1].append(item2)
    else:
        new_dict[item1] = [item2,]

print(new_dict)
# 
# for province in dict:
#     for amphoe in dict[province]:
#         exists = not df[(df['PROV_E'] == province) & (df['AMPHOE_E'] == amphoe)].empty

#         print(exists)



