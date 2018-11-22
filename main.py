# IMPORTS

import json

# GLOBALS

INPUT_FILE = 'ExportPre15_1.mbox'
FILE_OPEN_MODE = 'r'
FILE_WRITE_MODE = 'w'
FILE_ENCODING = 'utf-8'
OUTPUT_FILE = 'leads_json.txt'

YOU_ARE_RECEIVING_THIS_EMAIL = "You are receiving this email because you requested a quote on "

ACCOUNT_NUMBER_FIELD = 'AccountNumber'
SET_ACCOUNT_NUMBER_FIELD = {ACCOUNT_NUMBER_FIELD}
PROJECT_NAME_FIELD = 'ProjectName'
COMPANY_FIELD = 'Company'
FIRST_NAME_FIELD = 'FirstName'
LAST_NAME_FIELD = 'LastName'
JOB_TITLE_FIELD = 'JobTitle'
EMAIL_FIELD = 'Email'
PHONE_FIELD = 'Phone'
EMPLOYEES_FIELD = 'Employees'
COUNTRY_FIELD = 'Country'
LANGUAGE_FIELD = 'Language'
REFERRER_FIELD = 'Source'
WORK_STRUCT_FIELD = 'WorkStructure'
PROJECT_START_FIELD = 'StartDate'
DURATION_FIELD = 'Duration'
RESOURCE_LOCATION_FIELD = 'ResourceLocation'
BUDGET_FIELD = 'Budget'
PROJECT_BRANDING_FIELD = 'ProjectBranding'
PROJECT_FUNDING_FIELD = 'ProjectFunding'
PROJECT_STATUS_FIELD = 'ProjectStatus'
ADDITIONAL_INFO_FIELD = 'ProjectDescription'
SET_ADDITIONAL_INFO_FIELD = {ADDITIONAL_INFO_FIELD}
NON_FUNCTIONAL_RESOURCES_FIELD  = 'NonFunctionalResources'
SET_NON_FUNCTIONAL_RESOURCES_FIELD = {NON_FUNCTIONAL_RESOURCES_FIELD}

RESOURCE_FIELD = 'Technology'
TEAM_LEADER_FIELD = 'TeamLeader'
SET_TEAM_LEADER_FIELD = {TEAM_LEADER_FIELD}
SENIOR_FIELD = 'Senior'
MIDDLE_FIELD = 'Middle'
JUNIOR_FIELD = 'Junior'
SET_SENIORITY_FIELD = {TEAM_LEADER_FIELD, SENIOR_FIELD, MIDDLE_FIELD, JUNIOR_FIELD}

LABEL_TO_FIELD_DICT = {
	'Numero di conto:' : ACCOUNT_NUMBER_FIELD,
	'Kontonummer:' : ACCOUNT_NUMBER_FIELD,
	'Accountnummer:' : ACCOUNT_NUMBER_FIELD,
	'Konto number:' : ACCOUNT_NUMBER_FIELD,
	'Numar de cont:' : ACCOUNT_NUMBER_FIELD,
	'Αριθμός λογαριασμού:' : ACCOUNT_NUMBER_FIELD,
	'Számlaszám:' : ACCOUNT_NUMBER_FIELD,
	'Account Number:' : ACCOUNT_NUMBER_FIELD,
	'Numéro de compte:' : ACCOUNT_NUMBER_FIELD,
	'Номер на сметка:' : ACCOUNT_NUMBER_FIELD,
	'Broj računa:' : ACCOUNT_NUMBER_FIELD,
	'Номер учетной записи:' : ACCOUNT_NUMBER_FIELD,
	'Número de cuenta:' : ACCOUNT_NUMBER_FIELD,
	'Rekeningnummer:' : ACCOUNT_NUMBER_FIELD,
	'Número da conta:' : ACCOUNT_NUMBER_FIELD,
	'Project Name:' : PROJECT_NAME_FIELD,
	'Projekt Name:' : PROJECT_NAME_FIELD,
	'Projektnamn:' : PROJECT_NAME_FIELD,
	'Nombre del Proyecto:' : PROJECT_NAME_FIELD,
    'Projekt Navn:' : PROJECT_NAME_FIELD,
    'Nome do Projeto:' : PROJECT_NAME_FIELD,
	'Vállalat:' : COMPANY_FIELD,
	'Company:' : COMPANY_FIELD,
	'Bedrijf:' : COMPANY_FIELD,
	'Gesellschaft:' : COMPANY_FIELD,
	'Empresa:' : COMPANY_FIELD,
	'Εταιρία:' : COMPANY_FIELD,
	'Företag:' : COMPANY_FIELD,
	'Compania:' : COMPANY_FIELD,
	'Društvo:' : COMPANY_FIELD,
	'Компания:' : COMPANY_FIELD,
	'Ettevõte:' : COMPANY_FIELD,
	'Società:' : COMPANY_FIELD,
	'Société:' : COMPANY_FIELD,
    'Selskabet:' : COMPANY_FIELD,
    'Kompanija:' : COMPANY_FIELD,
	'First name:' : FIRST_NAME_FIELD,
	'Numele:' : FIRST_NAME_FIELD,
	'Prénom:' : FIRST_NAME_FIELD,
	'Keresztnév:' : FIRST_NAME_FIELD,
	'Voornaam:' : FIRST_NAME_FIELD,
	'Förnamn:' : FIRST_NAME_FIELD,
	'Nome:' : FIRST_NAME_FIELD,
	'Първо име:' : FIRST_NAME_FIELD,
	'Ονομα:' : FIRST_NAME_FIELD,
	'Eesnimi:' : FIRST_NAME_FIELD,
	'Primeiro nome:' : FIRST_NAME_FIELD,
	'Nombre:' : FIRST_NAME_FIELD,
	'Ime:' : FIRST_NAME_FIELD,
	'Vorname:' : FIRST_NAME_FIELD,
    'Fornavn:' : FIRST_NAME_FIELD,
    'Имя:' : FIRST_NAME_FIELD, # new
	'Apellido:' : LAST_NAME_FIELD,
	'Vezetéknév:' : LAST_NAME_FIELD,
	'Sobrenome:' : LAST_NAME_FIELD,
	'Prezime:' : LAST_NAME_FIELD,
	'Last name:' : LAST_NAME_FIELD,
	'Фамилия:' : LAST_NAME_FIELD,
	'Επίθετο:' : LAST_NAME_FIELD,
	'Achternaam:' : LAST_NAME_FIELD,
	'Efternamn:' : LAST_NAME_FIELD,
	'Perekonnanimi:' : LAST_NAME_FIELD,
	'Nachname:' : LAST_NAME_FIELD,
	'Cognome:' : LAST_NAME_FIELD,
	'Nom de famille:' : LAST_NAME_FIELD,
    'Efternavn:' : LAST_NAME_FIELD,
	'Job title:' : JOB_TITLE_FIELD,
	'Titre du poste:' : JOB_TITLE_FIELD,
	'Título del trabajo:' : JOB_TITLE_FIELD,
	'Должность:' : JOB_TITLE_FIELD,
	'Töö nimetus:' : JOB_TITLE_FIELD,
	'Professione:' : JOB_TITLE_FIELD,
	'Título do trabalho:' : JOB_TITLE_FIELD,
	'Naziv posla:' : JOB_TITLE_FIELD,
	'Длъжност:' : JOB_TITLE_FIELD,
	'Functietitel:' : JOB_TITLE_FIELD,
	'Τίτλος εργασίας:' : JOB_TITLE_FIELD,
	'Titlul postului:' : JOB_TITLE_FIELD,
	'Berufsbezeichnung:' : JOB_TITLE_FIELD,
	'Jobbtitel:' : JOB_TITLE_FIELD,
    'Stilling:' : JOB_TITLE_FIELD,
	'Email:' : EMAIL_FIELD,
	'електронна поща:' : EMAIL_FIELD,
	'E-post:' : EMAIL_FIELD,
	'E-mail:' : EMAIL_FIELD,
	'E-Mail:' : EMAIL_FIELD,
	'Munka megnevezése:' : EMAIL_FIELD,
	'ΗΛΕΚΤΡΟΝΙΚΗ ΔΙΕΥΘΥΝΣΗ:' : EMAIL_FIELD,
	'Электронная почта:' : EMAIL_FIELD,
	'Correo electrónico:' : EMAIL_FIELD,
	'Telefoon:' : PHONE_FIELD,
	'Телефон:' : PHONE_FIELD,
	'Teléfono:' : PHONE_FIELD,
	'Telefono:' : PHONE_FIELD,
	'Phone:' : PHONE_FIELD,
	'Telefone:' : PHONE_FIELD,
	'Τηλέφωνο:' : PHONE_FIELD,
	'Telefon:' : PHONE_FIELD,
	'Téléphone:' : PHONE_FIELD,
	'телефон:' : PHONE_FIELD,
	'Сотрудники:' : EMPLOYEES_FIELD,
	'Az alkalmazottak:' : EMPLOYEES_FIELD,
	'Werknemers:' : EMPLOYEES_FIELD,
	'Служители:' : EMPLOYEES_FIELD,
	'Zaposlenici:' : EMPLOYEES_FIELD,
	'Υπαλλήλους:' : EMPLOYEES_FIELD,
	'Empleados:' : EMPLOYEES_FIELD,
	'Töötajad:' : EMPLOYEES_FIELD,
	'dipendenti:' : EMPLOYEES_FIELD,
	'Funcionários:' : EMPLOYEES_FIELD,
	'Anställda:' : EMPLOYEES_FIELD,
	'Mitarbeiter:' : EMPLOYEES_FIELD,
	'Angajati:' : EMPLOYEES_FIELD,
	'Employees:' : EMPLOYEES_FIELD,
	'Employés:' : EMPLOYEES_FIELD,
    'Medarbejdere:' : EMPLOYEES_FIELD,
    'Zaposleni:' : EMPLOYEES_FIELD,
	'Country:' : COUNTRY_FIELD,
	'Land:' : COUNTRY_FIELD,
	'Riik:' : COUNTRY_FIELD,
	'Zemlja:' : COUNTRY_FIELD,
	'Χώρα:' : COUNTRY_FIELD,
	'Държава:' : COUNTRY_FIELD,
	'Tara:' : COUNTRY_FIELD,
	'País:' : COUNTRY_FIELD,
	'Paese:' : COUNTRY_FIELD,
	'Страна:' : COUNTRY_FIELD,
	'Ország:' : COUNTRY_FIELD,
	'Pays:' : COUNTRY_FIELD,
	'Language:' : LANGUAGE_FIELD,
	'Referrer:' : REFERRER_FIELD,
	'Δομή εργασίας:' : WORK_STRUCT_FIELD,
	'Estrutura de trabalho:' : WORK_STRUCT_FIELD,
	'Estructura de trabajo:' : WORK_STRUCT_FIELD,
	'Structura de lucru:' : WORK_STRUCT_FIELD,
	'Структура работы:' : WORK_STRUCT_FIELD,
	'Munka szerkezet:' : WORK_STRUCT_FIELD,
	'Structure de travail:' : WORK_STRUCT_FIELD,
	'Работна структура:' : WORK_STRUCT_FIELD,
	'Töö struktuur:' : WORK_STRUCT_FIELD,
	'Arbete struktur:' : WORK_STRUCT_FIELD,
	'Struttura di lavoro:' : WORK_STRUCT_FIELD,
	'Struktura rada:' : WORK_STRUCT_FIELD,
	'Werk Structuur:' : WORK_STRUCT_FIELD,
	'Work Structure:' : WORK_STRUCT_FIELD,
	'Arbeitsstruktur:' : WORK_STRUCT_FIELD,
    'Arbejde Struktur:' : WORK_STRUCT_FIELD,
	'Kada biste željeli početi?:' : PROJECT_START_FIELD,
    'Kada želite da počnete?:' : PROJECT_START_FIELD, # same language as the one above, croatian
	'Wann möchten Sie beginnen?:' : PROJECT_START_FIELD,
	'Mikor szeretne elkezdeni?:' : PROJECT_START_FIELD,
	'Millal soovite alustada?:' : PROJECT_START_FIELD,
	'Quando vuoi cominciare?:' : PROJECT_START_FIELD,
	'När vill du börja?:' : PROJECT_START_FIELD,
	'¿Cuándo quieres empezar?:' : PROJECT_START_FIELD,
	'When would you like to start?:' : PROJECT_START_FIELD,
	'Quando você gostaria de começar?:' : PROJECT_START_FIELD,
	'Quand souhaitez-vous commencer?:' : PROJECT_START_FIELD,
    'Hvornår vil du gerne begynde?:' : PROJECT_START_FIELD,
	'Kestus?:' : DURATION_FIELD,
	'Varaktighet?:' : DURATION_FIELD,
	'Durée?:' : DURATION_FIELD,
	'Duração?:' : DURATION_FIELD,
	'Duración?:' : DURATION_FIELD,
	'Trajanje?:' : DURATION_FIELD,
	'Időtartam?:' : DURATION_FIELD,
	'Durata?:' : DURATION_FIELD,
	'Dauer?:' : DURATION_FIELD,
    'Duration?:' : DURATION_FIELD,
    'Varighed?:' : DURATION_FIELD,
	'Allika asukoht:' : RESOURCE_LOCATION_FIELD,
	'Posizione risorsa:' : RESOURCE_LOCATION_FIELD,
	'Lokacija resursa:' : RESOURCE_LOCATION_FIELD,
	'Emplacement de la ressource:' : RESOURCE_LOCATION_FIELD,
	'Local do Recurso:' : RESOURCE_LOCATION_FIELD,
	'Ubicación del recurso:' : RESOURCE_LOCATION_FIELD,
	'Resource Location:' : RESOURCE_LOCATION_FIELD,
	'Erőforrás helye:' : RESOURCE_LOCATION_FIELD,
	'Ressource Standort:' : RESOURCE_LOCATION_FIELD,
	'Resurs Plats:' : RESOURCE_LOCATION_FIELD,
	'Budžet:' : BUDGET_FIELD,
	'Költségvetés:' : BUDGET_FIELD,
	'Бюджет:' : BUDGET_FIELD,
	'Προϋπολογισμός:' : BUDGET_FIELD,
	'Begroting:' : BUDGET_FIELD,
	'Buget:' : BUDGET_FIELD,
	'Budget:' : BUDGET_FIELD,
	'бюджет:' : BUDGET_FIELD,
	'Presupuesto:' : BUDGET_FIELD,
	'Orçamento:' : BUDGET_FIELD,
	'Projektmarkenbildung:' : PROJECT_BRANDING_FIELD,
	'Brendiranje projekata:' : PROJECT_BRANDING_FIELD,
	'Projekt Branding:' : PROJECT_BRANDING_FIELD,
	'Project Branding:' : PROJECT_BRANDING_FIELD,
	'Proyecto de marca:' : PROJECT_BRANDING_FIELD,
	'Branding do projeto:' : PROJECT_BRANDING_FIELD,
    'Branding af projektet:' : PROJECT_BRANDING_FIELD,
	'Projekt Finansiering:' : PROJECT_FUNDING_FIELD,
	'Project Funding:' : PROJECT_FUNDING_FIELD,
	'Finansiranje projekta:' : PROJECT_FUNDING_FIELD,
	'Financiamento do Projeto:' : PROJECT_FUNDING_FIELD,
	'Projektfinanzierung:' : PROJECT_FUNDING_FIELD,
	'Projektfinanszírozás:' : PROJECT_FUNDING_FIELD,
	'Financiación de proyectos:' : PROJECT_FUNDING_FIELD,
	'Projekt-Status?:' : PROJECT_STATUS_FIELD,
	'Status do projeto?:' : PROJECT_STATUS_FIELD,
	'Projekt állapota?:' : PROJECT_STATUS_FIELD,
	'Estado del proyecto?:' : PROJECT_STATUS_FIELD,
	'Projektstatus?:' : PROJECT_STATUS_FIELD,
	'Status projekta?:' : PROJECT_STATUS_FIELD,
	'Project Status?:' : PROJECT_STATUS_FIELD,
    'Status for projektet?:' : PROJECT_STATUS_FIELD,
	'Dodatne informacije:' : ADDITIONAL_INFO_FIELD,
	'Información adicional:' : ADDITIONAL_INFO_FIELD,
	'Informações adicionais:' : ADDITIONAL_INFO_FIELD,
	'Ytterligare information:' : ADDITIONAL_INFO_FIELD,
	'További információ:' : ADDITIONAL_INFO_FIELD,
	'Zusätzliche Informationen:' : ADDITIONAL_INFO_FIELD,
	'Additional information:' : ADDITIONAL_INFO_FIELD,
    'Yderligere oplysninger:' : ADDITIONAL_INFO_FIELD,
	'Team Leader:' : TEAM_LEADER_FIELD,
	'Csapatvezető:' : TEAM_LEADER_FIELD,
	'Guida del gruppo:' : TEAM_LEADER_FIELD,
	'Capitan del equipo:' : TEAM_LEADER_FIELD,
	'Chef d\'équipe:' : TEAM_LEADER_FIELD,
	'Vođa tima:' : TEAM_LEADER_FIELD,
	'Teamleiter:' : TEAM_LEADER_FIELD,
	'Lagledare:' : TEAM_LEADER_FIELD,
	'Meeskonna juh:' : TEAM_LEADER_FIELD,
	'Lider do Time:' : TEAM_LEADER_FIELD,
	'Supérieur:' : SENIOR_FIELD,
	'Mayor:' : SENIOR_FIELD,
	'Senior:' : SENIOR_FIELD,
	'Anziano:' : SENIOR_FIELD,
	'Meio:' : MIDDLE_FIELD,
	'Milieu:' : MIDDLE_FIELD,
	'Medio:' : MIDDLE_FIELD,
	'Middle:' : MIDDLE_FIELD,
	'Mitten:' : MIDDLE_FIELD,
	'In Mezzo:' : MIDDLE_FIELD,
	'Mitte:' : MIDDLE_FIELD,
	'Junior:' : JUNIOR_FIELD,
	'Júnior:' : JUNIOR_FIELD,
    'Skills:' : NON_FUNCTIONAL_RESOURCES_FIELD,
    'Habilidades:' : NON_FUNCTIONAL_RESOURCES_FIELD,
    'Fertigkeiten:' : NON_FUNCTIONAL_RESOURCES_FIELD, 
    'Compétences:' : NON_FUNCTIONAL_RESOURCES_FIELD,
    'Abilità:' : NON_FUNCTIONAL_RESOURCES_FIELD,
    'Kompetens:' : NON_FUNCTIONAL_RESOURCES_FIELD,
    'Oskused:' : NON_FUNCTIONAL_RESOURCES_FIELD,
    'Készségek:' : NON_FUNCTIONAL_RESOURCES_FIELD,
    'Vještine:' : NON_FUNCTIONAL_RESOURCES_FIELD,
    'Færdigheder:' : NON_FUNCTIONAL_RESOURCES_FIELD
}
SET_FIELD_LABELS = set(LABEL_TO_FIELD_DICT.keys())

RESOURCE_LABEL_TO_API_DICT = {
	'Other' : 'other',
	'Android' : 'android', 
	'Angularjs' : 'angularjs', 
	'Backbonejs' : 'backbonejs', 
	'Bootstrap' : 'bootstrap', 
	'C-sharp' : 'c-sharp',
	'C sharp' : 'c-sharp', 
	'Concrete5' : 'concrete5', 
	'Drupal' : 'drupal', 
	'Electron' : 'electron', 
	'Expressionengine' : 'expressionengine', 
	'Html5-css3' : 'html5-css3',
	'Html5 css3' : 'html5-css3',
	'Ios' : 'ios', 
	'Java' : 'java', 
	'Javascript' : 'javascript', 
	'Joomla' : 'joomla', 
	'Nodejs' : 'nodejs', 
	'Opencart' : 'opencart', 
	'Php' : 'php', 
	'Prestashop' : 'prestashop', 
	'Python' : 'python', 
	'R' : 'r',
	'React' : 'react', 
	'React-native' : 'react-native',
	'React native' : 'react-native', 
	'Typo3' : 'typo3', 
	'Vuejs' : 'vuejs',
    # newly discovered by me
    'Shopify' : 'shopify',
    'F-sharp' :	'f-sharp',
    'Woocommerce' : 'woocommerce',
    'Magento' : 'magento',
    'Wordpress' : 'wordpress',
    'Unity' : 'unity',
    'Ionic' : 'ionic',
    'Ios-swift' : 'ios-swift',
    'Ios swift' : 'ios-swift',
    'Rubyonrails' : 'rubyonrails',
    'Typescript' : 'typescript',
    'Meteor' : 'meteor',
    'Xamarin' : 'xamarin',
    'Rust' : 'rust',
    'Aurelia' : 'aurelia',
    'Rubyonrails' : 'rubyonrails',
    'Haskell' : 'haskell',
    'Bigcommerce' : 'bigcommerce'
}
SET_RESOURCE_LABELS = set(RESOURCE_LABEL_TO_API_DICT.keys())

GOOGLE_SOURCE_API = 'google.com'

FIELD_PICKLIST_VALS_TO_API_DICT = {
	EMPLOYEES_FIELD : {
		'Other' : 'other',
		'1-5' : '1-5',
		'6-18' : '6-18',
		'19-99' : '19-99',
		'100-349' : '100-349',
		'350-1499' : '350-1499',
		'1500' : '1500'
	},
	REFERRER_FIELD : { # Lead Source - Too many values
		'Other' : 'other',
        'Wizz' : 'wizz',
        'Hn' : 'hn',
        "Google.ro" : GOOGLE_SOURCE_API,
        "Google.mk" : GOOGLE_SOURCE_API,
        "Google.us" : GOOGLE_SOURCE_API,
        "Google.be" : GOOGLE_SOURCE_API,
        "Google.ie" : GOOGLE_SOURCE_API,
        "Google.ee" : GOOGLE_SOURCE_API,
        "Google.se" : GOOGLE_SOURCE_API,
        "Google.es" : GOOGLE_SOURCE_API,
        "Google.com.ar" : GOOGLE_SOURCE_API,
        "Google.bg" : GOOGLE_SOURCE_API,
        "Google.lt" : GOOGLE_SOURCE_API,
        "Google.pe" : GOOGLE_SOURCE_API,
        "Google.it" : GOOGLE_SOURCE_API,
        "Google.ch" : GOOGLE_SOURCE_API,
        "Google.in" : GOOGLE_SOURCE_API,
        "Google.al" : GOOGLE_SOURCE_API,
        "Google.pl" : GOOGLE_SOURCE_API,
        "Google.md" : GOOGLE_SOURCE_API,
        "Google.ba" : GOOGLE_SOURCE_API,
        "Google.ph" : GOOGLE_SOURCE_API,
        "Google.pt" : GOOGLE_SOURCE_API,
        "Google.hr" : GOOGLE_SOURCE_API,
        "Google.com.ua" : GOOGLE_SOURCE_API,
        "Google.rs" : GOOGLE_SOURCE_API,
        "Google.com.br" : GOOGLE_SOURCE_API,
        "Google.de" : GOOGLE_SOURCE_API,
        "Google.gr" : GOOGLE_SOURCE_API,
        "Google.dk" : GOOGLE_SOURCE_API,
        "Google.mx" : GOOGLE_SOURCE_API,
        "Google.vn" : GOOGLE_SOURCE_API,
        "Google.nl" : GOOGLE_SOURCE_API,
        "Google-ad-campaign" : GOOGLE_SOURCE_API,
        "Google.li" : GOOGLE_SOURCE_API,
        "Google.hu" : GOOGLE_SOURCE_API,
        "Google.by" : GOOGLE_SOURCE_API,
        "Google.co.uk" : GOOGLE_SOURCE_API,
        'Facebook-page' : 'facebook-page',
        'HTML5Doctor' : 'HTML5Doctor',
        'Friend' : 'friend',
        'Startupbase.io' : 'startupbase.io',
        'CloudFest' : 'CloudFest',
        'Another-blog' : 'another-blog',
        'Press' : 'press',
        'Coworker' : 'coworker',
        'Framework7' : 'Framework7'
	},
	WORK_STRUCT_FIELD : {
			#EN
		'Other' : 'other',
		'Resource Based' : 'resource-based',
		'Project Based' : 'project-based',
        'I don\'t know' : 'other',
			#PT
		'Baseado em projeto' : 'project-based',
		'Baseado em Recursos' : 'resource-based',
		'Eu não sei' : 'other',
			#ES
		'Basado en proyectos' : 'project-based',
		'Basado en recursos' : 'resource-based',
			#DE
		'Projektbasiert' : 'project-based',
		'Ressourcenbasiert' : 'resource-based',
			#FR
		'Basé par projet' : 'project-based',
		'Basé par ressources' : 'resource-based',
			#IT
		'progetto basato' : 'project-based',
		#'Resource Based' : 'resource-based',
		'Non lo so' : 'other',
			#SV
		'Projekt Baserat' : 'project-based',
		'Resurs baserad' : 'resource-based',
			#NL
		'Projectmatige' : 'project-based',
			#RO
		'Pe baza de proiect' : 'project-based',
			#RU
		'Проектная' : 'project-based',
			#BG
		'Проектиране' : 'project-based',
			#EE
		'Ma ei tea' : 'other',
		'Ressursipõhine' : 'resource-based',
			#HU
		'Projekt alapú' : 'project-based',
		'Erőforrás alapú' : 'resource-based',
		'Nem tudom' : 'other',
			#GR
		'Βασισμένο στο έργο' : 'project-based',
			#HR
		'Na temelju resursa' : 'resource-based',
		'Zasnovan na projektu' : 'project-based',
            #DA
        'Projekt Based' : 'project-based'
	},
	PROJECT_START_FIELD : {
		'Other' : 'other',
		'4 Weeks' : '4-weeks',
		'1 Week' : '1-week',
		'2 Weeks' : '2-weeks',
		'6 Weeks' : '6-weeks',
		'Not Sure' : 'not-sure',
		'Urgent Asap' : 'urgent-asap'
	},
	DURATION_FIELD : {
		'Other' : 'other',
		'1 Month' : '1-month',
		'1 Year' : '1-year',
		'3 Months' : '3-months',
		'6 Months' : '6-months',
		'2 Years' : '2-years',
		'Not Sure' : 'not-sure'
	},
	RESOURCE_LOCATION_FIELD : {
		'Other' : 'other',
		'Remote' : 'remote',
		'On Site' : 'on-site',
		'Mix' : 'mix',
		'Not Sure' : 'not-sure'
	},
	BUDGET_FIELD : {
		'Other' : 'other',
		'Max-5k' : 'Max-5k',
		'100k' : '100k',
		'50-100k' : '50-100k',
		'10-50k' : '10-50k',
		'5-10k' : '5-10k',
		'Not Sure' : 'Not-sure',
        'Not-sure' : 'Not-sure' # new
	},
	PROJECT_BRANDING_FIELD : {
		'Other' : 'other',
		'Not Started' : 'not-started',
		'Already Have' : 'already-have',
		'Not Sure' : 'not-sure'
	},
	PROJECT_FUNDING_FIELD : {
		'Other' : 'other',
		'Just Me' : 'just-me',
		'Angel' : 'angel',
        'Vc' : 'vc',
		'Not Sure' : 'not-sure'
	},
	PROJECT_STATUS_FIELD : {
		'Other' : 'other',
		'Not Started' : 'not-started',
		'Project Almost Live' : 'project-almost-live',
		'Just Started' : 'just-started',
		'Maintenance' : 'maintenance',
		'Not Sure' : 'not-sure'
	},
}
SET_PICKLIST_FIELDS = set (FIELD_PICKLIST_VALS_TO_API_DICT.keys ())

# FUNCTIONS

def get_contains_label (string):
    for label in SET_FIELD_LABELS:
        index = string.find (label)
        if index != -1:
            return label, index
    return "", -1

def get_last_resource_start_idx (string):
    str_len = len (string)
    for res_label in SET_RESOURCE_LABELS:
        index = string.rfind (res_label)
        if index != -1 and (index + len (res_label) == str_len):
            return index
    raise Exception("String " +  "' " + string + " '" + " does not contain a valid resource label at the end of it.") 

# INPUT

with open (INPUT_FILE, FILE_OPEN_MODE, encoding = FILE_ENCODING) as export_file:
    export_str = export_file.read ()

export_str_len = len (export_str)
export_str_last_idx = export_str_len - 1

# PARSE

leads = []
lead = {} # the current lead that is parsed

resource_list = [] # the resource list of the currently parsed lead
res_list_index_curr = 0 # the current resource is updated
res_field_set = set() # if a resource field is found in this set, that means we need to increment the index(update the next resource)

seq = "" # reader
field = "" # field associated with the field label
value = "" # value of the field found by the reader

# For every character in the input file
for idx, char in enumerate (export_str):
    # Concat it with a sequence var
    seq += char
    
    # Check whether we are searching for a field or a value
    if field:
        # Field var is not NULL, value searching mode
        
        if field in SET_ADDITIONAL_INFO_FIELD:
            # Ignore any field labels as additional info may contain them, until we find the end of lead part
            eol_index = seq.rfind (YOU_ARE_RECEIVING_THIS_EMAIL)
            if eol_index != -1:
                value = seq[:eol_index].strip ()
                lead[field] = value
                field = ""
                seq = ""
            continue
        
        # Check if the current sequence contains a field label(the next field label)
        label_next, label_next_start = get_contains_label (seq)
        
        if label_next:
            # Next field label found

            # Get the next field
            field_next = LABEL_TO_FIELD_DICT[label_next]
            
            if field_next in SET_ACCOUNT_NUMBER_FIELD:
                # Next field is account number, remove the end of lead part from the sequence
                value = seq[:seq.find (YOU_ARE_RECEIVING_THIS_EMAIL)].strip ()
            elif field_next in SET_TEAM_LEADER_FIELD:
                # TeamLeader is the next field, which means that we need to remove the Resource label from the value
                seq = seq[:seq.rfind (label_next)] # Remove the TeamLeader label from the sequence
                value = seq[:get_last_resource_start_idx (seq)].strip () # Remove the Resource label from the sequence
            else:
                # Normal field label found inside the current sequence, get value by splicing
                value = seq[:label_next_start].strip ()
        elif (idx == export_str_last_idx):
            # EOF reached, there is no next field. Remove the end of lead part from the sequence
            value = seq[:seq.find (YOU_ARE_RECEIVING_THIS_EMAIL)].strip ()
        else:
            # The next field has not been not found yet, continue searching
            continue

        if field in SET_ACCOUNT_NUMBER_FIELD:
            # Current field is AccountNumber, create new lead
            lead = {field: value, NON_FUNCTIONAL_RESOURCES_FIELD: []}
            # Append it to the leads list
            leads.append (lead)
        elif field in SET_PICKLIST_FIELDS:
            # Picklist is the field's type, get the api value of the resulting sequence and insert it
            value = FIELD_PICKLIST_VALS_TO_API_DICT[field][value]
            lead[field] = value
        elif field in SET_NON_FUNCTIONAL_RESOURCES_FIELD:
            # Current field is Skills
            # Split the skills' value at the commas, strip the whitespaces and wrap the (resource name => api name) in a dictionary object
            # Put every result in the resource list
            resource_list = [ {RESOURCE_FIELD: RESOURCE_LABEL_TO_API_DICT[resource.strip ()]} for resource in value.split(',')]
            # Put the result in the lead's non functional resources field
            lead[NON_FUNCTIONAL_RESOURCES_FIELD].extend (resource_list)
            # Reinitialize the resource vars
            res_list_index_curr = 0
            res_field_set = set()
        elif field in SET_SENIORITY_FIELD:
            # Current field is a Seniority (for resource)
            # Check if we are inserting this value to the correct resource
            if field in res_field_set:
                # The value for this field of this resource was already inserted, move to the next resource
                res_list_index_curr += 1
                res_field_set = set() # reset the field set

            # Insert the value to the resource's field
            resource_list[res_list_index_curr][field] = value
            res_field_set.add (field) # Update the field set
        else:
            # Some other lead field, insert the value
            lead[field] = value

        # Move to the next field
        field = field_next
        seq = ""
    else:
        # Field var is NULL, field searching mode
        # Check if a field label is in the current sequence
        label = get_contains_label (seq)[0] # Get the label only
        if not label:
            # No field label found, continue searching
            continue
            
        # Label found, get the field associated with it
        field = LABEL_TO_FIELD_DICT[label]
        seq = ""

# OUTPUT

leads_json = json.dumps(leads, indent = 4, ensure_ascii = False)
with open (OUTPUT_FILE, FILE_WRITE_MODE, encoding = FILE_ENCODING) as output_file:
    output_file.write(leads_json)
    
print ("Done! " + str(len(leads)) + " leads have been jsonified.")

# invalid_values = [{x : list(y)} for x, y in invalid_values.items ()]
# print(json.dumps(invalid_values, indent = 4, ensure_ascii = False))
