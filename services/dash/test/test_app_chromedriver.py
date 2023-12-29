from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from app.app import get_app


def test_update_graph_in_server(dash_duo):
    dash_duo.start_server(get_app())
    input_box = dash_duo.driver.find_element(By.ID, "input-n-coords")
    button = dash_duo.driver.find_element(By.ID, "button-update-coords")
    wait = WebDriverWait(dash_duo.driver, 3, 0.1)

    def is_num_points_expected(driver) -> bool:
        actual_num_points = len(driver.find_elements(By.CLASS_NAME, "point"))
        return actual_num_points == num_points  # num_points defined in for loop

    for num_points in [3, 2]:
        input_box.send_keys(Keys.BACK_SPACE + f"{num_points}")
        button.click()
        num_points = num_points
        wait.until(is_num_points_expected)
        points = dash_duo.driver.find_elements(By.CLASS_NAME, "point")
        assert len(points) == num_points
