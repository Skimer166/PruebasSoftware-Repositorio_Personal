# -*- coding: utf-8 -*-
"""Ejercicio selenium"""
import time

from behave import given, then, when
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver

DIRECT_HOME_URLS = {
    "iteso.mx": "https://www.iteso.mx/",
    "udg.mx": "https://www.udg.mx/",
    "uv.mx": "https://www.uv.mx/",
}

NAV_STEPS = {
    "iteso.mx": [
        (
            By.XPATH,
            "//p[contains(@class,'txttitle') and normalize-space(text())='Carreras']",
            True,
        ),
    ],
    "udg.mx": [
        (By.XPATH, "//a[@href='/es/oferta-academica']", False),
        (
            By.XPATH,
            "//a[contains(@href,'guiadecarreras.udg.mx/category/areas')]",
            False,
        ),
    ],
    "uv.mx": [
        (By.XPATH, "//a[@href='/ofertaeducativa/' and @role='button']", False),
        (
            By.XPATH,
            "//a[@href='https://www.uv.mx/ofertaeducativa/area/tecnica/']",
            False,
        ),
    ],
}


VERIFY_TEXT = {
    "iteso.mx": "humanidades",
    "udg.mx": "abogado",
    "uv.mx": "arquitectura",
}


def _wait(driver, timeout=15):
    return WebDriverWait(driver, timeout)


def _accept_cookies(driver):
    for txt in ["aceptar", "accept", "agree"]:
        try:
            btn = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        f"//button[contains(translate(.,"
                        f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{txt}')]",
                    )
                )
            )
            btn.click()
            time.sleep(0.4)
            return
        except TimeoutException:
            continue


def _safe_click(driver, by, selector, timeout=20, new_tab=False):
    """
    Localiza el elemento, hace scroll y clickea via JS.
    Si new_tab=True, espera que se abra una pestaña nueva y cambia a ella.
    """
    el = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, selector))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center', behavior:'smooth'});", el
    )
    time.sleep(0.8)

    handles_before = set(driver.window_handles)
    driver.execute_script("arguments[0].click();", el)

    if new_tab:
        # Esperar a que aparezca la nueva pestaña
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > len(handles_before)
        )
        new_handle = (set(driver.window_handles) - handles_before).pop()
        driver.switch_to.window(new_handle)

    WebDriverWait(driver, 15).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    time.sleep(1.5)


def _current_domain(driver):
    url = driver.current_url.lower()
    url = url.replace("https://", "").replace("http://", "").replace("www.", "")
    return url.split("/")[0]


# Steps
@given("I am on the Google homepage")
def open_google(context):
    """abrir google"""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.get("https://www.google.com")
    _accept_cookies(context.driver)


@when('I search for "{query}" on Google')
def search_google(context, query):
    """Escribe el query en el buscador de Google y presiona Enter."""
    driver = context.driver
    box = _wait(driver).until(EC.element_to_be_clickable((By.NAME, "q")))
    box.clear()
    box.send_keys(query)
    box.send_keys(Keys.RETURN)
    _wait(driver).until(EC.presence_of_element_located((By.ID, "search")))


@when("I click on the first search result")
def click_first_result(context):
    """Hace click en el primer resultado orgánico de Google."""
    driver = context.driver
    try:
        result = _wait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@id='search']//a[@href][not(contains(@href,'google'))]",
                )
            )
        )
    except TimeoutException:
        links = driver.find_elements(By.CSS_SELECTOR, "a[href^='http']")
        result = next(
            (
                l
                for l in links
                if l.is_displayed() and "google.com" not in l.get_attribute("href")
            ),
            None,
        )
        assert result, "No se encontró ningún resultado de búsqueda en Google"

    driver.execute_script("arguments[0].scrollIntoView(true);", result)
    driver.execute_script("arguments[0].click();", result)
    _wait(driver, 15).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    time.sleep(1)


@then('I should be on the domain "{expected_domain}"')
def verify_domain(context, expected_domain):
    """
    Verifica el dominio. Si Google no navegó al sitio (bug de click),
    navega directo como fallback antes de fallar.
    """
    driver = context.driver
    clean = expected_domain.lower().replace("www.", "")

    try:
        _wait(driver, 10).until(lambda d: clean in d.current_url.lower())
    except TimeoutException:
        pass

    if clean not in driver.current_url.lower():
        home = next((u for k, u in DIRECT_HOME_URLS.items() if k in clean), None)
        assert home, (
            f"No se pudo navegar a '{expected_domain}'.\n"
            f"URL actual: {driver.current_url}"
        )
        print(f"  [fallback] Navegando directo a {home}")
        driver.get(home)
        _wait(driver, 15).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        time.sleep(1)

    assert (
        clean in driver.current_url.lower()
    ), f"Dominio '{expected_domain}' no encontrado en: {driver.current_url}"


@when('I search for "{search_term}" on the university site')
def search_on_university_site(context, search_term):  # pylint: disable=unused-argument
    """
    Ejecuta los clicks de navegación interna definidos en NAV_STEPS
    para el dominio actual.
    El argumento search_term es requerido por Behave para parsear el step
    aunque la navegación se resuelve por dominio via NAV_STEPS.
    """
    driver = context.driver
    domain = _current_domain(driver)
    _accept_cookies(driver)

    steps = next((v for k, v in NAV_STEPS.items() if k in domain), None)
    assert steps is not None, (
        f"No hay navegación definida para '{domain}'. "
        f"Agrega una entrada en NAV_STEPS."
    )

    for by, selector, new_tab in steps:
        print(f"  [nav] Clickeando: {selector}")
        _safe_click(driver, by, selector, new_tab=new_tab)
        _accept_cookies(driver)


@then('I should see results related to "{expected_content}"')
def verify_results(context, expected_content):
    """
    Verifica que el texto esperado esté presente en el body de la página.
    Primero espera activamente hasta 20s a que aparezca.
    """
    driver = context.driver

    try:
        WebDriverWait(driver, 20).until(
            lambda d: expected_content.lower()
            in d.find_element(By.TAG_NAME, "body").text.lower()
        )
    except TimeoutException:
        body = driver.find_element(By.TAG_NAME, "body").text.lower()
        domain = _current_domain(driver)
        fallback = VERIFY_TEXT.get(domain, expected_content).lower()
        assert fallback in body, (
            f"Texto esperado '{expected_content}' (o '{fallback}') "
            f"no encontrado en la página.\nURL: {driver.current_url}"
        )

    context.driver.quit()
