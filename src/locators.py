from selenium.webdriver.common.by import By


class RegisterFormLocators:
    INPUT_NAME = (By.XPATH, ".//input[@type='text' and @name='name' and preceding-sibling::label[text()='Имя']]") #Поле Имя
    INPUT_LOGIN = (By.XPATH, ".//input[@type='text' and @name='name' and preceding-sibling::label[text()='Email']]") # Поле "Email"
    INPUT_PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # Поле "Пароль"
    BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться"
    LABEL_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка "Некорректный пароль"

class MainPageLocators:
    HEADER_PAGE = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']") # Заголовок
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']") #Кнопка "Конструктор"
    BUTTON_BURGER_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a") #Кнопка "burger"
    HEADER_MAKE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")  # header "Собери бургер"

class PersonalAccountLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") #Кнопка "Личный кабинет"
    LINK_PROFILE = (By.XPATH, "//a[text()='Профиль']") #ссылка "Профиль" в личном кабинете
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"

class LoginFormLocators:
    INPUT_EMAIL_LOGIN = (By.XPATH, "//input[@name='name']") #Поле "Email"
    BUTTON_LOGIN = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]") # Кнопка «Войти»
    LABEL_ENTER = (By.XPATH, "//h2[text()='Вход']")  # 'Вход'

class LoginButtonsLocators:
    BUTTON_LOGIN_RESTORE = (By.XPATH, "//a[@class='Auth_link__1fOlj']")  # Кнопка "Войти" - форма восстановления пароля
    BUTTON_REGISTER_LOGIN = (By.XPATH, "//a[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться" под формой входа
    BUTTON_RESTORE = (By.XPATH, "//a[text()='Восстановить пароль']") #Кнопка "Восстановить пароль" под формой входа
    BUTTON_LOGIN_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт" на главной странице
    LABEL_ENTER_REGISTER = (By.XPATH, "//a[text()='Войти']")  #Кнопка "Войти" на странице регистрации

class NavigationsTabsLocators:
    BUTTON_BUNS = (By.XPATH, "//span[text()='Булки']") #Кнопка "Булки"
    BUTTON_SAUCE = (By.XPATH, "//span[text()='Соусы']") #Кнопка "Соусы"
    BUTTON_FILLING = (By.XPATH, "//span[text()='Начинки']") #Кнопка "Начинки"
    HEADER_BUNS = (By.XPATH, "//h2[text()='Булки']") #h2 "Булки"
    HEADER_FILLINGS = (By.XPATH, "//h2[text()='Начинки']") #h2 "Начинки"
    HEADER_SAUCES = (By.XPATH, "//h2[text()='Соусы']") #h2 "Соусы"

class OrderButtonIsDisplayedLocators:
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") #Кнопка 'Оформить заказ'