
    DROP TABLE leagues_league ;
    CREATE TABLE leagues_league (
            id AUTO_INCREMENT PRIMARY_KEY NOT NULL,
            name VARCHAR(255) NOT NULL,
            link VARCHAR(255) NOT NULL,
            small_img VARCHAR(255) NOT NULL,
            img VARCHAR(255) NOT NULL, 
            outcomes VARCHAR(255) NOT NULL,
            incomes VARCHAR(255) NOT NULL,
            balance VARCHAR(255) NOT NULL,
            country_img VARCHAR(255) NOT NULL,
            country_name VARCHAR(255) NOT NULL
    );

    
    
    INSERT INTO leagues_league (name, link, small_img, img, outcomes, incomes, balance, country_img, country_name)
    VALUES 
    

                            (
                            'Premier League',
                            'https://www.transfermarkt.com.br/premier-league/startseite/wettbewerb/GB1',
                            'https://tmssl.akamaized.net/images/logo/small/gb1.png?lm=1521104656',
                            'https://tmssl.akamaized.net/images/logo/header/gb1.png?lm=1521104656',
                            '2,93 bilhões €',
                            '1,58 bilhões €',
                            '-1.353,11 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/189.png?lm=1520611569',
                            'Inglaterra'
                            ) ,               
                        
                            (
                            'Ligue 1',
                            'https://www.transfermarkt.com.br/ligue-1/startseite/wettbewerb/FR1',
                            'https://tmssl.akamaized.net/images/logo/small/fr1.png?lm=1702413832',
                            'https://tmssl.akamaized.net/images/logo/header/fr1.png?lm=1702413832',
                            '1,11 bilhões €',
                            '1,05 bilhões €',
                            '-63,17 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/50.png?lm=1520611569',
                            'França'
                            ) ,               
                        
                            (
                            'Serie A',
                            'https://www.transfermarkt.com.br/serie-a/startseite/wettbewerb/IT1',
                            'https://tmssl.akamaized.net/images/logo/small/it1.png?lm=1656073460',
                            'https://tmssl.akamaized.net/images/logo/header/it1.png?lm=1656073460',
                            '996,00 mi. €',
                            '1,16 bilhões €',
                            '164,43 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/75.png?lm=1520611569',
                            'Itália'
                            ) ,               
                        
                            (
                            'Saudi Pro League',
                            'https://www.transfermarkt.com.br/saudi-pro-league/startseite/wettbewerb/SA1',
                            'https://tmssl.akamaized.net/images/logo/small/sa1.png?lm=1692612717',
                            'https://tmssl.akamaized.net/images/logo/header/sa1.png?lm=1692612717',
                            '975,67 mi. €',
                            '70,64 mi. €',
                            '-905,03 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/146.png?lm=1520611569',
                            'Arábia Saudita'
                            ) ,               
                        
                            (
                            'Bundesliga',
                            'https://www.transfermarkt.com.br/bundesliga/startseite/wettbewerb/L1',
                            'https://tmssl.akamaized.net/images/logo/small/l1.png?lm=1525905518',
                            'https://tmssl.akamaized.net/images/logo/header/l1.png?lm=1525905518',
                            '843,38 mi. €',
                            '1,06 bilhões €',
                            '217,26 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525',
                            'Alemanha'
                            ) ,               
                        
                            (
                            'LaLiga',
                            'https://www.transfermarkt.com.br/laliga/startseite/wettbewerb/ES1',
                            'https://tmssl.akamaized.net/images/logo/small/es1.png?lm=1688466074',
                            'https://tmssl.akamaized.net/images/logo/header/es1.png?lm=1688466074',
                            '535,10 mi. €',
                            '643,25 mi. €',
                            '108,15 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/157.png?lm=1520611569',
                            'Espanha'
                            ) ,               
                        
                            (
                            'Championship',
                            'https://www.transfermarkt.com.br/championship/startseite/wettbewerb/GB2',
                            'https://tmssl.akamaized.net/images/logo/small/gb2.png?lm=1692214857',
                            'https://tmssl.akamaized.net/images/logo/header/gb2.png?lm=1692214857',
                            '257,81 mi. €',
                            '588,14 mi. €',
                            '330,33 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/189.png?lm=1520611569',
                            'Inglaterra'
                            ) ,               
                        
                            (
                            'Eredivisie',
                            'https://www.transfermarkt.com.br/eredivisie/startseite/wettbewerb/NL1',
                            'https://tmssl.akamaized.net/images/logo/small/nl1.png?lm=1674743474',
                            'https://tmssl.akamaized.net/images/logo/header/nl1.png?lm=1674743474',
                            '239,65 mi. €',
                            '387,33 mi. €',
                            '147,68 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/122.png?lm=1520611569',
                            'Holanda'
                            ) ,               
                        
                            (
                            'Campeonato Brasileiro Série A',
                            'https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/startseite/wettbewerb/BRA1',
                            'https://tmssl.akamaized.net/images/logo/small/bra1.png?lm=1682608836',
                            'https://tmssl.akamaized.net/images/logo/header/bra1.png?lm=1682608836',
                            '238,94 mi. €',
                            '378,34 mi. €',
                            '139,40 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/26.png?lm=1520611569',
                            'Brasil'
                            ) ,               
                        
                            (
                            'Liga Portugal',
                            'https://www.transfermarkt.com.br/liga-portugal/startseite/wettbewerb/PO1',
                            'https://tmssl.akamaized.net/images/logo/small/po1.png?lm=1688630708',
                            'https://tmssl.akamaized.net/images/logo/header/po1.png?lm=1688630708',
                            '237,73 mi. €',
                            '335,83 mi. €',
                            '98,10 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/136.png?lm=1520611569',
                            'Portugal'
                            ) ,               
                        
                            (
                            'Liga MX Apertura',
                            'https://www.transfermarkt.com.br/liga-mx-apertura/startseite/wettbewerb/MEXA',
                            'https://tmssl.akamaized.net/images/logo/small/mexa.png?lm=1406287644',
                            'https://tmssl.akamaized.net/images/logo/header/mexa.png?lm=1406287644',
                            '218,72 mi. €',
                            '144,52 mi. €',
                            '-74,19 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/110.png?lm=1520611569',
                            'México'
                            ) ,               
                        
                            (
                            'Major League Soccer',
                            'https://www.transfermarkt.com.br/major-league-soccer/startseite/wettbewerb/MLS1',
                            'https://tmssl.akamaized.net/images/logo/small/mls1.png?lm=1612117632',
                            'https://tmssl.akamaized.net/images/logo/header/mls1.png?lm=1612117632',
                            '200,92 mi. €',
                            '103,89 mi. €',
                            '-97,02 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/184.png?lm=1520611569',
                            'Estados Unidos'
                            ) ,               
                        
                            (
                            'Jupiler Pro League',
                            'https://www.transfermarkt.com.br/jupiler-pro-league/startseite/wettbewerb/BE1',
                            'https://tmssl.akamaized.net/images/logo/small/be1.png?lm=1601478124',
                            'https://tmssl.akamaized.net/images/logo/header/be1.png?lm=1601478124',
                            '194,59 mi. €',
                            '296,85 mi. €',
                            '102,26 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/19.png?lm=1520611569',
                            'Bélgica'
                            ) ,               
                        
                            (
                            'Qatar Stars League',
                            'https://www.transfermarkt.com.br/qatar-stars-league/startseite/wettbewerb/QSL',
                            'https://tmssl.akamaized.net/images/logo/small/qsl.png?lm=1404288206',
                            'https://tmssl.akamaized.net/images/logo/header/qsl.png?lm=1404288206',
                            '173,27 mi. €',
                            '-',
                            '-173,27 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/137.png?lm=1520611569',
                            'Qatar'
                            ) ,               
                        
                            (
                            'Süper Lig',
                            'https://www.transfermarkt.com.br/super-lig/startseite/wettbewerb/TR1',
                            'https://tmssl.akamaized.net/images/logo/small/tr1.png?lm=1705321006',
                            'https://tmssl.akamaized.net/images/logo/header/tr1.png?lm=1705321006',
                            '171,97 mi. €',
                            '164,34 mi. €',
                            '-7,63 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/174.png?lm=1520611569',
                            'Turquia'
                            ) ,               
                        
                            (
                            'Premier Liga',
                            'https://www.transfermarkt.com.br/premier-liga/startseite/wettbewerb/RU1',
                            'https://tmssl.akamaized.net/images/logo/small/ru1.png?lm=1674741180',
                            'https://tmssl.akamaized.net/images/logo/header/ru1.png?lm=1674741180',
                            '167,32 mi. €',
                            '135,18 mi. €',
                            '-32,14 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/141.png?lm=1520611569',
                            'Rússia'
                            ) ,               
                        
                            (
                            'Copa de la Liga Profesional de Fútbol',
                            'https://www.transfermarkt.com.br/copa-de-la-liga-profesional-de-futbol/startseite/wettbewerb/CDLP',
                            'https://tmssl.akamaized.net/images/logo/small/cdlp.png?lm=1647591044',
                            'https://tmssl.akamaized.net/images/logo/header/cdlp.png?lm=1647591044',
                            '76,89 mi. €',
                            '182,62 mi. €',
                            '105,73 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/9.png?lm=1520611569',
                            'Argentina'
                            ) ,               
                        
                            (
                            'Superliga',
                            'https://www.transfermarkt.com.br/superliga/startseite/wettbewerb/AR1N',
                            'https://tmssl.akamaized.net/images/logo/small/ar1n.png?lm=1612869286',
                            'https://tmssl.akamaized.net/images/logo/header/ar1n.png?lm=1612869286',
                            '76,30 mi. €',
                            '148,45 mi. €',
                            '72,15 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/9.png?lm=1520611569',
                            'Argentina'
                            ) ,               
                        
                            (
                            'Serie B',
                            'https://www.transfermarkt.com.br/serie-b/startseite/wettbewerb/IT2',
                            'https://tmssl.akamaized.net/images/logo/small/it2.png?lm=1548242827',
                            'https://tmssl.akamaized.net/images/logo/header/it2.png?lm=1548242827',
                            '65,00 mi. €',
                            '78,10 mi. €',
                            '13,10 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/75.png?lm=1520611569',
                            'Itália'
                            ) ,               
                        
                            (
                            'Superliga',
                            'https://www.transfermarkt.com.br/superliga/startseite/wettbewerb/DK1',
                            'https://tmssl.akamaized.net/images/logo/small/dk1.png?lm=1648289858',
                            'https://tmssl.akamaized.net/images/logo/header/dk1.png?lm=1648289858',
                            '60,13 mi. €',
                            '120,89 mi. €',
                            '60,76 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/39.png?lm=1520611569',
                            'Dinamarca'
                            ) ,               
                        
                            (
                            'Super League',
                            'https://www.transfermarkt.com.br/super-league/startseite/wettbewerb/C1',
                            'https://tmssl.akamaized.net/images/logo/small/c1.png?lm=1656407730',
                            'https://tmssl.akamaized.net/images/logo/header/c1.png?lm=1656407730',
                            '49,01 mi. €',
                            '117,28 mi. €',
                            '68,28 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/148.png?lm=1520611569',
                            'Suiça'
                            ) ,               
                        
                            (
                            'Scottish Premiership',
                            'https://www.transfermarkt.com.br/scottish-premiership/startseite/wettbewerb/SC1',
                            'https://tmssl.akamaized.net/images/logo/small/sc1.png?lm=1404071829',
                            'https://tmssl.akamaized.net/images/logo/header/sc1.png?lm=1404071829',
                            '45,81 mi. €',
                            '59,32 mi. €',
                            '13,51 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/190.png?lm=1520611569',
                            'Escócia'
                            ) ,               
                        
                            (
                            'Super League 1',
                            'https://www.transfermarkt.com.br/super-league-1/startseite/wettbewerb/GR1',
                            'https://tmssl.akamaized.net/images/logo/small/gr1.png?lm=1460983749',
                            'https://tmssl.akamaized.net/images/logo/header/gr1.png?lm=1460983749',
                            '45,50 mi. €',
                            '44,37 mi. €',
                            '-1,13 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/56.png?lm=1520611569',
                            'Grécia'
                            ) ,               
                        
                            (
                            'Bundesliga',
                            'https://www.transfermarkt.com.br/bundesliga/startseite/wettbewerb/A1',
                            'https://tmssl.akamaized.net/images/logo/small/a1.png?lm=1625144794',
                            'https://tmssl.akamaized.net/images/logo/header/a1.png?lm=1625144794',
                            '45,45 mi. €',
                            '117,90 mi. €',
                            '72,45 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/127.png?lm=1520611569',
                            'Áustria'
                            ) ,               
                        
                            (
                            'Premier Liga',
                            'https://www.transfermarkt.com.br/premier-liga/startseite/wettbewerb/UKR1',
                            'https://tmssl.akamaized.net/images/logo/small/ukr1.png?lm=1637135523',
                            'https://tmssl.akamaized.net/images/logo/header/ukr1.png?lm=1637135523',
                            '44,05 mi. €',
                            '25,43 mi. €',
                            '-18,62 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/177.png?lm=1520611569',
                            'Ucrânia'
                            ) ,               
                        
                            (
                            'UAE Pro League',
                            'https://www.transfermarkt.com.br/uae-pro-league/startseite/wettbewerb/UAE1',
                            'https://tmssl.akamaized.net/images/logo/small/uae1.png?lm=1670616425',
                            'https://tmssl.akamaized.net/images/logo/header/uae1.png?lm=1670616425',
                            '33,65 mi. €',
                            '700 mil €',
                            '-32,95 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/183.png?lm=1520611569',
                            'Emirados Árabes Unidos'
                            ) ,               
                        
                            (
                            'Ligue 2',
                            'https://www.transfermarkt.com.br/ligue-2/startseite/wettbewerb/FR2',
                            'https://tmssl.akamaized.net/images/logo/small/fr2.png?lm=1592648109',
                            'https://tmssl.akamaized.net/images/logo/header/fr2.png?lm=1592648109',
                            '30,58 mi. €',
                            '119,59 mi. €',
                            '89,01 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/50.png?lm=1520611569',
                            'França'
                            ) ,               
                        
                            (
                            'Eliteserien',
                            'https://www.transfermarkt.com.br/eliteserien/startseite/wettbewerb/NO1',
                            'https://tmssl.akamaized.net/images/logo/small/no1.png?lm=1481571796',
                            'https://tmssl.akamaized.net/images/logo/header/no1.png?lm=1481571796',
                            '27,59 mi. €',
                            '75,34 mi. €',
                            '47,75 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/125.png?lm=1520611569',
                            'Noruega'
                            ) ,               
                        
                            (
                            'Fortuna Liga',
                            'https://www.transfermarkt.com.br/fortuna-liga/startseite/wettbewerb/TS1',
                            'https://tmssl.akamaized.net/images/logo/small/ts1.png?lm=1704133970',
                            'https://tmssl.akamaized.net/images/logo/header/ts1.png?lm=1704133970',
                            '26,54 mi. €',
                            '44,40 mi. €',
                            '17,87 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/172.png?lm=1520611569',
                            'República Checa'
                            ) ,               
                        
                            (
                            'Egyptian Premier League',
                            'https://www.transfermarkt.com.br/egyptian-premier-league/startseite/wettbewerb/EGY1',
                            'https://tmssl.akamaized.net/images/logo/small/egy1.png?lm=1689370075',
                            'https://tmssl.akamaized.net/images/logo/header/egy1.png?lm=1689370075',
                            '23,76 mi. €',
                            '20,57 mi. €',
                            '-3,18 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/2.png?lm=1520611569',
                            'Egito'
                            ) ,               
                        
                            (
                            '2. Bundesliga',
                            'https://www.transfermarkt.com.br/2-bundesliga/startseite/wettbewerb/L2',
                            'https://tmssl.akamaized.net/images/logo/small/l2.png?lm=1525905553',
                            'https://tmssl.akamaized.net/images/logo/header/l2.png?lm=1525905553',
                            '22,47 mi. €',
                            '87,18 mi. €',
                            '64,71 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525',
                            'Alemanha'
                            ) ,               
                        
                            (
                            'Super liga Srbije',
                            'https://www.transfermarkt.com.br/super-liga-srbije/startseite/wettbewerb/SER1',
                            'https://tmssl.akamaized.net/images/logo/small/ser1.png?lm=1659602188',
                            'https://tmssl.akamaized.net/images/logo/header/ser1.png?lm=1659602188',
                            '20,02 mi. €',
                            '71,95 mi. €',
                            '51,93 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/215.png?lm=1520611569',
                            'Sérvia'
                            ) ,               
                        
                            (
                            'LaLiga2',
                            'https://www.transfermarkt.com.br/laliga2/startseite/wettbewerb/ES2',
                            'https://tmssl.akamaized.net/images/logo/small/es2.png?lm=1688466101',
                            'https://tmssl.akamaized.net/images/logo/header/es2.png?lm=1688466101',
                            '18,00 mi. €',
                            '119,26 mi. €',
                            '101,26 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/157.png?lm=1520611569',
                            'Espanha'
                            ) ,               
                        
                            (
                            'Ligat ha'Al',
                            'https://www.transfermarkt.com.br/ligat-haal/startseite/wettbewerb/ISR1',
                            'https://tmssl.akamaized.net/images/logo/small/isr1.png?lm=1658846140',
                            'https://tmssl.akamaized.net/images/logo/header/isr1.png?lm=1658846140',
                            '17,41 mi. €',
                            '27,25 mi. €',
                            '9,84 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/74.png?lm=1520611569',
                            'Israel'
                            ) ,               
                        
                            (
                            'J1 League',
                            'https://www.transfermarkt.com.br/j1-league/startseite/wettbewerb/JAP1',
                            'https://tmssl.akamaized.net/images/logo/small/jap1.png?lm=1685093750',
                            'https://tmssl.akamaized.net/images/logo/header/jap1.png?lm=1685093750',
                            '16,20 mi. €',
                            '10,19 mi. €',
                            '-6,01 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/77.png?lm=1520611569',
                            'Japão'
                            ) ,               
                        
                            (
                            'Allsvenskan',
                            'https://www.transfermarkt.com.br/allsvenskan/startseite/wettbewerb/SE1',
                            'https://tmssl.akamaized.net/images/logo/small/se1.png?lm=1618018440',
                            'https://tmssl.akamaized.net/images/logo/header/se1.png?lm=1618018440',
                            '16,13 mi. €',
                            '64,10 mi. €',
                            '47,97 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/147.png?lm=1520611569',
                            'Suécia'
                            ) ,               
                        
                            (
                            'Challenger Pro League',
                            'https://www.transfermarkt.com.br/challenger-pro-league/startseite/wettbewerb/BE2',
                            'https://tmssl.akamaized.net/images/logo/small/be2.png?lm=1656930062',
                            'https://tmssl.akamaized.net/images/logo/header/be2.png?lm=1656930062',
                            '14,21 mi. €',
                            '34,83 mi. €',
                            '20,62 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/19.png?lm=1520611569',
                            'Bélgica'
                            ) ,               
                        
                            (
                            'PKO BP Ekstraklasa',
                            'https://www.transfermarkt.com.br/pko-bp-ekstraklasa/startseite/wettbewerb/PL1',
                            'https://tmssl.akamaized.net/images/logo/small/pl1.png?lm=1601990839',
                            'https://tmssl.akamaized.net/images/logo/header/pl1.png?lm=1601990839',
                            '12,81 mi. €',
                            '43,84 mi. €',
                            '31,02 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/135.png?lm=1520611569',
                            'Polónia'
                            ) ,               
                        
                            (
                            'efbet Liga',
                            'https://www.transfermarkt.com.br/efbet-liga/startseite/wettbewerb/BU1',
                            'https://tmssl.akamaized.net/images/logo/small/bu1.png?lm=1566396154',
                            'https://tmssl.akamaized.net/images/logo/header/bu1.png?lm=1566396154',
                            '11,16 mi. €',
                            '32,78 mi. €',
                            '21,62 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/28.png?lm=1520611569',
                            'Bulgária'
                            ) ,               
                        
                            (
                            'Nemzeti Bajnokság',
                            'https://www.transfermarkt.com.br/nemzeti-bajnoksag/startseite/wettbewerb/UNG1',
                            'https://tmssl.akamaized.net/images/logo/small/ung1.png?lm=1619448842',
                            'https://tmssl.akamaized.net/images/logo/header/ung1.png?lm=1619448842',
                            '10,66 mi. €',
                            '7,65 mi. €',
                            '-3,01 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/178.png?lm=1521635893',
                            'Hungria'
                            ) ,               
                        
                            (
                            'Chinese Super League',
                            'https://www.transfermarkt.com.br/chinese-super-league/startseite/wettbewerb/CSL',
                            'https://tmssl.akamaized.net/images/logo/small/csl.png?lm=1601305342',
                            'https://tmssl.akamaized.net/images/logo/header/csl.png?lm=1601305342',
                            '10,37 mi. €',
                            '8,73 mi. €',
                            '-1,64 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/34.png?lm=1520611569',
                            'China'
                            ) ,               
                        
                            (
                            'SuperLiga',
                            'https://www.transfermarkt.com.br/superliga/startseite/wettbewerb/RO1',
                            'https://tmssl.akamaized.net/images/logo/small/ro1.png?lm=1703230805',
                            'https://tmssl.akamaized.net/images/logo/header/ro1.png?lm=1703230805',
                            '9,93 mi. €',
                            '26,89 mi. €',
                            '16,96 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/140.png?lm=1520611569',
                            'Roménia'
                            ) ,               
                        
                            (
                            'K League 1',
                            'https://www.transfermarkt.com.br/k-league-1/startseite/wettbewerb/RSK1',
                            'https://tmssl.akamaized.net/images/logo/small/rsk1.png?lm=1669660383',
                            'https://tmssl.akamaized.net/images/logo/header/rsk1.png?lm=1669660383',
                            '9,49 mi. €',
                            '20,56 mi. €',
                            '11,07 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/87.png?lm=1520611569',
                            'Coreia do Sul'
                            ) ,               
                        
                            (
                            'SuperSport HNL',
                            'https://www.transfermarkt.com.br/supersport-hnl/startseite/wettbewerb/KR1',
                            'https://tmssl.akamaized.net/images/logo/small/kr1.png?lm=1667669232',
                            'https://tmssl.akamaized.net/images/logo/header/kr1.png?lm=1667669232',
                            '8,06 mi. €',
                            '66,77 mi. €',
                            '58,71 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/37.png?lm=1520611569',
                            'Croácia'
                            ) ,               
                        
                            (
                            'Campeonato Brasileiro Série B',
                            'https://www.transfermarkt.com.br/campeonato-brasileiro-serie-b/startseite/wettbewerb/BRA2',
                            'https://tmssl.akamaized.net/images/logo/small/bra2.png?lm=1682607528',
                            'https://tmssl.akamaized.net/images/logo/header/bra2.png?lm=1682607528',
                            '6,97 mi. €',
                            '40,89 mi. €',
                            '33,92 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/26.png?lm=1520611569',
                            'Brasil'
                            ) ,               
                        
                            (
                            'League One',
                            'https://www.transfermarkt.com.br/league-one/startseite/wettbewerb/GB3',
                            'https://tmssl.akamaized.net/images/logo/small/gb3.png?lm=1692214205',
                            'https://tmssl.akamaized.net/images/logo/header/gb3.png?lm=1692214205',
                            '6,86 mi. €',
                            '30,13 mi. €',
                            '23,27 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/189.png?lm=1520611569',
                            'Inglaterra'
                            ) ,               
                        
                            (
                            'Liga Portugal 2',
                            'https://www.transfermarkt.com.br/liga-portugal-2/startseite/wettbewerb/PO2',
                            'https://tmssl.akamaized.net/images/logo/small/po2.png?lm=1640605712',
                            'https://tmssl.akamaized.net/images/logo/header/po2.png?lm=1640605712',
                            '6,52 mi. €',
                            '9,48 mi. €',
                            '2,96 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/136.png?lm=1520611569',
                            'Portugal'
                            ) ,               
                        
                            (
                            'Serie C - Girone B',
                            'https://www.transfermarkt.com.br/serie-c-girone-b/startseite/wettbewerb/IT3B',
                            'https://tmssl.akamaized.net/images/logo/small/it3b.png?lm=1693389112',
                            'https://tmssl.akamaized.net/images/logo/header/it3b.png?lm=1693389112',
                            '6,50 mi. €',
                            '21,34 mi. €',
                            '14,84 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/75.png?lm=1520611569',
                            'Itália'
                            ) ,               
                        
                            (
                            '1.Lig',
                            'https://www.transfermarkt.com.br/1-lig/startseite/wettbewerb/TR2',
                            'https://tmssl.akamaized.net/images/logo/small/tr2.png?lm=1691091073',
                            'https://tmssl.akamaized.net/images/logo/header/tr2.png?lm=1691091073',
                            '6,01 mi. €',
                            '2,70 mi. €',
                            '-3,31 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/174.png?lm=1520611569',
                            'Turquia'
                            ) ,               
                        
                            (
                            '1.Division',
                            'https://www.transfermarkt.com.br/1-division/startseite/wettbewerb/RU2',
                            'https://tmssl.akamaized.net/images/logo/small/ru2.png?lm=1657513085',
                            'https://tmssl.akamaized.net/images/logo/header/ru2.png?lm=1657513085',
                            '5,22 mi. €',
                            '2,73 mi. €',
                            '-2,49 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/141.png?lm=1520611569',
                            'Rússia'
                            ) ,               
                        
                            (
                            'Primera Federación - Grupo I',
                            'https://www.transfermarkt.com.br/primera-federacion-grupo-i/startseite/wettbewerb/E3G1',
                            'https://tmssl.akamaized.net/images/logo/small/e3g1.png?lm=1664271248',
                            'https://tmssl.akamaized.net/images/logo/header/e3g1.png?lm=1664271248',
                            '4,88 mi. €',
                            '4,81 mi. €',
                            '-70 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/157.png?lm=1520611569',
                            'Espanha'
                            ) ,               
                        
                            (
                            'DStv Premiership',
                            'https://www.transfermarkt.com.br/dstv-premiership/startseite/wettbewerb/SFA1',
                            'https://tmssl.akamaized.net/images/logo/small/sfa1.png?lm=1601669640',
                            'https://tmssl.akamaized.net/images/logo/header/sfa1.png?lm=1601669640',
                            '4,70 mi. €',
                            '3,14 mi. €',
                            '-1,56 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/159.png?lm=1520611569',
                            'África do Sul'
                            ) ,               
                        
                            (
                            'Protathlima Cyta',
                            'https://www.transfermarkt.com.br/protathlima-cyta/startseite/wettbewerb/ZYP1',
                            'https://tmssl.akamaized.net/images/logo/small/zyp1.png?lm=1629801510',
                            'https://tmssl.akamaized.net/images/logo/header/zyp1.png?lm=1629801510',
                            '4,48 mi. €',
                            '7,50 mi. €',
                            '3,02 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/188.png?lm=1520611569',
                            'Chipre'
                            ) ,               
                        
                            (
                            'Saudi First Division League',
                            'https://www.transfermarkt.com.br/saudi-first-division-league/startseite/wettbewerb/SA2L',
                            'https://tmssl.akamaized.net/images/logo/small/sa2l.png?lm=1693314633',
                            'https://tmssl.akamaized.net/images/logo/header/sa2l.png?lm=1693314633',
                            '4,29 mi. €',
                            '985 mil €',
                            '-3,30 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/146.png?lm=1520611569',
                            'Arábia Saudita'
                            ) ,               
                        
                            (
                            'Serie C - Girone A',
                            'https://www.transfermarkt.com.br/serie-c-girone-a/startseite/wettbewerb/IT3A',
                            'https://tmssl.akamaized.net/images/logo/small/it3a.png?lm=1693389108',
                            'https://tmssl.akamaized.net/images/logo/header/it3a.png?lm=1693389108',
                            '4,24 mi. €',
                            '7,37 mi. €',
                            '3,14 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/75.png?lm=1520611569',
                            'Itália'
                            ) ,               
                        
                            (
                            'Thai League',
                            'https://www.transfermarkt.com.br/thai-league/startseite/wettbewerb/THA1',
                            'https://tmssl.akamaized.net/images/logo/small/tha1.png?lm=1631571296',
                            'https://tmssl.akamaized.net/images/logo/header/tha1.png?lm=1631571296',
                            '4,20 mi. €',
                            '3,17 mi. €',
                            '-1,03 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/167.png?lm=1520611569',
                            'Tailândia'
                            ) ,               
                        
                            (
                            'Keuken Kampioen Divisie',
                            'https://www.transfermarkt.com.br/keuken-kampioen-divisie/startseite/wettbewerb/NL2',
                            'https://tmssl.akamaized.net/images/logo/small/nl2.png?lm=1688215713',
                            'https://tmssl.akamaized.net/images/logo/header/nl2.png?lm=1688215713',
                            '3,84 mi. €',
                            '14,22 mi. €',
                            '10,38 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/122.png?lm=1520611569',
                            'Holanda'
                            ) ,               
                        
                            (
                            'LigaPro Serie A Primera Etapa',
                            'https://www.transfermarkt.com.br/ligapro-serie-a-primera-etapa/startseite/wettbewerb/EL1A',
                            'https://tmssl.akamaized.net/images/logo/small/el1a.png?lm=1581952112',
                            'https://tmssl.akamaized.net/images/logo/header/el1a.png?lm=1581952112',
                            '3,66 mi. €',
                            '4,45 mi. €',
                            '786 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/44.png?lm=1520611569',
                            'Equador'
                            ) ,               
                        
                            (
                            'Serie C - Girone C',
                            'https://www.transfermarkt.com.br/serie-c-girone-c/startseite/wettbewerb/IT3C',
                            'https://tmssl.akamaized.net/images/logo/small/it3c.png?lm=1693389108',
                            'https://tmssl.akamaized.net/images/logo/header/it3c.png?lm=1693389108',
                            '3,51 mi. €',
                            '5,35 mi. €',
                            '1,84 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/75.png?lm=1520611569',
                            'Itália'
                            ) ,               
                        
                            (
                            '3. Liga',
                            'https://www.transfermarkt.com.br/3-liga/startseite/wettbewerb/L3',
                            'https://tmssl.akamaized.net/images/logo/small/l3.png?lm=1569702802',
                            'https://tmssl.akamaized.net/images/logo/header/l3.png?lm=1569702802',
                            '3,20 mi. €',
                            '15,39 mi. €',
                            '12,19 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525',
                            'Alemanha'
                            ) ,               
                        
                            (
                            'Persian Gulf Pro League',
                            'https://www.transfermarkt.com.br/persian-gulf-pro-league/startseite/wettbewerb/IRN1',
                            'https://tmssl.akamaized.net/images/logo/small/irn1.png?lm=1705357813',
                            'https://tmssl.akamaized.net/images/logo/header/irn1.png?lm=1705357813',
                            '3,17 mi. €',
                            '5,48 mi. €',
                            '2,31 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/71.png?lm=1520611569',
                            'Irão'
                            ) ,               
                        
                            (
                            'Premyer Liqa',
                            'https://www.transfermarkt.com.br/premyer-liqa/startseite/wettbewerb/AZ1',
                            'https://tmssl.akamaized.net/images/logo/small/az1.png?lm=1608210628',
                            'https://tmssl.akamaized.net/images/logo/header/az1.png?lm=1608210628',
                            '2,90 mi. €',
                            '1,33 mi. €',
                            '-1,57 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/13.png?lm=1520611569',
                            'Azerbaijão'
                            ) ,               
                        
                            (
                            'Fortuna 1 Liga',
                            'https://www.transfermarkt.com.br/fortuna-1-liga/startseite/wettbewerb/PL2',
                            'https://tmssl.akamaized.net/images/logo/small/pl2.png?lm=1531829876',
                            'https://tmssl.akamaized.net/images/logo/header/pl2.png?lm=1531829876',
                            '2,75 mi. €',
                            '2,02 mi. €',
                            '-728 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/135.png?lm=1520611569',
                            'Polónia'
                            ) ,               
                        
                            (
                            'Primera División de Chile',
                            'https://www.transfermarkt.com.br/primera-division-de-chile/startseite/wettbewerb/CLPD',
                            'https://tmssl.akamaized.net/images/logo/small/clpd.png?lm=1674331124',
                            'https://tmssl.akamaized.net/images/logo/header/clpd.png?lm=1674331124',
                            '2,58 mi. €',
                            '16,95 mi. €',
                            '14,38 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/33.png?lm=1520611569',
                            'Chile'
                            ) ,               
                        
                            (
                            'Liga de Ascenso - Fase Regular',
                            'https://www.transfermarkt.com.br/liga-de-ascenso-fase-regular/startseite/wettbewerb/URU2',
                            'https://tmssl.akamaized.net/images/logo/small/uru2.png?lm=1625570241',
                            'https://tmssl.akamaized.net/images/logo/header/uru2.png?lm=1625570241',
                            '2,50 mi. €',
                            '3,33 mi. €',
                            '827 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/179.png?lm=1520611569',
                            'Uruguai'
                            ) ,               
                        
                            (
                            'Primera División Clausura',
                            'https://www.transfermarkt.com.br/primera-division-clausura/startseite/wettbewerb/URUC',
                            'https://tmssl.akamaized.net/images/logo/small/uruc.png?lm=1419585209',
                            'https://tmssl.akamaized.net/images/logo/header/uruc.png?lm=1419585209',
                            '2,48 mi. €',
                            '31,95 mi. €',
                            '29,47 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/179.png?lm=1520611569',
                            'Uruguai'
                            ) ,               
                        
                            (
                            'Botola Pro Inwi',
                            'https://www.transfermarkt.com.br/botola-pro-inwi/startseite/wettbewerb/MAR1',
                            'https://tmssl.akamaized.net/images/logo/small/mar1.png?lm=1649263824',
                            'https://tmssl.akamaized.net/images/logo/header/mar1.png?lm=1649263824',
                            '1,80 mi. €',
                            '5,24 mi. €',
                            '3,44 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/107.png?lm=1520611569',
                            'Marrocos'
                            ) ,               
                        
                            (
                            'Prva Liga',
                            'https://www.transfermarkt.com.br/prva-liga/startseite/wettbewerb/SL1',
                            'https://tmssl.akamaized.net/images/logo/small/sl1.png?lm=1685026467',
                            'https://tmssl.akamaized.net/images/logo/header/sl1.png?lm=1685026467',
                            '1,48 mi. €',
                            '11,96 mi. €',
                            '10,48 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/155.png?lm=1520611569',
                            'Eslovénia'
                            ) ,               
                        
                            (
                            'Ligue Professionnelle 1',
                            'https://www.transfermarkt.com.br/ligue-professionnelle-1/startseite/wettbewerb/ALG1',
                            'https://tmssl.akamaized.net/images/logo/small/alg1.png?lm=1404056855',
                            'https://tmssl.akamaized.net/images/logo/header/alg1.png?lm=1404056855',
                            '1,38 mi. €',
                            '333 mil €',
                            '-1,04 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/4.png?lm=1520611569',
                            'Argélia'
                            ) ,               
                        
                            (
                            'Indian Super League',
                            'https://www.transfermarkt.com.br/indian-super-league/startseite/wettbewerb/IND1',
                            'https://tmssl.akamaized.net/images/logo/small/ind1.png?lm=1659779213',
                            'https://tmssl.akamaized.net/images/logo/header/ind1.png?lm=1659779213',
                            '1,27 mi. €',
                            '1,27 mi. €',
                            '3 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/67.png?lm=1520611569',
                            'Índia'
                            ) ,               
                        
                            (
                            'V.League 1',
                            'https://www.transfermarkt.com.br/v-league-1/startseite/wettbewerb/VIE1',
                            'https://tmssl.akamaized.net/images/logo/small/vie1.png?lm=1708593103',
                            'https://tmssl.akamaized.net/images/logo/header/vie1.png?lm=1708593103',
                            '1,27 mi. €',
                            '-',
                            '-1,27 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/185.png?lm=1520611569',
                            'Vietname'
                            ) ,               
                        
                            (
                            'Primera Nacional',
                            'https://www.transfermarkt.com.br/primera-nacional/startseite/wettbewerb/ARG2',
                            'https://tmssl.akamaized.net/images/logo/small/arg2.png?lm=1606232114',
                            'https://tmssl.akamaized.net/images/logo/header/arg2.png?lm=1606232114',
                            '1,24 mi. €',
                            '8,11 mi. €',
                            '6,86 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/9.png?lm=1520611569',
                            'Argentina'
                            ) ,               
                        
                            (
                            'Premier Liga',
                            'https://www.transfermarkt.com.br/premier-liga/startseite/wettbewerb/KAS1',
                            'https://tmssl.akamaized.net/images/logo/small/kas1.png?lm=1583155322',
                            'https://tmssl.akamaized.net/images/logo/header/kas1.png?lm=1583155322',
                            '1,20 mi. €',
                            '662 mil €',
                            '-538 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/81.png?lm=1520611569',
                            'Cazaquistão'
                            ) ,               
                        
                            (
                            'Ligue Professionnelle 1',
                            'https://www.transfermarkt.com.br/ligue-professionnelle-1/startseite/wettbewerb/TUN1',
                            'https://tmssl.akamaized.net/images/logo/small/tun1.png?lm=1534152824',
                            'https://tmssl.akamaized.net/images/logo/header/tun1.png?lm=1534152824',
                            '1,12 mi. €',
                            '3,55 mi. €',
                            '2,43 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/173.png?lm=1520611569',
                            'Tunísia'
                            ) ,               
                        
                            (
                            'Liga 3',
                            'https://www.transfermarkt.com.br/liga-3/startseite/wettbewerb/PT3A',
                            'https://tmssl.akamaized.net/images/logo/small/pt3a.png?lm=1688559412',
                            'https://tmssl.akamaized.net/images/logo/header/pt3a.png?lm=1688559412',
                            '1,00 mi. €',
                            '8,90 mi. €',
                            '7,90 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/136.png?lm=1520611569',
                            'Portugal'
                            ) ,               
                        
                            (
                            'Primera División Apertura',
                            'https://www.transfermarkt.com.br/primera-division-apertura/startseite/wettbewerb/PR1A',
                            'https://tmssl.akamaized.net/images/logo/small/pr1a.png?lm=1586638106',
                            'https://tmssl.akamaized.net/images/logo/header/pr1a.png?lm=1586638106',
                            '1,00 mi. €',
                            '8,70 mi. €',
                            '7,70 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/132.png?lm=1520611569',
                            'Paraguai'
                            ) ,               
                        
                            (
                            'Nike Liga',
                            'https://www.transfermarkt.com.br/nike-liga/startseite/wettbewerb/SLO1',
                            'https://tmssl.akamaized.net/images/logo/small/slo1.png?lm=1688328872',
                            'https://tmssl.akamaized.net/images/logo/header/slo1.png?lm=1688328872',
                            '935 mil €',
                            '5,65 mi. €',
                            '4,72 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/154.png?lm=1520611569',
                            'Eslováquia'
                            ) ,               
                        
                            (
                            'Liga 1 Apertura',
                            'https://www.transfermarkt.com.br/liga-1-apertura/startseite/wettbewerb/TDeA',
                            'https://tmssl.akamaized.net/images/logo/small/tdea.png?lm=1579456471',
                            'https://tmssl.akamaized.net/images/logo/header/tdea.png?lm=1579456471',
                            '918 mil €',
                            '3,53 mi. €',
                            '2,61 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/133.png?lm=1520611569',
                            'Perú'
                            ) ,               
                        
                            (
                            'Virsliga',
                            'https://www.transfermarkt.com.br/virsliga/startseite/wettbewerb/LET1',
                            'https://tmssl.akamaized.net/images/logo/small/let1.png?lm=1703175121',
                            'https://tmssl.akamaized.net/images/logo/header/let1.png?lm=1703175121',
                            '900 mil €',
                            '2,88 mi. €',
                            '1,98 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/92.png?lm=1520611569',
                            'Letónia'
                            ) ,               
                        
                            (
                            'China League One',
                            'https://www.transfermarkt.com.br/china-league-one/startseite/wettbewerb/CLO',
                            'https://tmssl.akamaized.net/images/logo/small/clo.png?lm=1602779471',
                            'https://tmssl.akamaized.net/images/logo/header/clo.png?lm=1602779471',
                            '847 mil €',
                            '38 mil €',
                            '-808 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/34.png?lm=1520611569',
                            'China'
                            ) ,               
                        
                            (
                            '1.Division',
                            'https://www.transfermarkt.com.br/1-division/startseite/wettbewerb/DK2',
                            'https://tmssl.akamaized.net/images/logo/small/dk2.png?lm=1642490201',
                            'https://tmssl.akamaized.net/images/logo/header/dk2.png?lm=1642490201',
                            '843 mil €',
                            '6,93 mi. €',
                            '6,09 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/39.png?lm=1520611569',
                            'Dinamarca'
                            ) ,               
                        
                            (
                            'Persha Liga',
                            'https://www.transfermarkt.com.br/persha-liga/startseite/wettbewerb/UKR2',
                            'https://tmssl.akamaized.net/images/logo/small/ukr2.png?lm=1665239718',
                            'https://tmssl.akamaized.net/images/logo/header/ukr2.png?lm=1665239718',
                            '755 mil €',
                            '1,41 mi. €',
                            '655 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/177.png?lm=1520611569',
                            'Ucrânia'
                            ) ,               
                        
                            (
                            'Challenge League',
                            'https://www.transfermarkt.com.br/challenge-league/startseite/wettbewerb/C2',
                            'https://tmssl.akamaized.net/images/logo/small/c2.png?lm=1656407822',
                            'https://tmssl.akamaized.net/images/logo/header/c2.png?lm=1656407822',
                            '700 mil €',
                            '2,02 mi. €',
                            '1,32 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/148.png?lm=1520611569',
                            'Suiça'
                            ) ,               
                        
                            (
                            'Liga Dimayor Apertura',
                            'https://www.transfermarkt.com.br/liga-dimayor-apertura/startseite/wettbewerb/COLP',
                            'https://tmssl.akamaized.net/images/logo/small/colp.png?lm=1580674248',
                            'https://tmssl.akamaized.net/images/logo/header/colp.png?lm=1580674248',
                            '642 mil €',
                            '36,63 mi. €',
                            '35,99 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/83.png?lm=1520611569',
                            'Colômbia'
                            ) ,               
                        
                            (
                            'Abissnet Superiore',
                            'https://www.transfermarkt.com.br/abissnet-superiore/startseite/wettbewerb/ALB1',
                            'https://tmssl.akamaized.net/images/logo/small/alb1.png?lm=1645711034',
                            'https://tmssl.akamaized.net/images/logo/header/alb1.png?lm=1645711034',
                            '625 mil €',
                            '2,42 mi. €',
                            '1,79 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/3.png?lm=1520611569',
                            'Albânia'
                            ) ,               
                        
                            (
                            'Premijer Liga',
                            'https://www.transfermarkt.com.br/premijer-liga/startseite/wettbewerb/BOS1',
                            'https://tmssl.akamaized.net/images/logo/small/bos1.png?lm=1708359973',
                            'https://tmssl.akamaized.net/images/logo/header/bos1.png?lm=1708359973',
                            '545 mil €',
                            '2,62 mi. €',
                            '2,08 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/24.png?lm=1569523290',
                            'Bósnia-Herzegovina'
                            ) ,               
                        
                            (
                            'Primera División Apertura',
                            'https://www.transfermarkt.com.br/primera-division-apertura/startseite/wettbewerb/URU1',
                            'https://tmssl.akamaized.net/images/logo/small/uru1.png?lm=1706881179',
                            'https://tmssl.akamaized.net/images/logo/header/uru1.png?lm=1706881179',
                            '519 mil €',
                            '17,68 mi. €',
                            '17,16 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/179.png?lm=1520611569',
                            'Uruguai'
                            ) ,               
                        
                            (
                            'K League 2',
                            'https://www.transfermarkt.com.br/k-league-2/startseite/wettbewerb/RSK2',
                            'https://tmssl.akamaized.net/images/logo/small/rsk2.png?lm=1669661442',
                            'https://tmssl.akamaized.net/images/logo/header/rsk2.png?lm=1669661442',
                            '466 mil €',
                            '3,59 mi. €',
                            '3,13 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/87.png?lm=1520611569',
                            'Coreia do Sul'
                            ) ,               
                        
                            (
                            'K3 League',
                            'https://www.transfermarkt.com.br/k3-league/startseite/wettbewerb/K3L',
                            'https://tmssl.akamaized.net/images/logo/small/k3l.png?lm=1580922939',
                            'https://tmssl.akamaized.net/images/logo/header/k3l.png?lm=1580922939',
                            '400 mil €',
                            '-',
                            '-400 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/87.png?lm=1520611569',
                            'Coreia do Sul'
                            ) ,               
                        
                            (
                            'Super Liga',
                            'https://www.transfermarkt.com.br/super-liga/startseite/wettbewerb/MO1N',
                            'https://tmssl.akamaized.net/images/logo/small/mo1n.png?lm=1666607427',
                            'https://tmssl.akamaized.net/images/logo/header/mo1n.png?lm=1666607427',
                            '400 mil €',
                            '4,16 mi. €',
                            '3,76 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/112.png?lm=1520611569',
                            'Moldávia'
                            ) ,               
                        
                            (
                            'Prva Makedonska Fudbalska Liga',
                            'https://www.transfermarkt.com.br/prva-makedonska-fudbalska-liga/startseite/wettbewerb/MAZ1',
                            'https://tmssl.akamaized.net/images/logo/small/maz1.png?lm=1404085586',
                            'https://tmssl.akamaized.net/images/logo/header/maz1.png?lm=1404085586',
                            '390 mil €',
                            '2,01 mi. €',
                            '1,62 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/100.png?lm=1520611569',
                            'Macedónia do Norte'
                            ) ,               
                        
                            (
                            'División Profesional',
                            'https://www.transfermarkt.com.br/division-profesional/startseite/wettbewerb/BO1A',
                            'https://tmssl.akamaized.net/images/logo/small/bo1a.png?lm=1602510560',
                            'https://tmssl.akamaized.net/images/logo/header/bo1a.png?lm=1602510560',
                            '306 mil €',
                            '-',
                            '-306 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/23.png?lm=1520611569',
                            'Bolívia'
                            ) ,               
                        
                            (
                            'Azadegan League',
                            'https://www.transfermarkt.com.br/azadegan-league/startseite/wettbewerb/IRN2',
                            'https://tmssl.akamaized.net/images/logo/small/irn2.png?lm=1446756375',
                            'https://tmssl.akamaized.net/images/logo/header/irn2.png?lm=1446756375',
                            '300 mil €',
                            '430 mil €',
                            '130 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/71.png?lm=1520611569',
                            'Irão'
                            ) ,               
                        
                            (
                            'Primera Federación - Grupo II',
                            'https://www.transfermarkt.com.br/primera-federacion-grupo-ii/startseite/wettbewerb/E3G2',
                            'https://tmssl.akamaized.net/images/logo/small/e3g2.png?lm=1664271281',
                            'https://tmssl.akamaized.net/images/logo/header/e3g2.png?lm=1664271281',
                            '250 mil €',
                            '11,09 mi. €',
                            '10,84 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/157.png?lm=1520611569',
                            'Espanha'
                            ) ,               
                        
                            (
                            'OBOS-ligaen',
                            'https://www.transfermarkt.com.br/obos-ligaen/startseite/wettbewerb/NO2',
                            'https://tmssl.akamaized.net/images/logo/small/no2.png?lm=1528662835',
                            'https://tmssl.akamaized.net/images/logo/header/no2.png?lm=1528662835',
                            '220 mil €',
                            '9,34 mi. €',
                            '9,12 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/125.png?lm=1520611569',
                            'Noruega'
                            ) ,               
                        
                            (
                            'O'zbekiston Superligasi',
                            'https://www.transfermarkt.com.br/ozbekiston-superligasi/startseite/wettbewerb/UZ1',
                            'https://tmssl.akamaized.net/images/logo/small/uz1.png?lm=1707031580',
                            'https://tmssl.akamaized.net/images/logo/header/uz1.png?lm=1707031580',
                            '215 mil €',
                            '1,70 mi. €',
                            '1,49 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/180.png?lm=1520611569',
                            'Uzbequistão'
                            ) ,               
                        
                            (
                            'Fortuna Narodni liga',
                            'https://www.transfermarkt.com.br/fortuna-narodni-liga/startseite/wettbewerb/TS2',
                            'https://tmssl.akamaized.net/images/logo/small/ts2.png?lm=1704133991',
                            'https://tmssl.akamaized.net/images/logo/header/ts2.png?lm=1704133991',
                            '205 mil €',
                            '480 mil €',
                            '275 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/172.png?lm=1520611569',
                            'República Checa'
                            ) ,               
                        
                            (
                            '2.Lig Kirmizi',
                            'https://www.transfermarkt.com.br/2-lig-kirmizi/startseite/wettbewerb/TR3B',
                            'https://tmssl.akamaized.net/images/logo/small/tr3b.png?lm=1639083517',
                            'https://tmssl.akamaized.net/images/logo/header/tr3b.png?lm=1639083517',
                            '204 mil €',
                            '520 mil €',
                            '316 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/174.png?lm=1520611569',
                            'Turquia'
                            ) ,               
                        
                            (
                            'A-League Men',
                            'https://www.transfermarkt.com.br/a-league-men/startseite/wettbewerb/AUS1',
                            'https://tmssl.akamaized.net/images/logo/small/aus1.png?lm=1644660263',
                            'https://tmssl.akamaized.net/images/logo/header/aus1.png?lm=1644660263',
                            '200 mil €',
                            '6,53 mi. €',
                            '6,33 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/12.png?lm=1520611569',
                            'Austrália'
                            ) ,               
                        
                            (
                            'Liga Pro Serie B',
                            'https://www.transfermarkt.com.br/liga-pro-serie-b/startseite/wettbewerb/EC2L',
                            'https://tmssl.akamaized.net/images/logo/small/ec2l.png?lm=1707832810',
                            'https://tmssl.akamaized.net/images/logo/header/ec2l.png?lm=1707832810',
                            '185 mil €',
                            '-',
                            '-185 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/44.png?lm=1520611569',
                            'Equador'
                            ) ,               
                        
                            (
                            'Erovnuli Liga',
                            'https://www.transfermarkt.com.br/erovnuli-liga/startseite/wettbewerb/GE1N',
                            'https://tmssl.akamaized.net/images/logo/small/ge1n.png?lm=1648352894',
                            'https://tmssl.akamaized.net/images/logo/header/ge1n.png?lm=1648352894',
                            '182 mil €',
                            '6,57 mi. €',
                            '6,39 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/53.png?lm=1520611569',
                            'Geórgia'
                            ) ,               
                        
                            (
                            '2. Division A (Phase 1)',
                            'https://www.transfermarkt.com.br/2-division-a-phase-1-/startseite/wettbewerb/R3D1',
                            'https://tmssl.akamaized.net/images/logo/small/r3d1.png?lm=1689773906',
                            'https://tmssl.akamaized.net/images/logo/header/r3d1.png?lm=1689773906',
                            '173 mil €',
                            '400 mil €',
                            '227 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/141.png?lm=1520611569',
                            'Rússia'
                            ) ,               
                        
                            (
                            'Kategoria e Parë',
                            'https://www.transfermarkt.com.br/kategoria-e-pare/startseite/wettbewerb/ALB2',
                            'https://tmssl.akamaized.net/images/logo/small/alb2.png?lm=1656879906',
                            'https://tmssl.akamaized.net/images/logo/header/alb2.png?lm=1656879906',
                            '150 mil €',
                            '180 mil €',
                            '30 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/3.png?lm=1520611569',
                            'Albânia'
                            ) ,               
                        
                            (
                            'Primera División Clausura',
                            'https://www.transfermarkt.com.br/primera-division-clausura/startseite/wettbewerb/PDV1',
                            'https://tmssl.akamaized.net/images/logo/small/pdv1.png?lm=1638269247',
                            'https://tmssl.akamaized.net/images/logo/header/pdv1.png?lm=1638269247',
                            '137 mil €',
                            '1,60 mi. €',
                            '1,47 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/36.png?lm=1520611569',
                            'Costa Rica'
                            ) ,               
                        
                            (
                            'Albi Mall Superliga',
                            'https://www.transfermarkt.com.br/albi-mall-superliga/startseite/wettbewerb/KO1',
                            'https://tmssl.akamaized.net/images/logo/small/ko1.png?lm=1670408167',
                            'https://tmssl.akamaized.net/images/logo/header/ko1.png?lm=1670408167',
                            '130 mil €',
                            '1,58 mi. €',
                            '1,45 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/244.png?lm=1520611569',
                            'Kosovo'
                            ) ,               
                        
                            (
                            'Liga 1 Clausura',
                            'https://www.transfermarkt.com.br/liga-1-clausura/startseite/wettbewerb/TDeC',
                            'https://tmssl.akamaized.net/images/logo/small/tdec.png?lm=1566312054',
                            'https://tmssl.akamaized.net/images/logo/header/tdec.png?lm=1566312054',
                            '91 mil €',
                            '1,78 mi. €',
                            '1,69 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/133.png?lm=1520611569',
                            'Perú'
                            ) ,               
                        
                            (
                            'Liga 1 Indonesia',
                            'https://www.transfermarkt.com.br/liga-1-indonesia/startseite/wettbewerb/IN1L',
                            'https://tmssl.akamaized.net/images/logo/small/in1l.png?lm=1628819483',
                            'https://tmssl.akamaized.net/images/logo/header/in1l.png?lm=1628819483',
                            '90 mil €',
                            '-',
                            '-90 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/68.png?lm=1520611569',
                            'Indonésia'
                            ) ,               
                        
                            (
                            '2. Liga',
                            'https://www.transfermarkt.com.br/2-liga/startseite/wettbewerb/A2',
                            'https://tmssl.akamaized.net/images/logo/small/a2.png?lm=1641377687',
                            'https://tmssl.akamaized.net/images/logo/header/a2.png?lm=1641377687',
                            '90 mil €',
                            '830 mil €',
                            '740 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/127.png?lm=1520611569',
                            'Áustria'
                            ) ,               
                        
                            (
                            'Vysshaya Liga',
                            'https://www.transfermarkt.com.br/vysshaya-liga/startseite/wettbewerb/WER1',
                            'https://tmssl.akamaized.net/images/logo/small/wer1.png?lm=1587831474',
                            'https://tmssl.akamaized.net/images/logo/header/wer1.png?lm=1587831474',
                            '80 mil €',
                            '2,84 mi. €',
                            '2,76 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/18.png?lm=1520611569',
                            'Bielorrússia'
                            ) ,               
                        
                            (
                            'Sports Direct Premiership',
                            'https://www.transfermarkt.com.br/sports-direct-premiership/startseite/wettbewerb/NIR1',
                            'https://tmssl.akamaized.net/images/logo/small/nir1.png?lm=1698034818',
                            'https://tmssl.akamaized.net/images/logo/header/nir1.png?lm=1698034818',
                            '76 mil €',
                            '420 mil €',
                            '344 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/192.png?lm=1520611569',
                            'Irlanda do Norte'
                            ) ,               
                        
                            (
                            'Liga Nacional Clausura',
                            'https://www.transfermarkt.com.br/liga-nacional-clausura/startseite/wettbewerb/HOC1',
                            'https://tmssl.akamaized.net/images/logo/small/hoc1.png?lm=1642198951',
                            'https://tmssl.akamaized.net/images/logo/header/hoc1.png?lm=1642198951',
                            '76 mil €',
                            '200 mil €',
                            '125 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/66.png?lm=1699286249',
                            'Honduras'
                            ) ,               
                        
                            (
                            'Liga Guate Clausura',
                            'https://www.transfermarkt.com.br/liga-guate-clausura/startseite/wettbewerb/GU1C',
                            'https://tmssl.akamaized.net/images/logo/small/gu1c.png?lm=1674032883',
                            'https://tmssl.akamaized.net/images/logo/header/gu1c.png?lm=1674032883',
                            '68 mil €',
                            '68 mil €',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/58.png?lm=1520611569',
                            'Guatemala'
                            ) ,               
                        
                            (
                            'Super League 2',
                            'https://www.transfermarkt.com.br/super-league-2/startseite/wettbewerb/GRS2',
                            'https://tmssl.akamaized.net/images/logo/small/grs2.png?lm=1635508832',
                            'https://tmssl.akamaized.net/images/logo/header/grs2.png?lm=1635508832',
                            '50 mil €',
                            '-',
                            '-50 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/56.png?lm=1520611569',
                            'Grécia'
                            ) ,               
                        
                            (
                            'League of Ireland Premier Division',
                            'https://www.transfermarkt.com.br/league-of-ireland-premier-division/startseite/wettbewerb/IR1',
                            'https://tmssl.akamaized.net/images/logo/small/ir1.png?lm=1672532090',
                            'https://tmssl.akamaized.net/images/logo/header/ir1.png?lm=1672532090',
                            '50 mil €',
                            '790 mil €',
                            '740 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/72.png?lm=1520611569',
                            'Irlanda '
                            ) ,               
                        
                            (
                            'LigaPro Serie A Segunda Etapa',
                            'https://www.transfermarkt.com.br/ligapro-serie-a-segunda-etapa/startseite/wettbewerb/EL1S',
                            'https://tmssl.akamaized.net/images/logo/small/el1s.png?lm=1581952120',
                            'https://tmssl.akamaized.net/images/logo/header/el1s.png?lm=1581952120',
                            '45 mil €',
                            '7,65 mi. €',
                            '7,60 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/44.png?lm=1520611569',
                            'Equador'
                            ) ,               
                        
                            (
                            'Lebanese Premier League',
                            'https://www.transfermarkt.com.br/lebanese-premier-league/startseite/wettbewerb/LIB1',
                            'https://tmssl.akamaized.net/images/logo/small/lib1.png?lm=1650213352',
                            'https://tmssl.akamaized.net/images/logo/header/lib1.png?lm=1650213352',
                            '37 mil €',
                            '37 mil €',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/94.png?lm=1520611569',
                            'Líbano'
                            ) ,               
                        
                            (
                            'Second League Division B Gruppe 3 (-2023)',
                            'https://www.transfermarkt.com.br/second-league-division-b-gruppe-3-2023-/startseite/wettbewerb/RPLZ',
                            'https://tmssl.akamaized.net/images/logo/small/rplz.png?lm=1689773997',
                            'https://tmssl.akamaized.net/images/logo/header/rplz.png?lm=1689773997',
                            '30 mil €',
                            '121 mil €',
                            '91 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/141.png?lm=1520611569',
                            'Rússia'
                            ) ,               
                        
                            (
                            'Taiwan Football Premier League',
                            'https://www.transfermarkt.com.br/taiwan-football-premier-league/startseite/wettbewerb/TFPL',
                            'https://tmssl.akamaized.net/images/logo/small/tfpl.png?lm=1586589765',
                            'https://tmssl.akamaized.net/images/logo/header/tfpl.png?lm=1586589765',
                            '30 mil €',
                            '30 mil €',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/164.png?lm=1679300082',
                            'Taipé Chinesa'
                            ) ,               
                        
                            (
                            'Scottish League One',
                            'https://www.transfermarkt.com.br/scottish-league-one/startseite/wettbewerb/SC3',
                            'https://tmssl.akamaized.net/images/logo/small/sc3.png?lm=1410807599',
                            'https://tmssl.akamaized.net/images/logo/header/sc3.png?lm=1410807599',
                            '29 mil €',
                            '-',
                            '-29 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/190.png?lm=1520611569',
                            'Escócia'
                            ) ,               
                        
                            (
                            'I-League',
                            'https://www.transfermarkt.com.br/i-league/startseite/wettbewerb/INIL',
                            'https://tmssl.akamaized.net/images/logo/small/inil.png?lm=1698333588',
                            'https://tmssl.akamaized.net/images/logo/header/inil.png?lm=1698333588',
                            '28 mil €',
                            '25 mil €',
                            '-3 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/67.png?lm=1520611569',
                            'Índia'
                            ) ,               
                        
                            (
                            '2 Liga',
                            'https://www.transfermarkt.com.br/2-liga/startseite/wettbewerb/PL2L',
                            'https://tmssl.akamaized.net/images/logo/small/pl2l.png?lm=1691575185',
                            'https://tmssl.akamaized.net/images/logo/header/pl2l.png?lm=1691575185',
                            '27 mil €',
                            '1,15 mi. €',
                            '1,12 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/135.png?lm=1520611569',
                            'Polónia'
                            ) ,               
                        
                            (
                            'League Two Relegation Stage',
                            'https://www.transfermarkt.com.br/league-two-relegation-stage/startseite/wettbewerb/CH3R',
                            'https://tmssl.akamaized.net/images/logo/small/ch3r.png?lm=1638278639',
                            'https://tmssl.akamaized.net/images/logo/header/ch3r.png?lm=1638278639',
                            '22 mil €',
                            '-',
                            '-22 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/34.png?lm=1520611569',
                            'China'
                            ) ,               
                        
                            (
                            'Liga 2',
                            'https://www.transfermarkt.com.br/liga-2/startseite/wettbewerb/RO2',
                            'https://tmssl.akamaized.net/images/logo/small/ro2.png?lm=1618761930',
                            'https://tmssl.akamaized.net/images/logo/header/ro2.png?lm=1618761930',
                            '20 mil €',
                            '415 mil €',
                            '395 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/140.png?lm=1520611569',
                            'Roménia'
                            ) ,               
                        
                            (
                            'Regionalliga Ost',
                            'https://www.transfermarkt.com.br/regionalliga-ost/startseite/wettbewerb/ATRO',
                            'https://tmssl.akamaized.net/images/logo/small/atro.png?lm=1497544630',
                            'https://tmssl.akamaized.net/images/logo/header/atro.png?lm=1497544630',
                            '20 mil €',
                            '-',
                            '-20 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/127.png?lm=1520611569',
                            'Áustria'
                            ) ,               
                        
                            (
                            'J3 League',
                            'https://www.transfermarkt.com.br/j3-league/startseite/wettbewerb/JAP3',
                            'https://tmssl.akamaized.net/images/logo/small/jap3.png?lm=1685093740',
                            'https://tmssl.akamaized.net/images/logo/header/jap3.png?lm=1685093740',
                            '16 mil €',
                            '-',
                            '-16 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/77.png?lm=1520611569',
                            'Japão'
                            ) ,               
                        
                            (
                            'Primera División Clausura',
                            'https://www.transfermarkt.com.br/primera-division-clausura/startseite/wettbewerb/PR1C',
                            'https://tmssl.akamaized.net/images/logo/small/pr1c.png?lm=1661778309',
                            'https://tmssl.akamaized.net/images/logo/header/pr1c.png?lm=1661778309',
                            '4 mil €',
                            '11,48 mi. €',
                            '11,48 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/132.png?lm=1520611569',
                            'Paraguai'
                            ) ,               
                        
                            (
                            'Premium Liiga',
                            'https://www.transfermarkt.com.br/premium-liiga/startseite/wettbewerb/EST1',
                            'https://tmssl.akamaized.net/images/logo/small/est1.png?lm=1694549093',
                            'https://tmssl.akamaized.net/images/logo/header/est1.png?lm=1694549093',
                            '3 mil €',
                            '375 mil €',
                            '372 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/47.png?lm=1520611569',
                            'Estónia'
                            ) ,               
                        
                            (
                            'Nepal Super League',
                            'https://www.transfermarkt.com.br/nepal-super-league/startseite/wettbewerb/NPL1',
                            'https://tmssl.akamaized.net/images/logo/small/npl1.png?lm=1619761556',
                            'https://tmssl.akamaized.net/images/logo/header/npl1.png?lm=1619761556',
                            '1 mil €',
                            '-',
                            '-1 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/119.png?lm=1520611569',
                            'Nepal'
                            ) ,               
                        
                            (
                            'Liga 2 Indonesia',
                            'https://www.transfermarkt.com.br/liga-2-indonesia/startseite/wettbewerb/ILI2',
                            'https://tmssl.akamaized.net/images/logo/small/ili2.png?lm=1693907778',
                            'https://tmssl.akamaized.net/images/logo/header/ili2.png?lm=1693907778',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/68.png?lm=1520611569',
                            'Indonésia'
                            ) ,               
                        
                            (
                            'League 2',
                            'https://www.transfermarkt.com.br/league-2/startseite/wettbewerb/IRN3',
                            'https://tmssl.akamaized.net/images/logo/small/irn3.png?lm=1539472125',
                            'https://tmssl.akamaized.net/images/logo/header/irn3.png?lm=1539472125',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/71.png?lm=1520611569',
                            'Irão'
                            ) ,               
                        
                            (
                            '2.Lig Beyaz',
                            'https://www.transfermarkt.com.br/2-lig-beyaz/startseite/wettbewerb/TR3A',
                            'https://tmssl.akamaized.net/images/logo/small/tr3a.png?lm=1639083499',
                            'https://tmssl.akamaized.net/images/logo/header/tr3a.png?lm=1639083499',
                            '-',
                            '1,62 mi. €',
                            '1,62 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/174.png?lm=1520611569',
                            'Turquia'
                            ) ,               
                        
                            (
                            'Prva liga Srbije',
                            'https://www.transfermarkt.com.br/prva-liga-srbije/startseite/wettbewerb/SER2',
                            'https://tmssl.akamaized.net/images/logo/small/ser2.png?lm=1688375013',
                            'https://tmssl.akamaized.net/images/logo/header/ser2.png?lm=1688375013',
                            '-',
                            '90 mil €',
                            '90 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/215.png?lm=1520611569',
                            'Sérvia'
                            ) ,               
                        
                            (
                            'Liga Leumit',
                            'https://www.transfermarkt.com.br/liga-leumit/startseite/wettbewerb/ISR2',
                            'https://tmssl.akamaized.net/images/logo/small/isr2.png?lm=1476188771',
                            'https://tmssl.akamaized.net/images/logo/header/isr2.png?lm=1476188771',
                            '-',
                            '1,40 mi. €',
                            '1,40 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/74.png?lm=1520611569',
                            'Israel'
                            ) ,               
                        
                            (
                            'Thai League 2',
                            'https://www.transfermarkt.com.br/thai-league-2/startseite/wettbewerb/THA2',
                            'https://tmssl.akamaized.net/images/logo/small/tha2.png?lm=1631570343',
                            'https://tmssl.akamaized.net/images/logo/header/tha2.png?lm=1631570343',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/167.png?lm=1520611569',
                            'Tailândia'
                            ) ,               
                        
                            (
                            'Ceska fotbalova liga',
                            'https://www.transfermarkt.com.br/ceska-fotbalova-liga/startseite/wettbewerb/CZ3C',
                            'https://tmssl.akamaized.net/images/logo/small/cz3c.png?lm=1575758168',
                            'https://tmssl.akamaized.net/images/logo/header/cz3c.png?lm=1575758168',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/172.png?lm=1520611569',
                            'República Checa'
                            ) ,               
                        
                            (
                            'Torneo Federal A',
                            'https://www.transfermarkt.com.br/torneo-federal-a/startseite/wettbewerb/ARG3',
                            'https://tmssl.akamaized.net/images/logo/small/arg3.png?lm=1649186614',
                            'https://tmssl.akamaized.net/images/logo/header/arg3.png?lm=1649186614',
                            '-',
                            '4 mil €',
                            '4 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/9.png?lm=1520611569',
                            'Argentina'
                            ) ,               
                        
                            (
                            'J2 League',
                            'https://www.transfermarkt.com.br/j2-league/startseite/wettbewerb/JAP2',
                            'https://tmssl.akamaized.net/images/logo/small/jap2.png?lm=1685093720',
                            'https://tmssl.akamaized.net/images/logo/header/jap2.png?lm=1685093720',
                            '-',
                            '2,65 mi. €',
                            '2,65 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/77.png?lm=1520611569',
                            'Japão'
                            ) ,               
                        
                            (
                            'Nigeria Professional Football League',
                            'https://www.transfermarkt.com.br/nigeria-professional-football-league/startseite/wettbewerb/NPFL',
                            'https://tmssl.akamaized.net/images/logo/small/npfl.png?lm=1557386764',
                            'https://tmssl.akamaized.net/images/logo/header/npfl.png?lm=1557386764',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/124.png?lm=1520611569',
                            'Nigéria'
                            ) ,               
                        
                            (
                            'Second Division',
                            'https://www.transfermarkt.com.br/second-division/startseite/wettbewerb/CYP2',
                            'https://tmssl.akamaized.net/images/logo/small/cyp2.png?lm=1677164201',
                            'https://tmssl.akamaized.net/images/logo/header/cyp2.png?lm=1677164201',
                            '-',
                            '52 mil €',
                            '52 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/188.png?lm=1520611569',
                            'Chipre'
                            ) ,               
                        
                            (
                            'Druga Liga',
                            'https://www.transfermarkt.com.br/druga-liga/startseite/wettbewerb/SL2',
                            'https://tmssl.akamaized.net/images/logo/small/sl2.png?lm=1424901190',
                            'https://tmssl.akamaized.net/images/logo/header/sl2.png?lm=1424901190',
                            '-',
                            '100 mil €',
                            '100 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/155.png?lm=1520611569',
                            'Eslovénia'
                            ) ,               
                        
                            (
                            'USL Championship',
                            'https://www.transfermarkt.com.br/usl-championship/startseite/wettbewerb/USL',
                            'https://tmssl.akamaized.net/images/logo/small/usl.png?lm=1543694624',
                            'https://tmssl.akamaized.net/images/logo/header/usl.png?lm=1543694624',
                            '-',
                            '1,89 mi. €',
                            '1,89 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/184.png?lm=1520611569',
                            'Estados Unidos'
                            ) ,               
                        
                            (
                            'Nemzeti Bajnokság II.',
                            'https://www.transfermarkt.com.br/nemzeti-bajnoksag-ii-/startseite/wettbewerb/UN2',
                            'https://tmssl.akamaized.net/images/logo/small/un2.png?lm=1619448884',
                            'https://tmssl.akamaized.net/images/logo/header/un2.png?lm=1619448884',
                            '-',
                            '450 mil €',
                            '450 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/178.png?lm=1521635893',
                            'Hungria'
                            ) ,               
                        
                            (
                            'Vtora Liga',
                            'https://www.transfermarkt.com.br/vtora-liga/startseite/wettbewerb/BU2',
                            'https://tmssl.akamaized.net/images/logo/small/bu2.png?lm=1609669142',
                            'https://tmssl.akamaized.net/images/logo/header/bu2.png?lm=1609669142',
                            '-',
                            '13 mil €',
                            '13 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/28.png?lm=1520611569',
                            'Bulgária'
                            ) ,               
                        
                            (
                            'Challenge League',
                            'https://www.transfermarkt.com.br/challenge-league/startseite/wettbewerb/MAL2',
                            'https://tmssl.akamaized.net/images/logo/small/mal2.png?lm=1649336319',
                            'https://tmssl.akamaized.net/images/logo/header/mal2.png?lm=1649336319',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/106.png?lm=1520611569',
                            'Malta'
                            ) ,               
                        
                            (
                            'Campionato Sammarinese',
                            'https://www.transfermarkt.com.br/campionato-sammarinese/startseite/wettbewerb/SMR1',
                            'https://tmssl.akamaized.net/images/logo/small/smr1.png?lm=1641157612',
                            'https://tmssl.akamaized.net/images/logo/header/smr1.png?lm=1641157612',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/144.png?lm=1520611569',
                            'San Marino'
                            ) ,               
                        
                            (
                            'Third Division',
                            'https://www.transfermarkt.com.br/third-division/startseite/wettbewerb/CYP3',
                            'https://tmssl.akamaized.net/images/logo/small/cyp3.png?lm=1677164215',
                            'https://tmssl.akamaized.net/images/logo/header/cyp3.png?lm=1677164215',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/188.png?lm=1520611569',
                            'Chipre'
                            ) ,               
                        
                            (
                            'Primera B',
                            'https://www.transfermarkt.com.br/primera-b/startseite/wettbewerb/CL2B',
                            'https://tmssl.akamaized.net/images/logo/small/cl2b.png?lm=1645086972',
                            'https://tmssl.akamaized.net/images/logo/header/cl2b.png?lm=1645086972',
                            '-',
                            '1,50 mi. €',
                            '1,50 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/33.png?lm=1520611569',
                            'Chile'
                            ) ,               
                        
                            (
                            'Torneo DIMAYOR I',
                            'https://www.transfermarkt.com.br/torneo-dimayor-i/startseite/wettbewerb/CO2T',
                            'https://tmssl.akamaized.net/images/logo/small/co2t.png?lm=1580728690',
                            'https://tmssl.akamaized.net/images/logo/header/co2t.png?lm=1580728690',
                            '-',
                            '2,18 mi. €',
                            '2,18 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/83.png?lm=1520611569',
                            'Colômbia'
                            ) ,               
                        
                            (
                            'Prva Nogometna Liga',
                            'https://www.transfermarkt.com.br/prva-nogometna-liga/startseite/wettbewerb/KR2',
                            'https://tmssl.akamaized.net/images/logo/small/kr2.png?lm=1662675729',
                            'https://tmssl.akamaized.net/images/logo/header/kr2.png?lm=1662675729',
                            '-',
                            '250 mil €',
                            '250 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/37.png?lm=1520611569',
                            'Croácia'
                            ) ,               
                        
                            (
                            'Cymru South',
                            'https://www.transfermarkt.com.br/cymru-south/startseite/wettbewerb/WA2S',
                            'https://tmssl.akamaized.net/images/logo/small/wa2s.png?lm=1668865420',
                            'https://tmssl.akamaized.net/images/logo/header/wa2s.png?lm=1668865420',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/191.png?lm=1520611569',
                            'País de Gales'
                            ) ,               
                        
                            (
                            'BGL Ligue',
                            'https://www.transfermarkt.com.br/bgl-ligue/startseite/wettbewerb/LUX1',
                            'https://tmssl.akamaized.net/images/logo/small/lux1.png?lm=1404087172',
                            'https://tmssl.akamaized.net/images/logo/header/lux1.png?lm=1404087172',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/99.png?lm=1520611569',
                            'Luxemburgo'
                            ) ,               
                        
                            (
                            'II. Liga',
                            'https://www.transfermarkt.com.br/ii-liga/startseite/wettbewerb/SK2',
                            'https://tmssl.akamaized.net/images/logo/small/sk2.png?lm=1539625603',
                            'https://tmssl.akamaized.net/images/logo/header/sk2.png?lm=1539625603',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/154.png?lm=1520611569',
                            'Eslováquia'
                            ) ,               
                        
                            (
                            'Cymru North',
                            'https://www.transfermarkt.com.br/cymru-north/startseite/wettbewerb/WAL2',
                            'https://tmssl.akamaized.net/images/logo/small/wal2.png?lm=1624021989',
                            'https://tmssl.akamaized.net/images/logo/header/wal2.png?lm=1624021989',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/191.png?lm=1520611569',
                            'País de Gales'
                            ) ,               
                        
                            (
                            'Championnat National',
                            'https://www.transfermarkt.com.br/championnat-national/startseite/wettbewerb/FR3',
                            'https://tmssl.akamaized.net/images/logo/small/fr3.png?lm=1655729224',
                            'https://tmssl.akamaized.net/images/logo/header/fr3.png?lm=1655729224',
                            '-',
                            '9,35 mi. €',
                            '9,35 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/50.png?lm=1520611569',
                            'França'
                            ) ,               
                        
                            (
                            'Premier League',
                            'https://www.transfermarkt.com.br/premier-league/startseite/wettbewerb/MAL1',
                            'https://tmssl.akamaized.net/images/logo/small/mal1.png?lm=1649336290',
                            'https://tmssl.akamaized.net/images/logo/header/mal1.png?lm=1649336290',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/106.png?lm=1520611569',
                            'Malta'
                            ) ,               
                        
                            (
                            'Prva liga FBiH',
                            'https://www.transfermarkt.com.br/prva-liga-fbih/startseite/wettbewerb/BOS2',
                            'https://tmssl.akamaized.net/images/logo/small/bos2.png?lm=1598130485',
                            'https://tmssl.akamaized.net/images/logo/header/bos2.png?lm=1598130485',
                            '-',
                            '40 mil €',
                            '40 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/24.png?lm=1569523290',
                            'Bósnia-Herzegovina'
                            ) ,               
                        
                            (
                            'Liga de Expansión MX Clausura',
                            'https://www.transfermarkt.com.br/liga-de-expansion-mx-clausura/startseite/wettbewerb/MEX2',
                            'https://tmssl.akamaized.net/images/logo/small/mex2.png?lm=1639483872',
                            'https://tmssl.akamaized.net/images/logo/header/mex2.png?lm=1639483872',
                            '-',
                            '2,42 mi. €',
                            '2,42 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/110.png?lm=1520611569',
                            'México'
                            ) ,               
                        
                            (
                            'Prva Liga RS',
                            'https://www.transfermarkt.com.br/prva-liga-rs/startseite/wettbewerb/BH2S',
                            'https://tmssl.akamaized.net/images/logo/small/bh2s.png?lm=1597512077',
                            'https://tmssl.akamaized.net/images/logo/header/bh2s.png?lm=1597512077',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/24.png?lm=1569523290',
                            'Bósnia-Herzegovina'
                            ) ,               
                        
                            (
                            'Gibraltar Football League',
                            'https://www.transfermarkt.com.br/gibraltar-football-league/startseite/wettbewerb/GI1',
                            'https://tmssl.akamaized.net/images/logo/small/gi1.png?lm=1657628016',
                            'https://tmssl.akamaized.net/images/logo/header/gi1.png?lm=1657628016',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/266.png?lm=1520611569',
                            'Gibraltar'
                            ) ,               
                        
                            (
                            'Promotion League',
                            'https://www.transfermarkt.com.br/promotion-league/startseite/wettbewerb/CHPR',
                            'https://tmssl.akamaized.net/images/logo/small/chpr.png?lm=1688637708',
                            'https://tmssl.akamaized.net/images/logo/header/chpr.png?lm=1688637708',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/148.png?lm=1520611569',
                            'Suiça'
                            ) ,               
                        
                            (
                            '1ste Nationale',
                            'https://www.transfermarkt.com.br/1ste-nationale/startseite/wettbewerb/BEL3',
                            'https://tmssl.akamaized.net/images/logo/small/bel3.png?lm=1484417840',
                            'https://tmssl.akamaized.net/images/logo/header/bel3.png?lm=1484417840',
                            '-',
                            '5 mil €',
                            '5 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/19.png?lm=1520611569',
                            'Bélgica'
                            ) ,               
                        
                            (
                            'Armenian First League',
                            'https://www.transfermarkt.com.br/armenian-first-league/startseite/wettbewerb/ARM2',
                            'https://tmssl.akamaized.net/images/logo/small/arm2.png?lm=1704901532',
                            'https://tmssl.akamaized.net/images/logo/header/arm2.png?lm=1704901532',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/10.png?lm=1520611569',
                            'Arménia'
                            ) ,               
                        
                            (
                            'Moravskoslezska fotbalova liga',
                            'https://www.transfermarkt.com.br/moravskoslezska-fotbalova-liga/startseite/wettbewerb/CZ3M',
                            'https://tmssl.akamaized.net/images/logo/small/cz3m.png?lm=1575758164',
                            'https://tmssl.akamaized.net/images/logo/header/cz3m.png?lm=1575758164',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/172.png?lm=1520611569',
                            'República Checa'
                            ) ,               
                        
                            (
                            'Championship',
                            'https://www.transfermarkt.com.br/championship/startseite/wettbewerb/NIR2',
                            'https://tmssl.akamaized.net/images/logo/small/nir2.png?lm=1519033686',
                            'https://tmssl.akamaized.net/images/logo/header/nir2.png?lm=1519033686',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/192.png?lm=1520611569',
                            'Irlanda do Norte'
                            ) ,               
                        
                            (
                            'Primera Divisió',
                            'https://www.transfermarkt.com.br/primera-divisio/startseite/wettbewerb/AND1',
                            'https://tmssl.akamaized.net/images/logo/small/and1.png?lm=1517041392',
                            'https://tmssl.akamaized.net/images/logo/header/and1.png?lm=1517041392',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/5.png?lm=1520611569',
                            'Andorra'
                            ) ,               
                        
                            (
                            'Second League Division B Gruppe 2 (-2023)',
                            'https://www.transfermarkt.com.br/second-league-division-b-gruppe-2-2023-/startseite/wettbewerb/RPLW',
                            'https://tmssl.akamaized.net/images/logo/small/rplw.png?lm=1689773971',
                            'https://tmssl.akamaized.net/images/logo/header/rplw.png?lm=1689773971',
                            '-',
                            '845 mil €',
                            '845 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/141.png?lm=1520611569',
                            'Rússia'
                            ) ,               
                        
                            (
                            'Druga Liga',
                            'https://www.transfermarkt.com.br/druga-liga/startseite/wettbewerb/UA3L',
                            'https://tmssl.akamaized.net/images/logo/small/ua3l.png?lm=1692796591',
                            'https://tmssl.akamaized.net/images/logo/header/ua3l.png?lm=1692796591',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/177.png?lm=1520611569',
                            'Ucrânia'
                            ) ,               
                        
                            (
                            'Intermedia',
                            'https://www.transfermarkt.com.br/intermedia/startseite/wettbewerb/NIR3',
                            'https://tmssl.akamaized.net/images/logo/small/nir3.png?lm=1541187384',
                            'https://tmssl.akamaized.net/images/logo/header/nir3.png?lm=1541187384',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/192.png?lm=1520611569',
                            'Irlanda do Norte'
                            ) ,               
                        
                            (
                            'Primera División Clausura',
                            'https://www.transfermarkt.com.br/primera-division-clausura/startseite/wettbewerb/SL1C',
                            'https://tmssl.akamaized.net/images/logo/small/sl1c.png?lm=1697094069',
                            'https://tmssl.akamaized.net/images/logo/header/sl1c.png?lm=1697094069',
                            '-',
                            '80 mil €',
                            '80 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/45.png?lm=1520611569',
                            'El Salvador'
                            ) ,               
                        
                            (
                            '2. CFL',
                            'https://www.transfermarkt.com.br/2-cfl/startseite/wettbewerb/MNE2',
                            'https://tmssl.akamaized.net/images/logo/small/mne2.png?lm=1625770218',
                            'https://tmssl.akamaized.net/images/logo/header/mne2.png?lm=1625770218',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/216.png?lm=1520611569',
                            'Montenegro'
                            ) ,               
                        
                            (
                            'Meridianbet 1. CFL',
                            'https://www.transfermarkt.com.br/meridianbet-1-cfl/startseite/wettbewerb/MNE1',
                            'https://tmssl.akamaized.net/images/logo/small/mne1.png?lm=1658245756',
                            'https://tmssl.akamaized.net/images/logo/header/mne1.png?lm=1658245756',
                            '-',
                            '180 mil €',
                            '180 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/216.png?lm=1520611569',
                            'Montenegro'
                            ) ,               
                        
                            (
                            'Hong Kong Premier League',
                            'https://www.transfermarkt.com.br/hong-kong-premier-league/startseite/wettbewerb/HGKG',
                            'https://tmssl.akamaized.net/images/logo/small/hgkg.png?lm=1692371410',
                            'https://tmssl.akamaized.net/images/logo/header/hgkg.png?lm=1692371410',
                            '-',
                            '130 mil €',
                            '130 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/218.png?lm=1520611569',
                            'Hong Kong'
                            ) ,               
                        
                            (
                            'Hong Kong Segunda Liga Divisão',
                            'https://www.transfermarkt.com.br/hong-kong-segunda-liga-divisao/startseite/wettbewerb/HK3L',
                            'https://tmssl.akamaized.net/images/logo/small/hk3l.png?lm=1681409733',
                            'https://tmssl.akamaized.net/images/logo/header/hk3l.png?lm=1681409733',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/218.png?lm=1520611569',
                            'Hong Kong'
                            ) ,               
                        
                            (
                            'Bardsragujn chumb',
                            'https://www.transfermarkt.com.br/bardsragujn-chumb/startseite/wettbewerb/ARM1',
                            'https://tmssl.akamaized.net/images/logo/small/arm1.png?lm=1691229942',
                            'https://tmssl.akamaized.net/images/logo/header/arm1.png?lm=1691229942',
                            '-',
                            '1,70 mi. €',
                            '1,70 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/10.png?lm=1520611569',
                            'Arménia'
                            ) ,               
                        
                            (
                            'Ehrenpromotion',
                            'https://www.transfermarkt.com.br/ehrenpromotion/startseite/wettbewerb/LUX2',
                            'https://tmssl.akamaized.net/images/logo/small/lux2.png?lm=1672393370',
                            'https://tmssl.akamaized.net/images/logo/header/lux2.png?lm=1672393370',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/99.png?lm=1520611569',
                            'Luxemburgo'
                            ) ,               
                        
                            (
                            'Scottish Championship',
                            'https://www.transfermarkt.com.br/scottish-championship/startseite/wettbewerb/SC2',
                            'https://tmssl.akamaized.net/images/logo/small/sc2.png?lm=1410807536',
                            'https://tmssl.akamaized.net/images/logo/header/sc2.png?lm=1410807536',
                            '-',
                            '368 mil €',
                            '368 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/190.png?lm=1520611569',
                            'Escócia'
                            ) ,               
                        
                            (
                            'Cymru Premier',
                            'https://www.transfermarkt.com.br/cymru-premier/startseite/wettbewerb/WAL1',
                            'https://tmssl.akamaized.net/images/logo/small/wal1.png?lm=1564139538',
                            'https://tmssl.akamaized.net/images/logo/header/wal1.png?lm=1564139538',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/191.png?lm=1520611569',
                            'País de Gales'
                            ) ,               
                        
                            (
                            'MLS Next Pro',
                            'https://www.transfermarkt.com.br/mls-next-pro/startseite/wettbewerb/MNP3',
                            'https://tmssl.akamaized.net/images/logo/small/mnp3.png?lm=1639596259',
                            'https://tmssl.akamaized.net/images/logo/header/mnp3.png?lm=1639596259',
                            '-',
                            '1,48 mi. €',
                            '1,48 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/184.png?lm=1520611569',
                            'Estados Unidos'
                            ) ,               
                        
                            (
                            'Tweede Divisie',
                            'https://www.transfermarkt.com.br/tweede-divisie/startseite/wettbewerb/NTD',
                            'https://tmssl.akamaized.net/images/logo/small/ntd.png?lm=1702393257',
                            'https://tmssl.akamaized.net/images/logo/header/ntd.png?lm=1702393257',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/122.png?lm=1520611569',
                            'Holanda'
                            ) ,               
                        
                            (
                            'Hong Kong First Division',
                            'https://www.transfermarkt.com.br/hong-kong-first-division/startseite/wettbewerb/HK2L',
                            'https://tmssl.akamaized.net/images/logo/small/hk2l.png?lm=1616692276',
                            'https://tmssl.akamaized.net/images/logo/header/hk2l.png?lm=1616692276',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/218.png?lm=1520611569',
                            'Hong Kong'
                            ) ,               
                        
                            (
                            'Superettan',
                            'https://www.transfermarkt.com.br/superettan/startseite/wettbewerb/SE2',
                            'https://tmssl.akamaized.net/images/logo/small/se2.png?lm=1633446978',
                            'https://tmssl.akamaized.net/images/logo/header/se2.png?lm=1633446978',
                            '-',
                            '550 mil €',
                            '550 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/147.png?lm=1520611569',
                            'Suécia'
                            ) ,               
                        
                            (
                            'League of Ireland First Division',
                            'https://www.transfermarkt.com.br/league-of-ireland-first-division/startseite/wettbewerb/IR2',
                            'https://tmssl.akamaized.net/images/logo/small/ir2.png?lm=1672532113',
                            'https://tmssl.akamaized.net/images/logo/header/ir2.png?lm=1672532113',
                            '-',
                            '20 mil €',
                            '20 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/72.png?lm=1520611569',
                            'Irlanda '
                            ) ,               
                        
                            (
                            'Regionalliga Mitte',
                            'https://www.transfermarkt.com.br/regionalliga-mitte/startseite/wettbewerb/ATRM',
                            'https://tmssl.akamaized.net/images/logo/small/atrm.png?lm=1647190277',
                            'https://tmssl.akamaized.net/images/logo/header/atrm.png?lm=1647190277',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/127.png?lm=1520611569',
                            'Áustria'
                            ) ,               
                        
                            (
                            'Philippines Football League',
                            'https://www.transfermarkt.com.br/philippines-football-league/startseite/wettbewerb/PFL1',
                            'https://tmssl.akamaized.net/images/logo/small/pfl1.png?lm=1659895243',
                            'https://tmssl.akamaized.net/images/logo/header/pfl1.png?lm=1659895243',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/134.png?lm=1520611569',
                            'Filipinas'
                            ) ,               
                        
                            (
                            'Bangladesh Premier League',
                            'https://www.transfermarkt.com.br/bangladesh-premier-league/startseite/wettbewerb/BGD1',
                            'https://tmssl.akamaized.net/images/logo/small/bgd1.png?lm=1551466827',
                            'https://tmssl.akamaized.net/images/logo/header/bgd1.png?lm=1551466827',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/16.png?lm=1520611569',
                            'Bangladeche'
                            ) ,               
                        
                            (
                            'Liga FUTVE Apertura',
                            'https://www.transfermarkt.com.br/liga-futve-apertura/startseite/wettbewerb/VZ1A',
                            'https://tmssl.akamaized.net/images/logo/small/vz1a.png?lm=1679095469',
                            'https://tmssl.akamaized.net/images/logo/header/vz1a.png?lm=1679095469',
                            '-',
                            '3,65 mi. €',
                            '3,65 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/182.png?lm=1520611569',
                            'Venezuela'
                            ) ,               
                        
                            (
                            'Veikkausliiga',
                            'https://www.transfermarkt.com.br/veikkausliiga/startseite/wettbewerb/FI1',
                            'https://tmssl.akamaized.net/images/logo/small/fi1.png?lm=1404085486',
                            'https://tmssl.akamaized.net/images/logo/header/fi1.png?lm=1404085486',
                            '-',
                            '1,88 mi. €',
                            '1,88 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/49.png?lm=1520611569',
                            'Finlândia'
                            ) ,               
                        
                            (
                            'Ettan Norra',
                            'https://www.transfermarkt.com.br/ettan-norra/startseite/wettbewerb/SE3N',
                            'https://tmssl.akamaized.net/images/logo/small/se3n.png?lm=1699739106',
                            'https://tmssl.akamaized.net/images/logo/header/se3n.png?lm=1699739106',
                            '-',
                            '100 mil €',
                            '100 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/147.png?lm=1520611569',
                            'Suécia'
                            ) ,               
                        
                            (
                            'Oman Professional League',
                            'https://www.transfermarkt.com.br/oman-professional-league/startseite/wettbewerb/OM1L',
                            'https://tmssl.akamaized.net/images/logo/small/om1l.png?lm=1705296147',
                            'https://tmssl.akamaized.net/images/logo/header/om1l.png?lm=1705296147',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/126.png?lm=1520611569',
                            'Omã'
                            ) ,               
                        
                            (
                            'Second League Division B Gruppe 1 (-2023)',
                            'https://www.transfermarkt.com.br/second-league-division-b-gruppe-1-2023-/startseite/wettbewerb/RPLS',
                            'https://tmssl.akamaized.net/images/logo/small/rpls.png?lm=1689773963',
                            'https://tmssl.akamaized.net/images/logo/header/rpls.png?lm=1689773963',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/141.png?lm=1520611569',
                            'Rússia'
                            ) ,               
                        
                            (
                            'Ettan Södra',
                            'https://www.transfermarkt.com.br/ettan-sodra/startseite/wettbewerb/SE3S',
                            'https://tmssl.akamaized.net/images/logo/small/se3s.png?lm=1699739136',
                            'https://tmssl.akamaized.net/images/logo/header/se3s.png?lm=1699739136',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/147.png?lm=1520611569',
                            'Suécia'
                            ) ,               
                        
                            (
                            'Pershaya Liga',
                            'https://www.transfermarkt.com.br/pershaya-liga/startseite/wettbewerb/WER2',
                            'https://tmssl.akamaized.net/images/logo/small/wer2.png?lm=1586259531',
                            'https://tmssl.akamaized.net/images/logo/header/wer2.png?lm=1586259531',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/18.png?lm=1520611569',
                            'Bielorrússia'
                            ) ,               
                        
                            (
                            '2.Division',
                            'https://www.transfermarkt.com.br/2-division/startseite/wettbewerb/DK3O',
                            'https://tmssl.akamaized.net/images/logo/small/dk3o.png?lm=1468946140',
                            'https://tmssl.akamaized.net/images/logo/header/dk3o.png?lm=1468946140',
                            '-',
                            '495 mil €',
                            '495 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/39.png?lm=1520611569',
                            'Dinamarca'
                            ) ,               
                        
                            (
                            'I-League 2',
                            'https://www.transfermarkt.com.br/i-league-2/startseite/wettbewerb/IND2',
                            'https://tmssl.akamaized.net/images/logo/small/ind2.png?lm=1705740752',
                            'https://tmssl.akamaized.net/images/logo/header/ind2.png?lm=1705740752',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/67.png?lm=1520611569',
                            'Índia'
                            ) ,               
                        
                            (
                            'Ghana Premier League',
                            'https://www.transfermarkt.com.br/ghana-premier-league/startseite/wettbewerb/GHPL',
                            'https://tmssl.akamaized.net/images/logo/small/ghpl.png?lm=1694436494',
                            'https://tmssl.akamaized.net/images/logo/header/ghpl.png?lm=1694436494',
                            '-',
                            '140 mil €',
                            '140 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/54.png?lm=1520611569',
                            'Gana'
                            ) ,               
                        
                            (
                            'Girabola',
                            'https://www.transfermarkt.com.br/girabola/startseite/wettbewerb/AN1L',
                            'https://tmssl.akamaized.net/images/logo/small/an1l.png?lm=1616743695',
                            'https://tmssl.akamaized.net/images/logo/header/an1l.png?lm=1616743695',
                            '-',
                            '350 mil €',
                            '350 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/6.png?lm=1520611569',
                            'Angola'
                            ) ,               
                        
                            (
                            'Liga 2',
                            'https://www.transfermarkt.com.br/liga-2/startseite/wettbewerb/PER2',
                            'https://tmssl.akamaized.net/images/logo/small/per2.png?lm=1579456913',
                            'https://tmssl.akamaized.net/images/logo/header/per2.png?lm=1579456913',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/133.png?lm=1520611569',
                            'Perú'
                            ) ,               
                        
                            (
                            'USL League One',
                            'https://www.transfermarkt.com.br/usl-league-one/startseite/wettbewerb/USC3',
                            'https://tmssl.akamaized.net/images/logo/small/usc3.png?lm=1538380520',
                            'https://tmssl.akamaized.net/images/logo/header/usc3.png?lm=1538380520',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/184.png?lm=1520611569',
                            'Estados Unidos'
                            ) ,               
                        
                            (
                            'National Premier League - Victoria',
                            'https://www.transfermarkt.com.br/national-premier-league-victoria/startseite/wettbewerb/A2VI',
                            'https://tmssl.akamaized.net/images/logo/small/a2vi.png?lm=1676575805',
                            'https://tmssl.akamaized.net/images/logo/header/a2vi.png?lm=1676575805',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/12.png?lm=1520611569',
                            'Austrália'
                            ) ,               
                        
                            (
                            'Liga Panameña de Fútbol Apertura',
                            'https://www.transfermarkt.com.br/liga-panamena-de-futbol-apertura/startseite/wettbewerb/PN1A',
                            'https://tmssl.akamaized.net/images/logo/small/pn1a.png?lm=1647938380',
                            'https://tmssl.akamaized.net/images/logo/header/pn1a.png?lm=1647938380',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/130.png?lm=1520611569',
                            'Panamá'
                            ) ,               
                        
                            (
                            'División Profesional Apertura',
                            'https://www.transfermarkt.com.br/division-profesional-apertura/startseite/wettbewerb/B1AP',
                            'https://tmssl.akamaized.net/images/logo/small/b1ap.png?lm=1638148860',
                            'https://tmssl.akamaized.net/images/logo/header/b1ap.png?lm=1638148860',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/23.png?lm=1520611569',
                            'Bolívia'
                            ) ,               
                        
                            (
                            'Liga Primera de Nicaragua Clausura',
                            'https://www.transfermarkt.com.br/liga-primera-de-nicaragua-clausura/startseite/wettbewerb/NC1C',
                            'https://tmssl.akamaized.net/images/logo/small/nc1c.png?lm=1674059028',
                            'https://tmssl.akamaized.net/images/logo/header/nc1c.png?lm=1674059028',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/121.png?lm=1520611569',
                            'Nicarágua'
                            ) ,               
                        
                            (
                            'Besta deild',
                            'https://www.transfermarkt.com.br/besta-deild/startseite/wettbewerb/IS1',
                            'https://tmssl.akamaized.net/images/logo/small/is1.png?lm=1646579749',
                            'https://tmssl.akamaized.net/images/logo/header/is1.png?lm=1646579749',
                            '-',
                            '305 mil €',
                            '305 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/73.png?lm=1520611569',
                            'Islândia'
                            ) ,               
                        
                            (
                            'Malaysia Super League',
                            'https://www.transfermarkt.com.br/malaysia-super-league/startseite/wettbewerb/MYS1',
                            'https://tmssl.akamaized.net/images/logo/small/mys1.png?lm=1675176671',
                            'https://tmssl.akamaized.net/images/logo/header/mys1.png?lm=1675176671',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/103.png?lm=1520611569',
                            'Malásia'
                            ) ,               
                        
                            (
                            'Regionalliga West',
                            'https://www.transfermarkt.com.br/regionalliga-west/startseite/wettbewerb/ATRW',
                            'https://tmssl.akamaized.net/images/logo/small/atrw.png?lm=1641377748',
                            'https://tmssl.akamaized.net/images/logo/header/atrw.png?lm=1641377748',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/127.png?lm=1520611569',
                            'Áustria'
                            ) ,               
                        
                            (
                            'Ykkösliiga',
                            'https://www.transfermarkt.com.br/ykkosliiga/startseite/wettbewerb/FI2',
                            'https://tmssl.akamaized.net/images/logo/small/fi2.png?lm=1706392336',
                            'https://tmssl.akamaized.net/images/logo/header/fi2.png?lm=1706392336',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/49.png?lm=1520611569',
                            'Finlândia'
                            ) ,               
                        
                            (
                            'Erovnuli Liga 2',
                            'https://www.transfermarkt.com.br/erovnuli-liga-2/startseite/wettbewerb/GEO2',
                            'https://tmssl.akamaized.net/images/logo/small/geo2.png?lm=1650631536',
                            'https://tmssl.akamaized.net/images/logo/header/geo2.png?lm=1650631536',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/53.png?lm=1520611569',
                            'Geórgia'
                            ) ,               
                        
                            (
                            'A Lyga',
                            'https://www.transfermarkt.com.br/a-lyga/startseite/wettbewerb/LI1',
                            'https://tmssl.akamaized.net/images/logo/small/li1.png?lm=1705689268',
                            'https://tmssl.akamaized.net/images/logo/header/li1.png?lm=1705689268',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/98.png?lm=1520611569',
                            'Lituânia'
                            ) ,               
                        
                            (
                            'Lengjudeild',
                            'https://www.transfermarkt.com.br/lengjudeild/startseite/wettbewerb/IS2',
                            'https://tmssl.akamaized.net/images/logo/small/is2.png?lm=1591283813',
                            'https://tmssl.akamaized.net/images/logo/header/is2.png?lm=1591283813',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/73.png?lm=1520611569',
                            'Islândia'
                            ) ,               
                        
                            (
                            'National Premier League - New South Wales',
                            'https://www.transfermarkt.com.br/national-premier-league-new-south-wales/startseite/wettbewerb/A2SW',
                            'https://tmssl.akamaized.net/images/logo/small/a2sw.png?lm=1676990286',
                            'https://tmssl.akamaized.net/images/logo/header/a2sw.png?lm=1676990286',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/12.png?lm=1520611569',
                            'Austrália'
                            ) ,               
                        
                            (
                            'PostNord-ligaen Avd. 1',
                            'https://www.transfermarkt.com.br/postnord-ligaen-avd-1/startseite/wettbewerb/NO31',
                            'https://tmssl.akamaized.net/images/logo/small/no31.png?lm=1478600434',
                            'https://tmssl.akamaized.net/images/logo/header/no31.png?lm=1478600434',
                            '-',
                            '270 mil €',
                            '270 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/125.png?lm=1520611569',
                            'Noruega'
                            ) ,               
                        
                            (
                            '2. deild',
                            'https://www.transfermarkt.com.br/2-deild/startseite/wettbewerb/ISL3',
                            'https://tmssl.akamaized.net/images/logo/small/isl3.png?lm=1648809208',
                            'https://tmssl.akamaized.net/images/logo/header/isl3.png?lm=1648809208',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/73.png?lm=1520611569',
                            'Islândia'
                            ) ,               
                        
                            (
                            'Jamaica Premier League',
                            'https://www.transfermarkt.com.br/jamaica-premier-league/startseite/wettbewerb/JPL1',
                            'https://tmssl.akamaized.net/images/logo/small/jpl1.png?lm=1626106395',
                            'https://tmssl.akamaized.net/images/logo/header/jpl1.png?lm=1626106395',
                            '-',
                            '125 mil €',
                            '125 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/76.png?lm=1520611569',
                            'Jamaica'
                            ) ,               
                        
                            (
                            'PostNord-ligaen Avd. 2',
                            'https://www.transfermarkt.com.br/postnord-ligaen-avd-2/startseite/wettbewerb/NO32',
                            'https://tmssl.akamaized.net/images/logo/small/no32.png?lm=1478600525',
                            'https://tmssl.akamaized.net/images/logo/header/no32.png?lm=1478600525',
                            '-',
                            '1,14 mi. €',
                            '1,14 mi. €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/125.png?lm=1520611569',
                            'Noruega'
                            ) ,               
                        
                            (
                            'Second League Division B Gruppe 4 (-2023)',
                            'https://www.transfermarkt.com.br/second-league-division-b-gruppe-4-2023-/startseite/wettbewerb/RPLU',
                            'https://tmssl.akamaized.net/images/logo/small/rplu.png?lm=1689774005',
                            'https://tmssl.akamaized.net/images/logo/header/rplu.png?lm=1689774005',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/141.png?lm=1520611569',
                            'Rússia'
                            ) ,               
                        
                            (
                            'Segona Divisió',
                            'https://www.transfermarkt.com.br/segona-divisio/startseite/wettbewerb/AND2',
                            'https://tmssl.akamaized.net/images/logo/small/and2.png?lm=1698310084',
                            'https://tmssl.akamaized.net/images/logo/header/and2.png?lm=1698310084',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/5.png?lm=1520611569',
                            'Andorra'
                            ) ,               
                        
                            (
                            '2. Division A (Phase 2)',
                            'https://www.transfermarkt.com.br/2-division-a-phase-2-/startseite/wettbewerb/R3D2',
                            'https://tmssl.akamaized.net/images/logo/small/r3d2.png?lm=1689773936',
                            'https://tmssl.akamaized.net/images/logo/header/r3d2.png?lm=1689773936',
                            '-',
                            '210 mil €',
                            '210 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/141.png?lm=1520611569',
                            'Rússia'
                            ) ,               
                        
                            (
                            'Liga Panameña de Fútbol Clausura',
                            'https://www.transfermarkt.com.br/liga-panamena-de-futbol-clausura/startseite/wettbewerb/PN1C',
                            'https://tmssl.akamaized.net/images/logo/small/pn1c.png?lm=1647938410',
                            'https://tmssl.akamaized.net/images/logo/header/pn1c.png?lm=1647938410',
                            '-',
                            '76 mil €',
                            '76 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/130.png?lm=1520611569',
                            'Panamá'
                            ) ,               
                        
                            (
                            'Challenge League - Finals',
                            'https://www.transfermarkt.com.br/challenge-league-finals/startseite/wettbewerb/MT2P',
                            'https://tmssl.akamaized.net/images/logo/small/mt2p.png?lm=1673944021',
                            'https://tmssl.akamaized.net/images/logo/header/mt2p.png?lm=1673944021',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/106.png?lm=1520611569',
                            'Malta'
                            ) ,               
                        
                            (
                            'Canadian Premier League',
                            'https://www.transfermarkt.com.br/canadian-premier-league/startseite/wettbewerb/CDN1',
                            'https://tmssl.akamaized.net/images/logo/small/cdn1.png?lm=1644928004',
                            'https://tmssl.akamaized.net/images/logo/header/cdn1.png?lm=1644928004',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/80.png?lm=1520611569',
                            'Canadá'
                            ) ,               
                        
                            (
                            'Pervaya Liga',
                            'https://www.transfermarkt.com.br/pervaya-liga/startseite/wettbewerb/KAS2',
                            'https://tmssl.akamaized.net/images/logo/small/kas2.png?lm=1681548307',
                            'https://tmssl.akamaized.net/images/logo/header/kas2.png?lm=1681548307',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/81.png?lm=1520611569',
                            'Cazaquistão'
                            ) ,               
                        
                            (
                            'Fiji Premier League',
                            'https://www.transfermarkt.com.br/fiji-premier-league/startseite/wettbewerb/FIJ1',
                            'https://tmssl.akamaized.net/images/logo/small/fij1.png?lm=1627666227',
                            'https://tmssl.akamaized.net/images/logo/header/fij1.png?lm=1627666227',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/48.png?lm=1520611569',
                            'Fiji'
                            ) ,               
                        
                            (
                            'Cambodian Premier League',
                            'https://www.transfermarkt.com.br/cambodian-premier-league/startseite/wettbewerb/KHM1',
                            'https://tmssl.akamaized.net/images/logo/small/khm1.png?lm=1692605660',
                            'https://tmssl.akamaized.net/images/logo/header/khm1.png?lm=1692605660',
                            '-',
                            '25 mil €',
                            '25 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/79.png?lm=1520611569',
                            'Camboja'
                            ) ,               
                        
                            (
                            'Singapore Premier League',
                            'https://www.transfermarkt.com.br/singapore-premier-league/startseite/wettbewerb/SIN1',
                            'https://tmssl.akamaized.net/images/logo/small/sin1.png?lm=1560163015',
                            'https://tmssl.akamaized.net/images/logo/header/sin1.png?lm=1560163015',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/153.png?lm=1520611569',
                            'Singapura'
                            ) ,               
                        
                            (
                            'National League - North',
                            'https://www.transfermarkt.com.br/national-league-north/startseite/wettbewerb/NNL1',
                            'https://tmssl.akamaized.net/images/logo/small/nnl1.png?lm=1705543185',
                            'https://tmssl.akamaized.net/images/logo/header/nnl1.png?lm=1705543185',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/120.png?lm=1520611569',
                            'Nova Zelândia'
                            ) ,               
                        
                            (
                            'Kyrgyz Premier League',
                            'https://www.transfermarkt.com.br/kyrgyz-premier-league/startseite/wettbewerb/KG1L',
                            'https://tmssl.akamaized.net/images/logo/small/kg1l.png?lm=1618860696',
                            'https://tmssl.akamaized.net/images/logo/header/kg1l.png?lm=1618860696',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/90.png?lm=1520611569',
                            'Quirguistão'
                            ) ,               
                        
                            (
                            'Ykkönen',
                            'https://www.transfermarkt.com.br/ykkonen/startseite/wettbewerb/FIYK',
                            'https://tmssl.akamaized.net/images/logo/small/fiyk.png?lm=1706392172',
                            'https://tmssl.akamaized.net/images/logo/header/fiyk.png?lm=1706392172',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/49.png?lm=1520611569',
                            'Finlândia'
                            ) ,               
                        
                            (
                            'Gozo Football League First Division',
                            'https://www.transfermarkt.com.br/gozo-football-league-first-division/startseite/wettbewerb/GZO1',
                            'https://tmssl.akamaized.net/images/logo/small/gzo1.png?lm=1657194391',
                            'https://tmssl.akamaized.net/images/logo/header/gzo1.png?lm=1657194391',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/106.png?lm=1520611569',
                            'Malta'
                            ) ,               
                        
                            (
                            'Uzbekistan Pro Liga',
                            'https://www.transfermarkt.com.br/uzbekistan-pro-liga/startseite/wettbewerb/UZ2L',
                            'https://tmssl.akamaized.net/images/logo/small/uz2l.png?lm=1620656401',
                            'https://tmssl.akamaized.net/images/logo/header/uz2l.png?lm=1620656401',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/180.png?lm=1520611569',
                            'Uzbequistão'
                            ) ,               
                        
                            (
                            'Vysshaya Liga',
                            'https://www.transfermarkt.com.br/vysshaya-liga/startseite/wettbewerb/TAD1',
                            'https://tmssl.akamaized.net/images/logo/small/tad1.png?lm=1591974959',
                            'https://tmssl.akamaized.net/images/logo/header/tad1.png?lm=1591974959',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/165.png?lm=1520611569',
                            'Tajiquistão'
                            ) ,               
                        
                            (
                            'Taiwan Football League Div.2',
                            'https://www.transfermarkt.com.br/taiwan-football-league-div-2/startseite/wettbewerb/TFL2',
                            'https://tmssl.akamaized.net/images/logo/small/tfl2.png?lm=1595058711',
                            'https://tmssl.akamaized.net/images/logo/header/tfl2.png?lm=1595058711',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/164.png?lm=1679300082',
                            'Taipé Chinesa'
                            ) ,               
                        
                            (
                            'Liga FUTVE 2. Segunda Fase',
                            'https://www.transfermarkt.com.br/liga-futve-2-segunda-fase/startseite/wettbewerb/VN2C',
                            'https://tmssl.akamaized.net/images/logo/small/vn2c.png?lm=1679136477',
                            'https://tmssl.akamaized.net/images/logo/header/vn2c.png?lm=1679136477',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/182.png?lm=1520611569',
                            'Venezuela'
                            ) ,               
                        
                            (
                            'Esiliiga',
                            'https://www.transfermarkt.com.br/esiliiga/startseite/wettbewerb/EST2',
                            'https://tmssl.akamaized.net/images/logo/small/est2.png?lm=1534338403',
                            'https://tmssl.akamaized.net/images/logo/header/est2.png?lm=1534338403',
                            '-',
                            '33 mil €',
                            '33 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/47.png?lm=1520611569',
                            'Estónia'
                            ) ,               
                        
                            (
                            'National League Championship',
                            'https://www.transfermarkt.com.br/national-league-championship/startseite/wettbewerb/NZNL',
                            'https://tmssl.akamaized.net/images/logo/small/nznl.png?lm=1705543218',
                            'https://tmssl.akamaized.net/images/logo/header/nznl.png?lm=1705543218',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/120.png?lm=1520611569',
                            'Nova Zelândia'
                            ) ,               
                        
                            (
                            'NISA',
                            'https://www.transfermarkt.com.br/nisa/startseite/wettbewerb/NIS3',
                            'https://tmssl.akamaized.net/images/logo/small/nis3.png?lm=1654793703',
                            'https://tmssl.akamaized.net/images/logo/header/nis3.png?lm=1654793703',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/184.png?lm=1520611569',
                            'Estados Unidos'
                            ) ,               
                        
                            (
                            'Liga FUTVE',
                            'https://www.transfermarkt.com.br/liga-futve/startseite/wettbewerb/VZ1L',
                            'https://tmssl.akamaized.net/images/logo/small/vz1l.png?lm=1648285303',
                            'https://tmssl.akamaized.net/images/logo/header/vz1l.png?lm=1648285303',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/182.png?lm=1520611569',
                            'Venezuela'
                            ) ,               
                        
                            (
                            'National League - Central',
                            'https://www.transfermarkt.com.br/national-league-central/startseite/wettbewerb/NCL1',
                            'https://tmssl.akamaized.net/images/logo/small/ncl1.png?lm=1705543193',
                            'https://tmssl.akamaized.net/images/logo/header/ncl1.png?lm=1705543193',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/120.png?lm=1520611569',
                            'Nova Zelândia'
                            ) ,               
                        
                            (
                            'Betri-deildin',
                            'https://www.transfermarkt.com.br/betri-deildin/startseite/wettbewerb/FARO',
                            'https://tmssl.akamaized.net/images/logo/small/faro.png?lm=1525363290',
                            'https://tmssl.akamaized.net/images/logo/header/faro.png?lm=1525363290',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/208.png?lm=1520611569',
                            'Ilhas Faroe'
                            ) ,               
                        
                            (
                            'China League Two A',
                            'https://www.transfermarkt.com.br/china-league-two-a/startseite/wettbewerb/CHL3',
                            'https://tmssl.akamaized.net/images/logo/small/chl3.png?lm=1618491912',
                            'https://tmssl.akamaized.net/images/logo/header/chl3.png?lm=1618491912',
                            '-',
                            '386 mil €',
                            '386 mil €',
                            'https://tmssl.akamaized.net/images/flagge/tiny/34.png?lm=1520611569',
                            'China'
                            ) ,               
                        
                            (
                            'Moçambola',
                            'https://www.transfermarkt.com.br/mocambola/startseite/wettbewerb/MO1L',
                            'https://tmssl.akamaized.net/images/logo/small/mo1l.png?lm=1616743589',
                            'https://tmssl.akamaized.net/images/logo/header/mo1l.png?lm=1616743589',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/115.png?lm=1520611569',
                            'Moçambique'
                            ) ,               
                        
                            (
                            'Esiliiga B',
                            'https://www.transfermarkt.com.br/esiliiga-b/startseite/wettbewerb/EST3',
                            'https://tmssl.akamaized.net/images/logo/small/est3.png?lm=1534338505',
                            'https://tmssl.akamaized.net/images/logo/header/est3.png?lm=1534338505',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/47.png?lm=1520611569',
                            'Estónia'
                            ) ,               
                        
                            (
                            'League Two Promotion Stage',
                            'https://www.transfermarkt.com.br/league-two-promotion-stage/startseite/wettbewerb/CH3P',
                            'https://tmssl.akamaized.net/images/logo/small/ch3p.png?lm=1638278660',
                            'https://tmssl.akamaized.net/images/logo/header/ch3p.png?lm=1638278660',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/34.png?lm=1520611569',
                            'China'
                            ) ,               
                        
                            (
                            'Nakotnes liga',
                            'https://www.transfermarkt.com.br/nakotnes-liga/startseite/wettbewerb/LET2',
                            'https://tmssl.akamaized.net/images/logo/small/let2.png?lm=1703175601',
                            'https://tmssl.akamaized.net/images/logo/header/let2.png?lm=1703175601',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/92.png?lm=1520611569',
                            'Letónia'
                            ) ,               
                        
                            (
                            'Lao League 1',
                            'https://www.transfermarkt.com.br/lao-league-1/startseite/wettbewerb/LAO1',
                            'https://tmssl.akamaized.net/images/logo/small/lao1.png?lm=1676437959',
                            'https://tmssl.akamaized.net/images/logo/header/lao1.png?lm=1676437959',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/91.png?lm=1520611569',
                            'Laos'
                            ) ,               
                        
                            (
                            'Liga Dimayor Finalización',
                            'https://www.transfermarkt.com.br/liga-dimayor-finalizacion/startseite/wettbewerb/COL1',
                            'https://tmssl.akamaized.net/images/logo/small/col1.png?lm=1630312566',
                            'https://tmssl.akamaized.net/images/logo/header/col1.png?lm=1630312566',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/83.png?lm=1520611569',
                            'Colômbia'
                            ) ,               
                        
                            (
                            'Liga Dominicana de Fútbol',
                            'https://www.transfermarkt.com.br/liga-dominicana-de-futbol/startseite/wettbewerb/DOM1',
                            'https://tmssl.akamaized.net/images/logo/small/dom1.png?lm=1705487387',
                            'https://tmssl.akamaized.net/images/logo/header/dom1.png?lm=1705487387',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/43.png?lm=1520611569',
                            'República Dominicana'
                            ) ,               
                        
                            (
                            'National League - South',
                            'https://www.transfermarkt.com.br/national-league-south/startseite/wettbewerb/NSL1',
                            'https://tmssl.akamaized.net/images/logo/small/nsl1.png?lm=1705543200',
                            'https://tmssl.akamaized.net/images/logo/header/nsl1.png?lm=1705543200',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/120.png?lm=1520611569',
                            'Nova Zelândia'
                            ) ,               
                        
                            (
                            'Liga 1 (Promoção)',
                            'https://www.transfermarkt.com.br/liga-1-promocao-/startseite/wettbewerb/ML1P',
                            'https://tmssl.akamaized.net/images/logo/small/ml1p.png?lm=1678301517',
                            'https://tmssl.akamaized.net/images/logo/header/ml1p.png?lm=1678301517',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/112.png?lm=1520611569',
                            'Moldávia'
                            ) ,               
                        
                            (
                            '1. deild',
                            'https://www.transfermarkt.com.br/1-deild/startseite/wettbewerb/FAR2',
                            'https://tmssl.akamaized.net/images/logo/small/far2.png?lm=1595275674',
                            'https://tmssl.akamaized.net/images/logo/header/far2.png?lm=1595275674',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/208.png?lm=1520611569',
                            'Ilhas Faroe'
                            ) ,               
                        
                            (
                            'Liga Dominicana de Fútbol - Liguilla',
                            'https://www.transfermarkt.com.br/liga-dominicana-de-futbol-liguilla/startseite/wettbewerb/DO1P',
                            'https://tmssl.akamaized.net/images/logo/small/do1p.png?lm=1651331150',
                            'https://tmssl.akamaized.net/images/logo/header/do1p.png?lm=1651331150',
                            '-',
                            '-',
                            '+-0',
                            'https://tmssl.akamaized.net/images/flagge/tiny/43.png?lm=1520611569',
                            'República Dominicana'
                            ) ,               
                        