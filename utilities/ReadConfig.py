import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfigClass:
    @staticmethod
    def geta_data_for_email():
        email = config.get('login data', 'email')
        return email

    @staticmethod
    def geta_data_for_password():
        password = config.get('login data', 'password')
        return password
    @staticmethod
    def get_Homepage_url():
        homepage=config.get("Application url","home_page")
        return homepage
    @staticmethod
    def get_login_url():
        login_url=config.get("Application url","login_page")
        return login_url
    @staticmethod
    def get_register_url():
        registerurl=config.get("Application url","register_page")
        return registerurl

    @staticmethod
    def section1_data():
        section2_data = config.get('section 1', 'key1')
        return section2_data