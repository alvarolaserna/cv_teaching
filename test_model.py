import base64
from io import BytesIO

import cv2 as cv
import argparse
import signal, time, os
import numpy as np
from numpy import ndarray

from PIL import Image
from cv_pom.cv_pom import POM
from selenium.webdriver.chrome.options import Options
from testui.support.appium_driver import NewDriver
from cv_pom.frameworks import TestUICVPOMDriver

parser = argparse.ArgumentParser(description="CV POM wrapper")
parser.add_argument("--model", help="The CV model to be used [path]")
parser.add_argument("--record", help="Records all the images in files")
args = parser.parse_args()

options = Options()
options.add_argument("disable-user-media-security")
driver = (
    NewDriver()
    .set_logger()
    .set_selenium_driver(chrome_options=options)
)
driver.navigate_to("https://flutter-gallery-archive.web.app/")

cv_pom = POM(args.model)
cv_pom_driver = TestUICVPOMDriver(model_path=args.model, driver=driver)


def _get_screenshot() -> ndarray:
    image = driver.get_driver.get_screenshot_as_base64()
    sbuf = BytesIO()
    sbuf.write(base64.b64decode(str(image)))
    pimg = Image.open(sbuf)
    return cv.cvtColor(np.array(pimg), cv.COLOR_RGB2BGR)


def handler(signum, frame):
    exit(1)


signal.signal(signal.SIGINT, handler)

WINDOW_NAME = 'TEST'
cv.namedWindow(WINDOW_NAME, cv.WINDOW_AUTOSIZE)
cv.startWindowThread()

i = 0
while True:
    img = _get_screenshot()
    time1 = time.time()
    cv_pom.convert_to_cvpom(img, use_ocr=True)
    time2 = time.time()
    print(time2 - time1)
    # Display labeled image
    if args.record is not None and i != 0:
        cv.imwrite(
            os.path.join(
                args.record, "test" + str(time.time()) + ".png"
            ), img
        )
    # print(cv_pom.filter_by_position(x='right', y='bottom').find_by_label('text-btn').center)
    print(cv_pom.to_json())

    cv.imshow('TEST', cv_pom.annotated_frame)
    cv.waitKey(0)
    cv.destroyAllWindows()
    i += 1
