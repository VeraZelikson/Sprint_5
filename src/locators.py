from selenium.webdriver.common.by import By


class RegisterFormLocators:
    input_name = (By.XPATH, "//fieldset[1][@class='Auth_fieldset__1QzWN mb-6']/div/div/input[@class='text input__textfield text_type_main-default']") #Поле Имя
    input_login = (By.XPATH, "//fieldset[2][@class='Auth_fieldset__1QzWN mb-6']/div/div/input[@class='text input__textfield text_type_main-default']") # Поле "Email"
    input_password = (By.XPATH, "//input[@name='Пароль']")  # Поле "Пароль"
    button_register = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться"
    label_error = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка "Некорректный пароль"

class MainPageLocators:
    header_page = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']") # Заголовок
    button_constructor = (By.XPATH, "//p[text()='Конструктор']") #Кнопка "Конструктор"
    button_burger_logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a") #Кнопка "burger"
    header_make_burger = (By.XPATH, "//h1[text()='Соберите бургер']")  # header "Собери бургер"

class PersonalAccountLocators:
    personal_account_button = (By.XPATH, "//p[text()='Личный Кабинет']") #Кнопка "Личный кабинет"
    link_profile = (By.XPATH, "//a[text()='Профиль']") #ссылка "Профиль" в личном кабинете
    button_logout = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"

class LoginFormLocators:
    input_email_login = (By.XPATH, "//input[@name='name']") #Поле "Email"
    button_login = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # Кнопка «Войти»
    label_enter = (By.XPATH, "//h2[text()='Вход']")  # 'Вход'

class LoginButtonsLocators:
    button_login_restore = (By.XPATH, "//a[@class='Auth_link__1fOlj']")  # Кнопка "Войти" - форма восстановления пароля
    button_register_login = (By.XPATH, "//a[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться" под формой входа
    button_restore = (By.XPATH, "//a[text()='Восстановить пароль']") #Кнопка "Восстановить пароль" под формой входа
    button_login_main = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт" на главной странице
    label_enter_register = (By.XPATH, "//a[text()='Войти']")  #Кнопка "Войти" на странице регистрации

class NavigationsTabsLocators:
    button_buns = (By.XPATH, "//span[text()='Булки']") #Кнопка "Булки"
    button_sauce = (By.XPATH, "//span[text()='Соусы']") #Кнопка "Соусы"
    button_filling = (By.XPATH, "//span[text()='Начинки']") #Кнопка "Начинки"
    header_buns = (By.XPATH, "//h2[text()='Булки']") #h2 "Булки"
    header_fillings = (By.XPATH, "//h2[text()='Начинки']") #h2 "Начинки"
    header_sauces = (By.XPATH, "//h2[text()='Соусы']") #h2 "Соусы"

class OrderButtonIsDisplayedLocators:
    button_order = (By.XPATH, "//button[text()='Оформить заказ']") #Кнопка 'Оформить заказ'